# Adding an additional table to BPS: step-by-step guide

[Overview](README.md) | [Metadata reference](02-metadata-database.md) | [Notebook behavior](03-notebook-transformations.md) | [Operational caveats](07-operations-and-caveats.md)

## 1. Short answer: what needs to change?

For an additional **SAP CDS/ODP table on the existing OpenMirroring path**, the standard extension is:

1. Make the source object and its schema metadata available in the mirrored database.
2. Register the object in `viewMetadata`.
3. Add its dataset/table scope configuration.
4. For a fact, configure its dimension relationships in `cubeMetadata`.
5. Run and validate B2S, then S2G.
6. If needed, add SQL presentation views, semantic model tables/relationships/measures, and report visuals or field-parameter entries.

**A normal supported table does not require a new pipeline, a new generic processing notebook, or a new SQL metadata table.** The existing pipeline lookups discover it from metadata.

However:

- Metadata does not configure the external SAP replication publisher.
- Loading a Gold table does not automatically add it to Power BI.
- A new hierarchy or translated presentation view is not generated simply by adding metadata.
- A new relationship on an existing fact does not guarantee historical rows will be re-enriched automatically.
- Some existing delta/multi-system behaviors need explicit validation before production use.

This guide is based on the checked-in implementation. SQL and M examples are templates, not statements executed during documentation. Example SAP object names and fields are **hypothetical**; replace them with verified source definitions.

### Change matrix

| Surface | Standalone dimension | Text table | New fact | New dimension used by an existing fact |
|---|---|---|---|---|
| Upstream SAP publisher and mirror | Required | Required for text object | Required | Required for new dimension |
| Mirrored DD03ND schema rows | Required | Required | Required | Required for new dimension; check fact fields too |
| `viewMetadata` | Add one row | Add one row linked to master | Add one row | Add dimension row |
| Dataset/table scope | Add membership; dataset must be enabled | Same | Same | Same |
| `cubeMetadata` | Only if a fact should reference it | Normally no separate fact relationship for the text | At least one valid relationship is required by current fact notebook | Add relationship for each affected fact |
| Standard pipelines/notebooks | Usually no edits | Usually no edits for supported snapshot processing | Usually no edits | Usually no routing edits; historical enrichment may need a controlled backfill |
| SQL presentation | Optional | Add/customize `vt*` view if translated columns are needed | Optional view/aggregate | Optional dimension/current-version view |
| Semantic model/report | Only if users need it | Update language selectors if used | Add model relationships and measures if used | Add model relationship/fields and affected selectors |

For a **derived Gold table** rather than a replicated SAP object, the source-registration steps are not sufficient: implement its producing notebook/SQL logic, wire dependencies into orchestration, then complete the reporting and validation steps. For a new connector such as Salesforce/ECC or a new SAP system, this is a larger onboarding task; the presence of support schemas does not make the included OpenMirroring pipeline support those paths.

## 2. Step 1: define the table contract and impact

Record these decisions before changing configuration:

| Decision | Required answer |
|---|---|
| Business purpose | What analysis or process needs the table? |
| Scope of delivery | Silver/Gold only, or also SQL presentation and the Financial Insights report? |
| Source system | Exact existing `systemDetails.SystemName` |
| Source location | Mirror display name, source schema, actual replicated ODP/CDS table name |
| Canonical name | `CDSViewName`; this becomes the Silver/Gold Delta table name |
| Dataset | Existing or deliberately created `DatasetName` |
| Grain | What does one source row represent? |
| Natural key | Exact ordered business key columns, including validity/language where applicable |
| Classification | `DIMENSION`, `DIMENSION-TD`, `HIERARCHY`, `TEXT`, or `FACT` |
| Extraction behavior | Snapshot versus changes; how inserts, updates, deletes, and empty snapshots behave |
| Dependencies | Master for a text, dimensions for a fact, consuming facts for a dimension |
| Reporting contract | Required fields, labels, measures, relationships, and storage mode |

### Running example

Suppose the existing SAP system gains a channel master:

```text
CDSViewName: ZI_BPS_CHANNEL
Business columns: CHANNEL, CHANNELNAME
Natural key: CHANNEL
Type: DIMENSION
Delta: 0
```

An optional associated text table and new fact could be:

```text
ZI_BPS_CHANNELTEXT
    fields: CHANNEL, LANGUAGE, CHANNELNAME
    key: CHANNEL + LANGUAGE
    Type=TEXT, Delta=0, relatedCDSViewName=ZI_BPS_CHANNEL

ZC_BPS_CHANNELITEM
    fields include DOCID, ITEMID, CHANNEL, AMOUNT, CURRENCY
    key: DOCID + ITEMID
    Type=FACT
    relationship: CHANNEL -> ZI_BPS_CHANNEL.CHANNEL
```

These are illustrative contracts, not actual objects found in this repository. Do not assume that an existing financial fact contains a `CHANNEL` field.

**Gate:** do not proceed until keys and field types are validated against real source data. A nonunique or incomplete key can corrupt merge results or multiply fact rows.

## 3. Step 2: confirm the source system and establish a safe change window

In the **metadata SQL database**, run a read-only preflight:

```sql
DECLARE @SystemName nvarchar(50) = N'<EXISTING_SYSTEM_NAME>';

SELECT
    SystemName, SourceType, SystemType, ConnectionType,
    ServerName, SubscriberName
FROM dbo.systemDetails
WHERE SystemName = @SystemName;
```

For the included B2S orchestration, the intended connection row must have:

```text
SourceType     = SAP
SystemType     = S4HANA
ConnectionType = OpenMirroring
```

`ServerName` is used as the mirrored database display name; `SubscriberName` is passed as the source schema. Do not assume the source schema is `dbo`.

Check whether the same system has additional connection rows. The S2G system lookup and `extractionMetadata` join only on system name in relevant places, so multiple connection rows can multiply work/metadata.

Before enabling anything:

1. Use a development/test workspace with representative data where possible.
2. Export the affected metadata rows and retain their original values outside source control if they contain sensitive configuration.
3. Record the current row counts, source-system coverage, and dimension keys for affected Gold objects.
4. Arrange a controlled run window or pause relevant scheduled triggers through the supported Fabric controls.
5. Avoid running onboarding and scheduled jobs concurrently.
6. Plan for BPS-managed notebook updates: notebook headers warn that manual edits are overwritten.

Do not silently enable an existing disabled dataset: that can activate **other tables**, not just the new one. Do not add a duplicate `systemDetails` row simply to register a table.

## 4. Step 3: publish the source table and its SAP schema metadata

Configure the existing external replication publisher to send the new table into the GenericMirror database. That publisher is not implemented in this repository.

Verify:

1. The source object is eligible for the selected replication mechanism.
2. A nonempty initial snapshot arrives, or empty-table behavior is explicitly tested.
3. Its actual table name matches either the ODP name after suffix stripping or the CDS name.
4. The table is a valid Delta source and source facts support Delta change data feed.
5. Source deletes and updates are published with the expected semantics.
6. DD03ND, or the configured schema table, includes the new object's field rows.

The [B2S dimension notebook](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py) and [B2S fact notebook](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py) try:

```text
<mirror tables path>/<source schema>/<normalized ODPName>
then, if not found:
<mirror tables path>/<source schema>/<CDSViewName>
```

ODP suffixes `$P`, `$T`, `$F`, and `$E` are removed. A metadata row pointing at a different nonexistent source table is not enough.

### DD03ND contract

For every field needing SAP type conversion, verify these fields in the mirrored schema table:

```text
STRUCOBJN = exact CDSViewName supplied to the notebook
FIELDNAME = source field name after standardization
DATATYPE  = SAP type
LENG      = length/precision input
DECIMALS  = scale input
```

The notebook filters `STRUCOBJN` using **the CDS name**, even if it reads data from an ODP-named table. It fails if no schema rows exist for that CDS name.

SAP schema metadata matters for dates, decimals, quantities, amounts, and numeric text. `NUMC` conversion can remove leading zeros; decimal conversion uses length/decimals. Verify identifier semantics and amount precision instead of relying solely on successful casts.

**Do not use `dbo.fieldMetadata` as a substitute for DD03ND on this path.** The current SAP B2S notebooks read the mirrored schema table, not `fieldMetadata`.

## 5. Step 4: choose the correct processor and metadata values

### Dispatch rules

| Metadata type | `Delta` | Current behavior |
|---|---:|---|
| `DIMENSION` | 0 | Latest complete Silver snapshot per system; preserve/allocate keys; overwrite Gold |
| `DIMENSION` | 1 | Silver rows newer than Gold watermark; merge updates/deletes/inserts |
| `DIMENSION-TD` or `HIERARCHY` | 0 | Snapshot processing with an entity key shared across validity records |
| `DIMENSION-TD` or `HIERARCHY` | 1 | Incremental validity-record merge with shared entity keys |
| `TEXT` | 0 | Snapshot text processing; copy master `Key`; derive `_ISOLanguage` |
| `TEXT` | 1 | Incremental text processing; current merge omits language from its predicate |
| `FACT` | 0 or 1 | Existing fact routing does not branch on this flag; B2S uses initial snapshot then CDF, S2G enriches/merges facts |

**Important:** B2S reads all non-fact tables as snapshots even when their metadata has `Delta=1`. The flag is not an instruction to enable source CDF or a guarantee of change-aware dimension ingestion.

For a new complete-snapshot master/text table, `Delta=0` is generally the appropriate starting point **if that matches the actual source contract**. In the current implementation:

- Snapshot-to-delta dimension processing does not synthesize delete markers for missing source rows.
- Multilingual `TEXT, Delta=1` has a language-key merge inconsistency.

Resolve these limitations before choosing a delta route that depends on their correct behavior.

### Keys and related masters

- Store keys as a Python-list literal, for example `["CHANNEL"]`.
- Use standardized uppercase business fields.
- Do **not** add `_SystemName` to `KeyFields`; the processors append it.
- Include `LANGUAGE` in a text table's natural key where language distinguishes rows.
- Set `relatedCDSViewName` for texts to an actual loaded master dimension, not another text view.
- Include full source validity-row keys for time-dependent objects. The TD processor removes exactly `VALIDITYENDDATE` from the surrogate entity-key set; it does not understand arbitrary alternative validity names.
- Do not add extra SCD logic by assumption: the TD notebook preserves supplied validity records and does not invent or close validity periods.

Source contracts: [viewMetadata](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/viewMetadata.sql), [dimension routing](../bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline/pipeline-content.json), and [fact routing](../bps_s2g_fact_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

## 6. Step 5: register the new object with processing initially disabled

Execute configuration changes against the **metadata database**, not a lakehouse SQL analytics endpoint.

For an ordinary table, the existing metadata schema is sufficient. Add **data rows**, not `CREATE TABLE` definitions for SAP business objects in the metadata SQL project.

### Example: new channel dimension

Replace the system, dataset, object names, keys, and descriptions before use. This example:

- Requires an existing supported source connection.
- Refuses to overwrite an existing view registration.
- Preserves an existing dataset's enable state.
- Creates a new dataset only if requested by a previously nonexistent name.
- Registers the table membership with `IsEnabled=0`.

```sql
SET XACT_ABORT ON;

DECLARE @SystemName nvarchar(50) = N'<EXISTING_SYSTEM_NAME>';
DECLARE @DatasetName nvarchar(300) = N'<TARGET_DATASET_NAME>';
DECLARE @CDSViewName nvarchar(300) = N'ZI_BPS_CHANNEL';
DECLARE @ODPName nvarchar(300) = N'ZI_BPS_CHANNEL';

IF @SystemName = N'<EXISTING_SYSTEM_NAME>'
   OR @DatasetName = N'<TARGET_DATASET_NAME>'
BEGIN
    THROW 50000, 'Replace the system and dataset placeholders before execution.', 1;
END;

BEGIN TRY
    BEGIN TRANSACTION;

    IF NOT EXISTS (
        SELECT 1
        FROM dbo.systemDetails
        WHERE SystemName = @SystemName
          AND SourceType = N'SAP'
          AND SystemType = N'S4HANA'
          AND ConnectionType = N'OpenMirroring'
    )
    BEGIN
        THROW 50001, 'No supported SAP OpenMirroring system registration exists.', 1;
    END;

    IF EXISTS (
        SELECT 1
        FROM dbo.viewMetadata
        WHERE SystemName = @SystemName
          AND CDSViewName = @CDSViewName
    )
    BEGIN
        THROW 50002, 'View metadata already exists; inspect it instead of overwriting.', 1;
    END;

    IF EXISTS (
        SELECT 1
        FROM dbo.extractionScope
        WHERE SystemName = @SystemName
          AND DatasetName = @DatasetName
          AND TableName = @CDSViewName
    )
    BEGIN
        THROW 50003, 'The table already has this dataset membership.', 1;
    END;

    IF NOT EXISTS (
        SELECT 1
        FROM dbo.extractionScopeByDataset
        WHERE SystemName = @SystemName
          AND DatasetName = @DatasetName
    )
    BEGIN
        INSERT INTO dbo.extractionScopeByDataset
            (SystemName, DatasetName, IsEnabled)
        VALUES
            (@SystemName, @DatasetName, 1);
    END;

    INSERT INTO dbo.viewMetadata
        (SystemName, CDSViewName, Context, Description, Type,
         ODPName, Delta, KeyFields, relatedCDSViewName)
    VALUES
        (@SystemName, @CDSViewName, N'Channel analytics',
         N'Channel master: one row per CHANNEL', N'DIMENSION',
         @ODPName, 0, N'["CHANNEL"]', NULL);

    INSERT INTO dbo.extractionScope
        (SystemName, DatasetName, TableName, IsEnabled)
    VALUES
        (@SystemName, @DatasetName, @CDSViewName, 0);

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF XACT_STATE() <> 0
        ROLLBACK TRANSACTION;
    THROW;
END CATCH;
```

This is a **new-registration template**, not a general idempotent upsert. If it reports existing rows, inspect and reconcile them; do not delete/recreate them just to rerun the example.

### Variations

Use the same registration/scope process for other objects, changing the metadata contract:

| Example object | `Type` | `Delta` | `KeyFields` stored value | `relatedCDSViewName` |
|---|---|---:|---|---|
| `ZI_BPS_CHANNEL` | `DIMENSION` | 0 | `["CHANNEL"]` | NULL |
| `ZI_BPS_CHANNELTEXT` | `TEXT` | 0 | `["CHANNEL", "LANGUAGE"]` | `ZI_BPS_CHANNEL` |
| `ZC_BPS_CHANNELITEM` | `FACT` | 1, by example convention | `["DOCID", "ITEMID"]` | NULL |

For the fact, its `Delta` value does not change the existing fact pipeline's CDF/incremental behavior. Correct source CDF configuration remains required.

Register a text master and its text table separately. Enabling only the text will not create its master or assign valid keys.

## 7. Step 6: configure fact relationships when required

Skip this step for a standalone dimension or text that no fact needs to reference.

For a new fact, the current [S2G fact notebook](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py) rejects an empty `p_cubeConfig`. A fact with no dimensions is therefore **not supported by metadata alone**; supporting that case would require an intentional notebook extension.

For a new dimension used by an existing fact, add a relationship only after confirming the fact has the required business join fields.

### Example relationship

After both source objects and their metadata are registered:

```sql
DECLARE @SystemName nvarchar(50) = N'<EXISTING_SYSTEM_NAME>';
DECLARE @FactTable nvarchar(300) = N'ZC_BPS_CHANNELITEM';
DECLARE @RelationshipName nvarchar(300) =
    N'ZC_BPS_CHANNELITEM_TO_ZI_BPS_CHANNEL';

IF @SystemName = N'<EXISTING_SYSTEM_NAME>'
BEGIN
    THROW 50010, 'Replace the system placeholder before execution.', 1;
END;

IF NOT EXISTS (
    SELECT 1 FROM dbo.viewMetadata
    WHERE SystemName = @SystemName
      AND CDSViewName = @FactTable
      AND Type = N'FACT'
)
BEGIN
    THROW 50011, 'Register the fact metadata before adding the relationship.', 1;
END;

IF NOT EXISTS (
    SELECT 1 FROM dbo.viewMetadata
    WHERE SystemName = @SystemName
      AND CDSViewName = N'ZI_BPS_CHANNEL'
      AND Type IN (N'DIMENSION', N'DIMENSION-TD', N'HIERARCHY')
)
BEGIN
    THROW 50012, 'Register the master dimension before adding the relationship.', 1;
END;

IF EXISTS (
    SELECT 1 FROM dbo.cubeMetadata
    WHERE SystemName = @SystemName
      AND RelationshipName = @RelationshipName
)
BEGIN
    THROW 50013, 'Relationship already exists; inspect its configuration.', 1;
END;

INSERT INTO dbo.cubeMetadata
    (SystemName, RelationshipName, FactTable, DimensionTable,
     JoinCondition, SKColumn, DimColumns, JoinOrder)
VALUES
    (@SystemName, @RelationshipName, @FactTable, N'ZI_BPS_CHANNEL',
     N'[("CHANNEL", "CHANNEL", "==")]',
     N'_key_ZIBPSCHANNEL', N'[]', 0);
```

The stored join string is a Python list of tuples; the double-quoted field names are compatible with `ast.literal_eval`.

### Relationship rules

1. `SKColumn` must be a new, unambiguous output key for that relationship. Use the same name later in the semantic model.
2. `DimColumns` is required. Use the literal `[]` for no copied attributes, not NULL.
3. The helper adds `_SystemName` equality automatically; do not redundantly add it to the tuple list.
4. Supported operators are `==`, `>=`, and `<=`.
5. A validity join can include a fact date bounded by dimension validity dates, but validate boundary conditions and uniqueness.
6. Set `JoinOrder` to ensure fields copied by an earlier join exist before a later join uses them. Do not assume the example's `0` is suitable for an existing fact's relationship chain.
7. Prefer deterministic order values; ties are not given an additional ordering key by the pipeline.
8. The fact pipeline includes relationships only for dimensions in extraction scope for that system. Registering a cube row does not make a disabled dimension usable.
9. Verify the join returns at most one intended dimension row per fact. Many matching validity rows can multiply facts.
10. Use `DimColumns` cautiously: copying a dimension column can replace an existing fact column of the same name.

For an existing fact, the relationship change and the historical backfill in Step 10 are a single delivery: do not announce the new dimension as complete after testing only new postings.

## 8. Step 7: verify metadata resolution, then enable only the intended membership

Check the raw configuration before running:

```sql
DECLARE @SystemName nvarchar(50) = N'<EXISTING_SYSTEM_NAME>';
DECLARE @DatasetName nvarchar(300) = N'<TARGET_DATASET_NAME>';
DECLARE @CDSViewName nvarchar(300) = N'ZI_BPS_CHANNEL';

SELECT *
FROM dbo.viewMetadata
WHERE SystemName = @SystemName AND CDSViewName = @CDSViewName;

SELECT *
FROM dbo.extractionScope
WHERE SystemName = @SystemName AND TableName = @CDSViewName;

SELECT *
FROM dbo.extractionScopeByDataset
WHERE SystemName = @SystemName AND DatasetName = @DatasetName;

SELECT
    SystemName, CDSViewName, SourceType, Type, Delta, ODPName,
    KeyFields, relatedCDSViewName,
    IsTableEnabled, IsDatasetEnabled, inScope
FROM dbo.extractionMetadata
WHERE SystemName = @SystemName AND CDSViewName = @CDSViewName;
```

Before enabling, this registration should normally have `IsTableEnabled=0` and `inScope=0`. Investigate:

- No row: a required system/scope/dataset join is missing.
- More rows than expected: multiple dataset memberships or system connection rows.
- Already in scope: another enabled membership may already activate the object.
- Incorrect keys/type/related master: fix before any load.

When prerequisites are ready and the change window is active, enable the one new membership:

```sql
DECLARE @SystemName nvarchar(50) = N'<EXISTING_SYSTEM_NAME>';
DECLARE @DatasetName nvarchar(300) = N'<TARGET_DATASET_NAME>';
DECLARE @CDSViewName nvarchar(300) = N'ZI_BPS_CHANNEL';

IF @SystemName = N'<EXISTING_SYSTEM_NAME>'
   OR @DatasetName = N'<TARGET_DATASET_NAME>'
BEGIN
    THROW 50020, 'Replace the system and dataset placeholders before execution.', 1;
END;

IF NOT EXISTS (
    SELECT 1
    FROM dbo.extractionScopeByDataset
    WHERE SystemName = @SystemName
      AND DatasetName = @DatasetName
      AND IsEnabled = 1
)
BEGIN
    THROW 50021, 'Dataset is missing or disabled; obtain approval before enabling it.', 1;
END;

UPDATE dbo.extractionScope
SET IsEnabled = 1
WHERE SystemName = @SystemName
  AND DatasetName = @DatasetName
  AND TableName = @CDSViewName;

IF @@ROWCOUNT <> 1
BEGIN
    THROW 50022, 'Expected exactly one table membership to enable.', 1;
END;
```

Repeat the verification query and require at least one resolved `inScope=1` row for each intended object. Do not treat raw `viewMetadata` insertion as proof of pipeline eligibility.

The routing view definition is [extractionMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Views/extractionMetadata.sql).

## 9. Step 8: run a restricted B2S test

Use [B2S orchestration](../bps_om_b2s_orchestration_pipeline_c792846f.DataPipeline/pipeline-content.json) with:

| Parameter | Example value |
|---|---|
| `Silver_Lakehouse_Name` | `bps_silver_c792846f`, or the deliberately prepared test target |
| `CdsViewNames` | `ZI_BPS_CHANNEL` |
| `Schema_Table_Name` | `DD03ND`, unless a verified alternative is used |

For a master and text, pass:

```text
ZI_BPS_CHANNEL,ZI_BPS_CHANNELTEXT
```

For a fact with newly onboarded dimensions, include all new source objects that need initial loads. The comma-separated allow-list does **not** automatically add dependencies.

### Scope precautions

- The top-level B2S pipeline has no system-selection parameter; it loops all eligible SAP/OpenMirroring/S4HANA system rows.
- The allow-list restricts CDS names, not systems. If the same CDS name is enabled elsewhere, it can also run there.
- For a single-system controlled test, use an isolated test configuration or invoke the appropriate child with explicit system/mirror/schema parameters.
- Non-fact B2S iterations are parallel. Do not rely on master/text B2S ordering; their key relationship is established later in S2G.
- A custom Silver target needs to be a prepared lakehouse with compatible access/attachments; changing one parameter does not validate all runtime dependencies.

### Verify Silver before continuing

Require:

1. The expected Delta table exists under the canonical CDS name.
2. Business columns are standardized and key fields exist.
3. `_SystemName`, `_UpdateTimeStamp`, and `_Delete` exist with expected values.
4. Source-system row counts and distinct key counts match expectations.
5. Date and decimal conversion is correct; no unexpected nulls or lost identifier semantics.
6. Fact CDF updates create new watermark values and tombstones as designed.
7. Logs and notebook exit values show no processing failures.

An empty mirrored dimension currently exits without clearing an existing Silver slice. Test that condition explicitly if it is valid for this source.

## 10. Step 9: load Gold in dependency order

For a normal integration test, use [full S2G orchestration](../bps_s2g_full_processing_pipeline_c792846f.DataPipeline/pipeline-content.json):

| Parameter | Example value |
|---|---|
| `p_silver_lakehouse_name` | `bps_silver_c792846f` |
| `p_gold_lakehouse_name` | `bps_gold_c792846f` |
| `CDSViewNames` | `ZI_BPS_CHANNEL,ZI_BPS_CHANNELTEXT,ZC_BPS_CHANNELITEM`, using only the actual new/affected objects |

Notice the exact top-level parameter casing: B2S uses `CdsViewNames`; full S2G declares `CDSViewNames`. Child pipelines declare `CdsViewNames`.

The standard order is dimensions, time-dependent dimensions/hierarchies, texts, then facts. This normally ensures texts can find master keys and facts can find Gold dimensions.

Already-loaded dependencies do not need to be on the allow-list just to be joined by a fact, but must exist and remain in extraction scope. New dependencies need their own successful loads.

### Avoid unintended side effects during isolated tests

The full pipeline also:

- Enumerates all SAP system rows; it does not expose a system-only selector.
- Executes the entire Gold SQL-view notebook after its system loop, even with a narrow CDS allow-list.
- Can run the currency notebook through the dimension pipeline's metadata gate, independently of the CDS allow-list.
- Uses hard-coded notebook target defaults for view creation/currency processing unless those calls are deliberately adapted.
- Runs balance aggregates if the selected fact list contains `I_OPERATIONALACCTGDOCITEM`.

Therefore, a narrow allow-list is not a guarantee of **zero side effects on other derived objects**. For a controlled test, invoke the relevant S2G child or notebook in an isolated environment, with explicit JSON/configuration and targets, and account for its own side effects. See [the interface catalog](08-workspace-object-catalog.md).

### Gold acceptance checks

| Object | Expected result |
|---|---|
| Standard dimension | Active rows plus one unknown row with `Key=-1`; unique business key/system mapping |
| TD dimension/hierarchy | Complete validity-row grain; shared entity keys only where intended |
| Text | Master `Key` populated for matching rows; correct language/ISO-language and uniqueness |
| Fact | Expected natural-key grain; correct `_key_*` columns; unresolved keys explained |

Do not use a raw Silver count equals raw Gold count as the only test: Gold can have an unknown row, physical deletes, or multiple translation/validity rows.

## 11. Step 10: backfill affected existing facts, if applicable

**Skip for a completely new fact that is successfully loading all its source history for the first time.**

If the new table is a dimension added to an **existing fact**, adding its cube relationship alone is not sufficient proof of completion.

The current [fact processor](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py) normally enriches only Silver rows newer than the Gold fact watermark. Its repair phase processes rows marked `_Reprocess` or containing null key columns already present in Gold. A newly configured key column may not yet exist in Gold, and otherwise valid historical rows may not qualify for repair.

Plan and execute an approved backfill that:

1. Loads and validates the new Gold dimension first.
2. Preserves its `Key` values and every pre-existing Gold dimension's key mapping.
3. Selects **all affected historical fact rows**, not just rows after the incremental watermark.
4. Reuses the same ordered join logic and source-system conditions.
5. Verifies a one-row-per-original-fact result and explains every unresolved key.
6. Updates or replaces the affected fact output through a controlled, recoverable procedure.
7. Preserves other systems and natural keys and establishes a correct continuation watermark.
8. Rebuilds or refreshes dependent aggregates/imported models as required.

There is **no generic `FullLoad` or `ResetWatermark` parameter** in the checked-in fact notebook. A full historical re-enrichment may require an approved notebook extension/backfill job or a carefully staged fact rebuild. That implementation must be designed and tested; this guide does not prescribe deleting production tables.

Do not force a reload by arbitrarily editing timestamps or deleting Gold dimensions. Regenerating surrogate keys can invalidate existing fact relationships and report results.

## 12. Step 11: expose the table through the Gold SQL endpoint

After the Delta load, wait for the SQL endpoint to recognize the expected table/schema and validate its queryability. The existing model reads SQL objects, not Delta paths directly.

### If the base table is enough

A loaded standard dimension or fact may be consumed directly under its canonical name. No extra SQL view is intrinsically required.

### If translated labels are needed

Add a presentation view using the pattern in the [Gold SQL view notebook](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py) and [view catalog](04-gold-sql-views.md):

1. Require both the master and text Gold tables, plus `SAPLANGUAGE`.
2. Select master keys and business-code fallback labels.
3. Combine keys with supported languages.
4. Join actual text by the intended key/language grain.
5. Use fallback values for missing/empty descriptions.
6. Pivot to the language columns required by the semantic model.
7. Verify uniqueness of the resulting dimension key.

Adding `TEXT` metadata loads a Gold text table but does **not** add a new `vt*` SQL cell automatically.

### If the table is time-dependent or hierarchical

Create a reporting projection with a deliberate uniqueness/as-of rule. The existing `vCOSTCENTER`/`vPROFITCENTER` pattern selects maximum validity end per key, which is not the same as “valid today.”

New hierarchy names do not automatically receive flattened hierarchy/text SQL views. Define the required hierarchy presentation; the existing templates are fixed to nine levels and need source-system/join-grain review before reuse.

### If an existing aggregate must expose the new dimension

If facts are summarized in a view such as `vGLACCOUNTLINEITEMRAWDATA_AGGR`, add the new key to both projection and grouping **only after deciding the new aggregate grain**. Then update the aggregate model table, relationships, and measures that should use it.

Otherwise a new detail-only dimension may not correctly slice measures evaluated from an unrelated summary table. Test detail and aggregate measure behavior separately.

### Deployment choice

The existing notebook is BPS-managed. Either use the supported BPS customization mechanism, or maintain a clearly owned extension notebook/SQL deployment step. Wire that extension after prerequisite Gold loads and before dependent model refresh.

Do not create a new custom notebook and assume it will run: it needs an explicit pipeline dependency and deployed item reference. Avoid adding metadata for a generated SQL view as if it were a replicated SAP source.

## 13. Step 12: add semantic model and report integration, if required

Skip this step if the agreed delivery is only engineering-layer availability.

The installed model is a **SQL-backed composite model**, not Direct Lake. It uses shared `Server`, `Database`, and `Schema_Name` expressions. See [model details](05-semantic-model-and-report.md).

### Semantic model

Using supported Power BI/Fabric modeling tooling:

1. Add the new SQL object using the existing shared connection expressions.
2. Select storage mode deliberately; existing dimensions are generally Dual, the GL detail is DirectQuery, and the GL aggregate is Import.
3. Add properly typed fields and hide technical keys where appropriate.
4. Relate a new dimension's unique `Key` to the fact's configured `_key_*` column.
5. For TD/text sources, ensure the selected reporting table really has a unique relationship-side key.
6. Choose cardinality and filter direction deliberately; do not copy all existing bidirectional relationships without checking ambiguity.
7. Add measures with the correct grain, currency, signs, and period semantics.
8. If an aggregate should support the new dimension, update its model table/relationship and relevant calculations too.
9. Add the table to the TMDL model references and relationships through the modeling tool's generated definitions; do not leave an unreferenced table file.
10. Refresh/process Import and Dual tables as needed and validate DirectQuery access.

An illustrative Power Query source expression is:

```powerquery
let
    Source = Sql.Database(Server, Database),
    Channel = Source{[Schema = Schema_Name, Item = "ZI_BPS_CHANNEL"]}[Data]
in
    Channel
```

This is only the navigation expression. It does not by itself define the model columns, storage mode, relationships, or refresh.

### Multilingual and report fields

The report uses calculated field/language selector tables. A new model column does not automatically appear in those selectors.

If the new dimension should participate:

1. Add the required translation-source fields.
2. Extend the relevant language-selection calculated table.
3. Extend the appropriate field-parameter table, with a unique label/order and valid field reference.
4. Add/update slicers, tables, matrices, drillthrough fields, and tooltips where intended.
5. Check slicer synchronization, saved selections, interactions, and bookmarks if introduced.
6. Confirm the visual actually uses the selector you edited.

There are already mismatched/stale selector/filter references in the checked-in report. Do not reproduce them as templates. The [report catalog](06-report-object-catalog.md) identifies exact existing bindings.

The engineering pipelines do not contain an explicit semantic-model refresh activity. Arrange refresh sequencing separately if the delivery requires automatically updated imported data.

## 14. Step 13: execute acceptance tests before production

Run these checks against the actual source/targets. Documentation validation cannot substitute for them.

| Test | Required evidence |
|---|---|
| Metadata dispatch | Exact CDS name resolves with intended type/system and `inScope=1`; duplicate metadata rows understood |
| Initial load | Source snapshot, Silver, and Gold reconcile at their respective grains |
| Key uniqueness | No unexplained duplicate natural keys; dimension keys have intended uniqueness/version behavior |
| Types and values | Dates, leading-zero identifiers, decimal precision, amounts, and language values match the contract |
| Insert | A new source key appears correctly downstream |
| Update | A changed row updates the intended record, without losing a CDF postimage or duplicating a fact |
| Delete | Source delete removes/marks the intended row through Silver and Gold; snapshot absence tested separately |
| No-change rerun | No duplicates, key churn, or unexplained amount changes |
| Empty source | Explicit expected behavior; current snapshot code does not automatically clear every target |
| Referential integrity | Key `-1`/null counts are explained; joins do not multiply fact rows |
| Historical coverage | Old as well as new facts receive the new relationship when required |
| Multi-system isolation | Another system's rows, timestamps, keys, balances, and rates remain intact |
| Presentation | Required SQL objects exist; each view's prerequisite/creation result is checked |
| Model/report | Relationships, currency/period totals, field selectors, labels, and filters work as intended |
| Logging | Per-table logs and notebook exit values checked, not just pipeline status |
| Performance | Runtime, row counts, join expansion, source scan volume, and capacity impact are acceptable |

### Example read-only Gold checks

Run against the **Gold SQL endpoint**, once the table is visible:

```sql
DECLARE @SystemName nvarchar(50) = N'<EXISTING_SYSTEM_NAME>';

SELECT CHANNEL, _SystemName, COUNT_BIG(*) AS RowCount
FROM dbo.ZI_BPS_CHANNEL
WHERE [Key] <> -1
  AND _SystemName = @SystemName
GROUP BY CHANNEL, _SystemName
HAVING COUNT_BIG(*) > 1;

SELECT [Key], COUNT_BIG(*) AS RowCount
FROM dbo.ZI_BPS_CHANNEL
GROUP BY [Key]
HAVING COUNT_BIG(*) > 1;

SELECT
    _SystemName,
    COUNT_BIG(*) AS RowCount,
    MIN(_UpdateTimeStamp) AS MinTimestamp,
    MAX(_UpdateTimeStamp) AS MaxTimestamp
FROM dbo.ZI_BPS_CHANNEL
GROUP BY _SystemName;
```

For the illustrative fact, verify its new relationship:

```sql
DECLARE @SystemName nvarchar(50) = N'<EXISTING_SYSTEM_NAME>';

SELECT _SystemName, COUNT_BIG(*) AS UnresolvedOrMissingDimensionRows
FROM dbo.ZC_BPS_CHANNELITEM
WHERE _SystemName = @SystemName
  AND (_key_ZIBPSCHANNEL = -1 OR _key_ZIBPSCHANNEL IS NULL)
GROUP BY _SystemName;
```

These queries expect the illustrative columns to exist. For TD/text tables, adapt the uniqueness checks to their actual full row grain rather than declaring every repeated shared master key an error.

### Existing limitations relevant to onboarding

See [Operations](07-operations-and-caveats.md) for the full evidence. In particular:

- S2G delta watermarks are not consistently system-isolated.
- B2S fact CDF latest-row selection occurs before preimage removal.
- Delta text merges do not include language in the merge predicate.
- Delta row-count checking does not consistently account for tombstones.
- Several notebooks return error strings without failing the activity.
- New balance/rate behavior is not automatically generalized to arbitrary new table names.

If your table depends on one of these paths working differently, the necessary change is **an implementation fix plus tests**, not another metadata flag.

## 15. Step 14: promote, monitor, and make the configuration reproducible

After successful tests:

1. Deploy any required publisher changes, custom processing/view logic, model changes, and report changes through the approved path.
2. Apply reviewed metadata changes to the correct environment; verify system-specific values rather than copying test targets blindly.
3. Run B2S to completion before S2G. The existing 10:00/13:00 schedules do not enforce this dependency.
4. Complete any approved historical fact backfill.
5. Refresh dependent imported/dual model data and verify report totals.
6. Restore/enable scheduled triggers intentionally.
7. Monitor the first scheduled runs for row counts, watermarks, unresolved keys, log errors, and performance.
8. Record ownership, expected grain, source naming, dependencies, and operational checks in the solution documentation.

**Git persistence matters:** the repository contains metadata SQL **schemas**, not the active metadata rows. Editing a DDL file does not register a table in the running solution, and a live SQL INSERT alone does not provide reproducible configuration deployment.

Keep reviewed, environment-aware configuration migration scripts in the project's approved deployment mechanism; do not embed credentials or personal data. Include rollback/reconciliation behavior and environment mapping. This guide adds no deployment script or source configuration automatically.

Normal metadata-only onboarding does not require changes to the Environment, its wheel, lakehouse shortcut lists, pipeline schedules, log collector, SQL checkpoint schemas, or stored procedures. Change those only when the new source's concrete requirements demand it.

## 16. Rollback and recovery

If onboarding fails:

1. Prevent the relevant scheduled/manual jobs from racing with recovery.
2. Disable the **new table membership**, not the entire shared dataset or system.
3. Check all dataset memberships: another enabled membership can still keep the object in scope.
4. If a new dimension is already referenced by active facts, coordinate disabling/restoring those cube relationships. Disabled dimensions can be omitted from relationship lookup; do not continue producing partially configured facts unknowingly.
5. Restore only the metadata/model/view changes introduced by this delivery from their recorded prior values.
6. If a backfill modified existing facts or aggregates, use the tested data-restoration/rebuild procedure; disabling scope does not undo written data.
7. Retain the logs and failure evidence.
8. Do not drop shared dimensions, reset global watermarks, or delete entire lakehouses as a generic rollback.

Disabling extraction does not delete Silver/Gold data or remove SQL views/model tables. Likewise, leaving old tables in place is not proof that the pipeline is still maintaining them.

## 17. Completion checklist

- [ ] Source object, actual mirror name/schema, and DD03ND rows verified.
- [ ] Grain, keys, type, and delete/delta contract approved.
- [ ] Supported existing system reused; unintended connection duplication excluded.
- [ ] `viewMetadata`, dataset enable state, and table scope reviewed.
- [ ] Text master registered and loaded, if applicable.
- [ ] Fact relationship configuration and ordering reviewed, if applicable.
- [ ] Restricted B2S and dependency-ordered S2G runs validated.
- [ ] Historical existing-fact coverage completed, if applicable.
- [ ] SQL presentation views deployed and individually verified, if required.
- [ ] Semantic model relationships/measures and report selectors/visuals updated, if required.
- [ ] Initial/update/delete/no-change/multi-system tests passed.
- [ ] Refresh sequencing, monitoring, recovery, and reproducible configuration delivery established.

**Definition of done:** the additional table is available at the agreed layer, maintains the correct grain and keys over repeated runs, and its intended downstream consumers work. A green pipeline activity or one inserted metadata row is not sufficient.
