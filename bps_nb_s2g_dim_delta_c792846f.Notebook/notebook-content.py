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

# ##### Input Parameters

# PARAMETERS CELL ********************

p_lookup_output = ""
p_guid = ""
p_system_name = ""
p_gold_lakehouse_name = ""
p_silver_lakehouse_name = ""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Import Modules

# CELL ********************

import ast
import json

from delta import DeltaTable
import sempy.fabric as fabric
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max, row_number, when
from pyspark.sql.window import Window

from common_lib.constants import DEFAULT_LOG_COLUMNS
from common_lib.expression_helper import get_merge_condition
from common_lib.logger.dataframe_logger import DataFrameLogger
from common_lib.utils import create_delta_file_in_gold, get_log_file_path, get_null_safe_join_condition, parse_lakehouse_details, \
    validate_required_params, validate_delta_table, validate_watermark_columns, \
    validate_duplicate_primary_keys, validate_record_count_match
from common_lib.exceptions import LakehouseNotFoundException, DeltaTableNotFoundException, DuplicateEntriesInTable, \
WaterMarkColumnsNotFound, RecordCountMismatchException
from pyspark.sql.utils import AnalysisException, PythonException, QueryExecutionException, IllegalArgumentException, ParseException

import notebookutils

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Initial Validations

# CELL ********************

validate_required_params(
    p_silver_lakehouse_name=p_silver_lakehouse_name,
    p_gold_lakehouse_name=p_gold_lakehouse_name,
    p_lookup_output=p_lookup_output
)

# MARKDOWN ********************

# ##### Common Helper Functions

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

silver_lakehouse_details = parse_lakehouse_details(get_lakehouse_details(p_silver_lakehouse_name))
gold_lakehouse_details = parse_lakehouse_details(get_lakehouse_details(p_gold_lakehouse_name))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Setup Spark Session and Logger

# CELL ********************

spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
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
    prefix="Delta Notebook",
    runtime_context = notebookutils.runtime.context,
    stage = "S2G",
    system_name = p_system_name
)

exit_message = f"Processing for Delta Dimensions completed successfully."
error_message = None

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Function to process Dimension (Delta Enabled)

# CELL ********************

def process_delta_data(
    p_CDSViewName: str,
    p_key_fields_arr: list,
    p_silver_tables_path: str,
    p_gold_tables_path: str,
):

    try:
        err_message = None
        # Defining paths
        silver_dim_path = p_silver_tables_path + p_CDSViewName

        # Validate if delta table exists or not.
        validate_delta_table(
            spark=spark,
            table_path=p_silver_tables_path,
            p_CDSViewName=p_CDSViewName,
            logger=logger
        )

        # Loading data to silver DF
        silver_dim = DeltaTable.forPath(spark, silver_dim_path)
        silver_dim_df = silver_dim.toDF()

        # check if table has proper watermark columns
        validate_watermark_columns(
            spark=spark,
            table_path=p_silver_tables_path,
            p_CDSViewName=p_CDSViewName,
            df=silver_dim_df,
            isDeltaTable=True,
            logger=logger
        )

        # Loading data to gold DF
        gold_dim_path = p_gold_tables_path + p_CDSViewName

        # check and create delta file in gold layer
        is_new_file_created = create_delta_file_in_gold(
            spark = spark,
            delta_file_path = gold_dim_path,
            silver_df = silver_dim_df,
            create_empty_df = False,
            logger = logger)

        gold_dim = DeltaTable.forPath(spark, gold_dim_path)
        gold_dim_df = gold_dim.toDF()

        max_timestamp = None
        if not is_new_file_created and gold_dim_df.limit(1).count() > 0:
            # Calculate the highest processing timestamp from the gold layer
            max_timestamp_row = gold_dim_df.agg(max("_UpdateTimestamp").alias("maxTimestamp")).collect()[0]
            max_timestamp = max_timestamp_row['maxTimestamp']
            logger.info(f"Max gold timestamp: {max_timestamp}")

        # Filter silver_dim_df based on the last processed timestamp
        if max_timestamp is not None:
            logger.info(f"Filtering silver fact DF based on max timestamp: {max_timestamp}")
            silver_dim_df = silver_dim_df.filter(col('_UpdateTimestamp') > max_timestamp)

        # Check the number of rows to be processed
        rows_to_process = silver_dim_df.count()
        if rows_to_process > 0:
            logger.info(f"Processing {rows_to_process} rows.")

            # Checking the highest assigned surrogate key
            if gold_dim_df.limit(1).count() > 0:
                max_sk_row = gold_dim_df.agg(max("Key").alias("maxKey")).collect()[0]
                if max_sk_row['maxKey'] is not None:
                    max_sk = max_sk_row['maxKey']
                else:
                    max_sk = -1

            # If max_sk is -1, start from 1, else continue from max_sk + 1
            if max_sk == -1:
                start_sk = 1
            else:
                start_sk = max_sk + 1

            logger.info(f"Starting surrogate key: {start_sk}, max surrogate key: {max_sk}")

            # Join to retrieve existing surrogate keys using primary key fields
            silver_key_alias = 'silver_key'
            gold_key_alias = 'gold_key'
            silver_key_df = silver_dim_df.alias(silver_key_alias)
            gold_key_df = gold_dim_df.select(*p_key_fields_arr, 'Key').alias(gold_key_alias)
            join_condition = get_null_safe_join_condition(
                silver_key_df,
                gold_key_df,
                p_key_fields_arr
            )
            joined_df = silver_key_df.join(
                gold_key_df,
                on=join_condition,
                how='left') \
                .select(
                    f"{silver_key_alias}.*",
                    col(f"{gold_key_alias}.Key").alias("Key")
                )

            # Window specification for generating new surrogate keys
            window_spec = Window \
                .orderBy(*p_key_fields_arr) \
                .rowsBetween(Window.unboundedPreceding, Window.currentRow)

            # Generate surrogate keys where needed and retain existing keys
            silver_dim_df = joined_df.withColumn(
                'Key',
                when(
                    col('Key').isNull(),
                    row_number().over(window_spec) + start_sk - 1
                ).otherwise(col('Key')))

            # validate if there are any duplicate rows in the table
            validate_duplicate_primary_keys(
                spark=spark,
                table_path=p_silver_tables_path,
                p_CDSViewName=p_CDSViewName,
                df=silver_dim_df,
                primary_key_columns=p_key_fields_arr,
                logger=logger
            )

            silver_dim_alias = 'silver_dim'
            gold_dim_alias = 'gold_dim'

            # Create merge condition string using primary key fields
            merge_condition = get_merge_condition(
                merge_keys = p_key_fields_arr,
                right_alias = silver_dim_alias,
                left_alias = gold_dim_alias)
            logger.debug(f"Merge condition: {merge_condition}")

            if is_new_file_created:
                silver_dim_df = silver_dim_df.where(col("_Delete") != "X")

            gold_dim \
                .alias(gold_dim_alias) \
                .merge(
                    source=silver_dim_df.alias(silver_dim_alias),
                    condition=merge_condition
                ) \
                .whenMatchedDelete(condition=f"{silver_dim_alias}._Delete = 'X'") \
                .whenMatchedUpdateAll(condition=f"{silver_dim_alias}._Delete != 'X'") \
                .whenNotMatchedInsertAll(condition=f"{silver_dim_alias}._Delete != 'X'") \
                .execute()
            logger.info(f"All {rows_to_process} rows processed")

            validate_record_count_match(
                spark=spark,
                p_CDSViewName=p_CDSViewName,
                table_path_1=p_silver_tables_path,
                table_path_2=p_gold_tables_path,
                logger=logger
            )

        else:
            logger.info("No rows to process")

    except (AnalysisException, PythonException, QueryExecutionException, IllegalArgumentException, ParseException) as exp:
        err_message = f"Dimension Processing for {p_CDSViewName} failed due to error: {exp.desc}"
        logger.error(err_message)

    except Exception as exception:
        err_message = f"Dimension Processing for {p_CDSViewName} failed due to error: {exception}"
        logger.error(err_message)

    finally:
        return err_message

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Code to process Input Parameters and call Process Dimension Function.

# CELL ********************

processed_input = json.loads(p_lookup_output)
full_error_message = ""

for input in processed_input:
    try:
        p_CDSViewName = input["CDSViewName"]
        p_key_fields = input["KeyFields"]
        p_key_fields_arr = ast.literal_eval(p_key_fields)
        p_key_fields_arr.append('_SystemName')

        logger.prefix = p_CDSViewName

        logger.info(f"Start processing for {p_CDSViewName}")
        error_message = process_delta_data(
            p_CDSViewName,
            p_key_fields_arr,
            silver_lakehouse_details['tables_path'],
            gold_lakehouse_details['tables_path']
        )
        logger.info(f"Processing completed for {p_CDSViewName}")

        # if return value if not None, then it means the processing failed.
        if error_message:
            full_error_message += "[Failed] - " + error_message[:500] + "... | "

    except Exception as exception:
        err_message = f"[Failed] - Dimension Processing for {p_CDSViewName} failed due to error: {exception}"
        logger.error(err_message)
        full_error_message += err_message[:500] + "... | "

    finally:
        logger.save_logs(spark=spark)
        if len(full_error_message) > 0:
            exit_message = full_error_message

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.exit(value = exit_message)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
