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

# ### Parameters

# CELL ********************

p_silver_lakehouse_name = "bps_silver_c792846f"
p_gold_lakehouse_name = "bps_gold_c792846f"
p_metadata_database_name = "bps_metadata_db_c792846f"

# global variables
p_guid = ""
p_CDSViewName = "I_EXCHANGERATERAWDATA"

# MARKDOWN ********************

# ### Import Modules

# CELL ********************

import sempy.fabric as fabric
from pyspark.sql import SparkSession

from pyspark.sql.types import DateType
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import DoubleType

import uuid
import json
import ast
import struct
import sqlalchemy
import pyodbc

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


from delta import DeltaTable
from datetime import datetime

from common_lib.logger.dataframe_logger import DataFrameLogger
from common_lib.constants import DEFAULT_LOG_COLUMNS, FABRIC_SQL_CONNECTION_STRING_TEMPLATE
from common_lib.utils import parse_query_output, parse_lakehouse_details,\
apply_join_conditions, check_if_table_exists, get_log_file_path, execute_sql_query_fsql, \
validate_required_params, validate_delta_table
from common_lib.exceptions import LakehouseNotFoundException, DeltaTableNotFoundException

from trident_token_library_wrapper import PyTridentTokenLibrary
import notebookutils

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

p_guid = str(uuid.uuid4()) if len(p_guid) == 0 else p_guid

# MARKDOWN ********************

# ### Initial Validations

# CELL ********************

validate_required_params(
    p_metadata_database_name=p_metadata_database_name,
    p_silver_lakehouse_name=p_silver_lakehouse_name,
    p_gold_lakehouse_name=p_gold_lakehouse_name,
    p_CDSViewName=p_CDSViewName
)

# CELL ********************

def get_lakehouse_details(lakehouse_name: str, workspace: str = None):
    """
    Function that fetches and stores all the details about the lakehouse.
    """
    try:
        lakehouse_name = lakehouse_name
        workspace = fabric.resolve_workspace_id(workspace) or fabric.get_workspace_id()

        # Fetch lakehouse data
        data = notebookutils.lakehouse.getWithProperties(name=lakehouse_name, workspaceId=workspace)
        return data
    except Exception as e:
        if "ArtifactNotFoundException" in str(e):
            raise LakehouseNotFoundException(lakehouse_name=lakehouse_name, workspace_id=workspace)
        else:
            print(f"An error occurred while fetching lakehouse details: {e}")
            raise e

silver_lakehouse_details = parse_lakehouse_details(get_lakehouse_details(p_silver_lakehouse_name))
gold_lakehouse_details = parse_lakehouse_details(get_lakehouse_details(p_gold_lakehouse_name))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Util functions for Fabric SQL DB
def create_engine_fsql(connection_string : str):
    token = notebookutils.credentials.getToken('https://analysis.windows.net/powerbi/api').encode("UTF-16-LE")
    token_struct = struct.pack(f'<I{len(token)}s', len(token), token)
    SQL_COPT_SS_ACCESS_TOKEN = 1256
    return sqlalchemy.create_engine("mssql+pyodbc://", creator=lambda: pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct}))

def connect_to_fabric_sql_db(connection_string):
    engine = create_engine_fsql(connection_string)
    connection = engine.connect()
    return connection

def get_fabric_sql_database_info(db_display_name, workspace: str = None):
    """
    Get the fully qualified database name (with GUID) and server FQDN for a Fabric SQL database

    Parameters:
    db_display_name (str): The display name of the database as shown in the Fabric UI

    Returns:
    dict: A dictionary containing 'database_name' (with GUID) and 'server_fqdn'
    """

    workspace_id = fabric.resolve_workspace_id(workspace) or fabric.get_workspace_id()

    fabric_client = fabric.FabricRestClient()

    response = fabric_client.get(f"/v1/workspaces/{workspace_id}/sqlDatabases")
    sql_databases = json.loads(response.text)

    for db in sql_databases['value']:
        if db['displayName'] == db_display_name:
            return {
                'database_name': db['properties']['databaseName'],
                'server_fqdn': db['properties']['serverFqdn']
            }

    return None

# MARKDOWN ********************

# ### Build Spark Session and Logger

# CELL ********************

spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "True")
spark.conf.set("spark.microsoft.delta.merge.lowShuffle.enabled", "true")
spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInWrite", "CORRECTED")
spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInRead", "CORRECTED")
spark.conf.set("spark.sql.parquet.datetimeRebaseModeInRead", "CORRECTED")
spark.conf.set("spark.sql.parquet.datetimeRebaseModeInWrite", "CORRECTED")
spark.conf.set("spark.sql.parquet.int96RebaseModeInWrite", "CORRECTED")
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")

# Setup Logger
log_folder_path = get_log_file_path(silver_lakehouse_details['tables_path'])
log_file_path = f'{log_folder_path}{p_guid}'
print(f"Logs will be saved at {log_file_path}")

# Create logger object
logger = DataFrameLogger(
    log_file_path = log_file_path,
    guid = p_guid,
    log_columns = DEFAULT_LOG_COLUMNS,
    prefix = p_CDSViewName,
    runtime_context = notebookutils.runtime.context,
    stage = "S2G",
    system_name = ""
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

database_info = get_fabric_sql_database_info(p_metadata_database_name)
full_database_name = database_info['database_name']
server_name = database_info['server_fqdn']
connection_string = FABRIC_SQL_CONNECTION_STRING_TEMPLATE.format(
    sql_endpoint=server_name,
    full_db_name=full_database_name
)
print (f"connection_string={connection_string}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

cube_metadata_query = f"SELECT Distinct FactTable, DimensionTable, JoinCondition, SKColumn, DimColumns, JoinOrder FROM dbo.cubeMetadata where FactTable = '{p_CDSViewName}' ORDER BY JoinOrder FOR JSON PATH"
conn = connect_to_fabric_sql_db(connection_string)

cube_tables_data = execute_sql_query_fsql(conn, cube_metadata_query)
p_cubeConfig = parse_query_output(cube_tables_data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

date_dimension_name = "I_DATE"
date_dimension_path = gold_lakehouse_details["tables_path"] + date_dimension_name

does_date_dimension_exist = check_if_table_exists(spark, date_dimension_path, logger)

if not does_date_dimension_exist:
    logger.info("Creating Date Dimension Table in Gold Lakehouse.")
    # Define the start and end date for the date table
    start_date = "2015-01-01"
    end_date = "2030-12-31"

    # Create a DataFrame with a sequence of dates between start_date and end_date
    date_df = spark.createDataFrame([(start_date, end_date)], ["start", "end"]) \
        .withColumn("start", F.col("start").cast(DateType())) \
        .withColumn("end", F.col("end").cast(DateType())) \
        .withColumn("date", F.explode(F.sequence(F.col("start"), F.col("end"), F.expr('INTERVAL 1 DAY'))))

    # Extract year, month, day, day of week, and other date components
    date_df = date_df.withColumn("year", F.year(F.col("date"))) \
        .withColumn("month", F.month(F.col("date"))) \
        .withColumn("day", F.dayofmonth(F.col("date"))) \
        .withColumn("day_of_week", F.dayofweek(F.col("date"))) \
        .withColumn("day_name", F.date_format(F.col("date"), "EEEE")) \
        .withColumn("month_name", F.date_format(F.col("date"), "MMMM")) \
        .drop("start", "end")

    date_df.write.format("delta").mode("overwrite").save(date_dimension_path)
else:
    logger.info("Date Dimension Table already exists in Gold Lakehouse.")

date_df = DeltaTable.forPath(spark, date_dimension_path)
date_df = date_df.toDF()
date_df = date_df.withColumnRenamed("date", "VALIDITYSTARTDATE")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exg_rate_table_path = silver_lakehouse_details["tables_path"] + p_CDSViewName

# Validate that the exchange rate fact table exists as a valid delta table
validate_delta_table(
    spark=spark,
    table_path=silver_lakehouse_details["tables_path"],
    p_CDSViewName=p_CDSViewName,
    logger=logger
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exg_rate_fact = DeltaTable.forPath(spark, exg_rate_table_path)
exg_rate_fact_df = exg_rate_fact.toDF()
exg_rate_fact_df = exg_rate_fact_df.drop(F.col("MANDT"))

# Loading data to gold DF
gold_fact_path = gold_lakehouse_details["tables_path"] + p_CDSViewName

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Convert VALIDITYSTARTDATE column to date
exg_rate_fact_df = exg_rate_fact_df.withColumn("VALIDITYSTARTDATE", F.to_date(F.col("VALIDITYSTARTDATE"), "yyyyMMdd"))

# If the Exchange rate value is negative then invert it.
exg_rate_fact_df = exg_rate_fact_df.withColumn(
    "EXCHANGERATE", 
    F.when(F.col("EXCHANGERATE") < 0, 1 / F.abs(F.col("EXCHANGERATE")))
    .otherwise(F.col("EXCHANGERATE"))
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Get distinct currency pairs
currency_pairs = exg_rate_fact_df.select("EXCHANGERATETYPE", "SOURCECURRENCY", "TARGETCURRENCY").distinct()

# Create a DataFrame with all combinations of currency pairs and dates
daily_rates = currency_pairs.crossJoin(date_df)

# Perform a left join to merge daily rates with original TCURR data to fill in known rates
exg_rate_fact_df = daily_rates.join(exg_rate_fact_df, on=["EXCHANGERATETYPE", "SOURCECURRENCY", "TARGETCURRENCY", "VALIDITYSTARTDATE"], how="left")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Mapping Source currency to itself.

# CELL ********************

required_columns = ['EXCHANGERATETYPE','SOURCECURRENCY', 'TARGETCURRENCY', 'VALIDITYSTARTDATE', 'EXCHANGERATE', 'NUMBEROFSOURCECURRENCYUNITS', 'NUMBEROFTARGETCURRENCYUNITS', '_SystemName','_UpdateTimeStamp']

# Get distinct currencies from both SOURCECURRENCY and TARGETCURRENCY
distinct_source_currencies = exg_rate_fact_df.select("EXCHANGERATETYPE", "_SystemName", "SOURCECURRENCY").distinct()
distinct_source_currencies = distinct_source_currencies.filter(F.isnotnull(F.col("_SystemName")))
distinct_source_currencies = distinct_source_currencies.withColumn("TARGETCURRENCY", F.col("SOURCECURRENCY"))

# Cross join with the date range DataFrame
daily_rates_same_currency = distinct_source_currencies.crossJoin(date_df)
daily_rates_same_currency = daily_rates_same_currency.withColumn("EXCHANGERATE", F.lit(1.0))
daily_rates_same_currency = daily_rates_same_currency.withColumn("NUMBEROFSOURCECURRENCYUNITS", F.lit(1.0))
daily_rates_same_currency = daily_rates_same_currency.withColumn("NUMBEROFTARGETCURRENCYUNITS", F.lit(1.0))
daily_rates_same_currency = daily_rates_same_currency.withColumn("_UpdateTimeStamp", F.lit(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))

daily_rates_same_currency = daily_rates_same_currency.select(*required_columns).orderBy(F.col("VALIDITYSTARTDATE"))

# Show the result
display(daily_rates_same_currency)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exg_rate_fact_df = exg_rate_fact_df.select(*required_columns)
daily_rates_same_currency = daily_rates_same_currency.select(*required_columns)

exg_rate_fact_df = exg_rate_fact_df.union(daily_rates_same_currency)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Fill missing rates by carrying forward the last available rate for each currency pair using Window functions
window_spec = Window.partitionBy("EXCHANGERATETYPE", "SOURCECURRENCY", "TARGETCURRENCY").orderBy("VALIDITYSTARTDATE")

# Fill forward the UKURS column
exg_rate_fact_df = exg_rate_fact_df.withColumn("EXCHANGERATE", F.last("EXCHANGERATE", ignorenulls=True).over(window_spec))
exg_rate_fact_df = exg_rate_fact_df.withColumn("NUMBEROFSOURCECURRENCYUNITS", F.last("NUMBEROFSOURCECURRENCYUNITS", ignorenulls=True).over(window_spec))
exg_rate_fact_df = exg_rate_fact_df.withColumn("NUMBEROFTARGETCURRENCYUNITS", F.last("NUMBEROFTARGETCURRENCYUNITS", ignorenulls=True).over(window_spec))
exg_rate_fact_df = exg_rate_fact_df.withColumn("_UpdateTimeStamp", F.last("_UpdateTimeStamp", ignorenulls=True).over(window_spec))
exg_rate_fact_df = exg_rate_fact_df.withColumn("_SystemName", F.last("_SystemName", ignorenulls=True).over(window_spec))

# Show the new daily conversion rate table
# display(exg_rate_fact_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

p_cubeConfig = json.loads(p_cubeConfig)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Validate that all fact and dimension tables from cubeConfig exist as valid delta tables
validated_tables = set()
for config in p_cubeConfig:
    fact_table = config['FactTable']
    dim_table = config['DimensionTable']

    if fact_table not in validated_tables:
        validate_delta_table(
            spark=spark,
            table_path=silver_lakehouse_details["tables_path"],
            p_CDSViewName=fact_table,
            logger=logger
        )
        validated_tables.add(fact_table)

    if dim_table not in validated_tables:
        validate_delta_table(
            spark=spark,
            table_path=gold_lakehouse_details["tables_path"],
            p_CDSViewName=dim_table,
            logger=logger
        )
        validated_tables.add(dim_table)

# CELL ********************

row_count = exg_rate_fact_df.count()
# Check the number of rows to be processed
partition_columns = ["EXCHANGERATETYPE", "SOURCECURRENCY"]

if row_count > 0:
    logger.info(f"Processing {row_count} rows.")

    if row_count > 200000:
        logger.info(f"Partitioning the table using column {partition_columns}")
        exg_rate_fact_df = exg_rate_fact_df.repartition(8, partition_columns)
        exg_rate_fact_df.groupBy(F.spark_partition_id()).count().show()

    # Iterate and join with each dimension
    for config in p_cubeConfig:
        # Loading data to gold DF
        gold_dim_path = gold_lakehouse_details["tables_path"] + config['DimensionTable']
        if check_if_table_exists(spark, gold_dim_path, logger):
            gold_dim_dt = DeltaTable.forPath(spark, gold_dim_path)
            gold_dim_df = gold_dim_dt.toDF()

            # Filter out fiscal period rows where the period spans only 1 day (special/adjustment periods)
            if config['DimensionTable'] == "I_FISCALPERIODFORVARIANT":
                gold_dim_df = gold_dim_df.filter(
                    F.datediff(F.col("FISCALPERIODENDDATE"), F.col("FISCALPERIODSTARTDATE")) > 1
                )

            extra_dim_cols = []
            if "DimColumns" in config and len(config["DimColumns"]) > 0:
                extra_dim_cols = ast.literal_eval(config["DimColumns"])

            exg_rate_fact_df = apply_join_conditions(
                fact_name = p_CDSViewName,
                dimension_name = config['DimensionTable'],
                fact_df = exg_rate_fact_df,
                dimension_df = gold_dim_df,
                join_conditions = config["JoinCondition"],
                sk_column = config["SKColumn"],
                extra_dim_cols=extra_dim_cols,
                logger = logger)

            # print(exg_rate_fact_df.schema)
        else:
            logger.info(f"dimension table not found at path {gold_dim_path}, skipping surrogate key creation.")

display(exg_rate_fact_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exg_rate_fact_df = exg_rate_fact_df.withColumn("NUMBEROFSOURCECURRENCYUNITS", exg_rate_fact_df["NUMBEROFSOURCECURRENCYUNITS"].cast(DoubleType()))
exg_rate_fact_df = exg_rate_fact_df.withColumn("NUMBEROFTARGETCURRENCYUNITS", exg_rate_fact_df["NUMBEROFTARGETCURRENCYUNITS"].cast(DoubleType()))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exchange_rate_table = gold_lakehouse_details["tables_path"] + p_CDSViewName + "_DAILY"
logger.info(f"Saving Exchange rate file in path: {exchange_rate_table}")
exg_rate_fact_df.write.format("delta").mode("overwrite").save(exchange_rate_table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Group by multiple columns and calculate the average exchange rate
# Get all column names except the 'ExchangeRate' column
group_columns = []

exg_rate_fact_df = exg_rate_fact_df.drop("VALIDITYSTARTDATE")

exclude_columns = set(["EXCHANGERATE", "VALIDITYSTARTDATE"])

for column in exg_rate_fact_df.columns:
    if column not in exclude_columns:
        group_columns.append(column) 

print(group_columns)

df_grouped = exg_rate_fact_df.groupBy(group_columns) \
               .agg(F.avg("EXCHANGERATE").alias("AVGEXCHANGERATE"))

display(df_grouped)

exchange_rate_grouped_table = gold_lakehouse_details["tables_path"] + p_CDSViewName + "_FISCALPERIOD"
logger.info(f"Saving Exchange rate file in path: {exchange_rate_grouped_table}")
df_grouped.write.format("delta").mode("overwrite").save(exchange_rate_grouped_table)

logger.save_logs(spark=spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
