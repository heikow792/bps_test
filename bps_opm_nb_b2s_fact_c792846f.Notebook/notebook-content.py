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

# ### Input Parameters

# PARAMETERS CELL ********************

p_guid = ""
p_silver_lakehouse_name = ""
p_mirror_db_name = ""
p_source_type = "open-mirroring"
p_schema_name = "dbo"
p_sort_dataframe_by_time = "_UpdateTimeStamp"
p_CDSViewName = ""
p_keyFields = ""
p_ODPName = ""
p_system_name = ""
p_mirror_db_workspace_id = ""
p_schema_table_name = ""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Import Libraries

# CELL ********************

import json
import time
import ast


from datetime import datetime
from trident_token_library_wrapper import PyTridentTokenLibrary

from delta import DeltaTable
import sempy.fabric as fabric
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, max, cast, when, lit, row_number
from pyspark.sql.window import Window
from pyspark.sql.types import StringType, DateType, IntegerType, DecimalType, TimestampType
from pyspark.sql import DataFrame

from common_lib.constants import DEFAULT_LOG_COLUMNS
from common_lib.expression_helper import get_merge_condition
from common_lib.logger.dataframe_logger import DataFrameLogger
from common_lib.data_type_mapping import sap_data_type_mapping
from common_lib.utils import get_log_file_path, check_if_table_exists, compare_time, parse_lakehouse_details, \
	validate_required_params, standardize_column_names, apply_data_types, validate_mirrored_delta_table, parse_mirror_db_details, \
	get_max_timestamp
from common_lib.exceptions import LakehouseNotFoundException, MirroredDatabaseNotFoundException, DeltaTableNotFoundException
import notebookutils

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Initial Validations

# CELL ********************

validate_required_params(
    p_system_name=p_system_name,
    p_CDSViewName=p_CDSViewName,
    p_ODPName=p_ODPName,
    p_silver_lakehouse_name=p_silver_lakehouse_name,
    p_mirror_db_name=p_mirror_db_name,
    p_mirror_db_workspace_id=p_mirror_db_workspace_id,
    p_schema_name=p_schema_name,
    p_keyFields=p_keyFields
)

# CELL ********************

p_ODPName = p_ODPName.replace("$P", "").replace("$T", "").replace("$F", "").replace("$E", "")

# MARKDOWN ********************

# ### Common Functions

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

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def get_mirrored_database_info(db_display_name: str, logger: DataFrameLogger, workspace: str = p_mirror_db_workspace_id):
    """
    Function to retrieve mirrored database information based on the display name.
    """
    try:
        workspace = fabric.resolve_workspace_id(workspace) or fabric.get_workspace_id()
        fabric_client = fabric.FabricRestClient()

        # API call with error handling
        try:
            response = fabric_client.get(f"v1/workspaces/{workspace}/mirroredDatabases")
        except Exception as e:
            error_message = f"Failed to connect to mirrored databases API: {str(e)}"
            logger.error(error_message)
            raise e

        # Parse response with error handling
        try:
            mirror_databases = json.loads(response.text)
        except json.JSONDecodeError as e:
            error_message = f"Failed to parse mirrored databases API response: {str(e)}"
            logger.error(error_message)
            raise e

        # Process database information
        for database in mirror_databases.get('value', []):
            if database.get("displayName") == db_display_name:
                return parse_mirror_db_details(
                        database,
                        db_display_name
                    )

        logger.info(f"Mirrored Database with name - {db_display_name} not found in workspace with id - {workspace}")
        raise MirroredDatabaseNotFoundException(database_name=db_display_name, workspace_id = workspace)
    except Exception as e:
        error_message = f"Unexpected error in get_mirrored_database_info: {str(e)}"
        logger.error(error_message)
        raise e


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Setup Constants

# CELL ********************

silver_fact_path = silver_lakehouse_details['tables_path'] + p_CDSViewName
p_keyFields_arr = ast.literal_eval(p_keyFields)
p_keyFields_arr.append('_SystemName')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Setup Spark Session and Logger

# CELL ********************

# Setup Spark Session
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
log_file_path = f'{log_folder_path}{p_guid}/{p_CDSViewName}'
print(f"Logs will be saved at {log_file_path}")

# Create logger object
logger = DataFrameLogger(
    log_file_path = log_file_path,
    guid = p_guid,
    log_columns = DEFAULT_LOG_COLUMNS,
    prefix = p_CDSViewName,
    runtime_context = notebookutils.runtime.context,
    stage = "B2S",
    system_name = p_system_name
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Get Mirror Database Details

# CELL ********************

# get details about the mirrored database
mirror_db_details = get_mirrored_database_info(
    db_display_name=p_mirror_db_name,
    logger=logger,
    workspace=p_mirror_db_workspace_id
)

# MARKDOWN ********************

# ### Get Max Timestamp from Silver Lakehouse

# CELL ********************

does_silver_table_exists = check_if_table_exists(
    spark,
    silver_fact_path,
    logger
)

max_time_stamp = None

if does_silver_table_exists:
    silver_fact = DeltaTable.forPath(spark, silver_fact_path)
    silver_fact_df = silver_fact.toDF()
    silver_table_schema = silver_fact_df.schema

    max_time_stamp = get_max_timestamp(
        df = silver_fact_df,
        logger = logger,
        timestamp_column="_UpdateTimeStamp",
        system_name=p_system_name)
    logger.info(f"Max Timestamp = {max_time_stamp} from table {p_CDSViewName}.")
else:
    logger.info(f"Table {p_CDSViewName} does not exist in Silver Lakehouse {p_silver_lakehouse_name}.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# read all data from mirrored database
def get_table_schema(
    spark,
    table_name: str,
    landing_zone_path: str,
    schema_name:str,
    schema_table_name:str,
    logger):
    try:
        # create table path by appending schema and table name and landing zone path.
        table_path = f"{landing_zone_path}{schema_name}/{schema_table_name}"
        logger.info(f"Reading table from path: {table_path}")

        does_schema_table_exists = check_if_table_exists(
            spark,
            table_path,
            logger
        )

        if not does_schema_table_exists:
            err_message = f"[TABLE NOT FOUND] - Cannot find {schema_table_name} in Mirrored Database at path {table_path}"
            logger.error(err_message)
            raise Exception(err_message)

        # load the DD03ND table to get the schema of the source table.
        df = spark.read.format("delta").load(table_path)
        df = standardize_column_names(df)
        schema_table = df.where(F.col("STRUCOBJN") == table_name)

        if schema_table.limit(1).count() == 0:
            err_message = f"[SCHEMA NOT FOUND] - Schema for table {table_name} not found in schema table {schema_table_name}." + \
                f"Please make sure schema for table {table_name} exists in table {schema_table_name} in mirrored database."
            logger.error(err_message)
            raise Exception(err_message)

        schema_table = schema_table.select(*["STRUCOBJN", "FIELDNAME", "DATATYPE", "LENG", "DECIMALS"])
        schema_table = schema_table \
                    .withColumnRenamed("STRUCOBJN", "CDSViewName") \
                    .withColumnRenamed("FIELDNAME", "fieldName") \
                    .withColumnRenamed("DATATYPE", "dataType") \
                    .withColumnRenamed("LENG", "length") \
                    .withColumnRenamed("DECIMALS", "decimals")

        schema_table = schema_table.withColumn("length", schema_table["length"].cast(IntegerType()))
        schema_table = schema_table.withColumn("decimals", schema_table["decimals"].cast(IntegerType()))

        return schema_table.toJSON().collect()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        logger.save_logs(spark=spark)
        raise e

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Validate if ODP name table or CDS view name table is present in the mirror database

# CELL ********************

landing_zone_path = ""
if mirror_db_details is not None:
    landing_zone_path = mirror_db_details["abfssTablesPath"]
else:
    notebookutils.notebook.exit(value = f"Unable to find mirrored database {p_mirror_db_name}. Please check if the name is correct.")

validate_mirrored_delta_table(
    spark=spark,
    table_path=f"{landing_zone_path}{p_schema_name}/",
    p_CDSViewName= p_CDSViewName,
    p_ODPName=p_ODPName,
    logger=logger
)

# MARKDOWN ********************

# ### Process Fact Table

# CELL ********************

try:
    landing_zone_path = ""
    if mirror_db_details is not None:
        landing_zone_path = mirror_db_details["abfssTablesPath"]
    else:
        # notebookutils.notebook.exit(value = f"Unable to find mirrored database {p_mirror_db_name}. Please check if the name is correct.")
        raise Exception(f"Unable to find mirrored database {p_mirror_db_name}. Please check if the name is correct.")

    # is_partition_required: indicates if we need to partition data over latest timestamp and filter only latest records.
    is_partition_required = True

    # create table path by appending schema and table name and landing zone path.
    table_path = f"{landing_zone_path}{p_schema_name}/{p_ODPName}"
    if not check_if_table_exists(spark, table_path, logger):
        table_path = f"{landing_zone_path}{p_schema_name}/{p_CDSViewName}"
    logger.info(f"Reading table from path: {table_path}")

    if max_time_stamp is not None:
        mirrored_df = spark.read.format("delta") \
            .option("readChangeFeed", "true") \
            .option("startingTimestamp", max_time_stamp)  \
            .load(table_path)
        mirrored_df = mirrored_df.filter(col("_commit_timestamp") > max_time_stamp)
        logger.info(f"Loaded Data from Mirrored Database using Timestamp: {max_time_stamp}.")

    else:
        # if max time stamp is not present then this is initial load.
        # we need to read all data from the mirrored database.
        # after reading the table we need to update max commit timestamp to the _UpdateTimeStamp to enable incremental load for next time.
        delta_table = DeltaTable.forPath(spark, table_path)
        history_df = delta_table.history()
        max__history_time_stamp = history_df.agg({'timestamp': 'max'}).collect()[0]["max(timestamp)"]
        formatted_datetime = max__history_time_stamp.strftime('%Y-%m-%d %H:%M:%S.%f')

        # read all data from mirrored database
        mirrored_df = spark.read.format("delta") \
            .load(table_path)

        # if the mirroring partner is publishing _UpdateTimeStamp we will delete it.
        # since we using _commit_timestamp for as _UpdateTimeStamp
        if "_UpdateTimeStamp" in mirrored_df.columns:
            mirrored_df = mirrored_df.drop("_UpdateTimeStamp")

        # update _UpdateTimeStamp with max_time_stamp
        mirrored_df = mirrored_df.withColumn(
            "_UpdateTimeStamp",
            F.to_timestamp(F.lit(formatted_datetime), "yyyy-MM-dd HH:mm:ss.SSSSSS")
        )
        logger.info(f"Loaded all data from Mirrored Database.")
        is_partition_required = False

    # display(mirrored_df)
    logger.info(f"Row count after loading data = {mirrored_df.count()}")

    # below will only execute while delta loads.
    # since _commit_timestamp is only available with readChangeFeed = True
    if "_commit_timestamp" in mirrored_df.columns:
        # if the mirroring partner is publishing _UpdateTimeStamp we will delete it.
        # since we using _commit_timestamp for as _UpdateTimeStamp
        if "_UpdateTimeStamp" in mirrored_df.columns:
            mirrored_df = mirrored_df.drop("_UpdateTimeStamp")
        mirrored_df = mirrored_df.withColumnRenamed("_commit_timestamp", "_UpdateTimeStamp")

    mirrored_df = mirrored_df.withColumn("_SystemName", F.lit(p_system_name))

    if is_partition_required:
        # Create a window specification with multiple partition columns
        window_spec = Window.partitionBy(p_keyFields_arr).orderBy(col("_UpdateTimeStamp").desc())

        mirrored_df = mirrored_df.withColumn("row_num", F.row_number().over(window_spec)) \
                                    .filter(col("row_num") == 1) \
                                    .drop("row_num")
        logger.info(f"Row count after selecting latest rows data = {mirrored_df.count()}")

    if "_change_type" in mirrored_df.columns:
        # filter table, remove rows where change_type is update_preimage
        mirrored_df = mirrored_df.filter(col("_change_type").isin(["insert", "update_postimage", "delete"]))
        logger.info(f"Row count after removing pre-image data = {mirrored_df.count()}")

        # create a new column _Delete and mark deleted columns.
        mirrored_df = mirrored_df.withColumn("_Delete", when(col("_change_type") == "delete", lit("X")).otherwise(lit("")))
    else:
        # create a new column _Delete and mark deleted columns.
        mirrored_df = mirrored_df.withColumn("_Delete", lit(""))

    bronze_spark_df = mirrored_df

except Exception as e:
    error_message = f"Unexpected error during merge process: {str(e)}"
    logger.error(error_message)
    logger.save_logs(spark=spark)
    raise e
finally:
    logger.save_logs(spark=spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Fix column case
# ###### We need to make columns upper case in case they are not

# CELL ********************

exclude_cols = []
bronze_spark_df =bronze_spark_df.transform(standardize_column_names, exclude_columns=exclude_cols)

# MARKDOWN ********************

# ### Fix dataframe data types

# CELL ********************

# get details about the mirrored database
mirror_db_details = get_mirrored_database_info(
    db_display_name = p_mirror_db_name,
    logger = logger)

landing_zone_path = mirror_db_details["abfssTablesPath"]
table_schema = get_table_schema(spark, p_CDSViewName, landing_zone_path, p_schema_name, p_schema_table_name, logger)
if table_schema:
    bronze_spark_df = apply_data_types(bronze_spark_df, table_schema, sap_data_type_mapping, logger)

# MARKDOWN ********************

# ### Merge delta table

# CELL ********************

try:
    if bronze_spark_df.limit(1).count() > 0:
        silver_fact_path = silver_lakehouse_details['tables_path'] + p_CDSViewName
        logger.info(f"Processing data merge to {silver_fact_path}")

        # check if dataframe exists in silver layer
        does_table_exist = check_if_table_exists(spark, silver_fact_path, logger)
        existing_df = None

        try:
            # if no then create a new deltatable
            # save all the records directly
            if not does_table_exist:
                logger.info(f"Table does not exists at path {silver_fact_path}, Creating new table.")
                try:
                    bronze_spark_df.write.format('delta').mode('overwrite').save(silver_fact_path)
                    logger.info(f"Successfully created new table at {silver_fact_path}")
                except Exception as e:
                    error_message = f"Failed to create new Delta table: {str(e)}"
                    logger.error(error_message)
                    notebookutils.notebook.exit(value=error_message)

            else:
                logger.info(f"Table already exists at path {silver_fact_path}, trying to merge tables.")
                try:
                    # Get existing Delta table
                    existing_silver_delta_table = DeltaTable.forPath(spark, silver_fact_path)

                    existing_alias = "ex"
                    new_df_alias = "df"

                    # Create merge condition string using primary key fields
                    merge_condition = get_merge_condition(
                        merge_keys = p_keyFields_arr,
                        right_alias = new_df_alias,
                        left_alias = existing_alias)

                    if not isinstance(merge_condition, str):
                        merge_condition = str(merge_condition)

                    # merge_condition = merge_condition + " AND ex.ACICRETIME < df.ACICRETIME"

                    logger.info(f"Merge condition: {merge_condition}")

                    # Execute merge operation with error handling
                    existing_silver_delta_table \
                    .alias(existing_alias) \
                        .merge(
                            source=bronze_spark_df.alias(new_df_alias),
                            condition=merge_condition
                        ) \
                        .whenMatchedUpdateAll() \
                        .whenNotMatchedInsertAll() \
                        .execute()

                    logger.info(f"Successfully merged data into existing table")

                except Exception as e:
                    error_message = f"Failed to merge data into Delta table: {str(e)}"
                    logger.error(error_message)
                    notebookutils.notebook.exit(value=error_message)
        except Exception as e:
            error_message = f"Error during table operation: {str(e)}"
            logger.error(error_message)
            notebookutils.notebook.exit(value=error_message)
    else:
        logger.info("No data to merge, bronze DataFrame is empty")

except Exception as e:
    error_message = f"Unexpected error during merge process: {str(e)}"
    logger.error(error_message)
    logger.save_logs(spark=spark)
    raise e
finally:
    logger.save_logs(spark=spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exit_message = f"Processing completed successfully for fact table {p_CDSViewName}."
notebookutils.notebook.exit(value = exit_message)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
