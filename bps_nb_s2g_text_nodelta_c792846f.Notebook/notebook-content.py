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

# ##### Import Module

# CELL ********************

import ast
import json

import sempy.fabric as fabric
from delta import DeltaTable
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max

from common_lib.constants import DEFAULT_LOG_COLUMNS
from common_lib.logger.dataframe_logger import DataFrameLogger
from common_lib.utils import create_delta_file_in_gold, get_null_safe_join_condition, parse_lakehouse_details, \
    get_iso_language_expression, get_log_file_path, validate_required_params, validate_delta_table, \
        validate_watermark_columns, validate_duplicate_primary_keys
from common_lib.exceptions import LakehouseNotFoundException, DeltaTableNotFoundException, DuplicateEntriesInTable, \
WaterMarkColumnsNotFound, RecordCountMismatchException
from pyspark.sql.utils import AnalysisException, PythonException, QueryExecutionException, IllegalArgumentException, ParseException
from pyspark.sql.types import StringType
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
spark.conf.set('spark.native.enabled', 'true')

# Setup Logger
log_folder_path = get_log_file_path(silver_lakehouse_details['tables_path'])
log_file_path = f'{log_folder_path}{p_guid}'
print(f"Logs will be saved at {log_file_path}")

# Create logger object
logger = DataFrameLogger(
    log_file_path = log_file_path,
    guid = p_guid,
    log_columns = DEFAULT_LOG_COLUMNS,
    prefix="Dim Text No Delta",
    runtime_context = notebookutils.runtime.context,
    stage = "S2G",
    system_name = p_system_name
)

exit_message = f"Processing for No-Delta Text Dimensions completed successfully."
error_message = None

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Function to process Text No-Delta Dimension

# CELL ********************

def process_no_delta_text_data(
    p_CDSViewName: str,
    p_relatedCDSViewName: str,
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
            isDeltaTable=False,
            logger=logger
        )

        # Loading data to gold DF
        gold_dim_path = p_gold_tables_path + p_CDSViewName

        does_gold_dim_exist = DeltaTable.isDeltaTable(spark, gold_dim_path)
        print(f"Does Gold Table Exist : {does_gold_dim_exist}")
        silver_schema = silver_dim_df.schema
        silver_columns = silver_dim_df.columns
        print(f"Current columns in Silver dataframe are {silver_columns}")
        if does_gold_dim_exist == False and 'LANGUAGE' in silver_columns and '_ISOLanguage' not in silver_columns:
            silver_schema.add("_ISOLanguage", StringType(), False)
            print(f"Schema for Silver Dataframe after adding column : {silver_schema}")
            silver_dim_df_new = spark.createDataFrame([], schema=silver_schema)

            # check and create delta file in gold layer
            is_new_file_created = create_delta_file_in_gold(
                spark = spark,
                delta_file_path = gold_dim_path,
                silver_df = silver_dim_df_new,
                create_empty_df = True,
                logger = logger)


        # check and create delta file in gold layer
        is_new_file_created = create_delta_file_in_gold(
            spark = spark,
            delta_file_path = gold_dim_path,
            silver_df = silver_dim_df,
            create_empty_df = True,
            logger = logger)

        gold_dim = DeltaTable.forPath(spark, gold_dim_path)
        gold_dim_df = gold_dim.toDF()

        # Loading master data table
        md_dim_path = p_gold_tables_path + p_relatedCDSViewName
        md_dim = DeltaTable.forPath(spark, md_dim_path)
        md_dim_df = md_dim.toDF()


        # Select the highest processing timestamp for each _SystemName
        # Group by _SystemName
        system_name_df = silver_dim_df.groupBy("_SystemName")

        # Calculate the highest _UpdateTimestamp for each group:
        max_timestamp_df = system_name_df.agg(max("_UpdateTimestamp").alias("MaxTimestamp"))

        # Alias both DataFrames
        silver_dim_df = silver_dim_df.alias("a")
        max_timestamp_df = max_timestamp_df.alias("b")

        # Now, join this DataFrame back with the original DataFrame to get the desired rows
        silver_dim_df = silver_dim_df.join(
            max_timestamp_df,
            [
                col("a._SystemName") == col("b._SystemName"),
                col("a._UpdateTimestamp") == col("b.MaxTimestamp")
            ],
            "inner") \
            .select("a.*")

        #Check the number of rows to be processed
        rows_to_process = silver_dim_df.count()
        if rows_to_process > 0:
            logger.info(f"Processing {rows_to_process} rows for {p_CDSViewName}.")

            # Join to retrieve existing surrogate keys using primary key fields
            silver_key_alias = 'silver_key'
            master_key_alias = 'master_key'
            silver_key_df = silver_dim_df.alias(silver_key_alias)
            master_key_df = md_dim_df.select(*p_key_fields_arr, 'Key').alias(master_key_alias)
            join_condition = get_null_safe_join_condition(
                silver_key_df,
                master_key_df,
                p_key_fields_arr
            )
            gold_dim_df = silver_key_df.join(
                master_key_df,
                on=join_condition,
                how='left') \
                .select(
                    f"{silver_key_alias}.*",
                    col(f"{master_key_alias}.Key").alias("Key")
                )

            # validate if there are any duplicate rows in the table
            if 'LANGUAGE' in gold_dim_df.columns:
                unique_key_columns = p_key_fields_arr + ['LANGUAGE']
            else:
                unique_key_columns = p_key_fields_arr

            validate_duplicate_primary_keys(
                spark=spark,
                table_path=p_silver_tables_path,
                p_CDSViewName=p_CDSViewName,
                df=gold_dim_df,
                primary_key_columns=unique_key_columns,
                logger=logger
            )

            # Check if the DataFrame contains the 'LANGUAGE' column
            if 'LANGUAGE' in gold_dim_df.columns:
                # Define the case-when logic for the '_ISOLanguage' column
                _ISOLanguage_expr = get_iso_language_expression()

                # Add the '_ISOLanguage' column to the DataFrame
                gold_dim_df = gold_dim_df.withColumn('_ISOLanguage', _ISOLanguage_expr)
                logger.info("Added Language column to gold dimension df")

            gold_dim_df.write.format("delta") \
                .mode("overwrite") \
                .option("mergeSchema", "true") \
                .save(gold_dim_path)

            logger.info(f"Written {gold_dim_df.count()} rows.")

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

# ##### Code to process Input Parameters and call Process Text No-Delta Dimension Function.

# CELL ********************

processed_input = json.loads(p_lookup_output)
full_error_message = ""

logger.info("Starting Processing for Dimension Text No Delta.")
# logger.info(p_lookup_output)

for input in processed_input:
    try:

        p_CDSViewName = input["CDSViewName"]
        p_relatedCDSViewName = input["relatedCDSViewName"]
        p_key_fields = input["KeyFields"]

        p_keyFields_arr = ast.literal_eval(p_key_fields)
        p_keyFields_arr.append('_SystemName')

        p_keyFields_dm = p_keyFields_arr.copy()
        if 'LANGUAGE' in p_keyFields_dm:
            p_keyFields_dm.remove('LANGUAGE')

        logger.prefix = p_CDSViewName
        logger.info(f"Start processing for {p_CDSViewName}")
        error_message = process_no_delta_text_data(
            p_CDSViewName,
            p_relatedCDSViewName,
            p_keyFields_dm,
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
