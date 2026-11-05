# Architecture, storage, runtime, and orchestration

[Overview](README.md) | [Metadata](02-metadata-database.md) | [Transformations](03-notebook-transformations.md)

## 1. Control plane and data plane

The metadata SQL database is the **control plane**: pipelines query its system list, scope, keys, extraction modes, and relationship configuration. The mirrored database and two BPS lakehouses form the **data plane**. Spark notebooks read and write Delta files; the final presentation notebook uses T-SQL against the Gold SQL analytics endpoint.

This is not a workspace of independent hand-written ETL jobs. A small number of parameterized notebooks processes a potentially large set of SAP tables.

### 1.1 Mirrored database

[Mirror configuration](../bps_mirrored_db_MySAP_c792846f.MirroredDatabase/mirroring.json):

| Property | Checked-in value | Meaning in this implementation |
|---|---|---|
| Source type | `GenericMirror` | Data must be published by an external producer |
| Target type | `MountedRelationalDatabase` | Mirrored tables are mounted as relational objects |
| Default schema | `dbo` | Default source schema; pipeline can pass another schema |
| Format | `Delta` | Read by Spark Delta readers |
| Change data feed | Enabled | Required by incremental B2S fact reads |
| Retention | 30 days | Declared retention setting; confirm effective history/CDF availability before replay |

It is the bronze-equivalent source; there is no separate BPS bronze lakehouse item. The definition contains no SAP connector credentials, publisher implementation, source table inventory, or replication schedule.

The B2S notebooks locate the mirror by display name using the Fabric REST API, convert its `oneLakeTablesPath` to an ABFSS path, and read `<schema>/<ODPName>`, falling back to `<schema>/<CDSViewName>`.

### 1.2 Lakehouses

| Item | Purpose and evidence |
|---|---|
| [Silver](../bps_silver_c792846f.Lakehouse/lakehouse.metadata.json) | Standardized SAP-shaped Delta tables plus notebook logs in Files |
| [Gold](../bps_gold_c792846f.Lakehouse/lakehouse.metadata.json) | Keyed dimensions, enriched facts, derived balances/rates, and SQL presentation views |
| [Sample](../Lakehouse_Sample.Lakehouse/lakehouse.metadata.json) | Only an empty item definition; no reference from the analyzed engineering code |

All three declare `defaultSchema: dbo`. Each has an empty `shortcuts.metadata.json`: the snapshot does **not** define shortcuts to source tables or another workspace. Their ALM settings enable shortcut synchronization for supported shortcut categories but disable DataAccessRoles synchronization. Those settings are capabilities, not evidence that shortcuts or security roles have been configured.

The common helper uses a schema-enabled lakehouse's `.../Tables/dbo/` path unless a system-specific schema is explicitly requested. The analyzed notebook callers normally use the default path, keeping multiple systems in the same table with `_SystemName` as a row attribute.

Logs are designed to live under `.../Files/Logs/<date>/<guid>/...`. A schema-enabled path construction inconsistency is documented in [Operations](07-operations-and-caveats.md).

## 2. Runtime environment

[Spark compute settings](../bps_env_c792846f.Environment/Setting/Sparkcompute.yml):

- Runtime version setting: `2.0`.
- Driver: 8 cores, `56g` memory.
- Executor: 8 cores, `56g` memory.
- Dynamic executor allocation: enabled, minimum 1 and maximum 1.
- Native execution engine setting: `false`.

Fourteen Spark notebooks reference this Environment. The SQL-view notebook instead declares a Jupyter Python 3.11 kernel and has no Environment binding. Several notebooks explicitly set `spark.native.enabled=true`, despite the Environment-level native execution setting being false; the effective behavior depends on Fabric runtime support and precedence.

The Environment includes [ei_common_lib-1.0.5-py3-none-any.whl](../bps_env_c792846f.Environment/Libraries/CustomLibraries/ei_common_lib-1.0.5-py3-none-any.whl). Its modules implement logging, SAP types, key construction, metadata joins, path parsing, and validation; see [Transformations](03-notebook-transformations.md). Package metadata declares `pyspark==3.5.0`, `delta-spark==3.0.0`, `azure-data-tables`, and `azure-storage-blob`; it does not declare a Python-version requirement. Effective compatibility with the deployed Fabric runtime has not been tested.

Spark notebooks also rely on platform/runtime-provided packages and objects: Delta Lake, PySpark, Semantic Link (`sempy.fabric`), `notebookutils`/`mssparkutils`, SQLAlchemy, pyodbc, SQL Server JDBC, and the platform token wrapper. The repository does not contain a complete pip requirements manifest.

Notebook comments identify the notebooks as BPS-managed and warn that updates overwrite manual changes. This documentation does not modify any deployed notebook.

## 3. B2S: mirrored source to Silver

### 3.1 Top-level orchestration

Source: [B2S orchestration definition](../bps_om_b2s_orchestration_pipeline_c792846f.DataPipeline/pipeline-content.json).

```text
Get Open Mirror System Details
  -> For each system [sequential]
       B2S Dimension Processing [wait for completion]
         -> B2S Fact Processing [wait for completion]
```

System selection:

```sql
SELECT *
FROM SystemDetails
WHERE SourceType = 'SAP'
  AND ConnectionType = 'OpenMirroring'
  AND SystemType = 'S4HANA';
```

For each system:

- `ServerName` becomes `Mirror_Database_Name`.
- `SystemName` becomes `System_Name`.
- `SubscriberName` becomes `Schema_Name`.
- Top-level `Silver_Lakehouse_Name`, `CdsViewNames`, and `Schema_Table_Name` are passed to both child pipelines.

Defaults are the installed Silver lakehouse, `CdsViewNames = " "` (one space), and schema metadata table `DD03ND`.

The children are strictly ordered per system, and systems are processed sequentially. There is no activity that waits for upstream SAP replication to catch up.

### 3.2 Dimension child pipeline

Source: [B2S dimensions](../bps_om_b2s_dim_processing_c792846f.DataPipeline/pipeline-content.json).

Independent initial activities retrieve dimension metadata and generate `v_guid`. The table loop waits for both.

- Metadata predicate: `em.Type <> 'FACT'`, `em.inScope = 1`, SAP/OpenMirroring/S4HANA system filters, requested system name, and optional comma-separated CDS allow-list.
- Return columns: distinct `CDSViewName`, normalized `ODPName`, `KeyFields`.
- Normalization removes ODP suffix patterns `\$[EFPT]`.
- Parallel `ForEach`, `batchCount = 6`.
- Each iteration calls [B2S dimension notebook](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py).

The notebook receives source system, mirror name/workspace, source schema and schema table, destination lakehouse, ODP/CDS names, keys, GUID, and `p_source_type="open-mirroring"`. Mirror workspace comes from `@pipeline().DataFactory`.

The session tag is `High_Concurrency_Session_Fact_<guid-prefix>` even for dimensions. It is a session-reuse hint, not an additional dependency or proof that six Spark sessions run simultaneously.

### 3.3 Fact child pipeline

Source: [B2S facts](../bps_om_b2s_fact_processing_c792846f.DataPipeline/pipeline-content.json).

The structure and parameter mapping mirror the dimension child, except:

- Selection is `em.Type = 'FACT'`.
- Parallel `ForEach` has `batchCount = 3`.
- The target is [B2S fact notebook](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py).

Dimensions are always read as snapshots in B2S. Facts use an initial snapshot and subsequent Delta CDF reads based on the Silver watermark.

## 4. S2G: Silver to Gold

### 4.1 Full processing pipeline

Source: [Full S2G definition](../bps_s2g_full_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

```text
Set GUID
  -> Get System Details
     -> For each source system [sequential]
          Run Dimension Processing
            -> Run Fact Processing
       -> Create Views in Gold Lakehouse
```

The system lookup selects `SystemName` from `systemDetails WHERE SourceType='SAP'`. It does **not** restrict the connection type or system type and does not use `DISTINCT`. Because the table key permits multiple connection rows per system, the same system could appear multiple times if configured that way.

A single generated GUID is shared across the full orchestration. Dimension/fact children receive the system, GUID, Gold/Silver names, and optional CDS allow-list.

The final SQL-view notebook is invoked **once after all systems**, with **no parameters passed**. It therefore uses its hard-coded Gold lakehouse name, even if the pipeline's Gold parameter is changed.

This pipeline does not invoke B2S first, collect logs afterward, or explicitly refresh the financial semantic model.

### 4.2 Dimension processing pipeline

Source: [S2G dimensions](../bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

The following branches form one serial chain, not six parallel branches:

| Order | Lookup predicate | JSON field | Notebook |
|---:|---|---|---|
| 1 | `Type='DIMENSION'`, `Delta=1` | `DimDelta` | `s2g_dim_delta` |
| 2 | `Type='DIMENSION'`, `Delta=0` | `DimNoDelta` | `s2g_dim_nodelta` |
| 3 | `Type IN ('DIMENSION-TD','HIERARCHY')`, `Delta=1` | `DimTDDelta` | `s2g_dimtd_delta` |
| 4 | Same types, `Delta=0` | `DimTDNoDelta` | `s2g_dimtd_nodelta` |
| 5 | `Type='TEXT'`, `Delta=1` | `DimTextDelta` | `s2g_text_delta` |
| 6 | `Type='TEXT'`, `Delta=0` | `DimTextNoDelta` | `s2g_text_nodelta` |

Every lookup also requires `inScope=1`, `SourceType='SAP'`, the current system name, and the optional CDS allow-list. Each serializes a distinct result into JSON with `CDSViewName`, `relatedCDSViewName`, `Delta`, `KeyFields`, `Type`, and `Inscope`; null/no-result is coalesced to `[]`.

Each notebook receives **one JSON array**, then loops through its tables itself. Pipeline-to-notebook parameters are `p_lookup_output`, lakehouse names, and GUID. **`p_system_name` is not passed to these six notebooks**, although they declare it; system filtering occurs in the lookup, not in their table reads.

All six use session tag `DimensionNotebook`. The ordering ensures master dimensions are available before texts copy their keys.

After texts:

1. `Get Exchange Table` counts `I_EXCHANGERATERAWDATA` rows in `extractionMetadata` for the system.
2. `If Condition1` tests whether `output.firstRow.value` equals exactly `1`.
3. On true, it calls the currency-conversion notebook with **no parameter overrides**.

The count has no `inScope=1` predicate. It counts metadata rows, not source data or distinct views; multiple dataset scope rows can affect this gate.

### 4.3 Fact processing pipeline

Source: [S2G facts](../bps_s2g_fact_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

1. Select distinct in-scope SAP `FACT` CDS names for the system and optional allow-list into JSON.
2. Iterate facts **sequentially**.
3. For each fact, perform two independent lookups:
   - Primary `KeyFields`.
   - Relationships from `cubeMetadata`, joined to in-scope dimension extraction metadata, ordered by `JoinOrder`, serialized as JSON.
4. Store the outputs in pipeline string variables `Keyfields` and `Cubeconfig`.
5. Invoke [S2G fact notebook](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py) after both variables are populated.

Sequential iteration avoids concurrent mutation of those shared variables. The notebook receives current system, table name, keys, relationships, lakehouses, GUID, and the platform option `useRootDefaultLakehouse=true`.

After the fact loop, `Finance Aggregate notebooks` tests whether the serialized selected fact list contains `I_OPERATIONALACCTGDOCITEM`. On true, it runs:

```text
Customer Balance Aggregate -> Supplier Balance Aggregate
```

They receive current system, GUID, lakehouses, and explicit output table names `BPS_CUSTOMERBALANCEAGGR` / `BPS_SUPPLIERBALANCEAGGR`.

Fact and aggregate session tags are based on the first eight GUID characters. A default GUID exists on the fact child for standalone execution; normal full orchestration overrides it.

## 5. Log collection pipeline

Source: [Collector pipeline](../bps_log_collector_pipeline_c792846f.DataPipeline/pipeline-content.json).

There is a single activity, `Log Collector Notebook`, calling the original collector notebook with installed Silver and metadata database names. The copied collector notebook is not referenced by any checked-in pipeline.

The collector discovers Delta logs in Silver Files, applies a SQL timestamp watermark, and appends messages to `dbo.log_events`. It does not update `ExtractionLogs`, `OrchestrationLogs`, or `VersionDetails`.

## 6. Schedules, timeouts, retries, and wiring

| Pipeline | Enabled schedule | Time zone | Declared window |
|---|---|---|---|
| [B2S orchestration](../bps_om_b2s_orchestration_pipeline_c792846f.DataPipeline/.schedules) | Daily 10:00 | UTC | 2026-10-07 to 2051-10-07 |
| [Full S2G](../bps_s2g_full_processing_pipeline_c792846f.DataPipeline/.schedules) | Daily 13:00 | UTC | 2026-10-07 to 2051-10-07 |
| [Log collector](../bps_log_collector_pipeline_c792846f.DataPipeline/.schedules) | `Cron`, interval `360` | UTC | 2026-10-07 to 2036-10-07 |

The collector declares an interval-based schedule without an explicit clock-time list. The serialized interval is 360; if interpreted as minutes by the deployed Fabric scheduler, that is six hours. This analysis does not infer actual firing times or verify live schedule activation.

There is a three-hour clock gap between B2S and S2G, **not an execution dependency**. If B2S is slow or fails, S2G can still start against stale or partly updated Silver data.

Most Lookup and Notebook policies use a 12-hour activity timeout (`0.12:00:00`) and a 30-second retry interval. B2S and most notebook activities have zero retries. The six main S2G dimension lookups and fact metadata lookups have two retries. SQL read queries typically declare a two-hour query timeout. Dependencies are success-based; no recovery, failure-notification, or compensation branches are present.

Metadata lookups consistently identify the synced metadata SQL database by logical artifact ID and share one external Fabric connection reference. Some connection display labels still use older `ei_*` names, but the ID is the operative binding. The connection object itself is not exported here.

## 7. Identity and deployment boundaries

`.platform` files provide Git logical IDs. Pipeline child/notebook references resolve to those IDs. Notebook lakehouse dependencies also contain concrete workspace and lakehouse IDs; these should not be assumed to have the same serialization as `.platform` logical IDs.

Portable deployment therefore needs more than copying code:

- Resolve/remap Fabric item and connection references.
- Ensure notebook default/known lakehouses target the intended workspace.
- Load metadata configuration rows separately.
- Configure the generic mirror producer.
- Verify SQL endpoint synchronization and presentation object names.
- Validate the semantic model's actual source and refresh.

See the [complete identity/activity catalog](08-workspace-object-catalog.md) for all objects, parameters, and bindings.
