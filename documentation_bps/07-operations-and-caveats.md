# Operations, evidence boundaries, and implementation caveats

[Overview](README.md) | [Orchestration](01-architecture-and-orchestration.md) | [Transformations](03-notebook-transformations.md)

## 1. Prerequisites for an end-to-end run

The repository is a definition snapshot, not a self-contained executable deployment. A working environment also needs:

1. A Fabric workspace/capacity supporting the declared item types and notebook runtime.
2. Deployed Silver/Gold lakehouses, metadata SQL database, Environment, notebooks, pipelines, model, and report.
3. An authenticated Fabric SQL connection matching the pipeline's external connection reference.
4. A functioning upstream publisher for the GenericMirror database and Delta CDF on relevant source facts.
5. Replicated SAP business tables and `DD03ND` schema rows for each onboarded CDS object.
6. Populated system, dataset/table scope, view/key, and cube-relationship metadata.
7. Identity permissions to discover/read the mirror, read/write the lakehouses, access the SQL endpoint, and append SQL logs.
8. Compatible PySpark/Delta/Semantic Link/SQL driver dependencies.
9. Resolved semantic model source bindings and a configured report/model relationship.

No live credentials, metadata rows, table data, run outputs, or refresh history were used to validate these prerequisites.

## 2. Recommended operational sequence

This sequence follows the repository's dependencies; it is not a new implemented automation:

1. Confirm upstream mirror replication and schema metadata are current.
2. Validate extraction scope and relationship metadata.
3. Run B2S orchestration; inspect the dimension/fact notebook results and logs.
4. Run full S2G only after B2S has actually completed successfully.
5. Confirm all required dimensions, texts, fact keys, balance outputs, and currency outputs.
6. Inspect the Gold view notebook's per-view summary; compare with the subset required by the report.
7. Validate exact model source object names and connectivity, then perform any required model refresh.
8. Run the log collector and verify new records reached `dbo.log_events`.

The checked-in schedules run B2S at 10:00 UTC and S2G at 13:00 UTC independently. There is no dependency that enforces step 4, and no explicit model-refresh activity enforces step 7.

## 3. What to inspect when troubleshooting

| Symptom | First evidence to inspect |
|---|---|
| No tables selected | `systemDetails`, both scope tables, `viewMetadata`, and the joined `extractionMetadata` view |
| Source table/schema missing | Mirror ODP/CDS table names and DD03ND `STRUCOBJN` rows |
| Type/date problems | Standardized field names, DD03ND types/length/decimals, source date format and Spark logs |
| Facts have key `-1` | Cube join conditions/order, source attributes, Gold dimension keys and `_SystemName` |
| Late dimension keys remain unresolved | `_Reprocess` flags, null key detection, and the second phase of the S2G fact notebook |
| Duplicate fact rows | Dimension join multiplicity, validity records, and exact metadata keys |
| Missing translations | Master/text key alignment, `LANGUAGE`, `_ISOLanguage`, and the corresponding `vt*` view |
| Missing hierarchy levels | Root/node types, current validity selection, nine-level depth cap, and node text joins |
| Incorrect running balances | Source sign convention, fiscal period join, entity grain, source/target watermarks, and densification |
| Pipeline green but output missing | Notebook exit text, structured logs, and the view notebook summary |
| Logs absent in SQL | Actual Files/Logs path, discovery output, skipped paths, timestamp watermark, and JDBC exit text |
| Report fails to load | Model partition source/connection and exact database schema/object names, not only business labels |

## 4. Important code-level caveats

These are observations from static definitions, **not claims of reproduced production incidents**. They are included because they materially affect how the solution should be understood. No implementation was changed.

### 4.1 Pipeline completion and failure are not equivalent

Sources: [dimension processor](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py), [B2S fact](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py), [collector](../bps_nb_log_collector_c792846f.Notebook/notebook-content.py), [view creator](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py).

Several notebooks return error text with `notebook.exit`, and pipeline activities do not inspect the exit value. The view notebook captures exceptions and prints a summary without raising. A success-based downstream edge can therefore be followed even when an upstream object failed to process.

### 4.2 Delta CDF latest-row ordering can discard an update

Source: [B2S fact processing](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py).

The code chooses one latest row per natural key by `_UpdateTimeStamp` before removing `update_preimage`. Preimage and postimage of the same commit can have identical timestamps. Without a deterministic change-type/version tie-break, the selected row can be the preimage and then be filtered out.

### 4.3 Global S2G watermarks are not per-system watermarks

Sources: [delta dimension](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py), [delta text](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py), [fact](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py), and corresponding TD processor.

These notebooks read entire named tables and compare to the global Gold maximum timestamp. `_SystemName` participates in keys, but a slower or late-arriving system's rows can be older than another system's maximum and be excluded.

The six dimension/text notebook calls also omit `p_system_name`, so their structured log system field is blank by default.

### 4.4 Snapshot ingestion does not synthesize missing-row tombstones

Sources: [B2S dimensions](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py) and [S2G delta dimensions](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py).

B2S dimensions overwrite a source-system snapshot. A row absent from a later snapshot disappears from Silver, but the normal path does not generate a delete event for it. If that dimension is routed through S2G delta merge, absence alone does not delete the prior Gold row.

An empty mirrored dimension snapshot exits without replacing Silver, preserving old rows rather than clearing them.

### 4.5 Text delta merge lacks the language key

Source: [delta texts](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py).

Language is removed to retrieve master keys. The same reduced key list is then used for merge, while duplicate validation includes language. Multilingual source rows are therefore not isolated by language in the merge predicate.

### 4.6 Delete-aware row-count checking is incomplete

Source: `common_lib.utils.validate_record_count_match` in the [wheel](../bps_env_c792846f.Environment/Libraries/CustomLibraries/ei_common_lib-1.0.5-py3-none-any.whl).

The validator excludes unknown `Key=-1` rows but not Silver `_Delete='X'` tombstones. Gold delta processors physically delete those rows, so equal source/destination row counts are not a reliable delete-aware invariant.

### 4.7 Unknown keys, duplicate checks, and null equality

Sources: [shared library](../bps_env_c792846f.Environment/Libraries/CustomLibraries/ei_common_lib-1.0.5-py3-none-any.whl), [dimension](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py), [fact](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py).

- Duplicate validation groups by natural keys **and surrogate Key**, potentially missing repeated natural keys assigned different keys.
- Key-retrieval joins are null-safe; Delta merge key strings use ordinary equality.
- `-1` marks unresolved/unknown dimension relationships; it is not a valid match to a populated master entity.
- The reprocessing projection's key-exclusion and key-detection casing differs.

Null key behavior and input uniqueness should be checked explicitly rather than assumed from the presence of validation helpers.

### 4.8 Currency processing has fixed defaults and cross-system assumptions

Sources: [dimension pipeline gate](../bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline/pipeline-content.json) and [currency notebook](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py).

- The gate requires **exactly one** extraction-metadata row, without testing scope.
- The notebook call supplies no overrides for installed lakehouse/database defaults.
- Cube metadata is not filtered by source system.
- Daily rate partitioning and pair/date construction omit `_SystemName`.
- The generated date horizon ends in 2030 unless the source is changed; an existing date table is reused without extension.
- Fiscal averages group by all other columns, including timestamp/unit fields.

This is rate preparation, not proof of correct multi-system reporting currency conversion.

### 4.9 Balance output overwrites can affect another system

Sources: [customer](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py) and [supplier](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py).

The source can be filtered to one system, but full output mode overwrites the entire output path. For example, an existing table with no rows/watermark for a newly processed system can cause that system's full load to replace other systems' balances.

Incremental delete-then-append is two separate Delta transactions; interruption between them can leave missing balances.

### 4.10 Balance incrementality cannot fully detect removed/moved postings

Sources: [balance scope and write logic](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py).

The algorithm detects changed **current source rows** after a timestamp. A posting physically deleted from Gold is no longer available to identify its old entity, and a posting moved to another entity only identifies its new entity. Old aggregate rows can remain unless affected entities are otherwise touched or explicitly rebuilt.

A source becoming empty exits early rather than clearing prior output.

### 4.11 Fiscal densification can cross variants

Source: [balance densify function](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py).

The entity grain does not include fiscal year variant. Densification cross-joins entities with the selected fiscal calendar variants and filters only by first fiscal year-period. Carry-forward partitions similarly omit variant. If the selected calendar contains multiple variants, validate that an entity is not expanded into unrelated variants.

### 4.12 SQL presentation is fixed-depth and not consistently system-isolated

Source: [Gold SQL definitions](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py).

- Hierarchy expansion stops at nine levels.
- Some self-join, leaf/master, and invoice-header/item predicates omit `_SystemName`.
- Current-version views select maximum validity end, not validity as of today.
- Ties on maximum end date may preserve multiple dimension rows.
- Supplier invoice header gross amounts repeat at item grain.
- The positive compliance string is literally `Complaint`, not `Compliant`.

These assumptions may work for a restricted source dataset but should be validated before broader onboarding.

### 4.13 Schema-enabled logging path construction is inconsistent

Sources: `parse_lakehouse_details` and `get_log_file_path` in the [wheel](../bps_env_c792846f.Environment/Libraries/CustomLibraries/ei_common_lib-1.0.5-py3-none-any.whl), plus [collector discovery](../bps_nb_log_collector_c792846f.Notebook/notebook-content.py).

For schema-enabled lakehouses, the table path ends in `Tables/dbo/`. `get_log_file_path` replaces `Tables/` with `Files/Logs/`, leaving `dbo/` in place:

```text
Writer:    .../Files/Logs/dbo/<date>/<guid>/...
Expected by collector date parser:
           .../Files/Logs/<date>/<guid>/...
```

Recursive discovery can still find the Delta roots, but the date-folder extraction reads `dbo` instead of a date. Folder-date pruning no longer has the intended meaning.

### 4.14 Log append and timestamp watermark are not exactly-once ingestion

Source: [log collector](../bps_nb_log_collector_c792846f.Notebook/notebook-content.py).

The collector uses a global `MAX` text timestamp, strict `>`, and append writes without event-key deduplication. Late-arriving files/events at older or equal timestamps can be missed; partial writes/retries can duplicate events. Unreadable log roots are skipped, and derived metric/error DataFrames are never persisted.

### 4.15 Customized pipeline names do not override every notebook target

Sources: [full S2G pipeline](../bps_s2g_full_processing_pipeline_c792846f.DataPipeline/pipeline-content.json) and [dimension pipeline](../bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

Most activities pass lakehouse parameters, but view creation and currency conversion do not. Changing pipeline defaults alone does not redirect those notebooks. Notebook attachment IDs and external connection references are additional deployment dependencies.

## 5. Reporting-layer reconciliation

The [semantic model analysis](05-semantic-model-and-report.md) documents exact model source expressions and the [visual catalog](06-report-object-catalog.md) documents the report definition.

The model's 24 SQL-backed logical tables explicitly resolve to ten `I_*` base tables, nine `vt*` text views, four `v*` presentation views, and `SAPLANGUAGE`. Logical names differing from those physical names are normal aliases. Connection expressions include a nonempty Fabric SQL endpoint default, `Database="bps_gold_c792846f"`, and `Schema_Name="dbo"`; no live connectivity was tested. Validate source availability and model refresh rather than assuming that a static definition proves successful loading.

An exact-name comparison confirms that all 14 required view definitions are present in the Gold notebook. The ten base-table sources depend on actual metadata-driven Delta loads; their absence or presence in the live workspace was not established.

The reporting analysis also established these definition-level limitations:

- Eight predicate-free filter cards reference absent model table `ISOLANGUAGE.LANGUAGECODE`; the model actually provides `SAPLANGUAGE` with `_ISOLanguage` and `LANGUAGECODE`. This is a stale table reference, not merely a missing underscore on a column.
- A control labeled Product selects `CUSTOMER.CUSTOMERNAME`.
- Line Item Details controls `_FIELD_PARAM_TRIALBALANCE_FIELDS`, while its table uses `_FIELD_PARAM_LINE_ITEM_FIELDS`.
- Some transaction-currency parameter choices are incomplete.
- Fifteen aggregate measures reference detail measures, so their names do not prove that the SQL aggregate source is used for those calculations.

No local-date tables or role definitions are checked in. Absence of model role definitions does not establish the live workspace's effective access controls.

## 6. What remains unverified

- Which SAP systems/datasets/tables are actually enabled.
- Whether initial loads, CDF replay, deletes, and late-arriving master data have succeeded.
- The effective runtime version/package/native execution combination.
- Actual capacity, performance, row counts, and concurrency.
- Whether live scheduler interval semantics/activation match the exported configuration.
- Whether every prerequisite SQL object exists at the endpoint.
- Effective workspace/table/model access controls.
- Model connectivity, refresh success, report rendering, and financial reconciliation.

The documentation was checked structurally against the repository and its links/object inventories. It is not a substitute for controlled Fabric integration tests or finance sign-off.
