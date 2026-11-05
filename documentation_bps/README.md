# Business Process Solution: repository analysis

## 1. Overview

This repository is a Git-synced Microsoft Fabric workspace containing a **metadata-driven SAP data engineering framework and a Record-to-Report financial analytics application**. The engineering framework is broader than the one installed report: it contains reusable processing for finance, sales, procurement, and production-related SAP objects.

The solution turns replicated SAP CDS/ODP data into standardized Delta tables, assigns dimension surrogate keys, enriches facts with those keys, exposes SQL reporting views, and presents financial analysis through a Power BI semantic model and report.

Its central design principle is **configuration rather than a separate notebook per SAP table**. Database metadata selects the tables to process, their keys, extraction mode, dimension relationships, and processing order. Generic notebooks interpret that metadata.

### Reading order

| Document | What it explains |
|---|---|
| [Architecture and orchestration](01-architecture-and-orchestration.md) | Storage layers, execution sequence, every pipeline, schedules, runtime environment, and dependency boundaries |
| [Metadata database](02-metadata-database.md) | All 14 tables, the extraction-routing view, seven stored procedures, and configuration contracts |
| [Notebook transformations](03-notebook-transformations.md) | All 15 notebooks, incremental processing, keys, currencies, balance calculations, and logging |
| [Gold SQL views](04-gold-sql-views.md) | All 80 view definitions, multilingual labels, hierarchies, latest-version dimensions, and SQL aggregates |
| [Semantic model and report](05-semantic-model-and-report.md) | Model sources, tables, relationships, DAX, and the financial reporting experience |
| [Report object catalog](06-report-object-catalog.md) | Page-by-page and visual-by-visual report inventory |
| [Operations and caveats](07-operations-and-caveats.md) | Operating sequence, prerequisites, failure semantics, and important implementation limitations |
| [Workspace object catalog](08-workspace-object-catalog.md) | Complete Fabric item inventory, IDs, notebook parameters, and pipeline activity bindings |
| [Adding a table: step-by-step guide](09-adding-a-table.md) | Required source/metadata changes, table-type branches, test runs, historical backfills, reporting integration, and rollback |

## 2. End-to-end flow

```text
SAP / external replication publisher
                 |
                 v
Generic mirrored database (bronze-equivalent landing layer)
  SAP tables + DD03ND schema metadata; Delta change data feed enabled
                 |
     B2S orchestration at 10:00 UTC
                 |
                 v
Silver lakehouse: normalized SAP-shaped Delta tables
  uppercase business columns, SAP types, source-system identity,
  update timestamp, logical delete markers
                 |
     S2G orchestration at 13:00 UTC
                 |
     +-----------+----------------------+
     |                                  |
     v                                  v
Gold dimensions/texts             Gold enriched facts
stable Key, unknown -1            dimension _key_* foreign keys
     |                                  |
     +----------------+-----------------+
                      |
          +-----------+------------------+
          |                              |
          v                              v
SQL views and hierarchies       Customer/supplier balance facts
          |
          v
Power BI financial semantic model and report

Side channel: notebook Delta logs in Silver Files/Logs
              -> collector pipeline -> metadata database dbo.log_events

Control plane: metadata SQL database drives B2S and S2G selection/joins
```

The diagram shows the intended architectural relationship. **The checked-in definitions do not prove a fully connected, runnable chain to the report.** Live source availability, semantic model refresh, and report bindings still require validation, and the two daily engineering pipelines are independently scheduled rather than connected by a dependency.

## 3. What each layer contributes

1. **Mirrored source:** supplies SAP objects already replicated to OneLake. This repository does not implement the upstream SAP publisher.
2. **Silver:** standardizes names and data types while preserving SAP business keys. Dimensions are refreshed from snapshots; facts use change feed after their first load.
3. **Gold:** gives dimensions integer keys, attaches those keys to fact rows, handles deletions, and prepares reusable analytics structures. Time-dependent dimensions retain validity records but share an entity-level key.
4. **SQL presentation:** produces multilingual pivoted text views, flattened nine-level hierarchies, current-version dimension projections, and transaction aggregates.
5. **Semantic layer:** a composite financial model with **67 tables, 1,224 columns, 106 measures, and 63 relationships**. There are 24 SQL-backed tables, 36 calculated tables, and seven measure containers. Storage modes are one DirectQuery, 22 Dual, and 44 Import partitions; these include parameter/helper/measure tables, not only business data.
6. **Report:** **six pages and 173 visual containers** covering Trial Balance, YTD Trial Balance, YTD Financial Statement, Accounting Documents, Line Item Details, and Profitability. See the dedicated model/report documents for business calculations and visual behavior.
7. **Metadata and logging:** control processing scope and relationships and make notebook messages available in SQL.

## 4. Object coverage

There are **30 top-level Fabric items**:

| Item type | Count | Responsibility |
|---|---:|---|
| Environment | 1 | Spark configuration and packaged common Python library |
| Lakehouse | 3 | Silver, Gold, and an unreferenced sample lakehouse |
| Mirrored database | 1 | Generic Delta landing layer |
| SQL database | 1 | Configuration, checkpoints, and operational logs |
| Data pipeline | 7 | Three B2S, three S2G, and one log collection pipeline |
| Notebook | 15 | Two B2S, six dimension/text S2G, one fact S2G, one currency, two balance, one SQL-view, and two identical log collectors |
| Semantic model | 1 | Financial reporting model |
| Report | 1 | Financial Insights report |

The analysis also covers the **22 SQL database objects**, **80 SQL views embedded in the view-creation notebook**, the Python modules inside the bundled wheel, and the semantic/report subobjects cataloged in the dedicated documents. The root repository README is only a repository-name heading, not existing solution documentation.

## 5. Evidence and limits

**Analysis date:** 2026-11-05. This documentation describes the checked-in snapshot, not an independently inspected live tenant.

- **Verified:** item definitions, code branches, pipeline expressions and dependencies, schedule configuration, SQL schemas, packaged helper implementation, model definitions, and report definitions.
- **Not present:** SAP publisher implementation, mirrored business data, lakehouse table contents, metadata table rows, connection authentication configuration, run history, Spark outputs, and live report results.
- **Inferred:** business intent where names and calculations make it clear; an inference is not proof that a feature is populated or enabled.
- **Not executed:** SAP/Fabric pipelines, Spark notebooks, SQL deployments, and semantic model refreshes. They require a configured Fabric workspace and data.

This distinction matters particularly for `viewMetadata`, `cubeMetadata`, and extraction scope: their **schemas** are in Git, but their **rows** determine the actual installed SAP extraction scope. A view definition for a business area does not establish that its source tables are onboarded.

## 6. Main conclusions

- The solution is an extensible SAP analytics framework, with a specific financial reporting application installed on top.
- The architecture is source-system-aware through `_SystemName`, but some watermarks, SQL joins, and overwrite paths are not isolated per system. Multi-system correctness must not be assumed.
- “Delta” in metadata routes S2G behavior; B2S non-fact ingestion still reads full mirrored snapshots.
- Time-dependent keys are shared across validity versions, so current-version SQL views are important for a unique reporting dimension.
- The runtime library is available for inspection inside the checked-in wheel; key handling and validation are not opaque dependencies.
- Notebook completion does not consistently imply successful processing: several paths return error text or print failures without raising.
- The model explicitly binds business-facing logical names to 24 SQL objects through `Server`, `Database`, and `Schema_Name` expressions; defaults name the installed Gold database and `dbo`. Logical names differing from physical names are normal, not inherently missing wiring.
- All 14 SQL view sources requested by that model have exact matching definitions in the Gold notebook. Availability of the other ten `I_*` table sources depends on the live metadata-driven loads.
- The reporting definitions also contain stale language filter references and mismatched field selectors; these are cataloged separately from live connectivity questions.

For concrete source evidence and the operational implications, continue with [Architecture](01-architecture-and-orchestration.md) and [Operations](07-operations-and-caveats.md).
