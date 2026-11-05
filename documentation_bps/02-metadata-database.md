# Metadata database and configuration contracts

[Overview](README.md) | [Architecture](01-architecture-and-orchestration.md) | [Transformations](03-notebook-transformations.md)

## 1. Role of the database

The [Fabric SQL database project](../bps_metadata_db_c792846f.SQLDatabase/bps_metadata_db_c792846f.sqlproj) defines **14 tables, one view, and seven stored procedures**. It contains DDL only: no checked-in seed/post-deployment script supplies the actual SAP systems, datasets, CDS view lists, keys, or relationships.

The executable path visible here uses metadata lookups for table selection and fact relationships. Several schemas/procedures support other connectors or lifecycle workflows, but no corresponding extraction pipelines are included.

The project targets `SqlDbFabricDatabaseSchemaProvider` using `Microsoft.Build.Sql` SDK 2.1 and the Fabric DACPAC dependency. It enables read-committed snapshot and snapshot isolation, automatic statistics, Query Store, and database-scoped MaxDOP 8. These are database project settings, not evidence of live deployment state.

## 2. Core configuration tables

### 2.1 `systemDetails`

Source: [systemDetails.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/systemDetails.sql).

**Primary key:** `(SystemName, ConnectionType)`.

| Columns | Function |
|---|---|
| `SystemName` | Source-system identifier propagated as `_SystemName` |
| `SourceType` | Source family; the included pipelines select `SAP` |
| `SystemType` | System category; B2S selects `S4HANA` |
| `SystemNumber`, `SystemVersion` | System descriptors; not otherwise consumed by included orchestration |
| `ConnectionType` | B2S selects `OpenMirroring` |
| `ServerName` | Mirrored database display name for this connection path |
| `SubscriberName` | Mirrored source schema passed as `Schema_Name` |
| `ClientId`, `UserName`, `SecretName` | Connector configuration/reference fields; not read as credentials by the included mirroring notebooks |

All columns are non-null. Most identifiers are `nvarchar(50)`; version and connection type are `nvarchar(100)`, and server name is `nvarchar(max)`.

Because a system can have multiple connection rows, consumers that join only on `SystemName` can multiply metadata rows. The S2G system lookup is one such consumer.

### 2.2 `viewMetadata`

Source: [viewMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/viewMetadata.sql).

**Primary key:** `(SystemName, CDSViewName)`.

| Column | Contract |
|---|---|
| `CDSViewName` | Standardized Silver/Gold Delta table name |
| `Context` | Required context grouping; not used by current selection logic |
| `Description` | Optional description |
| `Type` | Dispatch value: `DIMENSION`, `DIMENSION-TD`, `HIERARCHY`, `TEXT`, or `FACT` |
| `ODPName` | Source ODP/table name; suffixes `$P/$T/$F/$E` are stripped for mirror reads |
| `Delta` | Bit routing S2G delta versus snapshot handling for non-facts |
| `KeyFields` | `nvarchar(max)` containing a Python-list literal of column-name strings |
| `relatedCDSViewName` | Master dimension from which a text table obtains its `Key` |
| `SystemName` | Configuration ownership and scope |

`KeyFields` is not a JSON-array SQL type. Notebooks parse its string with `ast.literal_eval`; examples of the expected shape are `['COMPANYCODE']` or `['CHARTOFACCOUNTS', 'GLACCOUNT']`. These are illustrative contracts, not actual installed metadata rows.

Business column names should match standardized uppercase source columns. The notebooks append `_SystemName` themselves. For text processing they remove `LANGUAGE` from the master-key join; time-dependent processing removes `VALIDITYENDDATE` from the entity-key allocation set.

### 2.3 `extractionScope`

Source: [extractionScope.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/extractionScope.sql).

**Primary key:** `(SystemName, DatasetName, TableName)`. All names are required; `IsEnabled bit NOT NULL DEFAULT(1)`.

This table enables a source view/table within a named dataset. A CDS view can be referenced by multiple datasets. `TableName` is matched to `viewMetadata.CDSViewName`, not to ODP name.

### 2.4 `extractionScopeByDataset`

Source: [extractionScopeByDataset.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/extractionScopeByDataset.sql).

**Primary key:** `(SystemName, DatasetName)`; `IsEnabled bit NOT NULL DEFAULT(1)`.

This is the dataset-wide enable switch. A table is considered in scope only when both the table-in-dataset switch and the dataset switch are enabled.

### 2.5 `cubeMetadata`

Source: [cubeMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/cubeMetadata.sql).

**Primary key:** `(SystemName, RelationshipName)`. All columns are non-null.

| Column | Meaning |
|---|---|
| `FactTable` | Fact CDS/Delta table |
| `DimensionTable` | Gold dimension used to enrich the fact |
| `JoinCondition` | String representation of a list of `(fact_column, dimension_column, operator)` tuples |
| `SKColumn` | Output foreign-key column, conventionally `_key_I...` |
| `DimColumns` | String representation of a list of additional dimension attributes to copy |
| `JoinOrder` | Integer ordering; later joins may consume attributes added by earlier joins |
| `RelationshipName` | Unique name per system for the relationship |
| `SystemName` | Source-system owner |

An illustrative join contract is:

```text
[('COMPANYCODE', 'COMPANYCODE', '==')]
```

The helper accepts `==`, `>=`, and `<=` and appends the source-system equality join automatically. It uses a left join, copies configured attributes, and fills a missing dimension key with `-1`.

The main S2G fact pipeline filters relationships to dimensions that are in extraction scope and orders them by `JoinOrder`. The currency notebook queries this table directly without a system predicate or extraction-scope join.

### 2.6 `fieldMetadata`

Source: [fieldMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/fieldMetadata.sql).

**Primary key:** `(systemName, CDSViewName, fieldName)`.

Required identifiers are accompanied by nullable `dataType`, `length`, `decimals`, `systemType`, `Precision`, `Scale`, and `IsCalculated`. Length/decimals/precision/scale are integer fields; `IsCalculated` is a bit.

The Salesforce query-generation procedure uses these field names. The current SAP B2S notebooks do **not** use this table to cast source data: they read the mirrored SAP schema table, normally `DD03ND`.

## 3. The executable routing view: `extractionMetadata`

Source: [extractionMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Views/extractionMetadata.sql).

This is the main read interface used by pipelines. It inner-joins:

```text
viewMetadata vm
  -> extractionScope es
       vm.CDSViewName = es.TableName AND same SystemName
  -> extractionScopeByDataset esd
       es.DatasetName = esd.DatasetName AND same SystemName
  -> systemDetails sd
       same SystemName
```

It exposes system/source type; CDS/context/description/type/ODP/delta/keys/related view; both enable flags; and:

```sql
CASE WHEN es.IsEnabled = 1 AND esd.IsEnabled = 1 THEN 1 ELSE 0 END AS inScope
```

Important semantics:

- A `viewMetadata` row alone is insufficient; missing scope, dataset, or system rows remove it from this view.
- The view is **not distinct**, and does not aggregate multiple dataset memberships.
- It does not expose `DatasetName` or `ConnectionType`, even though those rows can create duplication.
- A table enabled through one dataset and disabled through another can produce both in-scope and out-of-scope rows. Most consumers explicitly select `inScope=1`.
- The S2G exchange-rate gate instead counts all matching rows and requires exactly one.

The database has primary keys on several configuration tables but no declared foreign keys tying these tables together. Configuration consistency is therefore largely a runtime responsibility.

## 4. Checkpoint and connector-support tables

| Table | Keys and fields | Visible use |
|---|---|---|
| [AdfExtractionCheckpoint](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/AdfExtractionCheckpoint.sql) | PK `(CDSViewName,systemName)`; nullable `checkpointId nvarchar(36)`, `maxId bigint`, `lastProcessedTimestamp datetime2(7)`, `systemType` | Used by `GetCheckpointId`; no included pipeline calls that procedure |
| [Ecc_Table_Checkpoint](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/Ecc_Table_Checkpoint.sql) | PK `(TableName,SystemName,RelatedCDSViewName)`; nullable `MaxProcessedTimestamp datetime2(7)` | ECC support; no ECC pipeline present |
| [Ecc_column_mapping](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/Ecc_column_mapping.sql) | Required `TableName`, `ColumnName`, `S4TableName`, `S4ColumnName`, `SystemName`; no PK | ECC-to-S/4 naming map; not consumed by included notebooks |
| [SalesforceTableCheckpoint](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/SalesforceTableCheckpoint.sql) | Required system/object; nullable `MaxSystemModStamp datetime2(7)`; no PK | Used by Salesforce timestamp procedure; no Salesforce pipeline present |

The active B2S fact checkpoint is instead the maximum `_UpdateTimeStamp` stored in Silver for the current system. Active S2G notebooks also derive checkpoints from their destination tables. Do not equate the presence of SQL checkpoint schemas with their use by this installed mirroring path.

## 5. Logging and lifecycle tables

### 5.1 `log_events`

Source: [log_events.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/log_events.sql).

All columns are nullable `nvarchar`; messages use `nvarchar(max)`. There is no primary key or uniqueness constraint.

- Correlation: `ServiceActivityId`.
- Event data: `level`, `PreciseTimestamp`, `SystemName`, `TableName`, `Message`, `Stage`, `LogType`.
- Runtime context: `rootNotebookName`, `currentNotebookName`, `currentNotebookId`, `currentWorkspaceName`, `currentWorkspaceId`, `defaultLakehouseName`, `environmentId`.
- Execution flags: `isForPipeline`, `isForInteractive`, `isReferenceRun`.

The collector appends here through JDBC. `PreciseTimestamp` is stored as text rather than SQL datetime; the collector's `MAX` and strict `>` comparison rely on consistent sortable timestamp strings.

### 5.2 Other log/version tables

| Table | Columns | Visible behavior |
|---|---|---|
| [ExtractionLogs](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/ExtractionLogs.sql) | Nullable `TimeStamp datetime2(7)`, `PipelineName`, `ExecutionId`, `Status`, `CDSView`, `SystemName`, `ConnectorType`, `ODPName` | Insert procedure exists; not called by included pipelines |
| [OrchestrationLogs](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/OrchestrationLogs.sql) | Required `TimeStamp datetime`, `PipelineName`, `ExecutionId`, `Status`, `VersionNumber` | Insert procedure exists; not called by included pipelines |
| [VersionDetails](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/VersionDetails.sql) | Required version, first/last execution dates; nullable last-success date | Update procedure exists; not called by included pipelines |

None of these three tables declares a primary key.

## 6. All seven stored procedures

### `GenerateSelectQueriesBySalesforceSystem`

Source: [procedure](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/GenerateSelectQueriesBySalesforceSystem.sql).

Inputs: required `@SystemName`; optional comma-separated `@ObjectNames = NULL`. It:

1. Splits and trims requested object names into a table variable.
2. Aggregates `fieldMetadata.fieldName` using `FOR XML PATH` and `STUFF`.
3. Produces one `ObjectName` and `select_query` of the form `SELECT f1, f2 FROM Object`.
4. Restricts objects to enabled `extractionScope` rows whose system source type is Salesforce.

It returns query strings; it does not execute Salesforce queries. It does not use the dataset enable table. Passing empty string is different from NULL: the object-name filter is active but its parsed list is empty.

### `GetCheckpointId`

Source: [procedure](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/GetCheckpointId.sql).

Inputs: CDS view and system. Reads the SQL checkpoint GUID, generates `NEWID()` if missing/null, upserts it with `MERGE`, and returns `CheckpointId`. It does not advance `maxId` or the processed timestamp.

### `GetMaxSystemModStamp`

Source: [procedure](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/GetMaxSystemModStamp.sql).

Inputs: system and object. If a Salesforce checkpoint exists, returns both a formatted timestamp and the raw timestamp. Otherwise returns a null `MaxSystemModStamp`. The format string uses lowercase `hh` (12-hour clock), so it should not be assumed to provide an unambiguous UTC 24-hour timestamp.

### `InsertExtractionLogs`

Source: [procedure](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/InsertExtractionLogs.sql).

Accepts the eight extraction-log values and inserts them into `ExtractionLogs` using positional column order.

### `InsertOrchestrationLogs`

Source: [procedure](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/InsertOrchestrationLogs.sql).

Accepts timestamp, pipeline, execution ID, status, and version, and inserts them into `OrchestrationLogs`.

### `UpdateVersionDetails`

Source: [procedure](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/UpdateVersionDetails.sql).

Inputs: version and success bit. For a new version, initializes first/last execution with `GETDATE()` but leaves last-success null, even when the first execution is marked successful. For an existing version, updates last execution and updates last-success only on success. There is no declared unique version constraint.

### `Upsert_Ecc_Table_Checkpoint`

Source: [procedure](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/Upsert_Ecc_Table_Checkpoint.sql).

Inputs: table, system, optional related CDS name, optional timestamp. Merges on table/system/related view, including explicit null equality for the related view. However, the target table declares related view non-null as part of its PK: the procedure's null default is incompatible with inserting a new checkpoint row without that value.

## 7. Configuration needed for a real run

The following illustrates the required configuration sequence; it does not claim that these rows already exist:

1. Register a SAP/OpenMirroring/S4HANA system with the mirror display name and source schema.
2. Register datasets in `extractionScopeByDataset`.
3. Register each CDS view in `viewMetadata`, with valid type, keys, ODP name, and delta flag.
4. Add table memberships in `extractionScope`.
5. For text views, set the related master dimension and align their natural keys.
6. Add ordered fact relationships in `cubeMetadata`; include required copied attributes for chained joins.
7. Replicate `DD03ND` with schema rows for each required CDS view.
8. Populate all required source tables before starting B2S.

The SQL project does not define the installed system names, dataset count, active CDS list, or actual join configuration. Those must be exported/read separately from the live metadata database to complete a deployment-specific inventory.
