# Financial insights: semantic model and report

## 1. Overview and scope

`Record_to_Report_Financial_Insights.SemanticModel` and `Record_to_Report_Financial_Insights.Report` are **two separate synced Fabric items** with the same display name. The semantic model exposes SAP-style general-ledger detail, an imported summary, financial-statement hierarchy, multilingual descriptions and DAX calculations. The Power BI report presents six pages, from trial balance to document drillthrough and profitability.

The report explicitly binds to its sibling semantic-model directory through [definition.pbir](../Record_to_Report_Financial_Insights.Report/definition.pbir). The model does **not** use Direct Lake: it is a SQL-backed composite model combining DirectQuery, Dual and Import partitions.

This chapter is an interpretation of the checked-in definitions, not a live-service inspection. Only these two artifact directories were examined. Other workspace items, source-view implementations, permissions, credentials, data contents and deployed refresh schedules were not read or tested here. Identifying connection endpoint values are deliberately not reproduced.

The [exhaustive object catalog](06-report-object-catalog.md) supplies:

- Every table and all 1,224 column definitions, including hidden and calculated columns.
- All 106 measures and their complete DAX; every partition and its M or DAX source.
- Every relationship, endpoint, cardinality, active/default state and filter direction.
- Every page definition and all 173 visual-container definitions, with labels, bindings, saved selections, filters, synchronization, expansion, actions and positions.
- Links accounting for all remaining files, including culture, theme and image resources.

### Verified static inventory

| Area | Count / classification |
|---|---|
| Synced Fabric items in scope | 1 semantic model; 1 report |
| Source files | 74 model files; 186 report files; **260 total** |
| Model tables / partitions | **67 / 67**, exactly one partition per table |
| Storage modes | **1 DirectQuery**, **22 Dual**, **44 Import** |
| Partition source types | **31 M**, **36 calculated** |
| SQL-backed tables | **24**; all use `Sql.Database(Server, Database)` and `Schema_Name` |
| Calculated tables | **36**: 26 currency/field selectors, 9 multilingual selectors, 1 fiscal-period helper |
| Measure-container tables | **7**, backed by empty local M tables |
| Columns | **1,224**, including **177 hidden** and **10 calculated** |
| Measures | **106**: 102 financial/hierarchy amount measures, 2 fiscal-selection measures, 2 hierarchy-visibility measures |
| Relationships | **63 active by default**; 38 bidirectional and 25 default single-direction |
| Relationship cardinalities | 37 one-to-one; 26 default many-to-one |
| Hidden tables / local-date tables | **0 / 0** |
| Declared tabular hierarchy objects | **0**; the statement matrix instead projects nine hierarchy-level columns |
| Defined roles / perspectives | **0 / 0** in these synced definitions |
| Report pages | **6**, all 1280 × 900 |
| Visual containers | **173**, comprising 167 visuals and 6 groups |
| Report bookmarks | No bookmark definitions or bookmark actions are present |

No RLS definition in the checkout is **not** evidence that the workspace or SQL source is publicly accessible. Fabric item permissions, SQL permissions and live effective identity are outside this evidence.

## 2. Source dependencies and model configuration

### 2.1 SQL connection contract

[expressions.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/expressions.tmdl) defines five shared expressions:

| Expression | Definition and role |
|---|---|
| `Server` | Required Text parameter; configured to a Fabric SQL endpoint. Endpoint value omitted here. |
| `Database` | Required Text parameter; checked-in default `bps_gold_c792846f`. A configured default is not proof of a currently reachable database. |
| `Schema_Name` | Required Text parameter, default `dbo`. Every SQL navigation step uses this parameter. |
| `Report Language` | Optional Text parameter, default `EN`, allowed values `EN`, `DE`, `ES`, `FR`. No table partition references it; it does not drive the report's language slicer. |
| `_AMOUNTS1` | Empty local M table expression built from compressed rows, then dropping its only column. It is not a referenced model table and is distinct from historical `_AMOUNTS` query-reference strings in some visuals. |

The 24 SQL partitions navigate by **exact SQL object name**. Their M variable names sometimes retain an old `dmgold_` or `vw` prefix; these variable names are not the object requested from SQL.

| Semantic table | SQL object under `Schema_Name` | Mode |
|---|---|---|
| `GLACCOUNTLINEITEMRAWDATA` | `I_GLACCOUNTLINEITEMRAWDATA` | DirectQuery |
| `AGGR_H` | `vGLACCOUNTLINEITEMRAWDATA_AGGR` | Import |
| `CHARTOFACCOUNTS` | `I_CHARTOFACCOUNTS` | Dual |
| `COMPANYCODE` | `I_COMPANYCODE` | Dual |
| `COSTCENTER` | `vCOSTCENTER` | Dual |
| `CUSTOMER` | `I_CUSTOMER` | Dual |
| `DEBITCREDITCODE` | `I_DEBITCREDITCODE` | Dual |
| `FISCALPERIODFORVARIANT` | `I_FISCALPERIODFORVARIANT` | Dual |
| `GLACCOUNTHIERARCHYWTEXT` | `vGLACCOUNTHIERARCHYWTEXT` | Dual |
| `GLACCOUNTINCHARTOFACCOUNTS` | `I_GLACCOUNTINCHARTOFACCOUNTS` | Dual |
| `LEDGER` | `I_LEDGER` | Dual |
| `PRODUCT` | `I_PRODUCT` | Dual |
| `PROFITCENTER` | `vPROFITCENTER` | Dual |
| `SAPLANGUAGE` | `SAPLANGUAGE` | Dual |
| `SEGMENT` | `I_SEGMENT` | Dual |
| `CHARTOFACCOUNTSTEXT` | `vtCHARTOFACCOUNTSTEXT` | Dual |
| `COSTCENTERTEXT` | `vtCOSTCENTERTEXT` | Dual |
| `DEBITCREDITCODETEXT` | `vtDEBITCREDITCODETEXT` | Dual |
| `GLACCOUNTINCHARTOFACCOUNTSTEXT` | `vtGLACCOUNTINCHARTOFACCOUNTSTEXT` | Dual |
| `LEDGERTEXT` | `vtLEDGERTEXT` | Dual |
| `PRODUCTGROUP2TEXT` | **`vtPRODUCTGROUP_2TEXT`** | Dual |
| `PRODUCTTEXT` | `vtPRODUCTTEXT` | Dual |
| `PROFITCENTERTEXT` | `vtPROFITCENTERTEXT` | Dual |
| `SEGMENTTEXT` | `vtSEGMENTTEXT` | Dual |

Each row links to its full source definition through the [catalog's model-table inventory](06-report-object-catalog.md#model-table-inventory).

**Cross-artifact integration note:** the overall workspace analysis supplied to this task reports 80 gold SQL views, including 64 multilingual `vt*` views, `SAPLANGUAGE`, `vCOSTCENTER`, `vPROFITCENTER`, `vGLACCOUNTHIERARCHYWTEXT` and `vGLACCOUNTLINEITEMRAWDATA_AGGR`. That supplied evidence explicitly accounts for the latter **five exact names**. This scoped analysis does not independently establish the nine individual `vt*` names against those 64 definitions; the gold-view chapter must close that exact-name crosswalk, particularly `vtPRODUCTGROUP_2TEXT`. The **ten `I_*` sources are not names of those reported generated views**: they require separately materialized or otherwise supplied SQL objects. Do not silently substitute a `v*` view for an `I_*` source or assume that a view-generation step creates the base `I_*` objects.

### 2.2 M transformations

The complete M is in each table's catalog excerpt. Beyond SQL navigation:

- `CHARTOFACCOUNTS` explicitly retains its business fields, `Key`, `_UpdateTimeStamp` and `_SystemName`.
- `COSTCENTER` and `PROFITCENTER` select explicit retained column lists, including their validity dates; latest-validity logic, if any, belongs to their SQL views rather than these partitions.
- `COSTCENTERTEXT`, `PROFITCENTERTEXT`, `PRODUCTGROUP2TEXT` and `PRODUCTTEXT` remove unwanted language columns. `PRODUCTTEXT` also removes `Key`; there is consequently no declared relationship linking that text table to `PRODUCT`.
- `SAPLANGUAGE` explicitly filters `_ISOLanguage` to `DE`, `EN`, `ES`, `FR`.
- The other SQL partitions return their selected SQL object without further explicit `Table.*` transformation.
- Seven measure-only tables use a compressed empty local table and remove `Column1`; their Import modes do not represent seven extra remote datasets.

The remove-column steps are authored without an explicit missing-field ignore option. **Inference:** an upstream schema change that removes one of those listed columns can break partition evaluation; no such failure was observed live.

### 2.3 Metadata and settings

- [database.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/database.tmdl): compatibility level **1600**.
- [model.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/model.tmdl): model `Model`, culture `en-US`, source-query culture `en-IN`, `powerBI_V3`, `legacyRedirects` and `returnErrorValuesAsNull`.
- `__PBI_TimeIntelligenceEnabled = 0`: automatic time-intelligence generation is disabled; no hidden local-date/date-template tables are present.
- Model query order is an annotation, not an orchestration graph or a refresh schedule. The recorded service save-version timestamp is metadata, not evidence of a recent successful refresh.
- [definition.pbism](../Record_to_Report_Financial_Insights.SemanticModel/definition.pbism): version **4.2**, `qnaEnabled: true`.
- [en-US.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/cultures/en-US.tmdl): JSON linguistic metadata, language `en-US`, version `2.0.0`, **66 generated entity/property bindings** with suggested terms from visual-column renaming. These are Q&A/linguistic synonyms, not additional data tables or translated report pages.
- No roles, perspectives, explicit refresh policies or incremental-refresh partition definitions are supplied.

## 3. Table design, columns and relationships

### 3.1 Financial detail versus imported summary

[GLACCOUNTLINEITEMRAWDATA](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTLINEITEMRAWDATA.tmdl) has **428 columns**, including 32 hidden columns. It exposes accounting-document identifiers, line-item information, fiscal attributes, dates, organizational and product/customer attributes, currency amounts, quantities, tax and other posting data. Hidden surrogate keys relate it to dimensions. It is a DirectQuery source, not a checked-in extract.

[AGGR_H](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/AGGR_H.tmdl) has **23 columns**, including 12 hidden keys. Its visible columns are company-code/global/transaction currency codes and amounts, fiscal year/period, partner company code, tax code and tax country. It relates to the shared dimensions using its key columns.

The summary table has `alternateSourcePrecedence: 10` and **five `alternateOf` base-column mappings**: the three currency-code columns, `FISCALYEAR` and `FISCALPERIOD`. There are **no `aggregationFunction` sum mappings on its three amount columns**. The report's summary pages explicitly reference aggregate measures, so their use of `AGGR_H` is a fact; transparent redirection of arbitrary detail measures to that Import summary is **not established** by the available metadata.

**Operational inference:** the detail and imported summary can represent different freshness points. The report can combine imported/Dual state and DirectQuery requests; synchronized consistency requires upstream completion and semantic-model refresh coordination, neither of which is proven here.

### 3.2 Dimensions and descriptions

- Core dimensions: `CHARTOFACCOUNTS` (5 columns), `COMPANYCODE` (25), `COSTCENTER` (13), `CUSTOMER` (116), `DEBITCREDITCODE` (4), `FISCALPERIODFORVARIANT` (14), `GLACCOUNTINCHARTOFACCOUNTS` (25), `LEDGER` (12), `PRODUCT` (152), `PROFITCENTER` (9), `SEGMENT` (4), and `SAPLANGUAGE` (5).
- `GLACCOUNTHIERARCHYWTEXT` has 39 columns and two measures. It supplies hierarchy codes/version, nine level-code/text projections, leaf account key, language and maximum hierarchy depth.
- Nine multilingual text tables expose language-named columns. Several retain many more languages than the four exposed by the language-selector network. The complete language-column lists and SQL provider types are retained in the catalog.
- Source bookkeeping columns and surrogate keys are generally hidden; the catalog preserves each exact `isHidden`, `isKey`, `isAvailableInMdx`, `summarizeBy`, format and source-column property rather than treating all underscored columns as equivalent.
- Customer and product schemas are broad, but this documentation includes **schema metadata only**, not personal/contact values or data rows.

### 3.3 Calculated tables, columns and field parameters

All **36 calculated tables are Import**:

1. **26 `_FIELD_PARAM_*` tables** define field/measures with DAX tuple constructors, `NAMEOF`, display labels and numeric order.
   - Detail and aggregate currency selectors each offer company-code, global and transaction currency.
   - Opening/current/closing selectors exist for detail, aggregate, detail-hierarchy and aggregate-hierarchy measures.
   - Trial-balance row selectors offer account group, profit center, cost center, company code, partner company code, tax code and tax country.
   - The line-item selector offers profit center, segment, cost center, tax code and tax country.
   - Nine profitability selectors cover revenue, COGS, inventory change, OPEX, other expenses, gross profit, operating profit, taxes and net profit. **Only revenue has all three currency choices; the other eight have company-code and global choices only.**
2. **Nine `_…TEXT` selector tables** map the same business description to `DE`, `EN`, `ES`, `FR` columns in the corresponding text table. Each has a calculated `_ISOLanguage` using `MID` and `SEARCH` against its generated field-reference string.
3. [`_FISCALPERIODTABLE`](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FISCALPERIODTABLE.tmdl) uses `GENERATESERIES(0, 16, 1)`. It has no declared relationships and no report field binding; the report instead uses `FISCALPERIODFORVARIANT`.

The tenth calculated column is `DEBITCREDITCODETEXT.SortOrder = IF(DEBITCREDITCODETEXT[Key] = 1, 2, 1)`. Every other calculated column is one of the nine selector-language extractions. No other calculated columns or hidden local-date tables were found.

Field-selector columns carry grouping, ordering and `ParameterMetadata` so Power BI can replace fields dynamically. The report definitions retain both the currently expanded projection and its field-parameter expression; a currently expanded company-code field is not, by itself, proof that currency switching is absent.

### 3.4 Relationship topology and filter propagation

The [63-row relationship catalog](06-report-object-catalog.md#relationships-complete-endpoint-and-direction-inventory) is the authoritative exhaustive matrix. Source: [relationships.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl).

- **25 default single-direction many-to-one** relationships connect facts/hierarchy language to dimensions. The one-side dimension filters the many-side table.
- **37 explicit bidirectional one-to-one** relationships coordinate selectors by order, language selectors with `SAPLANGUAGE`, and certain business/text table pairs by `Key`.
- **One bidirectional many-to-one** relationship connects `GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_NODE_KEY` to `GLACCOUNTINCHARTOFACCOUNTS.Key`. Thus hierarchy selections can filter accounts and then fact amounts, with reverse propagation possible on that edge.
- No relationship sets `isActive: false`; all 63 use the active default.
- Aggregate segment/debit-credit keys connect directly to `SEGMENTTEXT` and `DEBITCREDITCODETEXT`, while detail connects to `SEGMENT` and `DEBITCREDITCODE`; their one-to-one text links bridge these paths.
- `SAPLANGUAGE` filters hierarchy language. Nine bidirectional one-to-one selector relationships coordinate the text-column choices.
- Detail and aggregate currency-selector networks are separate. Most selector relationships join the numeric order columns so that 0/1/2 selects the same currency family across balance measures.
- `PRODUCTTEXT`, `_PRODUCTTEXT` and their language selector are present, but no `PRODUCT`–`PRODUCTTEXT` data relationship is declared. Treat a product-description filter path as unimplemented unless verified elsewhere.

**Inference, not an observed failure:** the bidirectional network makes effective filter propagation less obvious than a simple star schema. One-to-one text/key uniqueness, hierarchy-key multiplicity and selector-domain compatibility require live-data verification.

## 4. DAX behavior

The catalog contains **the full expression and formatting for every measure**, not merely representative formulas.

| Measure-bearing table | Measures | Function |
|---|---:|---|
| `__MEASURES_OTHER` | 9 | Detail opening/current/closing, three currencies |
| `_MEASURES_AGGR_H` | 9 | Same balance families over `AGGR_H` |
| `__MEASURES_GLACCOUNTHIERARCHY` | 12 | Detail hierarchy amount and opening/current/closing, three currencies |
| `__MEASURES_AGGR_HRCHY` | 12 | Aggregate hierarchy equivalents |
| `__MEASURES_PROFITABILITY` | 30 | Financial KPIs over detail |
| `__MEASURES_AGGR_PROFITABILITY` | 30 | Nominal aggregate KPI family, with dependency defects described below |
| `_MEASURES_GENERAL` | 2 | `SELECTEDFISCALPERIOD`, `SELECTEDFISCALYEAR` |
| `GLACCOUNTHIERARCHYWTEXT` | 2 | `_CurrentLevel`, `_Show` |

### 4.1 Fiscal selections and balances

[`_MEASURES_GENERAL`](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_MEASURES_GENERAL.tmdl) uses `SELECTEDVALUE` on fiscal period/year, without an alternate value. A multi-selection or unfiltered multi-valued context therefore returns BLANK, not an automatic latest period/year.

For [detail balances](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_OTHER.tmdl) and [aggregate balances](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_MEASURES_AGGR_H.tmdl):

- Closing balance sums the appropriate amount with `REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD])`, then `FISCALPERIOD <= selected`.
- Opening balance uses the same logic with `< selected`.
- Current-period measures constrain the fact table's fiscal-period column to the selected period.
- These are fiscal-period calculations, **not `TOTALYTD`/calendar-date time intelligence**. Fiscal-year selection is retained through existing context rather than explicitly re-applied by the opening/closing DAX.
- Only the period-column filter is removed; other filters, including year and fiscal variant, remain effective.

The older [detail hierarchy balance family](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_GLACCOUNTHIERARCHY.tmdl) applies `FILTER(GLACCOUNTLINEITEMRAWDATA, …)` rather than clearing the fiscal-dimension period column. The [aggregate hierarchy family](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_AGGR_HRCHY.tmdl) clears the dimension period for opening/closing and filters `AGGR_H` for current period. **Inference:** the two implementations need not return identical cumulative results under an existing period slicer; no reconciliation query was run.

### 4.2 Hierarchy depth suppression

`_CurrentLevel` checks `ISINSCOPE` from level 9 down to level 1. `_Show` returns 1 when the current level is no deeper than `MIN(MAXHIERARCHYLEVEL)`, otherwise BLANK. Hierarchy amount measures multiply the relevant summed amount by `_Show`, suppressing rows beyond the account's supported hierarchy depth. Grand-total behavior depends on the BLANK/comparison context and was not rendered or tested.

### 4.3 Profitability classification and arithmetic

[Profitability DAX](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_PROFITABILITY.tmdl) classifies amounts using hierarchy codes, preserving filters with `KEEPFILTERS` and using `ABS(SUM(amount))`:

| KPI | Classification / arithmetic |
|---|---|
| Revenue | `LEVEL8 = "023"` |
| COGS | `LEVEL7` in `"024"`, `"027"`, `"029"`, `"030"` |
| Inventory change | `LEVEL6 = "021"` |
| Other expenses | `LEVEL5` in `"016"`, `"017"`, `"018"`, `"019"` |
| Taxes | `LEVEL3 = "011"` |
| Gross profit | Revenue − COGS |
| OPEX | Inventory change + other expenses |
| Operating profit | Gross profit − OPEX |
| Net profit | Operating profit − taxes |
| Gross profit margin | Company-code gross profit / company-code revenue, using `DIVIDE` |
| Operating profit margin | Company-code operating profit / company-code revenue, using `DIVIDE` |
| OPEX ratio | Company-code OPEX / company-code revenue, using `DIVIDE` |

Underlying amount families exist for company-code, global and transaction currencies. The ratios are company-code-only, not parameterized ratios. No exchange-rate conversion is performed by these measures; they choose among already supplied amount columns.

`ABS(SUM(...))` makes the total positive after summing, which is not the same as summing row-wise absolute values. Business acceptance of this sign policy and of the hard-coded account-hierarchy code mapping requires financial validation.

Except for company-code revenue, classification measures use the selected chart of accounts, hierarchy and language. **`COMPANYCODE_REVENUE` hard-codes chart `YCOA` and hierarchy `YPA1`**, while retaining existing selections through `KEEPFILTERS`; another selected chart/hierarchy can intersect to no rows.

### 4.4 Confirmed static calculation inconsistencies

In [`__MEASURES_AGGR_PROFITABILITY`](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_AGGR_PROFITABILITY.tmdl), **15 derived measures have `AGGR_` names but reference non-aggregate measures**:

- Company-code: gross profit, gross profit margin, OPEX, operating profit, net profit.
- Global: gross profit, OPEX, operating profit, net profit.
- Transaction: gross profit, OPEX, operating profit, net profit.
- Aggregate operating-profit margin and OPEX ratio.

For example, `AGGR_COMPANYCODE_GROSSPROFIT = [COMPANYCODE_REVENUE] - [COMPANYCODE_COGS]`, not the `AGGR_` counterparts. These are definite static naming/dependency inconsistencies and can force detail-table evaluation or mix semantics. They are **not a demonstrated wrong value on the current report**: the saved Profitability visuals use the non-aggregate family, and no live query was executed.

The company-code aggregate balance family also has inconsistent display precision: opening is `#,0`, closing is `#,0.00`, while other measures rely on general-number hints. This is a formatting discrepancy, not an arithmetic defect.

## 5. Report configuration and navigation

[report.json](../Record_to_Report_Financial_Insights.Report/definition/report.json) configures theme `CY23SU04`, top vertical alignment, expanded filter pane, stylable visual headers, enhanced tooltips, default aggregation display names and `defaultDrillFilterOtherVisuals: true`. Cross-highlighting is **not disabled**. Apply-selection buttons for slicers/filters/field wells and Apply All are disabled in the slow-source settings.

There are **no report-level filter predicates** in this definition. Only Accounting Documents and Line Item Details have page-level filter cards, both authored as drillthrough bindings. No custom per-page visual-interaction override lists, page-navigation buttons, web actions or bookmark definitions are present. Default interactions remain applicable; absence of overrides is not evidence that visuals do not interact.

[pages.json](../Record_to_Report_Financial_Insights.Report/definition/pages/pages.json) supplies the order below and opens on **Trial Balance**. No page definition declares itself hidden.

| Order | Page / ID | Display | Containers | Principal analytic content |
|---|---|---|---:|---|
| 1 | Trial Balance / `e9a0daa552c5be7f88d0` | FitToPage | 21 | 1 aggregate matrix, 10 slicers |
| 2 | YTD Trial Balance / `29205fb9a9b601d02447` | FitToWidth | 21 | 1 aggregate opening/current/closing matrix, 10 slicers |
| 3 | YTD Financial Statement / `bf28c024fb01861a71b5` | FitToPage | 20 | 1 aggregate hierarchy matrix, 10 slicers |
| 4 | Accounting Documents / `e6299790245906d72cee` | FitToWidth | 20 | 1 detail matrix, 9 slicers, Back action |
| 5 | Line Item Details / `8b1b618b6ff001ff0e26` | FitToWidth | 22 | 2 tables, 9 slicers, Back action |
| 6 | Profitability / `9d8153603d7adaea330a` | ActualSize | 69 | 9 KPI cards, 9 currency cards, 3 gauges, 1 column chart, 13 slicers |

Across all pages there are **61 slicers, 4 matrices (`pivotTable`), 2 tables (`tableEx`), 9 `cardVisual`, 9 `multiRowCard`, 3 gauges, 1 column chart, 2 action buttons, 33 shapes, 37 textboxes, 6 images and 6 visual groups**. Every one has its own source link and configuration in the catalog.

### 5.1 Common slicers and saved state

All six pages contain chart-of-accounts, company-code, fiscal-year, fiscal-period, ledger, language, profit-center and segment slicers. Five pages also expose a currency selector; Line Item Details exposes a row-field selector instead. Trial Balance and YTD Trial Balance additionally expose trial-balance field selection; the financial statement adds hierarchy/version; Profitability adds hierarchy/version, product group and two customer-bound selectors.

Saved selections consistently include company `1710`, chart `YCOA`, fiscal year **2016**, fiscal period **2**, English and `Ledger 0L`. These are template/authoring selections, not evidence that this is the current reporting period.

- Trial Balance and YTD Trial Balance save **transaction currency**.
- YTD Financial Statement, Accounting Documents and Profitability save **company-code currency**.
- Financial Statement and Profitability save hierarchy `YPA1`.
- The detail and aggregate currency selectors are not all in the same report sync group.
- Each page's fiscal-year slicer has an explicit `ComparisonKind: 1` condition against `2015L` (greater-than semantics).
- Profit-center and ledger slicers on every page exclude null **German (`DE`) descriptions**, despite current projections expanding to `EN`. This is a static language/filter mismatch; a value with English text but missing German text can be excluded.
- There are **94 visual filter-card entries**, of which **18 contain an explicit filter predicate**. The others are field/filter-card metadata, not 76 additional active restrictions. Saved slicer selections live separately inside visual `objects.general.filter`.

Report synchronization groups `CHARTOFACCOUNTS`, `COMPANYCODE`, `FISCALPERIOD`, `FISCALYEAR`, `LANGUAGENAME`, `Ledger`, `ProfitCenter` and `Segment` each occur on all six pages and synchronize both field and filter changes. `GLACCOUNTHIERARCHY` occurs on two pages. `FIELD_PARAM_CURRENCY` occurs on two; `CUSTOMERNAME`, `CUSTOMERNAME1`, `EN` and `FIELD_PARAM_TRIALBALANCE_FIELDS` occur once each. The complete membership and visual IDs are recorded in each visual's catalog JSON.

### 5.2 Page-by-page functional walkthrough

#### Trial Balance

[Page source](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/page.json).

The main [matrix](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/2c604992f5e3ae683475/visual.json) uses `AGGR_H` currency and debit/credit text as columns; GL account and multilingual account name as base rows; and selectable account group, profit/cost center, company, partner company, tax code and tax country as additional rows. Values come from `_FIELD_PARAM_AGGR_CURRENT_PERIOD`, expanded to `AGGR_TRANSACTION_CURRENT_PERIOD` in the saved state. Field parameters, not a hard-coded single measure, govern currency switching.

The visible page textbox says **Trial Balance**. The matrix has a saved title string **Accounting Documents**, but `show: false`; it is not a visible matrix title. Other containers are four shapes, four textboxes, one decorative image and one group, all individually documented.

#### YTD Trial Balance

[Page source](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/page.json).

The [matrix](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/99f33e48f5863153f6fb/visual.json) has the same selectable rows and currency/debit-credit columns as Trial Balance, with **Opening Balance**, **Current Period** and **Closing Balance** parameterized aggregate measures. The saved projections are the three transaction-currency measures. Page text says **YTD Trial Balance**; the inherited **Accounting Documents** matrix title is hidden. Decoration is four shapes, four textboxes, one image and one group.

#### YTD Financial Statement

[Page source](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/page.json).

The [matrix](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/e53fc44ec2db63eb3626/visual.json) projects `GLACCOUNT_HIER_LEVEL1_TEXT` through `GLACCOUNT_HIER_LEVEL9_TEXT` as nested rows and aggregate hierarchy opening/current/closing measures as values. Its saved currency projection is company-code currency. Currency and debit/credit descriptions form columns. The hierarchy slicer projects both hierarchy code and version. Expansion state is preserved in the visual JSON; no separate tabular hierarchy object is required.

Page text says **YTD Financial Statement**; the inherited matrix title is hidden. Other containers are four shapes, three textboxes, one image and one group.

#### Accounting Documents

[Page source](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/page.json).

This page is a **drillthrough target bound to `GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT`**. Its [matrix](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/9fee9327dd090d2828d0/visual.json) shows GL account, multilingual name and accounting document, with currency/debit-credit columns and parameterized detail current-period amounts. It is not the same query path as the imported trial-balance matrix.

The heading textbox is **Account Documents Report**. The [Back button](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/d117bc05fdeb97785435/visual.json) has an enabled `visualLink` action of type **Back**, not a hard-coded destination page. The GL-account drillthrough parameter is defined; broader context propagation beyond explicitly serialized fields must be verified in the client. Decoration comprises four shapes, three textboxes, one image and one group.

#### Line Item Details

[Page source](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/page.json).

This is a **drillthrough target bound to `GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT`**.

- The [document header table](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/3ce787753854bbc32dd9/visual.json) shows accounting document, document/posting/creation dates and document type.
- The [line-item table](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/cbddb9d84a7933e1c1f2/visual.json) shows ledger GL line item, posting key, debit/credit description, account/name, three currencies and their **implicit Sum amount projections**, Sum quantity, partner company, product, document item text and plant. A field parameter adds profit center, segment, cost center, tax code and tax country.
- Both tables explicitly show a title of **Accounting Documents**, even though the page heading is **Line Item Details**.
- The [Back button](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/89630faab3ff40b159d6/visual.json) uses the **Back** action.

The visible field-selection slicer binds to **`_FIELD_PARAM_TRIALBALANCE_FIELDS`**, whereas the detail table's optional fields use **`_FIELD_PARAM_LINE_ITEM_FIELDS`**. There is no relationship between those selectors. This is a confirmed authored binding mismatch: the apparent control is not bound to the parameter that owns those optional table fields.

Document number alone may not be globally unique across companies and years. **Inference:** drillthrough correctness depends on retained context and source keys; uniqueness or cross-company isolation has not been tested. Other containers are five shapes, three textboxes, one image and one group.

#### Profitability

[Page source](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/page.json).

Nine KPI cards show **Revenue**, **COGS**, **Gross Profit**, **Inventory Change**, **Other Expenses**, **OPEX**, **Operating Profit**, **Taxes** and **Net Profit** using detail profitability measures and field parameters. Their adjacent textboxes provide business labels; the catalog preserves both label text and title visibility.

Nine multi-row cards display the selected amount's currency field, expanded to `GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY` in the saved state. Three gauges show **Gross Profit Margin**, **Operating Profit Margin** and **OPEX Ratio**, all bound to the company-code ratio measures. They contain no bound minimum/maximum/target measure; `target.show: true` alone is not evidence of a defined target.

The column chart plots **Revenue by raw-data fiscal period**, again through the revenue field parameter. The synchronized fiscal-period slicer remains present; **inference:** its selection can restrict this chart's period range under default interactions. There is no custom interaction override proving that the chart escapes the period selection.

The **Product Group** slicer correctly uses the multilingual product-group selector. The **Customer** and the spatially labeled **Product** selector both bind to `CUSTOMER.CUSTOMERNAME`; the latter [visual](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/8a9a5fbd8952886eb0ee/visual.json) sits next to the [Product textbox](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/d647a0b100002a3b4540/visual.json), but is not a product-field slicer. That is a confirmed label/binding mismatch.

The page also contains 12 shapes, 20 textboxes, one image and one group. There are no separate bookmark-driven profitability modes.

### 5.3 Static resources

The [base theme](../Record_to_Report_Financial_Insights.Report/StaticResources/SharedResources/BaseThemes/CY23SU04.json) is named `CY23SU04`; it supplies color, text-class and 32 visual-style entries. Theme styling for a visual type, such as a bookmark navigator, does **not** imply that this report instantiates that type.

All six image visuals reference the same [registered PNG](../Record_to_Report_Financial_Insights.Report/StaticResources/RegisteredResources/Data_Bar_Vertical_Highlight26202892008048195.png), used as a decorative vertical highlight. It is a bundled static resource, not an external data source or navigation destination.

## 6. Important mismatches and verification boundaries

| Finding | Evidence classification | Consequence / next verification |
|---|---|---|
| Ten `I_*` sources plus nine exact `vt*`, four `v*` and `SAPLANGUAGE` are required | Confirmed source contract | Cross-check exact gold SQL object names and schema; model display names do not establish SQL view names. |
| Imported aggregate versus DirectQuery detail | Confirmed mixed storage | Reconcile freshness after upstream loads and model refresh. A successful view deployment alone does not refresh imported data. |
| 15 `AGGR_` profitability measures call non-aggregate measures | Confirmed static dependency inconsistency | Validate intended aggregate-only execution and reconcile financial results before relying on that family. |
| Company-code revenue hard-codes `YCOA`/`YPA1` while other currency variants use selected values | Confirmed formula inconsistency | Test alternate charts/hierarchies; incompatible selections can intersect to empty results. |
| Eight profitability selectors omit transaction currency | Confirmed metadata mismatch with three-value currency selector | Test the transaction choice on each KPI; blank/suppressed outputs are a risk, not an observed rendered result. |
| Ratios remain company-code-based while KPI amount fields can switch | Confirmed fixed ratio dependencies | Check whether ratio currency semantics are intended; do not infer ratios switch with the amount cards. |
| Line Item Details field slicer controls a different parameter table than the line-item table | Confirmed binding mismatch | Verify/repair intended row-field control separately from source-data issues. |
| “Product” control binds to customer name | Confirmed spatial label/binding mismatch | Test product filtering; the current authored selector does not filter a product column directly. |
| Eight filter-card bindings refer to absent `ISOLANGUAGE.LANGUAGECODE` | Confirmed stale metadata | Six Segment slicers and two hierarchy slicers carry orphan field cards. These cards have no serialized predicate; report-load/runtime impact is unverified. |
| English-visible ledger/profit-center controls filter German text for non-null | Confirmed language/filter mismatch | Test partially translated master data. |
| Aggregate amount columns lack explicit sum aggregation mappings | Confirmed mapping absence | Do not claim general automatic aggregate substitution; verify query plans if performance depends on it. |
| Hidden “Accounting Documents” matrix title strings, visible same titles on both detail tables, and repeated “Language” headers on currency/field slicers | Confirmed authored labeling discrepancies | Distinguish hidden title metadata from visible textboxes and actual rendered controls. |

Historical gauge `queryRef` strings such as `_AMOUNTS.OPEX_RATIO` are **not unresolved measure bindings**: their typed field expressions correctly name `__MEASURES_PROFITABILITY`. The catalog retains both, avoiding a false missing-table defect.

No live rendering, DAX execution, source query, credential check, RLS impersonation, refresh, deployment or performance benchmark was performed. Accordingly, the table above distinguishes definite checked-in discrepancies from hypotheses about their runtime impact.

## 7. Coverage and documentation validation

The catalog was constructed by enumerating every file under the two scoped item directories, parsing all report JSON, reading every TMDL table and all relationships, and preserving functional definitions rather than sampling only visible business tables.

Validation checks:

- Exactly 67 table sections and 67 partitions, 1,224 columns, 106 measures and 63 relationship rows are represented.
- All six ordered page definitions and all 173 on-disk visual-container JSON files have catalog entries; the six groups are counted separately from visuals.
- The remaining 13 files have explicit source links, giving coverage of all 260 files.
- Source-relative links and chapter-to-catalog links were checked against existing files; URL encoding is used where a path component requires it.
- **603 Markdown link occurrences** across these two chapters resolve to existing files; no scoped source file is unreferenced.
- All **183 report JSON files** parse successfully. Each visual's configuration is exactly preserved in the catalog after omitting only the separately documented schema/name/position fields.
- Every relationship endpoint resolves to a declared column. Direct visual field-expression checks found only the eight documented `ISOLANGUAGE.LANGUAGECODE` orphan bindings.
- Table excerpts omit only opaque lineage tags and PBI IDs, not DAX, partition sources, hidden flags, formats or filter/aggregation metadata.
- No existing model or report definition was changed.
