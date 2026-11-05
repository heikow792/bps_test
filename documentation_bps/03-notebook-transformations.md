# Notebook transformations and shared implementation

[Overview](README.md) | [Orchestration](01-architecture-and-orchestration.md) | [SQL presentation](04-gold-sql-views.md)

## 1. Common data contract

The Spark notebooks are generic processors. Metadata supplies the SAP object and keys; lakehouse names are resolved at runtime into Delta paths.

| Column/convention | Meaning |
|---|---|
| Uppercase business columns | Standardized SAP field names |
| `_SystemName` | Source-system identifier; appended to natural keys and dimension join conditions |
| `_UpdateTimeStamp` | Replication/processing watermark |
| `_Delete` | `X` means deleted; empty string means active |
| `Key` | Gold dimension surrogate key |
| `_key_*` | Foreign key added to a fact; unresolved values are generally `-1` |
| `_Reprocess` | Fact row whose populated business attributes could not resolve a dimension key |
| `_ISOLanguage` | ISO language label derived from SAP language codes |

Some S2G code spells `_UpdateTimeStamp` as `_UpdateTimestamp`, relying on Spark's usual case-insensitive resolution. Validation checks column names using Python sets and the exact `_UpdateTimeStamp` spelling. Changing case-sensitivity or upstream conventions can therefore affect behavior.

The main S2G dimension processors read the **whole named Silver table**, not only the system selected in their pipeline lookup. Their keys include `_SystemName`, but their incremental destination watermark is global. Source-system-aware keys are not the same thing as source-system-isolated processing.

## 2. B2S dimension notebook

Source: [bps_opm_nb_b2s_dim](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py).

### Input and discovery

Required inputs include system, CDS and ODP names, keys, Silver name, mirror name/workspace, and source schema. `p_schema_table_name` specifies the mirrored SAP schema metadata table; the parent defaults it to `DD03ND`.

The notebook:

1. Validates required parameters and strips `$P`, `$T`, `$F`, `$E` from the ODP name.
2. Resolves the Silver lakehouse and mirror through platform APIs.
3. Checks that an ODP- or CDS-named Delta table exists.
4. Prefers the ODP path and falls back to the CDS path.

### Snapshot processing

Every execution reads the full current mirrored dimension snapshot. It obtains the latest Delta history timestamp and puts that same value in `_UpdateTimeStamp` on all snapshot rows, replacing any source-provided column of that name.

It adds `_SystemName` and `_Delete`. There is code for CDF-style `_change_type` handling, but the normal dimension path reads a snapshot and disables latest-row partitioning.

It then:

- Uppercases business column names, preserving special technical-column spellings.
- Reads schema rows from `<mirror>/<schema>/<schema_table>`, filtering `STRUCOBJN` to the CDS name.
- Maps `FIELDNAME`, `DATATYPE`, `LENG`, and `DECIMALS` into casting metadata.
- Applies SAP-aware types.
- Converts `LANGUAGE` and `LANGUAGECODE` from ISO to SAP codes when recognized; existing SAP codes are preserved.

The output is written to Silver under the CDS view name with overwrite, `overwriteSchema=true`, and `replaceWhere "_SystemName = '<system>'"`. This is intended to refresh only that system's slice.

An empty snapshot exits before writing. Consequently, a source dimension becoming completely empty does not clear an existing Silver slice.

### Optional Datasphere branch

If invoked manually with `p_source_type="sap-datasphere"`, a fixed set of unavailable master views is skipped. The list includes billing-plan rule, customer payment terms, several delivery/shipping objects, equipment, functional location, sales group/office, segment, GL account text, and address.

The included pipeline always passes `open-mirroring`, so this branch is not active there. A comment says skipped masters will be generated from texts, but this notebook does not implement that generation.

## 3. B2S fact notebook

Source: [bps_opm_nb_b2s_fact](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py).

Inputs and mirror/schema discovery are similar to the dimension notebook. Natural merge keys are metadata `KeyFields` plus `_SystemName`.

### Initial load

If Silver has no applicable watermark:

- Read the current mirrored snapshot.
- Read the maximum timestamp from mirror Delta history.
- Stamp all rows with that timestamp.
- Add `_SystemName` and active `_Delete`.
- Standardize names, apply DD03ND-derived types, and create the Silver Delta table.

### Incremental load

If Silver has a maximum `_UpdateTimeStamp` for the current system:

```text
readChangeFeed=true
startingTimestamp=<Silver maximum>
then filter _commit_timestamp > <Silver maximum>
```

The commit timestamp becomes `_UpdateTimeStamp`. The intended latest-row logic partitions by natural keys plus system and orders descending by timestamp.

**Implementation detail:** latest-row selection occurs before filtering out `update_preimage`. A preimage and postimage can share a commit timestamp, so ordering by timestamp alone does not deterministically retain the desired postimage. The code then keeps only `insert`, `update_postimage`, and `delete`.

Deletes become `_Delete='X'`. Silver uses `MERGE` with matched update-all and unmatched insert-all, so deletion is a **tombstone update in Silver**, not a physical delete. Gold consumes that marker later.

This notebook does not normalize SAP language fields as the dimension notebook does. It logs write/merge exceptions, but several inner handlers exit with an error string rather than raising.

## 4. Six S2G dimension/text processors

All six receive a JSON array from a Lookup, parse each `KeyFields` string with `ast.literal_eval`, process its tables serially, and accumulate per-table errors into a final notebook exit string.

Common setup resolves lakehouses, enables Delta schema auto-merge and corrected legacy date handling, configures logging, validates source Delta tables/watermarks, and retains existing keys where possible.

### 4.1 Standard dimension, delta

Source: [s2g_dim_delta](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py).

1. Load Silver and validate `_UpdateTimeStamp`, `_SystemName`, `_Delete`.
2. Create Gold if absent. The common helper creates a schema-compatible unknown row with `Key=-1`, not a copy of the complete Silver dataset.
3. For an existing Gold table, find its global maximum update timestamp and take newer Silver rows.
4. Join Silver natural keys plus system to Gold using null-safe equality to retrieve existing `Key`.
5. Allocate new integer keys after the maximum existing key using an ordered row number.
6. Validate duplicates.
7. Merge on natural keys plus system:
   - matched delete marker -> physically delete;
   - matched active row -> update;
   - unmatched active row -> insert.
8. Compare source and destination row counts, excluding `Key=-1` rows.

It implements upsert/delete current-state handling, **not an SCD Type 2 history mechanism**. New keys can have gaps because row numbering spans changed rows that already have keys.

The row-count validator does not filter Silver tombstones, so a valid physical Gold delete can still produce a mismatch error.

### 4.2 Standard dimension, non-delta

Source: [s2g_dim_nodelta](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/notebook-content.py).

Instead of taking rows after a Gold watermark, it selects Silver rows at the maximum timestamp **per `_SystemName`**. This assumes every complete system snapshot has one common timestamp.

It retrieves/allocates stable keys, validates duplicates, appends the unknown `Key=-1` row, and overwrites the entire Gold table. Thus records absent from a complete snapshot disappear.

For `I_LANGUAGE`, it also duplicates `LANGUAGE` into `LANGUAGECODE`.

An empty selected dataset is logged as no work; it does not overwrite Gold with an empty result.

### 4.3 Time-dependent dimension/hierarchy, delta

Source: [s2g_dimtd_delta](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/notebook-content.py).

Two key sets are deliberately used:

- **Row/merge key:** full metadata keys plus `_SystemName`, including validity end when configured.
- **Entity key for surrogate allocation:** the same set **minus `VALIDITYENDDATE`**.

Distinct entity keys are matched to existing Gold keys, new keys allocated, and the entity key joined back to all validity rows. Different validity versions of the same entity can therefore share `Key`.

It then performs the same delta watermark filtering, delete/update/insert merge, duplicate validation, and source/destination row-count comparison as the standard delta processor.

This preserves source-supplied validity rows; it does not generate validity periods or automatically close historical records.

### 4.4 Time-dependent dimension/hierarchy, non-delta

Source: [s2g_dimtd_nodelta](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/notebook-content.py).

Uses the same full-row versus entity-key distinction, but selects the latest complete Silver snapshot per system and overwrites Gold after key assignment and unknown-row union.

Because `Key` can repeat across validity versions, reporting typically needs a latest-version projection such as `vCOSTCENTER` or `vPROFITCENTER` rather than a direct many-to-one relationship to the unfiltered versioned table.

### 4.5 Text dimension, delta

Source: [s2g_text_delta](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py).

1. Load Silver text and the `relatedCDSViewName` master from Gold.
2. Derive a master join key by removing `LANGUAGE` from metadata keys and adding system.
3. Apply the global Gold text timestamp watermark.
4. Left-join to the master to copy its `Key`; do not allocate separate text keys.
5. Validate uniqueness using master join keys plus `LANGUAGE`, when present.
6. Derive `_ISOLanguage`.
7. Create an empty Gold target if needed, then merge deletes/updates/inserts.

**Important inconsistency:** the merge condition uses the master join keys, with `LANGUAGE` removed, while uniqueness validation includes language. Multiple language rows for one master can therefore match the same target rows. This should not be described as a correctly language-isolated incremental merge.

If there is no data and no Gold target, it creates an empty text target. That zero-row path does not assign a master `Key` to actual rows.

### 4.6 Text dimension, non-delta

Source: [s2g_text_nodelta](../bps_nb_s2g_text_nodelta_c792846f.Notebook/notebook-content.py).

Selects the latest Silver snapshot per system, copies keys from the related master using natural keys without language, validates text uniqueness, adds `_ISOLanguage`, and overwrites Gold. No separate unknown text row is added after the join.

The later `vt*` SQL views fill missing translations using the master code; that fallback is a SQL presentation concern, not part of this Spark text load.

## 5. S2G fact processor

Source: [s2g_fact](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py).

### 5.1 Validation and initial target

The notebook requires lakehouse names, CDS name, key fields, and nonempty cube configuration. It validates the Silver fact and each configured Gold dimension/required join field.

An empty Gold fact is created on first load, without a dimension-style `Key=-1` row. The main merge key is the fact's natural key plus `_SystemName`.

### 5.2 New/changed fact rows

For an existing fact, it takes Silver rows newer than the **global** Gold fact maximum timestamp. There is no system filter on this read, despite a declared system parameter.

For more than 200,000 rows, it repartitions into eight partitions on the first natural-key field.

For each configured relationship, in supplied order:

1. Load its Gold dimension.
2. Apply dimension/fact-specific filtering.
3. Parse tuple-list join conditions and append `_SystemName` equality.
4. Left-join, copy requested dimension attributes, and create the configured surrogate foreign key.
5. Coalesce unmatched dimension keys to `-1`.

Special cases include excluding fiscal special periods; deduplicating cost/profit/activity-type dimensions at join grain; and restricting purchasing document category to `F` for specified purchase-order/requisition facts.

A row is marked `_Reprocess=true` if relevant business join fields are populated but its surrogate key is `-1`. Active records are merged, and delete markers physically remove Gold records.

### 5.3 Repairing unresolved keys

On subsequent runs, a second phase reads Gold rows with `_Reprocess=true` **or any null `_key` column**, rejoins dimensions, recalculates the flag, and updates matched active facts.

This is intended to repair late-arriving master data even if the fact itself did not change. It is not a full rebuild of all historical fact relationships when valid dimension assignments change.

One implementation caveat is inconsistent key-column casing in the reprocessing projection: exclusion tests `"_key" not in col`, while discovery tests `"_key" in col.lower()`. Whether prior key columns are removed therefore depends on their exact casing.

## 6. Currency conversion notebook

Source: [s2g_currency_conversion](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py).

This notebook prepares exchange-rate facts; it does **not** rewrite transaction amounts into a reporting currency.

### Inputs and scope

Defaults name the installed Silver/Gold/metadata objects and `I_EXCHANGERATERAWDATA`. It creates its own GUID when empty. These values are ordinary cells rather than the parameter-cell pattern used by most other notebooks, and its pipeline call passes no overrides.

It queries `cubeMetadata` for that fact's relationships without filtering `SystemName`.

### Daily rate construction

1. Create Gold `I_DATE` if absent, covering **2015-01-01 through 2030-12-31**, with year/month/day and day/month labels.
2. Read the Silver exchange-rate table, drop `MANDT`, and parse `VALIDITYSTARTDATE`.
3. For negative SAP exchange rates, use `1 / abs(rate)`.
4. Cross-join distinct `(EXCHANGERATETYPE,SOURCECURRENCY,TARGETCURRENCY)` combinations with dates.
5. Left-join observed rates.
6. Add same-currency rates of 1, with source/target unit factors of 1, for distinct source currencies and source systems.
7. Forward-fill exchange rate, unit factors, update timestamp, and system along each rate-type/currency-pair timeline.
8. Join configured Gold dimensions; filter fiscal rows whose date span is not greater than one day and apply the shared fiscal rules.
9. Cast unit factors to double and overwrite `I_EXCHANGERATERAWDATA_DAILY`.

Forward-fill partitions do not include `_SystemName`, and the ordinary pair/date expansion also omits system. Multi-system rate isolation is therefore not guaranteed. Dates before the first known rate are not backfilled.

### Fiscal-period rates

It drops `VALIDITYSTARTDATE`, groups by **every remaining column except `EXCHANGERATE`**, averages the rate, and overwrites `I_EXCHANGERATERAWDATA_FISCALPERIOD` with `AVGEXCHANGERATE`.

The intended fiscal-period grain depends on configured joins and copied fields. Since update timestamp and unit-factor columns remain grouping fields, this is not unconditionally one arithmetic average per fiscal period and currency pair.

## 7. Customer and supplier balance aggregates

Sources: [customer](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py) and [supplier](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py).

The notebooks share the same implementation except customer/supplier identity, output name, logging labels, and financial account filter.

| Property | Customer | Supplier |
|---|---|---|
| Account filter | `FINANCIALACCOUNTTYPE='D'` | `FINANCIALACCOUNTTYPE='K'` |
| Party foreign key | `_key_ICUSTOMER` | `_key_ISUPPLIER` |
| Output | `BPS_CUSTOMERBALANCEAGGR` | `BPS_SUPPLIERBALANCEAGGR` |

Both read Gold `I_OPERATIONALACCTGDOCITEM` and `I_FISCALPERIODFORVARIANT`, optionally filtered to the supplied system.

### 7.1 Grain and currencies

The entity grain contains:

- Company code key.
- GL account-in-chart key.
- Customer or supplier key.
- Special GL code key.
- Accounting document category key.
- `_SystemName`.

Noted/statistical document categories are deliberately retained rather than removed. Currency-code fields further separate running-balance streams.

Four source amount/code pairs become a long output:

| `CURRENCYTYPE` | Currency code | Amount |
|---|---|---|
| `CC` | `COMPANYCODECURRENCY` | `AMOUNTINCOMPANYCODECURRENCY` |
| `FC` | `FUNCTIONALCURRENCY` | `AMOUNTINFUNCTIONALCURRENCY` |
| `TC` | `TRANSACTIONCURRENCY` | `AMOUNTINTRANSACTIONCURRENCY` |
| `GC` | `ADDITIONALCURRENCY1` | `AMOUNTINADDITIONALCURRENCY1` |

The aggregation adds fiscal period key, fiscal year, year variant, period, and year-period. Output includes `CURRENCY`, `CURRENCYTYPE`, debit/credit/net, and three carry-forward measures.

### 7.2 Calculation

For each amount field:

```text
DEBIT_BALANCE  = sum(amount where DEBITCREDITCODE = 'S')
CREDIT_BALANCE = sum(-amount where DEBITCREDITCODE = 'H')
NET_BALANCE    = DEBIT_BALANCE - CREDIT_BALANCE
```

The credit sign inversion assumes the source credit amounts already have the corresponding SAP sign convention; this is not an absolute-value calculation.

Each entity is densified over the fiscal calendar from its first active fiscal year-period through the end of the selected year range. Missing posting periods get zero activity.

```text
CARRY_FORWARD_FROM_PREV_PERIOD = prior period net sum in the same year
CARRY_FORWARD_FROM_PREV_YEAR   = net sum from all earlier years
CARRY_FORWARD_TOTAL            = sum of those two opening-balance components
```

The “previous year” field includes **all earlier fiscal years**, not only the immediately preceding year. Current closing balance would combine opening carry-forward and current-period net; `NET_BALANCE` alone is period movement.

### 7.3 Incremental scope and write

If output is absent or has no watermark, process the full selected source. Otherwise:

1. Find source rows newer than the output's system-specific maximum timestamp.
2. Identify touched dimension-key entities.
3. Re-read **their complete posting history**, not only the delta, so running totals remain consistent.
4. Recalculate all their output rows.
5. Delete existing rows for touched entities via Delta merge, then append replacements.

Full mode overwrites the complete output table; incremental mode deletes and appends in two transactions. The watermark stamped on all replacement rows is the selected source's maximum timestamp.

Physical deletions from the upstream Gold fact and changes moving a posting to another entity are not fully represented by this current-row timestamp mechanism. Multi-system initial/full overwrites and fiscal-variant densification also need validation; see [Operations](07-operations-and-caveats.md).

## 8. SQL view-creation notebook

Source: [gold_view_creation](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py).

This notebook is not a PySpark materialization job. It uses Jupyter `%%tsql` magic to issue `CREATE OR ALTER VIEW` statements against the installed Gold lakehouse SQL endpoint.

It defines 80 views. Every SQL cell checks prerequisites through `INFORMATION_SCHEMA.TABLES`, emitting an `ERROR:` result if they are missing.

A Python wrapper replaces the T-SQL cell magic with a version that captures output and exceptions, records the view result, and continues. The final cell prints totals for success/failure/missing prerequisites. It does **not** raise if any view failed.

Consequently, a completed view notebook is not proof that all 80 views were deployed. See [the full SQL view catalog](04-gold-sql-views.md).

## 9. Log collector and its copy

Sources: [scheduled original](../bps_nb_log_collector_c792846f.Notebook/notebook-content.py) and [copy](../bps_nb_log_collector_c792846f%20Copy.Notebook/notebook-content.py).

Their notebook-content files are identical; only item identity differs. The copied item has no inbound pipeline reference.

The collector:

1. Resolves the Silver lakehouse and metadata SQL database.
2. Builds an encrypted SQL connection using a platform access token and ODBC Driver 18.
3. Gets the SQL `MAX(PreciseTimestamp)` from `log_events`.
4. Recursively discovers folders containing `_delta_log` under Silver `Files/Logs`.
5. Skips older date folders, reads Delta log tables, and unions schemas by name with missing columns allowed.
6. Keeps log rows whose timestamp is strictly newer than the SQL maximum.
7. Renames `guid -> ServiceActivityId`, `precise_timestamp -> PreciseTimestamp`, `view_name -> TableName`, `message -> Message`, `log_type -> LogType`, and `systemName -> SystemName`.
8. Appends all logs to SQL via JDBC, batch size 1,000.

It also computes a `metrics_df` from messages containing case-sensitive `"Written"` and an `errorlogs_df` from level `ERROR`. **Neither is persisted.** Only `final_df` is written.

Read failures are printed/skipped; JDBC errors exit with text rather than raising. With no unique event key, append retries can duplicate messages; a strict global timestamp watermark can miss late-arriving logs.

## 10. Bundled `common_lib`

Source archive: [ei_common_lib wheel](../bps_env_c792846f.Environment/Libraries/CustomLibraries/ei_common_lib-1.0.5-py3-none-any.whl). Its Python source was inspected directly from the archive without installing or executing it.

| Module | Responsibility |
|---|---|
| `constants.py` | Log columns/stages, delete marker, SQL connection template, CDS-to-business-date lookup |
| `data_type_mapping.py` | SAP CHAR/CUKY/TIMS/UNIT/LANG strings, DATS dates, NUMC integers, and QUAN/DEC/CURR decimals |
| `expression_helper.py` | Merge key conditions and insert/update expression helpers |
| `utils.py` | Delta initialization, paths, source discovery parsing, joins, language conversion, types, timestamps, validation |
| `exceptions.py` | Named errors for missing artifacts/tables, watermark/key/count/cube validation |
| `logger/dataframe_logger.py` | Buffered structured logs with correlation, stage/system, runtime context, and Delta persistence |

### Helpers that materially affect the solution

- **Gold initialization:** removes `_Delete` from the initial schema, adds integer `Key` for dimensions, and creates either an empty target or a single unknown row.
- **Key retrieval joins:** use Spark null-safe equality. Final merge key strings instead use ordinary `=`, so null natural keys are not consistently treated across all phases.
- **Fact dimension joins:** parse configured tuple lists, append system equality, use `coalesce(...,'NULL_VALUE')` for equality and ordinary bounds comparisons for validity conditions, left join and default keys to `-1`.
- **SAP type application:** decimals use DD03ND length/decimals; dates use a sampled format detector; NUMC converts `00000000` to null then casts to integer. Numeric conversion can remove leading zeros.
- **Language mapping:** ISO-to-SAP preserves unrecognized input; SAP-to-ISO text mapping uses a dictionary lookup and can return null for unknown codes.
- **Duplicate validation:** groups by configured primary-key columns **plus `Key`**, not primary keys alone.
- **Cube validation:** checks Gold dimensions and their join fields plus key/system columns; fact-field validation is limited to relationships with `JoinOrder==0`.
- **Required parameter validation:** rejects null and zero-length strings, but does not trim whitespace.
- **Logger:** records local `datetime.now()` strings with microseconds, buffers entries, and appends Delta logs with schema merge. Runtime fields can be null when callers omit context/stage/system (as the balance notebooks do).

Additional utility functions support SQL connections/query parsing, Silver target creation, ODP mapping, unused-column removal, date detection, and path parsing. Their presence does not imply every helper is used on the installed orchestration path.

## 11. Error semantics

The code uses three materially different failure patterns:

1. **Raise an exception:** the Fabric activity can fail naturally.
2. **Log and `notebook.exit(error_text)`:** returns diagnostic text but does not itself enforce a failed pipeline status.
3. **Print and continue:** used by the SQL-view wrapper and some collector discovery paths.

The dimension notebooks deliberately aggregate per-table errors into exit text, and pipelines do not inspect that text. Operators must therefore check the detailed logs and notebook summary, not only the pipeline's green activity indicators.
