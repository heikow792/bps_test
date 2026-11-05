# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7c0efad9-aa68-4f6f-ad1b-d055d687a18f",
# META       "default_lakehouse_name": "bps_silver_c792846f",
# META       "default_lakehouse_workspace_id": "649676ea-3e7c-457d-a728-7e8e8cdafee9",
# META       "known_lakehouses": [
# META         {
# META           "id": "7c0efad9-aa68-4f6f-ad1b-d055d687a18f"
# META         },
# META         {
# META           "id": "18275add-7d43-4a42-815a-b1c738d97308"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "0aba069f-9427-ae29-43d5-d8ff05f1a1ba",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# > ⚠️ **Do Not Edit** — This notebook is maintained and deployed by **Business Process Solutions**. Any manual changes will be overwritten during the next update. Want to make changes? Duplicate this notebook and work from the copy.

# MARKDOWN ********************

# # Supplier Balance Aggregate
# 
# Builds the `BPS_SUPPLIERBALANCEAGGR` fact (supplier debit/credit balances and carry-forward) from `I_OPERATIONALACCTGDOCITEM`.
# 
# **Design**
# - One **grain config** (`DIMENSION_KEYS`, `CURRENCY_TYPES`) drives the whole pipeline; the aggregation / carry-forward / output key sets are *derived*, never hand-synced.
# - **Config-driven currencies** using the SAP source field names directly.
# - **Incremental**: reprocesses the full history of any entity the delta touched, then replaces those entities in the output (correct running totals).
# - Same output schema as the original notebook (Power BI model unaffected).

# MARKDOWN ********************

# ## 1. Parameters

# PARAMETERS CELL ********************

p_guid = ''
p_gold_lakehouse_name = ''
p_silver_lakehouse_name = ''
p_output_table_name = 'BPS_SUPPLIERBALANCEAGGR'
p_system_name = ''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 2. Imports

# CELL ********************

import uuid
from functools import reduce

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from delta.tables import DeltaTable

import sempy.fabric as fabric
from common_lib.utils import parse_lakehouse_details, get_log_file_path
from common_lib.constants import DEFAULT_LOG_COLUMNS
from common_lib.logger.dataframe_logger import DataFrameLogger

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 3. Configuration
# 
# Single source of truth for the grain. Add a dimension in `DIMENSION_KEYS` (or a currency in `CURRENCY_TYPES`) once and it flows through aggregation, the dense grid, the carry-forward partitions, the output and the merge keys.

# CELL ********************

# Surrogate FKs that define one supplier-balance entity (one running-balance stream).
DIMENSION_KEYS = [
    '_key_ICOMPANYCODE',
    '_key_IGLACCOUNTINCHARTOFACCOUNTS',
    '_key_ISUPPLIER',
    '_key_ISPECIALGLCODE',
    '_key_IACCOUNTINGDOCUMENTCATEGORY',
    '_SystemName'
]

PERIOD_KEY  = '_key_IFISCALPERIODFORVARIANT'
FISCAL_COLS = ['FISCALYEAR', 'FISCALYEARVARIANT', 'FISCALPERIOD', 'FISCALYEARPERIOD']

# Output CURRENCYTYPE -> (source currency-code column, source amount column).
# The CC/FC/TC/GC keys are the output contract consumed by Power BI
# (the _Currency Types dimension and the CURRENCYTYPE measures).
CURRENCY_TYPES = {
    'CC': ('COMPANYCODECURRENCY', 'AMOUNTINCOMPANYCODECURRENCY'),
    'FC': ('FUNCTIONALCURRENCY',  'AMOUNTINFUNCTIONALCURRENCY'),
    'TC': ('TRANSACTIONCURRENCY', 'AMOUNTINTRANSACTIONCURRENCY'),
    'GC': ('ADDITIONALCURRENCY1', 'AMOUNTINADDITIONALCURRENCY1'),
}
CURRENCY_CODE_COLS = [code for code, _amt in CURRENCY_TYPES.values()]
AMOUNT_COLS        = [amt for _code, amt in CURRENCY_TYPES.values()]

# Derived key sets - never hand-maintained again.
GROUP_BY    = DIMENSION_KEYS + [PERIOD_KEY] + FISCAL_COLS + CURRENCY_CODE_COLS   # aggregation grain
ENTITY_KEYS = DIMENSION_KEYS + CURRENCY_CODE_COLS                               # carry-forward / dense-grid grain (no period)
OUTPUT_KEYS = DIMENSION_KEYS + [PERIOD_KEY] + FISCAL_COLS                       # keys carried into the final fact

# SAP debit/credit indicator (BSEG-SHKZG): S = debit, H = credit.
DEBIT_CODE, CREDIT_CODE = 'S', 'H'

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 4. Helpers

# CELL ********************

def get_lakehouse_details(lakehouse_name: str, workspace: str = None):
    """
    Function that fetches and stores all the details about the lakehouse.
    """
    try:
        workspace = fabric.resolve_workspace_id(workspace) or fabric.get_workspace_id()
        data = notebookutils.lakehouse.getWithProperties(name=lakehouse_name, workspaceId=workspace)
        return data
    except Exception as e:
        if "ArtifactNotFoundException" in str(e):
            raise LakehouseNotFoundException(lakehouse_name=lakehouse_name, workspace_id=workspace)
        else:
            print(f"An error occurred while fetching lakehouse details: {e}")
            raise e

def get_max_timestamp(df, timestamp_column='_UpdateTimeStamp'):
    if timestamp_column not in df.columns:
        return None
    row = df.agg(F.max(F.col(timestamp_column)).alias('mx')).first()
    return row['mx'] if row else None


def read_delta(path: str, system_name: str):
    if not DeltaTable.isDeltaTable(spark, path):
        raise ValueError(f'Delta table not found at path: {path}')
    if system_name and len(system_name) > 0:
        df = DeltaTable.forPath(spark, path).toDF()
        df_filtered = df.filter(F.col("_SystemName") == p_system_name)
        return df_filtered
    return DeltaTable.forPath(spark, path).toDF()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 5. Setup (Spark, paths, logging)

# CELL ********************

if not p_guid:
    p_guid = str(uuid.uuid4())

spark = SparkSession.builder.appName('SupplierBalanceAggregate').getOrCreate()
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInWrite", "CORRECTED")
spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInRead", "CORRECTED")
spark.conf.set("spark.sql.parquet.datetimeRebaseModeInRead", "CORRECTED")
spark.conf.set("spark.sql.parquet.datetimeRebaseModeInWrite", "CORRECTED")
spark.conf.set("spark.sql.parquet.int96RebaseModeInWrite", "CORRECTED")
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")

gold_details   = parse_lakehouse_details(get_lakehouse_details(p_gold_lakehouse_name))
silver_details = parse_lakehouse_details(get_lakehouse_details(p_silver_lakehouse_name))

gold_tables_path       = gold_details['tables_path']
operational_acctg_path = gold_tables_path + 'I_OPERATIONALACCTGDOCITEM'
fiscal_period_path     = gold_tables_path + 'I_FISCALPERIODFORVARIANT'
output_path            = gold_tables_path + p_output_table_name

_log_folder   = get_log_file_path(silver_details['tables_path'])
log_file_path = f'{_log_folder}{p_guid}'
logger = DataFrameLogger(
    log_file_path=log_file_path,
    guid=p_guid,
    log_columns=DEFAULT_LOG_COLUMNS,
    prefix='Supplier Balance Aggregate',
)
print(f'Logs will be saved at {log_file_path}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 6. Extract & scope
# 
# `read_source` returns debitor line items (noted / statistical items are kept and carried via `_key_IACCOUNTINGDOCUMENTCATEGORY`). `resolve_scope` decides full vs incremental and, for incremental, returns the full history of every entity the delta touched.

# CELL ********************

def read_source(p_system_name: str):
    # Customer (debitor) line items. Noted / statistical items
    # (ACCOUNTINGDOCUMENTCATEGORY non-blank) are RETAINED and carried via
    # _key_IACCOUNTINGDOCUMENTCATEGORY so the report can include/exclude them.
    logger.info(f"Loading Operation Accouting Document data for system {p_system_name} from {operational_acctg_path}")
    df = read_delta(operational_acctg_path, p_system_name)
    return df.filter(F.col('FINANCIALACCOUNTTYPE') == 'K')


def resolve_scope(source_df, p_system_name: str):
    # Decide full vs incremental. Returns (scope_df, touched_entities_or_None).
    # Incremental reprocesses the FULL history of every entity the delta touched,
    # because running totals need all of an entity timeline.

    if source_df.limit(1).count() == 0:
        logger.info(f"Fact table has no rows for source system {p_system_name}, Stop processing run.")
        logger.save_logs(spark)
        notebookutils.notebook.exit(value=f"Fact table has no rows for source system {p_system_name}, Stop processing run.")

    if not DeltaTable.isDeltaTable(spark, output_path):
        logger.info(f'Output table {p_output_table_name} does not exist in lakehouse -> Performing FULL load.')
        return source_df, None

    aggr_table = read_delta(output_path, p_system_name)
    max_ts = get_max_timestamp(aggr_table)
    print(f"Max timestamp from Aggregate table {p_output_table_name} for system name {p_system_name} is {max_ts}")
    if max_ts is None:
        logger.info(f'Output table {p_output_table_name} has no watermark -> Performing FULL load.')
        return source_df, None

    changed = source_df.filter(F.col('_UpdateTimeStamp') > max_ts)
    if changed.limit(1).count() == 0:
        logger.info('No new source rows modified since last run. Stop processing run')
        logger.save_logs(spark)
        notebookutils.notebook.exit(value='Customer Balance Aggregate completed - no new rows.')

    touched = changed.select(*DIMENSION_KEYS).distinct()
    logger.info('Modified rows detected in source table -> Performing INCREMENTAL load')
    scope = source_df.join(F.broadcast(touched), on=DIMENSION_KEYS, how='inner')
    return scope, touched

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 7. Transform
# 
# Aggregate debit/credit/net per currency, densify (fill every period per entity **from its first active period onward**), carry-forward, reshape to long.

# CELL ********************

def prepare_postings(scope_df, fiscal_period_df):
    keep = DIMENSION_KEYS + [PERIOD_KEY, 'DEBITCREDITCODE'] + CURRENCY_CODE_COLS + AMOUNT_COLS
    postings = scope_df.select(*keep)
    calendar = fiscal_period_df.select(F.col('Key').alias(PERIOD_KEY), *FISCAL_COLS)
    return postings.join(calendar, on=PERIOD_KEY, how='left')


def aggregate_balances(postings):
    agg_exprs = []
    for ctype, (_code, amount) in CURRENCY_TYPES.items():
        amt = F.col(amount)
        agg_exprs.append(
            F.coalesce(F.sum(F.when(F.col('DEBITCREDITCODE') == DEBIT_CODE, amt)), F.lit(0)).alias(f'DEBIT_{ctype}'))
        agg_exprs.append(
            F.coalesce(F.sum(F.when(F.col('DEBITCREDITCODE') == CREDIT_CODE, -amt)), F.lit(0)).alias(f'CREDIT_{ctype}'))

    agg = postings.groupBy(*GROUP_BY).agg(*agg_exprs)
    for ctype in CURRENCY_TYPES:
        agg = agg.withColumn(f'NET_{ctype}', F.col(f'DEBIT_{ctype}') - F.col(f'CREDIT_{ctype}'))
    return agg


def densify(agg, fiscal_period_df):
    # Fill every fiscal period for every entity so carry-forward runs over a
    # continuous timeline (inactive periods carry the balance forward).
    #
    # Optimisation (a): each entity is densified only from its FIRST active period
    # onward (up to the end of the range), not from the global start. Periods
    # before an entity existed carry a zero balance and zero carry-forward, so
    # generating them adds only empty rows. FISCALYEARPERIOD (YYYYPPP) is a
    # chronological integer, so it is used as the ordering key.

    # from the aggregated postings, find the global min/max fiscal year and all variants.
    bounds   = agg.select(F.min('FISCALYEAR').alias('mn'), F.max('FISCALYEAR').alias('mx')).first()
    variants = [r['FISCALYEARVARIANT'] for r in agg.select('FISCALYEARVARIANT').distinct().collect()]

    # for the fiscal year range, get all fiscal periods (calendar)
    calendar = (fiscal_period_df
        .filter((F.col('FISCALYEAR') >= bounds['mn']) & (F.col('FISCALYEAR') <= bounds['mx']))
        .filter(F.col('FISCALYEARVARIANT').isin(variants))
        .select(*FISCAL_COLS, F.col('Key').alias(PERIOD_KEY))
        .distinct())

    entity_start = agg.groupBy(*ENTITY_KEYS).agg(F.min('FISCALYEARPERIOD').alias('_first_fyp'))

    grid = (entity_start.crossJoin(calendar)
                        .filter(F.col('FISCALYEARPERIOD') >= F.col('_first_fyp'))
                        .drop('_first_fyp'))

    dense      = grid.join(agg, on=GROUP_BY, how='left')
    value_cols = [f'{m}_{c}' for c in CURRENCY_TYPES for m in ('DEBIT', 'CREDIT', 'NET')]
    return dense.fillna(0, subset=value_cols)


def add_carry_forward(dense):
    # Opening balance from earlier periods in the SAME fiscal year.
    w_period = (Window.partitionBy(*ENTITY_KEYS, 'FISCALYEAR')
                      .orderBy('FISCALYEAR', 'FISCALPERIOD')
                      .rowsBetween(Window.unboundedPreceding, -1))
    for ctype in CURRENCY_TYPES:
        dense = dense.withColumn(
            f'CF_PREV_PERIOD_{ctype}',
            F.coalesce(F.sum(f'NET_{ctype}').over(w_period), F.lit(0.0)).cast('decimal(31,2)'))

    # Opening balance from ALL previous fiscal years (running sum of yearly nets).
    year_totals = dense.groupBy(*ENTITY_KEYS, 'FISCALYEAR').agg(
        *[F.sum(f'NET_{c}').alias(f'YR_NET_{c}') for c in CURRENCY_TYPES])
    w_year = (Window.partitionBy(*ENTITY_KEYS)
                    .orderBy('FISCALYEAR')
                    .rowsBetween(Window.unboundedPreceding, -1))
    for ctype in CURRENCY_TYPES:
        year_totals = year_totals.withColumn(
            f'CF_PREV_YEAR_{ctype}',
            F.coalesce(F.sum(f'YR_NET_{ctype}').over(w_year), F.lit(0.0)))

    prev_year_cols = [f'CF_PREV_YEAR_{c}' for c in CURRENCY_TYPES]
    dense = dense.join(
        year_totals.select(*ENTITY_KEYS, 'FISCALYEAR', *prev_year_cols),
        on=ENTITY_KEYS + ['FISCALYEAR'], how='left')
    for col in prev_year_cols:
        dense = dense.withColumn(col, F.coalesce(F.col(col), F.lit(0.0)))

    # Total opening = previous periods (this year) + all previous years.
    for ctype in CURRENCY_TYPES:
        dense = dense.withColumn(
            f'CF_TOTAL_{ctype}',
            F.col(f'CF_PREV_PERIOD_{ctype}') + F.col(f'CF_PREV_YEAR_{ctype}'))
    return dense


def to_long(dense):
    # Reshape the wide (per-currency) frame into the long output fact, one block
    # per currency type - a loop instead of four copy-pasted blocks.
    frames = []
    for ctype, (code_col, _amt) in CURRENCY_TYPES.items():
        rename = {
            code_col: 'CURRENCY',
            f'DEBIT_{ctype}':  'DEBIT_BALANCE',
            f'CREDIT_{ctype}': 'CREDIT_BALANCE',
            f'NET_{ctype}':    'NET_BALANCE',
            f'CF_PREV_PERIOD_{ctype}': 'CARRY_FORWARD_FROM_PREV_PERIOD',
            f'CF_PREV_YEAR_{ctype}':   'CARRY_FORWARD_FROM_PREV_YEAR',
            f'CF_TOTAL_{ctype}':       'CARRY_FORWARD_TOTAL',
        }
        frame = (dense.select(*OUTPUT_KEYS, *rename.keys())
                      .withColumnsRenamed(rename)
                      .withColumn('CURRENCYTYPE', F.lit(ctype)))
        frames.append(frame)
    return reduce(DataFrame.unionByName, frames)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 8. Load
# 
# Full load overwrites; incremental replaces every output row of a touched entity (delete-then-append), which also removes stale rows a plain upsert would miss.

# CELL ********************

def write_output(long_df, touched, source_max_ts):
    stamped = long_df.withColumn('_UpdateTimeStamp', F.lit(source_max_ts))

    if touched is None:
        logger.info('Writing FULL load (overwrite).')
        (stamped.write.format('delta')
                .mode('overwrite')
                .option('mergeSchema', 'true')
                .save(output_path))
        return

    logger.info('Writing INCREMENTAL load (replace touched entities).')
    delete_cond = ' AND '.join(f't.{k} = d.{k}' for k in DIMENSION_KEYS)
    (DeltaTable.forPath(spark, output_path).alias('t')
        .merge(touched.alias('d'), delete_cond)
        .whenMatchedDelete()
        .execute())
    (stamped.write.format('delta')
            .mode('append')
            .option('mergeSchema', 'true')
            .save(output_path))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 9. Run

# CELL ********************

source_df     = read_source(p_system_name)
source_max_ts = get_max_timestamp(source_df)

scope_df, touched = resolve_scope(source_df, p_system_name)   # may exit early when nothing changed

logger.info(f"Loading Fiscal Period for Variant table.")
fiscal_period_df = read_delta(fiscal_period_path, p_system_name)

logger.info("Processing data for documents that have been updated.")
postings = prepare_postings(scope_df, fiscal_period_df)

logger.info("Calculating NET_BALANCE, CREDIT_BALANCE, DEBIT_BALANCE for all rows.")
agg      = aggregate_balances(postings)

logger.info("Calculating CARRY_FORWARD BALANCES for previous fiscal year and fiscal periods.")
dense    = densify(agg, fiscal_period_df)
dense    = add_carry_forward(dense)
long_df  = to_long(dense)

logger.info("Saving current data to table.")
write_output(long_df, touched, source_max_ts)

logger.info(f'Supplier Balance Aggregate processing completed successfully for system name {p_system_name}.')
logger.save_logs(spark)
notebookutils.notebook.exit(value=f'Supplier Balance Aggregate completed successfully for system name {p_system_name}.')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
