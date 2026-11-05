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
p_sort_dataframe_by_time = "_UpdateTimeStamp"
p_schema_name = "dbo"
p_source_type = "open-mirroring"
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
from pyspark.sql.types import StringType, DecimalType, IntegerType, DateType, TimestampType
from pyspark.sql.column import Column
from pyspark.sql import DataFrame

from common_lib.constants import DEFAULT_LOG_COLUMNS
from common_lib.expression_helper import get_merge_condition
from common_lib.logger.dataframe_logger import DataFrameLogger
from common_lib.data_type_mapping import sap_data_type_mapping
from common_lib.utils import get_log_file_path, check_if_table_exists, compare_time, parse_lakehouse_details, parse_mirror_db_details, \
    standardize_column_names, apply_data_types, get_sap_language_expression, validate_required_params, validate_mirrored_delta_table
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

# ### Setup Constants

# CELL ********************

silver_fact_path = silver_lakehouse_details['tables_path'] + p_CDSViewName
p_keyFields_arr = ast.literal_eval(p_keyFields)
# p_keyFields_arr.append('_SystemName')

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

# CELL ********************

logger.info(f"Starting processing for CDS View: {p_CDSViewName} with ODP Name: {p_ODPName} and System Name: {p_system_name}")

# MARKDOWN ********************

# ### Handle tables not available in SAP Datasphere Replication Flow
# 
# few tables are not available in SAP Datasphere Replication Flow. While this issue is being resolved, we will generate those tables from text tables. Below code will help us to skip processing for those tables and log the same information. This will ensure that notebooks do not fail due to missing tables and we have a log of which tables are being skipped.

# CELL ********************

if p_source_type == "sap-datasphere":
    tables_not_available = set([
        "I_BILLINGPLANRULE", "I_CUSTOMERPAYMENTTERMS", "I_DELIVERYBLOCKREASON", "I_DELIVERYBLOCKSTATUS",
        "I_DELIVERYDOCUMENTTYPE", "I_DUNNINGAREA", "I_EQUIPMENT", "I_FUNCTIONALLOCATION", "I_INCOTERMSVERSION", "I_PURCHASINGPROCESSINGSTATUS",
        "I_SALESGROUP", "I_SALESOFFICE", "I_SEGMENT", "I_SHIPPINGPOINT", "I_GLACCOUNTTEXT", "I_ADDRESS_2"
    ])
    if p_CDSViewName in tables_not_available:
        logger.info(f"Table {p_CDSViewName} is not available in SAP Datasphere Replication Flow. This will be generated from text tables.")
        logger.info(f"Completed processing for CDS View: {p_CDSViewName} with ODP Name: {p_ODPName} and System Name: {p_system_name}")
        logger.save_logs(spark=spark)
        notebookutils.notebook.exit(f"Skipped processing for {p_CDSViewName} as it is not available in SAP Datasphere Replication Flow.")

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

# ### Process Dimension Table

# CELL ********************

try:
    landing_zone_path = ""
    if mirror_db_details is not None:
        landing_zone_path = mirror_db_details["abfssTablesPath"]
    else:
        notebookutils.notebook.exit(value = f"Unable to find mirrored database {p_mirror_db_name}. Please check if the name is correct.")

    # create table path by appending schema and table name and landing zone path.
    table_path = f"{landing_zone_path}{p_schema_name}/{p_ODPName}"
    if not check_if_table_exists(spark, table_path, logger):
        table_path = f"{landing_zone_path}{p_schema_name}/{p_CDSViewName}"
    logger.info(f"Reading table from path: {table_path}")

    # is_partition_required: indicates if we need to partition data over latest timestamp and filter only latest records.
    is_partition_required = True

    # This is initial load.
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
    # since the dimension is loaded from the mirrored db, all data is latest.
    is_partition_required = False
    logger.info(f"Loaded all data from Mirrored Database.")

    number_of_rows = mirrored_df.count()
    logger.info(f"Number of rows in the Dataframe: {number_of_rows}")

    if number_of_rows > 0:

        # below will only execute while delta loads.
        # since _commit_timestamp is only available with readChangeFeed = True
        if "_commit_timestamp" in mirrored_df.columns:
            # if the mirroring partner is publishing _UpdateTimeStamp we will delete it.
            # since we using _commit_timestamp for as _UpdateTimeStamp
            if "_UpdateTimeStamp" in mirrored_df.columns:
                mirrored_df = mirrored_df.drop("_UpdateTimeStamp")
            mirrored_df = mirrored_df.withColumnRenamed("_commit_timestamp", "_UpdateTimeStamp")

        if is_partition_required:
            # Create a window specification with multiple partition columns
            window_spec = Window.partitionBy(p_keyFields_arr).orderBy(col("_UpdateTimeStamp").desc())

            mirrored_df = mirrored_df.withColumn("row_num", F.row_number().over(window_spec)) \
                                        .filter(col("row_num") == 1) \
                                        .drop("row_num")

        mirrored_df = mirrored_df.withColumn("_SystemName", F.lit(p_system_name))

        if "_change_type" in mirrored_df.columns:
            # filter table, remove rows where change_type is update_preimage
            mirrored_df = mirrored_df.filter(col("_change_type").isin(["insert", "update_postimage", "delete"]))

        if "_change_type" in mirrored_df.columns:
            # create a new column _Delete and mark deleted columns.
            mirrored_df = mirrored_df.withColumn("_Delete", when(col("_change_type") == "delete", lit("X")).otherwise(lit("")))
        else:
            mirrored_df = mirrored_df.withColumn("_Delete", lit(""))

    bronze_spark_df = mirrored_df

except Exception as e:
    logger.error(f"Error processing CDS View - {p_CDSViewName} for system - {p_system_name}. Error details: {str(e)}")
    logger.save_logs(spark)
    raise e
finally:
    logger.save_logs(spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# if there are no rows to process after filtering with max timestamp
# then we can exit the notebook as there is no processing required.
if bronze_spark_df.limit(1).count() == 0:
    logger.info(f"No rows for processing for table {p_CDSViewName}")
    logger.info(f"Completed processing for CDS View: {p_CDSViewName} with ODP Name: {p_ODPName} and System Name: {p_system_name}")
    logger.save_logs(spark=spark)
    notebookutils.notebook.exit(f"Processing for table {p_CDSViewName} completed successfully.")

# MARKDOWN ********************

# ### Fix column case

# CELL ********************

exclude_cols = []
logger.info(f"Standardizing column names in the dataframe.")
bronze_spark_df = bronze_spark_df.transform(standardize_column_names, exclude_columns=exclude_cols)

# MARKDOWN ********************

# ### Fix dataframe data types

# CELL ********************

logger.info(f"Applying data types to the dataframe based on the schema from table - {p_schema_table_name}.")
landing_zone_path = mirror_db_details["abfssTablesPath"]
table_schema = get_table_schema(spark, p_CDSViewName, landing_zone_path, p_schema_name, p_schema_table_name, logger)
if table_schema:
    bronze_spark_df = apply_data_types(bronze_spark_df, table_schema, sap_data_type_mapping, logger)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Normalize SAP Language

# CELL ********************

logger.info(f"Processing language column in the dataframe.")
if 'LANGUAGE' in bronze_spark_df.columns:
	_iso_language_expr = get_sap_language_expression('LANGUAGE')
	bronze_spark_df = bronze_spark_df.withColumn('SAPLANGUAGE', _iso_language_expr)
	bronze_spark_df = bronze_spark_df.drop('LANGUAGE')
	bronze_spark_df = bronze_spark_df.withColumnRenamed('SAPLANGUAGE', 'LANGUAGE')

logger.info(f"Processing language code column in the dataframe.")
if 'LANGUAGECODE' in bronze_spark_df.columns:
	_iso_language_expr = get_sap_language_expression('LANGUAGECODE')
	bronze_spark_df = bronze_spark_df.withColumn('LANGUAGECODE', _iso_language_expr)

# MARKDOWN ********************

# ### Save delta table

# CELL ********************

try:
	if bronze_spark_df.limit(1).count() > 0:
		silver_table_path = silver_lakehouse_details['tables_path'] + p_CDSViewName

		# for dimensions we always take the latest version and overwrite the table in Silver Lakehouse
		bronze_spark_df.write.format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
		.option("replaceWhere", f"_SystemName = '{p_system_name}'") \
        .save(silver_table_path)
except Exception as e:
	logger.error(f"Error writing table {p_CDSViewName} to Silver Lakehouse {p_silver_lakehouse_name}. Error details: {str(e)}")
	logger.save_logs(spark)
	raise e
finally:
    logger.info(f"Completed processing for CDS View: {p_CDSViewName} with ODP Name: {p_ODPName} and System Name: {p_system_name}")
logger.save_logs(spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exit_message = f"Completed processing for CDS View: {p_CDSViewName} with System Name: {p_system_name}"
notebookutils.notebook.exit(value = exit_message)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
