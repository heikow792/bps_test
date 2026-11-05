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

p_guid = ""
p_gold_lakehouse_name = ""
p_silver_lakehouse_name = ""
p_CDSViewName = ""
p_keyFields = ""
p_cubeConfig = ""
p_system_name = ""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Import required python modules.

# CELL ********************

import ast
import json

from delta import DeltaTable
from functools import reduce
from operator import or_
import sempy.fabric as fabric
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max, when, lit
from pyspark.sql import functions as F

from common_lib.constants import DEFAULT_LOG_COLUMNS
from common_lib.expression_helper import get_merge_condition
from common_lib.logger.dataframe_logger import DataFrameLogger
from common_lib.utils import apply_join_conditions, create_delta_file_in_gold, get_log_file_path, check_if_table_exists,\
    get_reprocess_condition, parse_lakehouse_details, validate_required_params, validate_delta_table, validate_cube_config, validate_watermark_columns
from common_lib.exceptions import LakehouseNotFoundException, CubeConfigValidationFailed, DeltaTableNotFoundException, WaterMarkColumnsNotFound
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
    p_CDSViewName=p_CDSViewName,
    p_keyFields=p_keyFields,
    p_cubeConfig=p_cubeConfig
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

# add system name column to the key fields array
p_keyFields_arr = ast.literal_eval(p_keyFields)
p_keyFields_arr.append('_SystemName')

# serialize the cube config json input.
p_cubeConfig = json.loads(p_cubeConfig)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Setup for Logger and spark session

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
    prefix = p_CDSViewName,
    runtime_context = notebookutils.runtime.context,
    stage = "S2G",
    system_name = p_system_name
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# after loading the json, if the array for cube config is empty, then stop the processing.
if len(p_cubeConfig) == 0:
    error_message = f"[EMPTY CUBE CONFIG] - Fact processing failed for {p_CDSViewName}, recieved empty p_cubeConfig. " + \
        "Please make sure relationships are defined for this fact table and try again."
    logger.error(error_message)
    logger.save_logs(spark=spark)
    raise Exception(error_message)

# Validate if delta table exists or not.
validate_delta_table(
    spark=spark,
    table_path=silver_lakehouse_details['tables_path'],
    p_CDSViewName=p_CDSViewName,
    logger=logger
)

# check if the cube config is valid
validate_cube_config(
    spark=spark,
    p_CDSViewName=p_CDSViewName,
    p_cubeConfig=p_cubeConfig,
    p_silver_tables_path=silver_lakehouse_details['tables_path'],
    p_gold_tables_path=gold_lakehouse_details['tables_path'],
    logger=logger
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Process Fact Table
# 
# Before processing the fact table we first verify if the fact table is created in the gold lakehouse or not, if it is not created then we create an empty table in the gold lakehouse.
# We also fetch the latest timestamp in the gold delta table and consider records which are older than the latest timestamp from processing.

# CELL ********************

gold_lakehouse_details['tables_path']

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exit_message = f"Processing for Fact {p_CDSViewName} completed successfully."
error_message = None

# this flag is used to identify whether we are processing the fact for the first time or not.
# this indicates if this is a delta load or initial load.
# default value is false, if we create a new file in gold layer, then we set it to true.
is_new_file_created = False

try:
    # Defining paths
    silver_fact_path = silver_lakehouse_details['tables_path'] + p_CDSViewName

    # Loading data to silver DF
    silver_fact = DeltaTable.forPath(spark, silver_fact_path)
    silver_fact_df = silver_fact.toDF()

    # check if table has proper watermark columns
    validate_watermark_columns(
        spark=spark,
        table_path=silver_lakehouse_details['tables_path'],
        p_CDSViewName=p_CDSViewName,
        df=silver_fact_df,
        isDeltaTable=True,
        logger=logger
    )

    # Loading data to gold DF
    gold_fact_path = gold_lakehouse_details['tables_path'] + p_CDSViewName

    # check and create delta file in gold layer
    is_new_file_created = create_delta_file_in_gold(
        spark = spark,
        delta_file_path = gold_fact_path,
        silver_df = silver_fact_df,
        create_empty_df = True,
        logger = logger,
        is_fact_df = True)

    gold_fact = DeltaTable.forPath(spark, gold_fact_path)
    gold_fact_df = gold_fact.toDF()

    max_time_stamp = None

    # check if the gold_fact_df is empty
    if not is_new_file_created and gold_fact_df.limit(1).count() > 0:
        # Calculate the highest processing timestamp from the gold layer
        max_time_stamp_row = \
            gold_fact_df.agg(max("_UpdateTimeStamp").alias("maxTimestamp")).collect()[0]
        max_time_stamp = max_time_stamp_row['maxTimestamp']
        print(f"Max gold timestamp: {max_time_stamp}")

    # Filter silverDimDF based on the last processed timestamp
    if max_time_stamp is not None:
        logger.info(f"Filtering silver fact DF based on max timestamp: {max_time_stamp}")
        silver_fact_df = silver_fact_df.filter(
            (col('_UpdateTimeStamp') > max_time_stamp)
        )

    row_count = silver_fact_df.count()
    # Check the number of rows to be processed
    if row_count > 0:
        logger.info(f"Processing {row_count} rows.")

        if row_count > 200000:
            logger.info(f"Partitioning the table using column {p_keyFields_arr[0]}")
            silver_fact_df = silver_fact_df.repartition(8, p_keyFields_arr[0])
            silver_fact_df.groupBy(F.spark_partition_id()).count().show()

        # Iterate and join with each dimension
        for config in p_cubeConfig:
            # Loading data to gold DF
            gold_dim_path = gold_lakehouse_details['tables_path'] + config['DimensionTable']
            if check_if_table_exists(spark, gold_dim_path, logger):
                gold_dim_dt = DeltaTable.forPath(spark, gold_dim_path)
                gold_dim_df = gold_dim_dt.toDF()

                if p_CDSViewName == "C_PURCHASEORDERDEX" and config['DimensionTable'] == "I_PURCHASINGDOCUMENTTYPE":
                    gold_dim_df = gold_dim_df.filter(col('PURCHASINGDOCUMENTCATEGORY') == "F")

                extra_dim_cols = []
                if "DimColumns" in config and len(config["DimColumns"]) > 0:
                    extra_dim_cols = ast.literal_eval(config["DimColumns"])

                silver_fact_df = apply_join_conditions(
                    fact_name = p_CDSViewName,
                    dimension_name = config['DimensionTable'],
                    fact_df = silver_fact_df,
                    dimension_df = gold_dim_df,
                    join_conditions = config["JoinCondition"],
                    sk_column = config["SKColumn"],
                    extra_dim_cols = extra_dim_cols,
                    logger = logger)

                # print(silver_fact_df.schema)
            else:
                logger.info(f"dimension table not found at path {gold_dim_path}, skipping surrogate key creation.")

        silver_fact_alias = 'silver_fact'
        gold_fact_alias = 'gold_fact'

        # Create merge condition string using primary key fields
        merge_condition = get_merge_condition(
            merge_keys = p_keyFields_arr,
            right_alias = silver_fact_alias,
            left_alias = gold_fact_alias)

        if not isinstance(merge_condition, str):
            merge_condition = str(merge_condition)

        logger.info(f"Merge condition: {merge_condition}")

        required_dimension_tables = set([item["SKColumn"] for item in p_cubeConfig])
        available_silver_columns = set(silver_fact_df.columns)

        silver_fact_df = silver_fact_df.withColumn("_Reprocess", lit(False))

        reprocess_condition_list = get_reprocess_condition(p_cubeConfig, available_silver_columns)

        for condition in reprocess_condition_list:
            logger.info(f"Applying condition : {condition}")

            filtered_df = silver_fact_df.filter(condition)
            #filtered_df_count = filtered_df.count()

            # print("Count of filtered rows:", filtered_df_count)
            silver_fact_df = silver_fact_df.withColumn(
                "_Reprocess", when(condition, True).otherwise(col('_Reprocess'))
            )

        # display(silver_fact_df)
        logger.info("Starting merge operation.")
        gold_fact \
            .alias(gold_fact_alias) \
            .merge(
                source=silver_fact_df.alias(silver_fact_alias),
                condition=merge_condition
            ) \
            .whenMatchedDelete(condition=f"{silver_fact_alias}._Delete = 'X'") \
            .whenMatchedUpdateAll(condition=f"{silver_fact_alias}._Delete != 'X'") \
            .whenNotMatchedInsertAll(condition=f"{silver_fact_alias}._Delete != 'X'") \
            .execute()

        logger.info(f"Written {silver_fact_df.count()} rows")

    else:
        logger.info("No rows to process")

except (AnalysisException, PythonException, QueryExecutionException, IllegalArgumentException, ParseException) as exp:
    error_message = f"Fact Processing for {p_CDSViewName} failed due to error: {exp.desc}"
    logger.error(error_message)
    logger.save_logs(spark=spark)
    notebookutils.notebook.exit(value = error_message)

except Exception as exception:
    logger.error(str(exception))
    logger.save_logs(spark=spark)
    raise exception

finally:
    logger.save_logs(spark=spark)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

try:
    if not is_new_file_created and check_if_table_exists(spark, gold_fact_path, logger):
        print(gold_fact_path)
        gold_fact_dt = DeltaTable.forPath(spark, gold_fact_path)
        gold_fact_df = gold_fact_dt.toDF()

        gold_columns = set(gold_fact_df.columns)

        req_gold_columns = [col for col in gold_columns if "_key" not in col]
        key_columns = [col for col in gold_columns if "_key" in col.lower()]

        gold_fact = DeltaTable.forPath(spark, gold_fact_path)

        req_gold_columns.sort()

        # check if the gold_fact_df is empty
        if gold_fact_df.limit(1).count() > 0 and "_Reprocess" in gold_columns:

            # Build the condition: TRUE if ANY of the identified key columns are null
            # This creates a chain like: (col('_Key_A').isNull() | col('_Key_B').isNull() | ...)
            if key_columns:
                # Get the list of individual null checks (e.g., [col('C1').isNull(), col('C2').isNull(), ...])
                null_conditions = [col(c).isNull() for c in key_columns]

                # Use reduce to apply the OR operator ('|') across all conditions
                any_key_is_null_condition = reduce(or_, null_conditions)
            else:
                # Handle the case where no '_key_' columns are found (filter won't add any rows based on null)
                # Using 'lit(False)' ensures the OR condition evaluates to False if no key columns exist.
                from pyspark.sql.functions import lit
                any_key_is_null_condition = lit(False)

            # Combine the two main conditions with OR ('|')
            # (Reprocess is True) OR (Any Key Column is Null)
            final_filter_condition = (col("_Reprocess") == True) | any_key_is_null_condition
            logger.info(f"Filter Condition for reprocess rows: {final_filter_condition}")

            # Apply the final filter and select the required columns
            reprocess_gold = gold_fact_df.filter(final_filter_condition).select(req_gold_columns)

            row_count = reprocess_gold.count()

            if row_count > 0:
                logger.info(f"Processing {row_count} rows.")

                if row_count > 200000:
                    logger.info(f"Partitioning the table using column {p_keyFields_arr[0]}")
                    reprocess_gold = reprocess_gold.repartition(8, p_keyFields_arr[0])
                    reprocess_gold.groupBy(F.spark_partition_id()).count().show()

                # Iterate and join with each dimension
                for config in p_cubeConfig:
                    # Loading data to gold DF
                    gold_dim_path = gold_lakehouse_details['tables_path'] + config['DimensionTable']
                    if check_if_table_exists(spark, gold_dim_path, logger):
                        gold_dim_dt = DeltaTable.forPath(spark, gold_dim_path)
                        gold_dim_df = gold_dim_dt.toDF()

                        if p_CDSViewName == "C_PURCHASEORDERDEX" and config['DimensionTable'] == "I_PURCHASINGDOCUMENTTYPE":
                            gold_dim_df = gold_dim_df.filter(col('PURCHASINGDOCUMENTCATEGORY') == "F")

                        extra_dim_cols = []
                        if "DimColumns" in config and len(config["DimColumns"]) > 0:
                            extra_dim_cols = ast.literal_eval(config["DimColumns"])

                        reprocess_gold = apply_join_conditions(
                            fact_name = p_CDSViewName,
                            dimension_name = config['DimensionTable'],
                            fact_df = reprocess_gold,
                            dimension_df = gold_dim_df,
                            join_conditions = config["JoinCondition"],
                            sk_column = config["SKColumn"],
                            extra_dim_cols = extra_dim_cols,
                            logger = logger)

                silver_fact_alias = 'silver_fact'
                gold_fact_alias = 'gold_fact'

                # Create merge condition string using primary key fields
                merge_condition = get_merge_condition(
                    merge_keys = p_keyFields_arr,
                    right_alias = silver_fact_alias,
                    left_alias = gold_fact_alias)

                if not isinstance(merge_condition, str):
                    merge_condition = str(merge_condition)

                logger.info(f"Merge condition: {merge_condition}")
                available_columns = set(reprocess_gold.columns)

                reprocess_gold = reprocess_gold.withColumn("_Reprocess", lit(False))
                reprocess_condition_list = get_reprocess_condition(p_cubeConfig, available_columns)
                for condition in reprocess_condition_list:
                    logger.info(f"Applying condition : {condition}")

                    # filtered_df = reprocess_gold.filter(condition)
                    # filtered_df_count = filtered_df.count()
                    # display(filtered_df)

                    reprocess_gold = reprocess_gold.withColumn(
                        "_Reprocess", when(condition, True).otherwise(col('_Reprocess'))
                    )

                gold_fact \
                    .alias(gold_fact_alias) \
                    .merge(
                        source=reprocess_gold.alias(silver_fact_alias),
                        condition=merge_condition
                    ) \
                    .whenMatchedUpdateAll(condition=f"{silver_fact_alias}._Delete != 'X'") \
                    .execute()

                logger.info("Merge Completed for reprocessing rows.")
            else:
                logger.info("No rows marked for reprocessing.")
    elif is_new_file_created:
        logger.info("New file created in gold layer, This is initial load, no need to check for reprocessing condition.")
    else:
	    logger.info(f"Table not found in gold lakehouse. Skipping reprocessing for {p_CDSViewName}")

except (AnalysisException, PythonException, QueryExecutionException, IllegalArgumentException, ParseException) as exp:
    error_message = f"Fact Processing for {p_CDSViewName} failed due to error: {exp.desc}"
    logger.error(error_message)
    logger.save_logs(spark=spark)
    notebookutils.notebook.exit(value = error_message)

except Exception as exception:
    logger.error(str(exception))
    logger.save_logs(spark=spark)
    raise exception

finally:
    logger.save_logs(spark=spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

if error_message:
    notebookutils.notebook.exit(value = error_message)

notebookutils.notebook.exit(value = exit_message)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
