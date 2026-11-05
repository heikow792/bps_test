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

# ## 1. Parameters

# PARAMETERS CELL ********************

p_silver_lakehouse_name = ""
p_metadata_database_name = ""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 2. Imports

# CELL ********************

import json
import pyodbc
import struct
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from pyspark.sql import DataFrame
from pyspark.sql.functions import lit
from typing import Optional
from pyspark.sql import functions as F
import sempy.fabric as fabric

from common_lib.utils import parse_lakehouse_details, parse_query_output, execute_sql_query_fsql
from common_lib.exceptions import LakehouseNotFoundException, FabricSqlDatabaseNotFoundException
from common_lib.constants import FABRIC_SQL_CONNECTION_STRING_TEMPLATE

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 3. Helpers

# CELL ********************

spark.conf.set('spark.native.enabled', 'true')  

def get_lakehouse_details(lakehouse_name: str, workspace: str = None) -> dict:
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

def get_fabric_sql_database_info(db_display_name, workspace: str = None):
    """
    Get the fully qualified database name (with GUID) and server FQDN for a Fabric SQL database

    Parameters:
    db_display_name (str): The display name of the database as shown in the Fabric UI

    Returns:
    dict: A dictionary containing 'database_name' (with GUID) and 'server_fqdn'
    """

    workspace_id = fabric.resolve_workspace_id(workspace) or fabric.get_workspace_id()
    try:
        fabric_client = fabric.FabricRestClient()

        response = fabric_client.get(f"/v1/workspaces/{workspace_id}/sqlDatabases")
        sql_databases = json.loads(response.text)

        for db in sql_databases['value']:
            if db['displayName'] == db_display_name:
                return {
                    'database_name': db['properties']['databaseName'],
                    'server_fqdn': db['properties']['serverFqdn']
                }

        raise FabricSqlDatabaseNotFoundException(database_name=db_display_name, workspace_id=workspace_id)
    except Exception as e:
        if "ArtifactNotFoundException" in str(e):
            raise FabricSqlDatabaseNotFoundException(database_name=db_display_name, workspace_id=workspace_id)
        else:
            print(f"An error occurred while fetching SQL Database details: {e}")
            raise e

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

# check if log_events table exists in database
def check_if_mdb_table_exists(table_name: str) -> bool:
    check_log_table_query = f"SELECT 1 FROM sys.tables where name = '{table_name}'"
    conn = connect_to_fabric_sql_db(connection_string)
    dim_tables_data = execute_sql_query_fsql(conn, check_log_table_query)
    if len(dim_tables_data) > 0 and dim_tables_data[0][0] == 1:
        return True
    return False

def get_max_timestamp_from_mdb_table(table_name: str):
    max_time_query = f"SELECT MAX(PreciseTimestamp) from dbo.{table_name}"
    conn = connect_to_fabric_sql_db(connection_string)
    dim_tables_data = execute_sql_query_fsql(conn, max_time_query)
    if len(dim_tables_data) > 0 and len(dim_tables_data[0]):
        return dim_tables_data[0][0]
    return None

def has_delta_log(mssparkutils, path: str) -> bool:
    """Check if a folder contains _delta_log (i.e., is a delta table root)."""
    try:
        children = [f.name for f in mssparkutils.fs.ls(path)]
        return "_delta_log" in children
    except Exception:
        return False

def discover_delta_tables(mssparkutils, root: str) -> list[str]:
    """
    Recursively walk root, collecting paths that contain _delta_log.
    Stops descending into a folder once _delta_log is found there.
    """
    delta_paths = []
    try:
        entries = mssparkutils.fs.ls(root)
    except Exception as e:
        print(f"[WARN] Cannot list {root}: {e}")
        return delta_paths

    for entry in entries:
        if not entry.isDir:
            continue
        if entry.name == "_delta_log":
            continue  # skip the log folder itself
        full_path = entry.path
        if has_delta_log(mssparkutils, full_path):
            delta_paths.append(full_path)
        else:
            # go deeper
            delta_paths.extend(discover_delta_tables(mssparkutils, full_path))

    return delta_paths

def union_with_schema_merge(dfs: list[DataFrame]) -> Optional[DataFrame]:
    """Union a list of DataFrames by name, filling missing columns with null."""
    if not dfs:
        return None
    result = dfs[0]
    for df in dfs[1:]:
        result = result.unionByName(df, allowMissingColumns=True)
    return result

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 4. Extract & scope

# CELL ********************

print(f"Fetching Silver lakehouse details - {p_silver_lakehouse_name}")
silver_lakehouse_details = parse_lakehouse_details(get_lakehouse_details(p_silver_lakehouse_name))

print(f"Fetching metadata database details - {p_metadata_database_name}")
database_info = get_fabric_sql_database_info(p_metadata_database_name)
full_database_name = database_info['database_name']
server_name = database_info['server_fqdn']
connection_string = FABRIC_SQL_CONNECTION_STRING_TEMPLATE.format(
    sql_endpoint=server_name,
    full_db_name=full_database_name
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

table_name = 'log_events'

logs_max_timestamp = None
logs_max_source_date = None

if check_if_mdb_table_exists(table_name):
    logs_max_timestamp = get_max_timestamp_from_mdb_table(table_name)
print(f"Max Timestamp in the log events table is {logs_max_timestamp}")

if logs_max_timestamp:
    logs_max_source_date = logs_max_timestamp.split(" ")[0]
    print(f"Max Source Date in the log events table is {logs_max_source_date}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

BASE_PATH = silver_lakehouse_details['logs_path']

# ── MAIN ────────────────────────────────────────────────────────────────────

# 1. Discover
print("Discovering delta tables...")
delta_table_paths = discover_delta_tables(mssparkutils, BASE_PATH)
print(f"Found {len(delta_table_paths)} delta table(s):")

# 2. Read + tag with date folder
dataframes = []
skipped = []

for path in delta_table_paths:
    try:
        # Extract date from path  e.g. .../Logs/2026-06-01/guid-here  -> "2026-06-01"
        parts = path.rstrip("/").split("/")
        logs_idx = next((i for i, p in enumerate(parts) if p == "Logs"), None)
        date_folder = parts[logs_idx + 1] if logs_idx is not None and logs_idx + 1 < len(parts) else "unknown"
        if logs_max_source_date and date_folder < str(logs_max_source_date):
            continue

        df = spark.read.format("delta").load(path)
        dataframes.append(df)
    except Exception as e:
        print(f"[SKIP] {path} — {e}")
        skipped.append(path)

# 3. Union
if len(dataframes) > 0:
    final_df = union_with_schema_merge(dataframes)
    if logs_max_timestamp:
        final_df = final_df.filter(F.col("precise_timestamp") > logs_max_timestamp)

    print(f"Done. Unioned {len(dataframes)} table(s), skipped {len(skipped)}.")
    if final_df:
        print(f"Final schema ({len(final_df.columns)} columns):")
        final_df.printSchema()
else:
    notebookutils.notebook.exit(value='No new logs files found, stop processing')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 5. Transform

# CELL ********************

#--------------------------------#
#            ALL LOGS            #
#--------------------------------#

final_df = (
    final_df.withColumnsRenamed(
        {
            "guid": "ServiceActivityId",
            "precise_timestamp": "PreciseTimestamp",
            "view_name": "TableName",
            "message": "Message",
            "log_type": "LogType",
            "systemName": "SystemName"
        }
    )
)

#--------------------------------#
#            METRIC LOGS         #
#--------------------------------#

metrics_df = final_df.filter(F.col("Message").contains("Written"))
metrics_df = (
    metrics_df
    .withColumn("MetricValue", F.regexp_extract(F.col("Message"), r"(\d+)", 1).cast("int"))
    .withColumn("MetricName", F.lit("RowsProcessed"))
)

metrics_df = metrics_df.drop(*["Message", "_source_date"])

#--------------------------------#
#            ERROR LOGS          #
#--------------------------------#

errorlogs_df = final_df.filter(F.col("level") == "ERROR")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 6. Save Logs

# CELL ********************

try:
    server_name_without_port = server_name.replace(",1433", "")
    jdbc_url = "jdbc:sqlserver://" + server_name_without_port + ":1433;databaseName={" + full_database_name + "};encrypt=true"
    token = notebookutils.credentials.getToken('https://analysis.windows.net/powerbi/api')

    connection_properties = {
        "url": jdbc_url,
        "accessToken": token, # Pass the access token for authentication
        "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    }

    print(f"Saving data to table {table_name}")
    final_df.write \
    .option("batchsize", "1000") \
    .jdbc(url=jdbc_url, table=table_name, mode="append", properties=connection_properties)
    print(f"All logs saved to table {table_name}")
    notebookutils.notebook.exit(value = f"All logs saved to table {table_name}")
except Exception as e:
    print(f"An error occurred: {e}")
    notebookutils.notebook.exit(value = f"An error occurred: {e}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
