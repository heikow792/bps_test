# Semantic-model and report object catalog

This exhaustive static catalog complements [the overview and analysis](05-semantic-model-and-report.md). It covers only the two assigned Fabric items. Source links are relative to this document. No live query, refresh, rendering, access-control or deployment result is asserted.

## Reading the inventory

- Every TMDL table has an inventory row and a complete functional definition below: columns, hidden flags, formats, sort/group metadata, DAX, partition M/DAX, storage mode, hierarchy and aggregation mappings. Only opaque lineage tags and opaque PBI IDs are omitted from excerpts; source files remain authoritative.
- Every visual container has a section, including decorative shapes, images, text and groups. Labels are authored text, not guaranteed runtime text. Fields include query references as well as typed field expressions.
- Visual configuration is preserved as compact JSON, including queries, filters, saved selections, sync groups, expansion state, actions, formatting and parent-group metadata. Only `$schema` and the already-tabulated `name`/`position` are omitted. Absence of an explicit property is not evidence that the Power BI default is disabled.
- Literal filter values are saved authoring state, not a row-data extract. Position records x/y/z, width/height and keyboard tab order; coordinates are authored canvas units.

## Model table inventory

| Table | Columns (hidden / calculated) | Measures | Partition type / mode | SQL object |
|---|---:|---:|---|---|
| [__MEASURES_AGGR_HRCHY](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_AGGR_HRCHY.tmdl) | 0 (0 / 0) | 12 | m / import |  |
| [__MEASURES_AGGR_PROFITABILITY](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_AGGR_PROFITABILITY.tmdl) | 0 (0 / 0) | 30 | m / import |  |
| [__MEASURES_GLACCOUNTHIERARCHY](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_GLACCOUNTHIERARCHY.tmdl) | 0 (0 / 0) | 12 | m / import |  |
| [__MEASURES_OTHER](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_OTHER.tmdl) | 0 (0 / 0) | 9 | m / import |  |
| [__MEASURES_PROFITABILITY](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_PROFITABILITY.tmdl) | 0 (0 / 0) | 30 | m / import |  |
| [_CHARTOFACCOUNTSTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_CHARTOFACCOUNTSTEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [_COSTCENTERTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_COSTCENTERTEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [_DEBITCREDITCODETEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_DEBITCREDITCODETEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_CLOSING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_CLOSING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_CURRENCY](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_CURRENCY.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_CURRENT_PERIOD](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_CURRENT_PERIOD.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_OPENING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_OPENING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_CLOSING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_CLOSING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_COGS](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_COGS.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_CURRENCY](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_CURRENCY.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_CURRENT_PERIOD](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_CURRENT_PERIOD.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_GROSSPROFIT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GROSSPROFIT.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_INVENTORYCHANGE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_INVENTORYCHANGE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_LINE_ITEM_FIELDS](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_LINE_ITEM_FIELDS.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_NETPROFIT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_NETPROFIT.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_OPENING_BALANCE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OPENING_BALANCE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_OPERATINGPROFIT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OPERATINGPROFIT.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_OPEX](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OPEX.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_OTHEREXPENSES](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OTHEREXPENSES.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_REVENUE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_REVENUE.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_TAXES](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_TAXES.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FIELD_PARAM_TRIALBALANCE_FIELDS](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_TRIALBALANCE_FIELDS.tmdl) | 3 (2 / 0) | 0 | calculated / import |  |
| [_FISCALPERIODTABLE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FISCALPERIODTABLE.tmdl) | 1 (0 / 0) | 0 | calculated / import |  |
| [_GLACCOUNTINCHARTOFACCOUNTSTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_GLACCOUNTINCHARTOFACCOUNTSTEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [_LEDGERTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_LEDGERTEXT.tmdl) | 4 (2 / 1) | 0 | calculated / import |  |
| [_MEASURES_AGGR_H](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_MEASURES_AGGR_H.tmdl) | 0 (0 / 0) | 9 | m / import |  |
| [_MEASURES_GENERAL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_MEASURES_GENERAL.tmdl) | 0 (0 / 0) | 2 | m / import |  |
| [_PRODUCTGROUP2TEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_PRODUCTGROUP2TEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [_PRODUCTTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_PRODUCTTEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [_PROFITCENTERTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_PROFITCENTERTEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [_SEGMENTTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_SEGMENTTEXT.tmdl) | 4 (3 / 1) | 0 | calculated / import |  |
| [AGGR_H](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/AGGR_H.tmdl) | 23 (12 / 0) | 0 | m / import | vGLACCOUNTLINEITEMRAWDATA_AGGR |
| [CHARTOFACCOUNTS](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/CHARTOFACCOUNTS.tmdl) | 5 (3 / 0) | 0 | m / dual | I_CHARTOFACCOUNTS |
| [CHARTOFACCOUNTSTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/CHARTOFACCOUNTSTEXT.tmdl) | 41 (2 / 0) | 0 | m / dual | vtCHARTOFACCOUNTSTEXT |
| [COMPANYCODE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/COMPANYCODE.tmdl) | 25 (3 / 0) | 0 | m / dual | I_COMPANYCODE |
| [COSTCENTER](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/COSTCENTER.tmdl) | 13 (3 / 0) | 0 | m / dual | vCOSTCENTER |
| [COSTCENTERTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/COSTCENTERTEXT.tmdl) | 8 (2 / 0) | 0 | m / dual | vtCOSTCENTERTEXT |
| [CUSTOMER](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/CUSTOMER.tmdl) | 116 (3 / 0) | 0 | m / dual | I_CUSTOMER |
| [DEBITCREDITCODE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/DEBITCREDITCODE.tmdl) | 4 (3 / 0) | 0 | m / dual | I_DEBITCREDITCODE |
| [DEBITCREDITCODETEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/DEBITCREDITCODETEXT.tmdl) | 42 (2 / 1) | 0 | m / dual | vtDEBITCREDITCODETEXT |
| [FISCALPERIODFORVARIANT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/FISCALPERIODFORVARIANT.tmdl) | 14 (3 / 0) | 0 | m / dual | I_FISCALPERIODFORVARIANT |
| [GLACCOUNTHIERARCHYWTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTHIERARCHYWTEXT.tmdl) | 39 (3 / 0) | 2 | m / dual | vGLACCOUNTHIERARCHYWTEXT |
| [GLACCOUNTINCHARTOFACCOUNTS](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTINCHARTOFACCOUNTS.tmdl) | 25 (3 / 0) | 0 | m / dual | I_GLACCOUNTINCHARTOFACCOUNTS |
| [GLACCOUNTINCHARTOFACCOUNTSTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTINCHARTOFACCOUNTSTEXT.tmdl) | 41 (2 / 0) | 0 | m / dual | vtGLACCOUNTINCHARTOFACCOUNTSTEXT |
| [GLACCOUNTLINEITEMRAWDATA](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTLINEITEMRAWDATA.tmdl) | 428 (32 / 0) | 0 | m / directQuery | I_GLACCOUNTLINEITEMRAWDATA |
| [LEDGER](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/LEDGER.tmdl) | 12 (3 / 0) | 0 | m / dual | I_LEDGER |
| [LEDGERTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/LEDGERTEXT.tmdl) | 41 (2 / 0) | 0 | m / dual | vtLEDGERTEXT |
| [PRODUCT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PRODUCT.tmdl) | 152 (3 / 0) | 0 | m / dual | I_PRODUCT |
| [PRODUCTGROUP2TEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PRODUCTGROUP2TEXT.tmdl) | 7 (2 / 0) | 0 | m / dual | vtPRODUCTGROUP_2TEXT |
| [PRODUCTTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PRODUCTTEXT.tmdl) | 6 (1 / 0) | 0 | m / dual | vtPRODUCTTEXT |
| [PROFITCENTER](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PROFITCENTER.tmdl) | 9 (3 / 0) | 0 | m / dual | vPROFITCENTER |
| [PROFITCENTERTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PROFITCENTERTEXT.tmdl) | 8 (2 / 0) | 0 | m / dual | vtPROFITCENTERTEXT |
| [SAPLANGUAGE](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/SAPLANGUAGE.tmdl) | 5 (2 / 0) | 0 | m / dual | SAPLANGUAGE |
| [SEGMENT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/SEGMENT.tmdl) | 4 (3 / 0) | 0 | m / dual | I_SEGMENT |
| [SEGMENTTEXT](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/SEGMENTTEXT.tmdl) | 41 (2 / 0) | 0 | m / dual | vtSEGMENTTEXT |

## Relationships: complete endpoint and direction inventory

Omitted TMDL cardinalities use the tabular defaults: from=many and to=one. Omitted cross-filtering is oneDirection (the one/to side filters the many/from side); omitted isActive is true. Explicit bothDirections is bidirectional. These are metadata semantics, not an assertion of uniqueness in loaded data.

| Source relationship | From endpoint | To endpoint | From : to | Cross-filter | Active | Other properties |
|---|---|---|---|---|---|---|
| [306767f2-169b-4fcb-8837-be53efc7f233](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_ICHARTOFACCOUNTS | CHARTOFACCOUNTS.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [30b51c5e-7a83-4a0f-914d-8086fa7dd70a](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_IGLACCOUNTINCHARTOFACCOUNTS | GLACCOUNTINCHARTOFACCOUNTS.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [e2f4e1f6-c6fa-41a5-ac4e-ae393e88cd2d](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_ILEDGER | LEDGER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [24aba630-4c83-48f4-bb5a-22a23c0ada2f](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_OPENING_BALANCE.'FIELD_PARAM_OPENING_BALANCE Order' | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [da486f99-0f0f-40d6-b520-93b38ca3fd13](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_CURRENT_PERIOD.'FIELD_PARAM_CURRENT_PERIOD Order' | one : one (default) | bothDirections | true (default) |  |
| [83a931ae-547c-4fb9-bc61-8c3d107ec896](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_CLOSING_BALANCE.'FIELD_PARAM_CLOSING_BALANCE Order' | one : one (default) | bothDirections | true (default) |  |
| [0b7a891c-7638-41ed-bb8b-c4877dae3a92](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE.'FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE Order' | one : one (default) | bothDirections | true (default) |  |
| [48fef95e-aaf9-45a4-a8ba-84d44d6abec6](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD.'FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD Order' | one : one (default) | bothDirections | true (default) |  |
| [13011088-0362-4970-8457-238ca09c65b1](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE.'FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE Order' | one : one (default) | bothDirections | true (default) |  |
| [bd188e63-6ac1-4fa0-b9a1-1621f92d48d1](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_ICOMPANYCODE | COMPANYCODE.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [2428e9c2-14ff-452c-a914-7957bf90df64](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_ICOMPANYCODE | COMPANYCODE.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [84568371-39c3-45e4-93f2-8225048c9572](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_ICHARTOFACCOUNTS | CHARTOFACCOUNTS.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [025e65e8-e4eb-472d-8c76-54340bda4c70](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_ILEDGER | LEDGER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [0db6aa6d-9bca-40fd-909b-63456ed119d2](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_IGLACCOUNTINCHARTOFACCOUNTS | GLACCOUNTINCHARTOFACCOUNTS.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [a782e259-a2b0-4af7-8fbc-44c0933c52fd](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | CHARTOFACCOUNTSTEXT.Key | CHARTOFACCOUNTS.Key | one : one (default) | bothDirections | true (default) |  |
| [9d88e9bd-1837-44c1-be24-46256a3b70e4](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _CHARTOFACCOUNTSTEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [a8a95c6c-0025-4850-af8d-971a353d8b19](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _DEBITCREDITCODETEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [1d231f51-351b-47b0-8f2f-f661112f53de](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | LEDGERTEXT.Key | LEDGER.Key | one : one (default) | bothDirections | true (default) |  |
| [7c3cbff1-142b-4d8f-8655-6b46df890fa1](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | SAPLANGUAGE._ISOLanguage | _LEDGERTEXT._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [0a5ccfd6-0a16-4cea-9611-122dd92e48f5](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _SEGMENTTEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [e5991b82-37ea-4aab-ac0f-ac4408e9801e](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _COSTCENTERTEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [64c2dc78-64df-449e-8f2a-b79d38a85c71](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _PROFITCENTERTEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [fb81100d-536a-4bcd-ba15-1181609bacc7](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTINCHARTOFACCOUNTSTEXT.Key | GLACCOUNTINCHARTOFACCOUNTS.Key | one : one (default) | bothDirections | true (default) |  |
| [27a46f75-216a-4eb4-9eb6-878dda39b000](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _GLACCOUNTINCHARTOFACCOUNTSTEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [b23b556c-9773-43f2-9cb0-ff5e35982216](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_IDEBITCREDITCODE | DEBITCREDITCODETEXT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [3968a6d7-5cd4-4a66-a965-ca01f9f4014d](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_ISEGMENT | SEGMENTTEXT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [ab5e3fa8-ca6a-4563-b5b7-fbb832cf0096](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_COGS.'FIELD_PARAM_COGS Order' | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [cf46a66b-1ad3-463e-b84c-0fac6354167f](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_GROSSPROFIT.'FIELD_PARAM_GROSSPROFIT Order' | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [975cfdb5-c92c-4d18-a709-b54f2e2a08f5](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_INVENTORYCHANGE.'FIELD_PARAM_INVENTORYCHANGE Order' | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [503b9c98-504f-4746-b9cd-d258fe0331e7](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_OPEX.'FIELD_PARAM_OPEX Order' | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [fc7c908a-de1c-408d-b3db-6850ca1dfc25](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_OTHEREXPENSES.'FIELD_PARAM_OTHEREXPENSES Order' | one : one (default) | bothDirections | true (default) |  |
| [aef8e29d-ba17-40a8-8f4b-8102edad4764](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_OPERATINGPROFIT.'FIELD_PARAM_OPERATINGPROFIT Order' | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [12acd182-078d-4540-9dba-2a435a9fcfc6](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_ICUSTOMER | CUSTOMER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [545233db-6b6a-4348-b287-fc84c06a3f24](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_NETPROFIT.'FIELD_PARAM_NETPROFIT Order' | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [14f8fccb-7e98-4cc6-a520-ed6a244e2fd8](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_IPRODUCTGROUP2 | PRODUCTGROUP2TEXT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [6d1de1fa-aecf-4b00-ad71-0f05b071a6ff](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _PRODUCTTEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [73ec3372-f74f-428e-a48f-7e711d6cd773](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _PRODUCTGROUP2TEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | one : one (default) | bothDirections | true (default) |  |
| [93f493fe-800b-46cb-bd3c-ec69c3a503e1](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_IPRODUCTGROUP2 | PRODUCTGROUP2TEXT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [670824f9-26be-45c0-b434-2c674b1fe1a7](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_ICUSTOMER | CUSTOMER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [bd41e66b-7140-4381-8404-0957087990b5](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTHIERARCHYWTEXT._ISOLanguage | SAPLANGUAGE._ISOLanguage | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [a712766b-93e3-4b86-9dc8-8cc5b2f32aaa](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_NODE_KEY | GLACCOUNTINCHARTOFACCOUNTS.Key | many (default) : one (default) | bothDirections | true (default) |  |
| [ac7674fa-6c13-488a-8ff5-6df5ee53bcad](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_TAXES.'FIELD_PARAM_TAXES Order' | one : one (default) | bothDirections | true (default) |  |
| [8ecdb630-f6f2-e47b-0557-ab249f1867b8](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_IPROFITCENTER | PROFITCENTER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [e0a02501-944a-4ec8-6d4b-5516d9485c3d](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | PROFITCENTER.Key | PROFITCENTERTEXT.Key | one : one (default) | bothDirections | true (default) |  |
| [97f0b183-a5c0-0fac-1a58-e62ba06f7c55](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_ICOSTCENTER | COSTCENTER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [be87cab3-2d43-9359-d40d-e924849f69c1](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | COSTCENTER.Key | COSTCENTERTEXT.Key | one : one (default) | bothDirections | true (default) |  |
| [ecb6ecde-5b10-4e82-8055-cd80236303ee](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_CURRENCY.'FIELD_PARAM_CURRENCY Order' | _FIELD_PARAM_REVENUE.'FIELD_PARAM_INCOMESTATEMENT Order' | one : one (default) | bothDirections | true (default) |  |
| [45c64ca5-41b7-e88d-7d66-58ecc4feb714](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_IFISCALPERIODFORVARIANT | FISCALPERIODFORVARIANT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [8797cfe1-e404-c59d-9f18-53f377fd2c68](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_IPRODUCT | PRODUCT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [480f73c3-67d9-ae5a-a08b-26010eb61b2f](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_IPRODUCT | PRODUCT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [de4c9776-8601-7cab-a24e-529bd296ff6a](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | SEGMENT.Key | SEGMENTTEXT.Key | one : one (default) | bothDirections | true (default) |  |
| [4f0c8592-475a-757e-5ba4-7fd48eb7fffd](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | DEBITCREDITCODE.Key | DEBITCREDITCODETEXT.Key | one : one (default) | bothDirections | true (default) |  |
| [9ff22770-623f-d896-aa1e-6ac8b9916617](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_ISEGMENT | SEGMENT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [b6ab937b-52be-58d0-c5ef-670cd6ff59f2](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | GLACCOUNTLINEITEMRAWDATA._key_IDEBITCREDITCODE | DEBITCREDITCODE.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [b6ecf395-88a3-ae9c-fbff-4a8be133ecd3](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_IPROFITCENTER | PROFITCENTER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [3be2b52e-457b-c9c2-c65c-797ada40e3ba](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_AGGR_CURRENCY.'_FIELD_PARAM_AGGR_CURRENCY Order' | _FIELD_PARAM_AGGR_CURRENT_PERIOD.'_FIELD_PARAM_AGGR_CURRENT_PERIOD Order' | one : one (default) | bothDirections | true (default) |  |
| [6d287599-968e-8b23-33e9-463f6afd0769](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_AGGR_OPENING_BALANCE.'_FIELD_PARAM_AGGR_OPENING_BALANCE Order' | _FIELD_PARAM_AGGR_CURRENCY.'_FIELD_PARAM_AGGR_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [b078e4ef-0067-87bf-8a6c-682afab4c705](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_AGGR_CLOSING_BALANCE.'_FIELD_PARAM_AGGR_CLOSING_BALANCE Order' | _FIELD_PARAM_AGGR_CURRENCY.'_FIELD_PARAM_AGGR_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [f3d63945-571d-f44c-3d18-8941891f1a3d](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE.'FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE Order' | _FIELD_PARAM_AGGR_CURRENCY.'_FIELD_PARAM_AGGR_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [4e3297a3-9d6c-a631-0312-9f8b1dcfa1c6](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD.'FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD Order' | _FIELD_PARAM_AGGR_CURRENCY.'_FIELD_PARAM_AGGR_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [9073059f-a419-2a6e-2548-d534d033117d](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | _FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE.'FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE Order' | _FIELD_PARAM_AGGR_CURRENCY.'_FIELD_PARAM_AGGR_CURRENCY Order' | one : one (default) | bothDirections | true (default) |  |
| [766a0705-b6a1-f701-37ab-f3a5290a70fb](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_ICOSTCENTER | COSTCENTER.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |
| [c1667456-1a24-7c2b-7c7b-cf875c03dfbe](../Record_to_Report_Financial_Insights.SemanticModel/definition/relationships.tmdl) | AGGR_H._key_IFISCALPERIODFORVARIANT | FISCALPERIODFORVARIANT.Key | many (default) : one (default) | oneDirection (default) | true (default) |  |

## Functional TMDL definitions: all tables

### __MEASURES_AGGR_HRCHY

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_AGGR_HRCHY.tmdl). 0 columns; 0 hidden columns; 0 calculated columns; 12 measures; m partition; import mode.

````tmdl
table __MEASURES_AGGR_HRCHY

	measure AGGR_HRCHY_COMPANYCODE_AMOUNT = CALCULATE(SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY]) * GLACCOUNTHIERARCHYWTEXT[_Show])
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_COMPANYCODE_CLOSING_BALANCE =
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = CALCULATE(
			    [AGGR_HRCHY_COMPANYCODE_AMOUNT],
				REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_COMPANYCODE_CURRENT_PERIOD =
			CALCULATE(
			    [AGGR_HRCHY_COMPANYCODE_AMOUNT],
			    FILTER(AGGR_H, AGGR_H[FISCALPERIOD] = [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_COMPANYCODE_OPENING_BALANCE =
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = CALCULATE(
			    [AGGR_HRCHY_COMPANYCODE_AMOUNT],
				REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_GLOBAL_AMOUNT = CALCULATE(SUM(AGGR_H[AMOUNTINGLOBALCURRENCY]) * GLACCOUNTHIERARCHYWTEXT[_Show])
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_GLOBAL_CLOSING_BALANCE =
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = CALCULATE(
			    [AGGR_HRCHY_GLOBAL_AMOUNT],
				REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			RETURN CLOSING_BALANCE
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_GLOBAL_CURRENT_PERIOD =
			CALCULATE(
			    [AGGR_HRCHY_GLOBAL_AMOUNT],
			    FILTER(AGGR_H, AGGR_H[FISCALPERIOD] = [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_GLOBAL_OPENING_BALANCE =
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = CALCULATE(
			    [AGGR_HRCHY_GLOBAL_AMOUNT],
				REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_TRANSACTION_AMOUNT = CALCULATE(SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY]) * GLACCOUNTHIERARCHYWTEXT[_Show])
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_TRANSACTION_CLOSING_BALANCE =
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = CALCULATE(
			    [AGGR_HRCHY_TRANSACTION_AMOUNT],
				REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			RETURN CLOSING_BALANCE
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_TRANSACTION_CURRENT_PERIOD =
			CALCULATE(
			    [AGGR_HRCHY_TRANSACTION_AMOUNT],
			    FILTER(AGGR_H, AGGR_H[FISCALPERIOD] = [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_HRCHY_TRANSACTION_OPENING_BALANCE =
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = CALCULATE(
			    [AGGR_HRCHY_TRANSACTION_AMOUNT],
				REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	partition __MEASURES_GLACCOUNTHIERARCHY-06c64b67-a072-40aa-a591-f9f0843c91c6 = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table
````

### __MEASURES_AGGR_PROFITABILITY

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_AGGR_PROFITABILITY.tmdl). 0 columns; 0 hidden columns; 0 calculated columns; 30 measures; m partition; import mode.

````tmdl
table __MEASURES_AGGR_PROFITABILITY

	measure AGGR_COMPANYCODE_COGS =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "024" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "027" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "029" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "030"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANYCODE_GROSSPROFIT = [COMPANYCODE_REVENUE] - [COMPANYCODE_COGS]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANYCODE_GROSSPROFITMARGIN = DIVIDE ( [COMPANYCODE_GROSSPROFIT], [COMPANYCODE_REVENUE] )
		formatString: 0.00%;-0.00%;0.00%
		displayFolder: COMPANYCODE_CURRENCY

	measure AGGR_COMPANYCODE_INVENTORYCHANGE =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL6] = "021"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANYCODE_OPERATINGPROFIT = [COMPANYCODE_GROSSPROFIT] - [COMPANYCODE_OPEX]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANYCODE_OPEX = [COMPANYCODE_INVENTORYCHANGE] + [COMPANYCODE_OTHEREXPENSES]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANYCODE_OTHEREXPENSES =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "016" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "017" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "018" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "019"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANYCODE_REVENUE =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL8] = "023"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_COGS =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "024" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "027" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "029" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "030"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_GROSSPROFIT = [GLOBAL_REVENUE] - [GLOBAL_COGS]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_INVENTORYCHANGE =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL6] = "021"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_OPERATINGPROFIT = [GLOBAL_GROSSPROFIT] - [GLOBAL_OPEX]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_OPEX = [GLOBAL_INVENTORYCHANGE] + [GLOBAL_OTHEREXPENSES]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_OTHEREXPENSES =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "016" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "017" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "018" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "019"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_REVENUE =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL8] = "023"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_OPERATING_PROFIT_MARGIN = DIVIDE([COMPANYCODE_OPERATINGPROFIT], [COMPANYCODE_REVENUE])
		formatString: 0.00%;-0.00%;0.00%

	measure AGGR_OPEX_RATIO = DIVIDE([COMPANYCODE_OPEX], [COMPANYCODE_REVENUE])
		formatString: 0.00%;-0.00%;0.00%

	measure AGGR_COMPANYCODE_TAXES =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL3] = "011"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_TAXES =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL3] = "011"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_NETPROFIT = [GLOBAL_OPERATINGPROFIT] - [GLOBAL_TAXES]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANYCODE_NETPROFIT = [COMPANYCODE_OPERATINGPROFIT] - [COMPANYCODE_TAXES]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_TRANSACTION_REVENUE =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL8] = "023"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure AGGR_TRANSACTION_COGS =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "024" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "027" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "029" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "030"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure AGGR_TRANSACTION_GROSSPROFIT = [TRANSACTION_REVENUE] - [TRANSACTION_COGS]
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure AGGR_TRANSACTION_INVENTORYCHANGE =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL6] = "021"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure AGGR_TRANSACTION_NETPROFIT = [TRANSACTION_OPERATINGPROFIT] - [TRANSACTION_TAXES]
		displayFolder: TRANSACTION_CURRENCY

	measure AGGR_TRANSACTION_OPERATINGPROFIT = [TRANSACTION_GROSSPROFIT] - [TRANSACTION_OPEX]
		displayFolder: TRANSACTION_CURRENCY

	measure AGGR_TRANSACTION_OPEX = [TRANSACTION_INVENTORYCHANGE] + [TRANSACTION_OTHEREXPENSES]
		displayFolder: TRANSACTION_CURRENCY

	measure AGGR_TRANSACTION_OTHEREXPENSES =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "016" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "017" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "018" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "019"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure AGGR_TRANSACTION_TAXES =
			CALCULATE(ABS(SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL3] = "011"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	partition __MEASURES_PROFITABILITY = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table
````

### __MEASURES_GLACCOUNTHIERARCHY

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_GLACCOUNTHIERARCHY.tmdl). 0 columns; 0 hidden columns; 0 calculated columns; 12 measures; m partition; import mode.

````tmdl
table __MEASURES_GLACCOUNTHIERARCHY

	measure GLACCT_HRCHY_COMPANYCODE_AMOUNT = CALCULATE(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY]) * GLACCOUNTHIERARCHYWTEXT[_Show])
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_COMPANYCODE_CLOSING_BALANCE =
			CALCULATE(
			    [GLACCT_HRCHY_COMPANYCODE_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] <= [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_COMPANYCODE_CURRENT_PERIOD =
			CALCULATE(
			    [GLACCT_HRCHY_COMPANYCODE_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] = [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_COMPANYCODE_OPENING_BALANCE =
			CALCULATE(
			    [GLACCT_HRCHY_COMPANYCODE_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] < [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_GLOBAL_AMOUNT = CALCULATE(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY]) * GLACCOUNTHIERARCHYWTEXT[_Show])
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_GLOBAL_CLOSING_BALANCE =
			CALCULATE(
			    [GLACCT_HRCHY_GLOBAL_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] <= [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_GLOBAL_CURRENT_PERIOD =
			CALCULATE(
			    [GLACCT_HRCHY_GLOBAL_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] = [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_GLOBAL_OPENING_BALANCE =
			CALCULATE(
			    [GLACCT_HRCHY_GLOBAL_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] < [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_TRANSACTION_AMOUNT = CALCULATE(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY]) * GLACCOUNTHIERARCHYWTEXT[_Show])
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_TRANSACTION_CLOSING_BALANCE =
			CALCULATE(
			    [GLACCT_HRCHY_TRANSACTION_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] <= [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_TRANSACTION_CURRENT_PERIOD =
			CALCULATE(
			    [GLACCT_HRCHY_TRANSACTION_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] = [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLACCT_HRCHY_TRANSACTION_OPENING_BALANCE =
			CALCULATE(
			    [GLACCT_HRCHY_TRANSACTION_AMOUNT],
			    FILTER(GLACCOUNTLINEITEMRAWDATA, GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] < [SELECTEDFISCALPERIOD]
			    ))
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	partition __MEASURES_GLACCOUNTHIERARCHY-06c64b67-a072-40aa-a591-f9f0843c91c6 = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table
````

### __MEASURES_OTHER

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_OTHER.tmdl). 0 columns; 0 hidden columns; 0 calculated columns; 9 measures; m partition; import mode.

````tmdl
table __MEASURES_OTHER

	measure COMPANYCODE_CLOSING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = 
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			
			RETURN CLOSING_BALANCE
			
			```
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_OPENING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = 
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			
			RETURN CLOSING_BALANCE
			```
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_CURRENT_PERIOD =
			
			VAR CurrentFP = [SELECTEDFISCALPERIOD]
			RETURN
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY]),
			    GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] = CurrentFP
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_CLOSING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = 
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			RETURN CLOSING_BALANCE
			```
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_CURRENT_PERIOD =
			
			VAR CurrentFP = [SELECTEDFISCALPERIOD]
			RETURN
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY]),
			    GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] = CurrentFP
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_OPENING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = 
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
			```
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure TRANSACTION_CLOSING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = 
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			RETURN CLOSING_BALANCE
			```
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure TRANSACTION_CURRENT_PERIOD =
			
			VAR CurrentFP = [SELECTEDFISCALPERIOD]
			RETURN
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY]),
			    GLACCOUNTLINEITEMRAWDATA[FISCALPERIOD] = CurrentFP
			)
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure TRANSACTION_OPENING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = 
			CALCULATE(
			    SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
			```
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	partition __MEASURES_OTHER-89b17d01-3478-4f8c-be54-38cbf82e03ae = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table
````

### __MEASURES_PROFITABILITY

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/__MEASURES_PROFITABILITY.tmdl). 0 columns; 0 hidden columns; 0 calculated columns; 30 measures; m partition; import mode.

````tmdl
table __MEASURES_PROFITABILITY

	measure COMPANYCODE_COGS =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "024" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "027" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "029" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "030"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_GROSSPROFIT = [COMPANYCODE_REVENUE] - [COMPANYCODE_COGS]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_GROSSPROFITMARGIN = DIVIDE ( [COMPANYCODE_GROSSPROFIT], [COMPANYCODE_REVENUE] )
		formatString: 0.00%;-0.00%;0.00%
		displayFolder: COMPANYCODE_CURRENCY

	measure COMPANYCODE_INVENTORYCHANGE =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL6] = "021"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_OPERATINGPROFIT = [COMPANYCODE_GROSSPROFIT] - [COMPANYCODE_OPEX]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_OPEX = [COMPANYCODE_INVENTORYCHANGE] + [COMPANYCODE_OTHEREXPENSES]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_OTHEREXPENSES =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "016" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "017" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "018" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "019"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_REVENUE = ```
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY])), 
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL8] = "023"), 
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = "YCOA"), 
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = "YPA1")
			)
			```
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_COGS =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "024" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "027" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "029" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "030"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_GROSSPROFIT = [GLOBAL_REVENUE] - [GLOBAL_COGS]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_INVENTORYCHANGE =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL6] = "021"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_OPERATINGPROFIT = [GLOBAL_GROSSPROFIT] - [GLOBAL_OPEX]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_OPEX = [GLOBAL_INVENTORYCHANGE] + [GLOBAL_OTHEREXPENSES]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_OTHEREXPENSES =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "016" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "017" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "018" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "019"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_REVENUE =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL8] = "023"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure OPERATING_PROFIT_MARGIN = DIVIDE([COMPANYCODE_OPERATINGPROFIT], [COMPANYCODE_REVENUE])
		formatString: 0.00%;-0.00%;0.00%

	measure OPEX_RATIO = DIVIDE([COMPANYCODE_OPEX], [COMPANYCODE_REVENUE])
		formatString: 0.00%;-0.00%;0.00%

	measure COMPANYCODE_TAXES =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINCOMPANYCODECURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL3] = "011"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_TAXES =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINGLOBALCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL3] = "011"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure GLOBAL_NETPROFIT = [GLOBAL_OPERATINGPROFIT] - [GLOBAL_TAXES]
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure COMPANYCODE_NETPROFIT = [COMPANYCODE_OPERATINGPROFIT] - [COMPANYCODE_TAXES]
		displayFolder: COMPANYCODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure TRANSACTION_REVENUE =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL8] = "023"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure TRANSACTION_COGS =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "024" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "027" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "029" || GLACCOUNTHIERARCHYWTEXT[LEVEL7] = "030"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure TRANSACTION_GROSSPROFIT = [TRANSACTION_REVENUE] - [TRANSACTION_COGS]
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure TRANSACTION_INVENTORYCHANGE =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL6] = "021"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure TRANSACTION_NETPROFIT = [TRANSACTION_OPERATINGPROFIT] - [TRANSACTION_TAXES]
		displayFolder: TRANSACTION_CURRENCY

	measure TRANSACTION_OPERATINGPROFIT = [TRANSACTION_GROSSPROFIT] - [TRANSACTION_OPEX]
		displayFolder: TRANSACTION_CURRENCY

	measure TRANSACTION_OPEX = [TRANSACTION_INVENTORYCHANGE] + [TRANSACTION_OTHEREXPENSES]
		displayFolder: TRANSACTION_CURRENCY

	measure TRANSACTION_OTHEREXPENSES =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "016" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "017" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "018" || GLACCOUNTHIERARCHYWTEXT[LEVEL5] = "019"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	measure TRANSACTION_TAXES =
			CALCULATE(ABS(SUM(GLACCOUNTLINEITEMRAWDATA[AMOUNTINTRANSACTIONCURRENCY])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[LEVEL3] = "011"),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[_ISOLanguage] = SELECTEDVALUE(SAPLANGUAGE[_ISOLanguage]) ),
			KEEPFILTERS(CHARTOFACCOUNTS[CHARTOFACCOUNTS] = SELECTEDVALUE(CHARTOFACCOUNTS[CHARTOFACCOUNTS])),
			KEEPFILTERS(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY] = SELECTEDVALUE(GLACCOUNTHIERARCHYWTEXT[GLACCOUNTHIERARCHY]))
			)
		formatString: "₹"\ #,0.###############;#,0.###############\ -"₹";"₹"\ #,0.###############
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"currencyCulture":"en-IN"}

	partition __MEASURES_PROFITABILITY = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table
````

### _CHARTOFACCOUNTSTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_CHARTOFACCOUNTSTEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _CHARTOFACCOUNTSTEXT

	column FIELD_PARAM_CHARTOFACCOUNTSTEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_CHARTOFACCOUNTSTEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_CHARTOFACCOUNTSTEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CHARTOFACCOUNTSTEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_CHARTOFACCOUNTSTEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CHARTOFACCOUNTSTEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_CHARTOFACCOUNTSTEXT[FIELD_PARAM_CHARTOFACCOUNTSTEXT Fields], SEARCH("[", _CHARTOFACCOUNTSTEXT[FIELD_PARAM_CHARTOFACCOUNTSTEXT Fields])+1, 2)
		isHidden
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _CHARTOFACCOUNTSTEXT = calculated
		mode: import
		source =
				{
				    ("ChartOfAccountsText", NAMEOF('CHARTOFACCOUNTSTEXT'[DE]), 0),
				    ("ChartOfAccountsText", NAMEOF('CHARTOFACCOUNTSTEXT'[EN]), 1),
				    ("ChartOfAccountsText", NAMEOF('CHARTOFACCOUNTSTEXT'[ES]), 2),
				    ("ChartOfAccountsText", NAMEOF('CHARTOFACCOUNTSTEXT'[FR]), 3)
				}
````

### _COSTCENTERTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_COSTCENTERTEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _COSTCENTERTEXT

	column FIELD_PARAM_COSTCENTERTEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_COSTCENTERTEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_COSTCENTERTEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_COSTCENTERTEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_COSTCENTERTEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_COSTCENTERTEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_COSTCENTERTEXT[FIELD_PARAM_COSTCENTERTEXT Fields], SEARCH("[", _COSTCENTERTEXT[FIELD_PARAM_COSTCENTERTEXT Fields])+1, 2)
		isHidden
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _COSTCENTERTEXT = calculated
		mode: import
		source =
				{
				    ("CostCenterText", NAMEOF('COSTCENTERTEXT'[DE]), 0),
				    ("CostCenterText", NAMEOF('COSTCENTERTEXT'[EN]), 1),
				    ("CostCenterText", NAMEOF('COSTCENTERTEXT'[ES]), 2),
				    ("CostCenterText", NAMEOF('COSTCENTERTEXT'[FR]), 3)
				}
````

### _DEBITCREDITCODETEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_DEBITCREDITCODETEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _DEBITCREDITCODETEXT

	column FIELD_PARAM_DEBITCREDITCODETEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_DEBITCREDITCODETEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_DEBITCREDITCODETEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_DEBITCREDITCODETEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_DEBITCREDITCODETEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_DEBITCREDITCODETEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_DEBITCREDITCODETEXT[FIELD_PARAM_DEBITCREDITCODETEXT Fields], SEARCH("[", _DEBITCREDITCODETEXT[FIELD_PARAM_DEBITCREDITCODETEXT Fields])+1, 2)
		isHidden
		isAvailableInMdx: false
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _DEBITCREDITCODETEXT = calculated
		mode: import
		source =
				{
				    ("Debit/Credit", NAMEOF('DEBITCREDITCODETEXT'[DE]), 0),
				    ("Debit/Credit", NAMEOF('DEBITCREDITCODETEXT'[EN]), 1),
				    ("Debit/Credit", NAMEOF('DEBITCREDITCODETEXT'[ES]), 2),
				    ("Debit/Credit", NAMEOF('DEBITCREDITCODETEXT'[FR]), 3)
				}
````

### _FIELD_PARAM_AGGR_CLOSING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_CLOSING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_CLOSING_BALANCE

	column _FIELD_PARAM_AGGR_CLOSING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: '_FIELD_PARAM_AGGR_CLOSING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: '_FIELD_PARAM_AGGR_CLOSING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_CLOSING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: '_FIELD_PARAM_AGGR_CLOSING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_CLOSING_BALANCE Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_CLOSING_BALANCE = calculated
		mode: import
		source =
				{
				    ("Closing Balance", NAMEOF('_MEASURES_AGGR_H'[AGGR_COMPANY_CODE_CLOSING_BALANCE]), 0),
				    ("Closing Balance", NAMEOF('_MEASURES_AGGR_H'[AGGR_GLOBAL_CLOSING_BALANCE]), 1),
				    ("Closing Balance", NAMEOF('_MEASURES_AGGR_H'[AGGR_TRANSACTION_CLOSING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_AGGR_CURRENCY

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_CURRENCY.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_CURRENCY

	column _FIELD_PARAM_AGGR_CURRENCY
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: '_FIELD_PARAM_AGGR_CURRENCY Order'

		relatedColumnDetails
			groupByColumn: '_FIELD_PARAM_AGGR_CURRENCY Fields'

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_CURRENCY Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: '_FIELD_PARAM_AGGR_CURRENCY Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_CURRENCY Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_CURRENCY = calculated
		mode: import
		source =
				{
				    ("Company Code Currency", NAMEOF('AGGR_H'[COMPANYCODECURRENCY]), 0),
				    ("Global Currency", NAMEOF('AGGR_H'[GLOBALCURRENCY]), 1),
				    ("Transaction Currency", NAMEOF('AGGR_H'[TRANSACTIONCURRENCY]), 2)
				}
````

### _FIELD_PARAM_AGGR_CURRENT_PERIOD

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_CURRENT_PERIOD.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_CURRENT_PERIOD

	column _FIELD_PARAM_AGGR_CURRENT_PERIOD
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: '_FIELD_PARAM_AGGR_CURRENT_PERIOD Order'

		relatedColumnDetails
			groupByColumn: '_FIELD_PARAM_AGGR_CURRENT_PERIOD Fields'

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_CURRENT_PERIOD Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: '_FIELD_PARAM_AGGR_CURRENT_PERIOD Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_CURRENT_PERIOD Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_CURRENT_PERIOD = calculated
		mode: import
		source =
				{
				    ("Current Period", NAMEOF('_MEASURES_AGGR_H'[AGGR_COMPANY_CODE_CURRENT_PERIOD]), 0),
				    ("Current Period", NAMEOF('_MEASURES_AGGR_H'[AGGR_GLOBAL_CURRENT_PERIOD]), 1),
				    ("Current Period", NAMEOF('_MEASURES_AGGR_H'[AGGR_TRANSACTION_CURRENT_PERIOD]), 2)
				}
````

### _FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE

	column FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE-1fd65a89-4c7c-4d9d-988e-cd2af47b8a65 = calculated
		mode: import
		source =
				{
				    ("Closing Balance", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_COMPANYCODE_CLOSING_BALANCE]), 0),
				    ("Closing Balance", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_GLOBAL_CLOSING_BALANCE]), 1),
				    ("Closing Balance", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_TRANSACTION_CLOSING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD

	column FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD-2efeb96e-32e0-4d06-944d-c4daf6d08705 = calculated
		mode: import
		source =
				{
				    ("Current Period", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_COMPANYCODE_CURRENT_PERIOD]), 0),
				    ("Current Period", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_GLOBAL_CURRENT_PERIOD]), 1),
				    ("Current Period", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_TRANSACTION_CURRENT_PERIOD]), 2)
				}
````

### _FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE

	column FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE-558e30a3-25fa-4c91-baee-e2c08e75572f = calculated
		mode: import
		source =
				{
				    ("Opening Balance", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_COMPANYCODE_OPENING_BALANCE]), 0),
				    ("Opening Balance", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_GLOBAL_OPENING_BALANCE]), 1),
				    ("Opening Balance", NAMEOF('__MEASURES_AGGR_HRCHY'[AGGR_HRCHY_TRANSACTION_OPENING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_AGGR_OPENING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_OPENING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_OPENING_BALANCE

	column _FIELD_PARAM_AGGR_OPENING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: '_FIELD_PARAM_AGGR_OPENING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: '_FIELD_PARAM_AGGR_OPENING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_OPENING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: '_FIELD_PARAM_AGGR_OPENING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_OPENING_BALANCE Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_OPENING_BALANCE = calculated
		mode: import
		source =
				{
				    ("Opening Balance", NAMEOF('_MEASURES_AGGR_H'[AGGR_COMPANY_CODE_OPENING_BALANCE]), 0),
				    ("Opening Balance", NAMEOF('_MEASURES_AGGR_H'[AGGR_GLOBAL_OPENING_BALANCE]), 1),
				    ("Opening Balance", NAMEOF('_MEASURES_AGGR_H'[AGGR_TRANSACTION_OPENING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS

	column _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: '_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS Order'

		relatedColumnDetails
			groupByColumn: '_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS Fields'

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: '_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column '_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS = calculated
		mode: import
		source =
				{
				    ("GLACCOUNTGROUP", NAMEOF('GLACCOUNTINCHARTOFACCOUNTS'[GLACCOUNTGROUP]), 0),
				    ("PROFITCENTER", NAMEOF('PROFITCENTER'[PROFITCENTER]), 1),
				    ("COSTCENTER", NAMEOF('COSTCENTER'[COSTCENTER]), 2),
				    ("COMPANYCODE", NAMEOF('COMPANYCODE'[COMPANYCODE]), 3),
				    ("PARTNERCOMPANYCODE", NAMEOF('AGGR_H'[PARTNERCOMPANYCODE]), 4),
				    ("TAXCODE", NAMEOF('AGGR_H'[TAXCODE]), 5),
				    ("TAXCOUNTRY", NAMEOF('AGGR_H'[TAXCOUNTRY]), 6)
				}
````

### _FIELD_PARAM_CLOSING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_CLOSING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_CLOSING_BALANCE

	column FIELD_PARAM_CLOSING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_CLOSING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_CLOSING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CLOSING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_CLOSING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CLOSING_BALANCE Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_CLOSING_BALANCE-5567e162-ab7a-44a8-b649-99482d358867 = calculated
		mode: import
		source =
				{
				    ("Closing Balance", NAMEOF('__MEASURES_OTHER'[COMPANYCODE_CLOSING_BALANCE]), 0),
				    ("Closing Balance", NAMEOF('__MEASURES_OTHER'[GLOBAL_CLOSING_BALANCE]), 1),
				    ("Closing Balance", NAMEOF('__MEASURES_OTHER'[TRANSACTION_CLOSING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_COGS

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_COGS.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_COGS

	column FIELD_PARAM_COGS
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_COGS Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_COGS Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_COGS Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_COGS Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_COGS Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_COGS = calculated
		mode: import
		source =
				{
				    ("COGS", NAMEOF([COMPANYCODE_COGS]), 0),
				    ("COGS", NAMEOF([GLOBAL_COGS]), 1)
				}
````

### _FIELD_PARAM_CURRENCY

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_CURRENCY.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_CURRENCY

	column FIELD_PARAM_CURRENCY
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_CURRENCY Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_CURRENCY Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CURRENCY Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_CURRENCY Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CURRENCY Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_CURRENCY-e31f8fbb-e46e-49e6-b582-7f920aa679d4 = calculated
		mode: import
		source =
				{
				    ("Company Code Currency", NAMEOF('GLACCOUNTLINEITEMRAWDATA'[COMPANYCODECURRENCY]), 0),
				    ("Global Currency", NAMEOF('GLACCOUNTLINEITEMRAWDATA'[GLOBALCURRENCY]), 1),
				    ("Transaction Currency", NAMEOF('GLACCOUNTLINEITEMRAWDATA'[TRANSACTIONCURRENCY]), 2)
				}
````

### _FIELD_PARAM_CURRENT_PERIOD

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_CURRENT_PERIOD.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_CURRENT_PERIOD

	column FIELD_PARAM_CURRENT_PERIOD
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_CURRENT_PERIOD Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_CURRENT_PERIOD Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CURRENT_PERIOD Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_CURRENT_PERIOD Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_CURRENT_PERIOD Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_CURRENT_PERIOD-48c741ce-f5a9-4f76-a82e-0ce4197c3285 = calculated
		mode: import
		source =
				{
				    ("Current Period", NAMEOF('__MEASURES_OTHER'[COMPANYCODE_CURRENT_PERIOD]), 0),
				    ("Current Period", NAMEOF('__MEASURES_OTHER'[GLOBAL_CURRENT_PERIOD]), 1),
				    ("Current Period", NAMEOF('__MEASURES_OTHER'[TRANSACTION_CURRENT_PERIOD]), 2)
				}
````

### _FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE

	column FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_GLACCT_HRCHY_CLOSING_BALANCE-1fd65a89-4c7c-4d9d-988e-cd2af47b8a65 = calculated
		mode: import
		source =
				{
				    ("Closing Balance", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_COMPANYCODE_CLOSING_BALANCE]), 0),
				    ("Closing Balance", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_GLOBAL_CLOSING_BALANCE]), 1),
				    ("Closing Balance", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_TRANSACTION_CLOSING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD

	column FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_GLACCT_HRCHY_CURRENT_PERIOD-2efeb96e-32e0-4d06-944d-c4daf6d08705 = calculated
		mode: import
		source =
				{
				    ("Current Period", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_COMPANYCODE_CURRENT_PERIOD]), 0),
				    ("Current Period", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_GLOBAL_CURRENT_PERIOD]), 1),
				    ("Current Period", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_TRANSACTION_CURRENT_PERIOD]), 2)
				}
````

### _FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE

	column FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_GLACCT_HRCHY_OPENING_BALANCE-558e30a3-25fa-4c91-baee-e2c08e75572f = calculated
		mode: import
		source =
				{
				    ("Opening Balance", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_COMPANYCODE_OPENING_BALANCE]), 0),
				    ("Opening Balance", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_GLOBAL_OPENING_BALANCE]), 1),
				    ("Opening Balance", NAMEOF('__MEASURES_GLACCOUNTHIERARCHY'[GLACCT_HRCHY_TRANSACTION_OPENING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_GROSSPROFIT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_GROSSPROFIT.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_GROSSPROFIT

	column FIELD_PARAM_GROSSPROFIT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_GROSSPROFIT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_GROSSPROFIT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GROSSPROFIT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_GROSSPROFIT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GROSSPROFIT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_GROSSPROFIT = calculated
		mode: import
		source =
				{
				    ("Gross Profit", NAMEOF([COMPANYCODE_GROSSPROFIT]), 0),
				    ("Gross Profit", NAMEOF([GLOBAL_GROSSPROFIT]), 1)
				}
````

### _FIELD_PARAM_INVENTORYCHANGE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_INVENTORYCHANGE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_INVENTORYCHANGE

	column FIELD_PARAM_INVENTORYCHANGE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_INVENTORYCHANGE Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_INVENTORYCHANGE Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_INVENTORYCHANGE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_INVENTORYCHANGE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_INVENTORYCHANGE Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_INVENTORYCHANGE = calculated
		mode: import
		source =
				{
				    ("Inventory Change", NAMEOF([COMPANYCODE_INVENTORYCHANGE]), 0),
				    ("Inventory Change", NAMEOF([GLOBAL_INVENTORYCHANGE]), 1)
				}
````

### _FIELD_PARAM_LINE_ITEM_FIELDS

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_LINE_ITEM_FIELDS.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_LINE_ITEM_FIELDS

	column FIELD_PARAM_LINE_ITEM_FIELDS
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_LINE_ITEM_FIELDS Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_LINE_ITEM_FIELDS Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_LINE_ITEM_FIELDS Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_LINE_ITEM_FIELDS Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_LINE_ITEM_FIELDS Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_LINE_ITEM_FIELDS = calculated
		mode: import
		source =
				{
				    ("Profit Center", NAMEOF('PROFITCENTER'[PROFITCENTER]), 0),
				    ("Segment", NAMEOF(SEGMENTTEXT[SEGMENT]), 1),
				    ("Cost Center", NAMEOF('COSTCENTER'[COSTCENTER]), 2),
				    ("Tax Code", NAMEOF('GLACCOUNTLINEITEMRAWDATA'[TAXCODE]), 3),
				    ("Tax Country", NAMEOF('GLACCOUNTLINEITEMRAWDATA'[TAXCOUNTRY]), 4)
				}
````

### _FIELD_PARAM_NETPROFIT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_NETPROFIT.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_NETPROFIT

	column FIELD_PARAM_NETPROFIT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_NETPROFIT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_NETPROFIT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_NETPROFIT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_NETPROFIT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_NETPROFIT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_NETPROFIT = calculated
		mode: import
		source =
				{
				    ("Net Profit", NAMEOF('__MEASURES_PROFITABILITY'[COMPANYCODE_NETPROFIT]), 0),
				    ("Net Profit", NAMEOF('__MEASURES_PROFITABILITY'[GLOBAL_NETPROFIT]), 1)
				}
````

### _FIELD_PARAM_OPENING_BALANCE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OPENING_BALANCE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_OPENING_BALANCE

	column FIELD_PARAM_OPENING_BALANCE
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_OPENING_BALANCE Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_OPENING_BALANCE Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OPENING_BALANCE Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_OPENING_BALANCE Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OPENING_BALANCE Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_OPENING_BALANCE-649688a7-d5ad-4dad-8e69-4d883ee34857 = calculated
		mode: import
		source =
				{
				    ("Opening Balance", NAMEOF('__MEASURES_OTHER'[COMPANYCODE_OPENING_BALANCE]), 0),
				    ("Opening Balance", NAMEOF('__MEASURES_OTHER'[GLOBAL_OPENING_BALANCE]), 1),
				    ("Opening Balance", NAMEOF('__MEASURES_OTHER'[TRANSACTION_OPENING_BALANCE]), 2)
				}
````

### _FIELD_PARAM_OPERATINGPROFIT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OPERATINGPROFIT.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_OPERATINGPROFIT

	column FIELD_PARAM_OPERATINGPROFIT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_OPERATINGPROFIT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_OPERATINGPROFIT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OPERATINGPROFIT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_OPERATINGPROFIT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OPERATINGPROFIT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_OPERATINGPROFIT = calculated
		mode: import
		source =
				{
				    ("Operating Profit", NAMEOF([COMPANYCODE_OPERATINGPROFIT]), 0),
				    ("Operating Profit", NAMEOF([GLOBAL_OPERATINGPROFIT]), 1)
				}
````

### _FIELD_PARAM_OPEX

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OPEX.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_OPEX

	column FIELD_PARAM_OPEX
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_OPEX Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_OPEX Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OPEX Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_OPEX Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OPEX Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_OPEX = calculated
		mode: import
		source =
				{
				    ("OPEX", NAMEOF([COMPANYCODE_OPEX]), 0),
				    ("OPEX", NAMEOF([GLOBAL_OPEX]), 1)
				}
````

### _FIELD_PARAM_OTHEREXPENSES

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_OTHEREXPENSES.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_OTHEREXPENSES

	column FIELD_PARAM_OTHEREXPENSES
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_OTHEREXPENSES Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_OTHEREXPENSES Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OTHEREXPENSES Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_OTHEREXPENSES Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_OTHEREXPENSES Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_OTHEREXPENSES = calculated
		mode: import
		source =
				{
				    ("Other Expenses", NAMEOF([COMPANYCODE_OTHEREXPENSES]), 0),
				    ("Other Expenses", NAMEOF([GLOBAL_OTHEREXPENSES]), 1)
				}
````

### _FIELD_PARAM_REVENUE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_REVENUE.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_REVENUE

	column FIELD_PARAM_INCOMESTATEMENT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_INCOMESTATEMENT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_INCOMESTATEMENT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_INCOMESTATEMENT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_INCOMESTATEMENT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_INCOMESTATEMENT Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_REVENUE = calculated
		mode: import
		source =
				{
				    ("Revenue", NAMEOF([COMPANYCODE_REVENUE]), 0),
				    ("Revenue", NAMEOF([GLOBAL_REVENUE]), 1),
				    ("Revenue", NAMEOF([TRANSACTION_REVENUE]), 2)
				}
````

### _FIELD_PARAM_TAXES

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_TAXES.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_TAXES

	column FIELD_PARAM_TAXES
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_TAXES Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_TAXES Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_TAXES Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_TAXES Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_TAXES Order'
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_TAXES = calculated
		mode: import
		source =
				{
				    ("Taxes", NAMEOF('__MEASURES_PROFITABILITY'[COMPANYCODE_TAXES]), 0),
				    ("Taxes", NAMEOF('__MEASURES_PROFITABILITY'[GLOBAL_TAXES]), 1)
				}
````

### _FIELD_PARAM_TRIALBALANCE_FIELDS

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FIELD_PARAM_TRIALBALANCE_FIELDS.tmdl). 3 columns; 2 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FIELD_PARAM_TRIALBALANCE_FIELDS

	column FIELD_PARAM_TRIALBALANCE_FIELDS
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_TRIALBALANCE_FIELDS Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_TRIALBALANCE_FIELDS Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_TRIALBALANCE_FIELDS Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_TRIALBALANCE_FIELDS Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_TRIALBALANCE_FIELDS Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	partition _FIELD_PARAM_TRIALBALANCE_FIELDS-461fa6af-bf22-4079-9955-06e2fe86092c = calculated
		mode: import
		source =
				{
				    ("GL Account Group", NAMEOF('GLACCOUNTINCHARTOFACCOUNTS'[GLACCOUNTGROUP]), 0),
				    ("Profit Center", NAMEOF(PROFITCENTER[PROFITCENTER]), 1),
				    ("Cost Center", NAMEOF(COSTCENTER[COSTCENTER]), 2),
				    ("Company Code", NAMEOF(COMPANYCODE[COMPANYCODE]), 3),
				    ("Partner Company Code", NAMEOF(GLACCOUNTLINEITEMRAWDATA[PARTNERCOMPANYCODE]), 4),
				    ("Tax Code", NAMEOF('GLACCOUNTLINEITEMRAWDATA'[TAXCODE]), 5),
				    ("Tax Country", NAMEOF('GLACCOUNTLINEITEMRAWDATA'[TAXCOUNTRY]), 6)
				}
````

### _FISCALPERIODTABLE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_FISCALPERIODTABLE.tmdl). 1 columns; 0 hidden columns; 0 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _FISCALPERIODTABLE

	column FISCALPERIOD
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value]

		annotation SummarizationSetBy = User

	partition _FISCALPERIODTABLE-aa87d8b7-80ec-415d-8c12-c670b39cfbd9 = calculated
		mode: import
		source = GENERATESERIES(0, 16, 1)
````

### _GLACCOUNTINCHARTOFACCOUNTSTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_GLACCOUNTINCHARTOFACCOUNTSTEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _GLACCOUNTINCHARTOFACCOUNTSTEXT

	column FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_GLACCOUNTINCHARTOFACCOUNTSTEXT[FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT Fields], SEARCH("[", _GLACCOUNTINCHARTOFACCOUNTSTEXT[FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT Fields])+1, 2)
		isHidden
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _GLACCOUNTINCHARTOFACCOUNTSTEXT = calculated
		mode: import
		source =
				{
				    ("GL Account Name", NAMEOF('GLACCOUNTINCHARTOFACCOUNTSTEXT'[DE]), 0),
				    ("GL Account Name", NAMEOF('GLACCOUNTINCHARTOFACCOUNTSTEXT'[EN]), 1),
				    ("GL Account Name", NAMEOF('GLACCOUNTINCHARTOFACCOUNTSTEXT'[ES]), 2),
				    ("GL Account Name", NAMEOF('GLACCOUNTINCHARTOFACCOUNTSTEXT'[FR]), 3)
				}
````

### _LEDGERTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_LEDGERTEXT.tmdl). 4 columns; 2 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _LEDGERTEXT

	column FIELD_PARAM_LEDGERTEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_LEDGERTEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_LEDGERTEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_LEDGERTEXT Fields'
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_LEDGERTEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_LEDGERTEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_LEDGERTEXT[FIELD_PARAM_LEDGERTEXT Fields], SEARCH("[", _LEDGERTEXT[FIELD_PARAM_LEDGERTEXT Fields])+1, 2)
		isHidden
		isAvailableInMdx: false
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _LEDGERTEXT = calculated
		mode: import
		source =
				{
				    ("LedgerText", NAMEOF('LEDGERTEXT'[DE]), 0),
				    ("LedgerText", NAMEOF('LEDGERTEXT'[EN]), 1),
				    ("LedgerText", NAMEOF('LEDGERTEXT'[ES]), 2),
				    ("LedgerText", NAMEOF('LEDGERTEXT'[FR]), 3)
				}
````

### _MEASURES_AGGR_H

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_MEASURES_AGGR_H.tmdl). 0 columns; 0 hidden columns; 0 calculated columns; 9 measures; m partition; import mode.

````tmdl
table _MEASURES_AGGR_H

	measure AGGR_GLOBAL_CLOSING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = 
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINGLOBALCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			
			RETURN CLOSING_BALANCE
			```
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_CURRENT_PERIOD =
			
			VAR CurrentFP = [SELECTEDFISCALPERIOD]
			RETURN
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINGLOBALCURRENCY]),
			    AGGR_H[FISCALPERIOD] = CurrentFP
			)
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_GLOBAL_OPENING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = 
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINGLOBALCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
			```
		displayFolder: GLOBAL_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_TRANSACTION_CLOSING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = 
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			
			RETURN CLOSING_BALANCE
			```
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_TRANSACTION_CURRENT_PERIOD =
			
			VAR CurrentFP = [SELECTEDFISCALPERIOD]
			RETURN
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY]),
			    AGGR_H[FISCALPERIOD] = CurrentFP
			)
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_TRANSACTION_OPENING_BALANCE = ```
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = 
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINTRANSACTIONCURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			RETURN OPENING_BALANCE
			```
		displayFolder: TRANSACTION_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	measure AGGR_COMPANY_CODE_CLOSING_BALANCE = ```
			
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR CLOSING_BALANCE = 
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] <= CurrentSelectedFiscalPeriod
			)
			
			RETURN CLOSING_BALANCE
			```
		formatString: #,0.00
		displayFolder: COMPANY_CODE_CURRENCY

	measure AGGR_COMPANY_CODE_OPENING_BALANCE = ```
			
			
			VAR CurrentSelectedFiscalPeriod = [SELECTEDFISCALPERIOD]
			VAR OPENING_BALANCE = 
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY]),
			    REMOVEFILTERS(FISCALPERIODFORVARIANT[FISCALPERIOD]),
			    FISCALPERIODFORVARIANT[FISCALPERIOD] < CurrentSelectedFiscalPeriod
			)
			
			RETURN OPENING_BALANCE
			```
		formatString: #,0
		displayFolder: COMPANY_CODE_CURRENCY

	measure AGGR_COMPANY_CODE_CURRENT_PERIOD =
			
			VAR CurrentFP = [SELECTEDFISCALPERIOD]
			RETURN
			CALCULATE(
			    SUM(AGGR_H[AMOUNTINCOMPANYCODECURRENCY]),
			    AGGR_H[FISCALPERIOD] = CurrentFP
			)
		displayFolder: COMPANY_CODE_CURRENCY

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	partition _MEASURES_AGGR_H = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### _MEASURES_GENERAL

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_MEASURES_GENERAL.tmdl). 0 columns; 0 hidden columns; 0 calculated columns; 2 measures; m partition; import mode.

````tmdl
table _MEASURES_GENERAL

	measure SELECTEDFISCALPERIOD = SELECTEDVALUE(FISCALPERIODFORVARIANT[FISCALPERIOD])
		formatString: 0

	measure SELECTEDFISCALYEAR = SELECTEDVALUE(FISCALPERIODFORVARIANT[FISCALYEAR])
		formatString: 0

	partition _MEASURES_GENERAL = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### _PRODUCTGROUP2TEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_PRODUCTGROUP2TEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _PRODUCTGROUP2TEXT

	column FIELD_PARAM_PRODUCTGROUP2TEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_PRODUCTGROUP2TEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_PRODUCTGROUP2TEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_PRODUCTGROUP2TEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_PRODUCTGROUP2TEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_PRODUCTGROUP2TEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_PRODUCTGROUP2TEXT[FIELD_PARAM_PRODUCTGROUP2TEXT Fields], SEARCH("[", _PRODUCTGROUP2TEXT[FIELD_PARAM_PRODUCTGROUP2TEXT Fields])+1, 2)
		isHidden
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _PRODUCTGROUP2TEXT = calculated
		mode: import
		source =
				{
				    ("Product Group 2", NAMEOF('PRODUCTGROUP2TEXT'[DE]), 0),
				    ("Product Group 2", NAMEOF('PRODUCTGROUP2TEXT'[EN]), 1),
				    ("Product Group 2", NAMEOF('PRODUCTGROUP2TEXT'[ES]), 2),
				    ("Product Group 2", NAMEOF('PRODUCTGROUP2TEXT'[FR]), 3)
				}
````

### _PRODUCTTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_PRODUCTTEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _PRODUCTTEXT

	column FIELD_PARAM_PRODUCTTEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_PRODUCTTEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_PRODUCTTEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_PRODUCTTEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_PRODUCTTEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_PRODUCTTEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_PRODUCTTEXT[FIELD_PARAM_PRODUCTTEXT Fields], SEARCH("[", _PRODUCTTEXT[FIELD_PARAM_PRODUCTTEXT Fields])+1, 2)
		isHidden
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _PRODUCTTEXT = calculated
		mode: import
		source =
				{
				    ("Product", NAMEOF('PRODUCTTEXT'[DE]), 0),
				    ("Product", NAMEOF('PRODUCTTEXT'[EN]), 1),
				    ("Product", NAMEOF('PRODUCTTEXT'[ES]), 2),
				    ("Product", NAMEOF('PRODUCTTEXT'[FR]), 3)
				}
````

### _PROFITCENTERTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_PROFITCENTERTEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _PROFITCENTERTEXT

	column FIELD_PARAM_PROFITCENTERTEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_PROFITCENTERTEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_PROFITCENTERTEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_PROFITCENTERTEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_PROFITCENTERTEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_PROFITCENTERTEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_PROFITCENTERTEXT[FIELD_PARAM_PROFITCENTERTEXT Fields], SEARCH("[", _PROFITCENTERTEXT[FIELD_PARAM_PROFITCENTERTEXT Fields])+1, 2)
		isHidden
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _PROFITCENTERTEXT = calculated
		mode: import
		source =
				{
				    ("ProfitCenterText", NAMEOF('PROFITCENTERTEXT'[DE]), 0),
				    ("ProfitCenterText", NAMEOF('PROFITCENTERTEXT'[EN]), 1),
				    ("ProfitCenterText", NAMEOF('PROFITCENTERTEXT'[ES]), 2),
				    ("ProfitCenterText", NAMEOF('PROFITCENTERTEXT'[FR]), 3)
				}
````

### _SEGMENTTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/_SEGMENTTEXT.tmdl). 4 columns; 3 hidden columns; 1 calculated columns; 0 measures; calculated partition; import mode.

````tmdl
table _SEGMENTTEXT

	column FIELD_PARAM_SEGMENTTEXT
		summarizeBy: none
		sourceColumn: [Value1]
		sortByColumn: 'FIELD_PARAM_SEGMENTTEXT Order'

		relatedColumnDetails
			groupByColumn: 'FIELD_PARAM_SEGMENTTEXT Fields'

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_SEGMENTTEXT Fields'
		isHidden
		summarizeBy: none
		sourceColumn: [Value2]
		sortByColumn: 'FIELD_PARAM_SEGMENTTEXT Order'

		extendedProperty ParameterMetadata =
				{
				  "kind": 2,
				  "version": 3
				}

		annotation SummarizationSetBy = Automatic

	column 'FIELD_PARAM_SEGMENTTEXT Order'
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: [Value3]

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage = MID(_SEGMENTTEXT[FIELD_PARAM_SEGMENTTEXT Fields], SEARCH("[", _SEGMENTTEXT[FIELD_PARAM_SEGMENTTEXT Fields])+1, 2)
		isHidden
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition _SEGMENTTEXT = calculated
		mode: import
		source =
				{
				    ("SegmentText", NAMEOF('SEGMENTTEXT'[DE]), 0),
				    ("SegmentText", NAMEOF('SEGMENTTEXT'[EN]), 1),
				    ("SegmentText", NAMEOF('SEGMENTTEXT'[ES]), 2),
				    ("SegmentText", NAMEOF('SEGMENTTEXT'[FR]), 3)
				}
````

### AGGR_H

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/AGGR_H.tmdl). 23 columns; 12 hidden columns; 0 calculated columns; 0 measures; m partition; import mode.

````tmdl
table AGGR_H
	alternateSourcePrecedence: 10

	column _key_IDEBITCREDITCODE
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_IDEBITCREDITCODE

		annotation SummarizationSetBy = Automatic

	column _key_ICOMPANYCODE
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_ICOMPANYCODE

		annotation SummarizationSetBy = Automatic

	column COMPANYCODECURRENCY
		dataType: string
		summarizeBy: none
		sourceColumn: COMPANYCODECURRENCY

		alternateOf
			baseColumn: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY

		annotation SummarizationSetBy = Automatic

	column GLOBALCURRENCY
		dataType: string
		summarizeBy: none
		sourceColumn: GLOBALCURRENCY

		alternateOf
			baseColumn: GLACCOUNTLINEITEMRAWDATA.GLOBALCURRENCY

		annotation SummarizationSetBy = Automatic

	column TRANSACTIONCURRENCY
		dataType: string
		summarizeBy: none
		sourceColumn: TRANSACTIONCURRENCY

		alternateOf
			baseColumn: GLACCOUNTLINEITEMRAWDATA.TRANSACTIONCURRENCY

		annotation SummarizationSetBy = Automatic

	column _key_ILEDGER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_ILEDGER

		annotation SummarizationSetBy = Automatic

	column _key_IPROFITCENTER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_IPROFITCENTER

		annotation SummarizationSetBy = Automatic

	column _key_ICHARTOFACCOUNTS
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_ICHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	column _key_ISEGMENT
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_ISEGMENT

		annotation SummarizationSetBy = Automatic

	column FISCALYEAR
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: FISCALYEAR

		alternateOf
			baseColumn: GLACCOUNTLINEITEMRAWDATA.FISCALYEAR

		annotation SummarizationSetBy = User

	column FISCALPERIOD
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: FISCALPERIOD

		alternateOf
			baseColumn: GLACCOUNTLINEITEMRAWDATA.FISCALPERIOD

		annotation SummarizationSetBy = User

	column AMOUNTINCOMPANYCODECURRENCY
		dataType: decimal
		summarizeBy: none
		sourceColumn: AMOUNTINCOMPANYCODECURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column AMOUNTINGLOBALCURRENCY
		dataType: decimal
		summarizeBy: none
		sourceColumn: AMOUNTINGLOBALCURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column AMOUNTINTRANSACTIONCURRENCY
		dataType: decimal
		summarizeBy: none
		sourceColumn: AMOUNTINTRANSACTIONCURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column _key_IGLACCOUNTINCHARTOFACCOUNTS
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_IGLACCOUNTINCHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	column _key_IPRODUCTGROUP2
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_IPRODUCTGROUP2

		annotation SummarizationSetBy = Automatic

	column _key_IPRODUCT
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_IPRODUCT

		annotation SummarizationSetBy = Automatic

	column _key_ICUSTOMER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_ICUSTOMER

		annotation SummarizationSetBy = Automatic

	column PARTNERCOMPANYCODE
		dataType: string
		summarizeBy: none
		sourceColumn: PARTNERCOMPANYCODE

		annotation SummarizationSetBy = Automatic

	column TAXCODE
		dataType: string
		summarizeBy: none
		sourceColumn: TAXCODE

		annotation SummarizationSetBy = Automatic

	column TAXCOUNTRY
		dataType: string
		summarizeBy: none
		sourceColumn: TAXCOUNTRY

		annotation SummarizationSetBy = Automatic

	column _key_ICOSTCENTER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _key_ICOSTCENTER

		annotation SummarizationSetBy = Automatic

	column _key_IFISCALPERIODFORVARIANT
		dataType: int64
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: _key_IFISCALPERIODFORVARIANT

		annotation SummarizationSetBy = Automatic

	partition AGGR_H-bc5ecb7e-3e0e-43d9-b993-8916c01ed7f0 = m
		mode: import
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vGLACCOUNTLINEITEMRAWDATA_AGGR = Source{[Schema=Schema_Name,Item="vGLACCOUNTLINEITEMRAWDATA_AGGR"]}[Data]
				in
				    dmgold_vGLACCOUNTLINEITEMRAWDATA_AGGR

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### CHARTOFACCOUNTS

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/CHARTOFACCOUNTS.tmdl). 5 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Master table defining the chart of accounts structure
table CHARTOFACCOUNTS

	/// Primary Key for the table.
	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = User

	/// Timestamp indicating last update time in silver lakehouse.
	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	/// Name of the source system.
	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	/// Chart of Accounts.
	column CHARTOFACCOUNTS
		dataType: string
		summarizeBy: none
		sourceColumn: CHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// Maintenance Language for the Chart of Accounts.
	column MAINTENANCELANGUAGE
		dataType: string
		summarizeBy: none
		sourceColumn: MAINTENANCELANGUAGE

		annotation SummarizationSetBy = Automatic

	partition CHARTOFACCOUNTS-d5d0986b-18cf-46a1-a4fb-eb88d5e7d9ce = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_I_CHARTOFACCOUNTS = Source{[Schema=Schema_Name,Item="I_CHARTOFACCOUNTS"]}[Data],
				  #"Choose columns" = Table.SelectColumns(dmgold_I_CHARTOFACCOUNTS, {"CHARTOFACCOUNTS", "MAINTENANCELANGUAGE", "_UpdateTimeStamp", "_SystemName", "Key"})
				in
				    #"Choose columns"

	annotation PBI_ResultType = Table
````

### CHARTOFACCOUNTSTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/CHARTOFACCOUNTSTEXT.tmdl). 41 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for chart of accounts entries
table CHARTOFACCOUNTSTEXT

	column Key
		dataType: int64
		isHidden
		formatString: 0
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column CHARTOFACCOUNTS
		dataType: string
		summarizeBy: none
		sourceColumn: CHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	column ZH
		dataType: string
		summarizeBy: none
		sourceColumn: ZH

		annotation SummarizationSetBy = Automatic

	column TH
		dataType: string
		summarizeBy: none
		sourceColumn: TH

		annotation SummarizationSetBy = Automatic

	column KO
		dataType: string
		summarizeBy: none
		sourceColumn: KO

		annotation SummarizationSetBy = Automatic

	column RO
		dataType: string
		summarizeBy: none
		sourceColumn: RO

		annotation SummarizationSetBy = Automatic

	column SL
		dataType: string
		summarizeBy: none
		sourceColumn: SL

		annotation SummarizationSetBy = Automatic

	column HR
		dataType: string
		summarizeBy: none
		sourceColumn: HR

		annotation SummarizationSetBy = Automatic

	column UK
		dataType: string
		summarizeBy: none
		sourceColumn: UK

		annotation SummarizationSetBy = Automatic

	column ET
		dataType: string
		summarizeBy: none
		sourceColumn: ET

		annotation SummarizationSetBy = Automatic

	column AR
		dataType: string
		summarizeBy: none
		sourceColumn: AR

		annotation SummarizationSetBy = Automatic

	column HE
		dataType: string
		summarizeBy: none
		sourceColumn: HE

		annotation SummarizationSetBy = Automatic

	column CA
		dataType: string
		summarizeBy: none
		sourceColumn: CA

		annotation SummarizationSetBy = Automatic

	column CS
		dataType: string
		summarizeBy: none
		sourceColumn: CS

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column SH
		dataType: string
		summarizeBy: none
		sourceColumn: SH

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column EL
		dataType: string
		summarizeBy: none
		sourceColumn: EL

		annotation SummarizationSetBy = Automatic

	column HU
		dataType: string
		summarizeBy: none
		sourceColumn: HU

		annotation SummarizationSetBy = Automatic

	column IT
		dataType: string
		summarizeBy: none
		sourceColumn: IT

		annotation SummarizationSetBy = Automatic

	column JA
		dataType: string
		summarizeBy: none
		sourceColumn: JA

		annotation SummarizationSetBy = Automatic

	column DA
		dataType: string
		summarizeBy: none
		sourceColumn: DA

		annotation SummarizationSetBy = Automatic

	column PL
		dataType: string
		summarizeBy: none
		sourceColumn: PL

		annotation SummarizationSetBy = Automatic

	column ZF
		dataType: string
		summarizeBy: none
		sourceColumn: ZF

		annotation SummarizationSetBy = Automatic

	column NL
		dataType: string
		summarizeBy: none
		sourceColumn: NL

		annotation SummarizationSetBy = Automatic

	column NO
		dataType: string
		summarizeBy: none
		sourceColumn: NO

		annotation SummarizationSetBy = Automatic

	column PT
		dataType: string
		summarizeBy: none
		sourceColumn: PT

		annotation SummarizationSetBy = Automatic

	column SK
		dataType: string
		summarizeBy: none
		sourceColumn: SK

		annotation SummarizationSetBy = Automatic

	column RU
		dataType: string
		summarizeBy: none
		sourceColumn: RU

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	column TR
		dataType: string
		summarizeBy: none
		sourceColumn: TR

		annotation SummarizationSetBy = Automatic

	column FI
		dataType: string
		summarizeBy: none
		sourceColumn: FI

		annotation SummarizationSetBy = Automatic

	column SV
		dataType: string
		summarizeBy: none
		sourceColumn: SV

		annotation SummarizationSetBy = Automatic

	column BG
		dataType: string
		summarizeBy: none
		sourceColumn: BG

		annotation SummarizationSetBy = Automatic

	column LT
		dataType: string
		summarizeBy: none
		sourceColumn: LT

		annotation SummarizationSetBy = Automatic

	column LV
		dataType: string
		summarizeBy: none
		sourceColumn: LV

		annotation SummarizationSetBy = Automatic

	column HI
		dataType: string
		summarizeBy: none
		sourceColumn: HI

		annotation SummarizationSetBy = Automatic

	column KK
		dataType: string
		summarizeBy: none
		sourceColumn: KK

		annotation SummarizationSetBy = Automatic

	column VI
		dataType: string
		summarizeBy: none
		sourceColumn: VI

		annotation SummarizationSetBy = Automatic

	partition CHARTOFACCOUNTSTEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwCHARTOFACCOUNTSTEXT = Source{[Schema=Schema_Name,Item="vtCHARTOFACCOUNTSTEXT"]}[Data]
				in
				    dmgold_vwCHARTOFACCOUNTSTEXT

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### COMPANYCODE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/COMPANYCODE.tmdl). 25 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Company code dimension with organizational unit details
table COMPANYCODE

	/// Primary Key for the table.
	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	/// Timestamp indicating last update time in silver lakehouse.
	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	/// Name of the source system.
	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	/// Address.
	column ADDRESSID
		dataType: string
		summarizeBy: none
		sourceColumn: ADDRESSID

		annotation SummarizationSetBy = Automatic

	/// Indicator: Discount base amount is the net value.
	column CASHDISCOUNTBASEAMTISNETAMT
		dataType: string
		summarizeBy: none
		sourceColumn: CASHDISCOUNTBASEAMTISNETAMT

		annotation SummarizationSetBy = Automatic

	/// Chart of Accounts.
	column CHARTOFACCOUNTS
		dataType: string
		summarizeBy: none
		sourceColumn: CHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// City.
	column CITYNAME
		dataType: string
		summarizeBy: none
		sourceColumn: CITYNAME

		annotation SummarizationSetBy = Automatic

	/// Company.
	column COMPANY
		dataType: string
		summarizeBy: none
		sourceColumn: COMPANY

		annotation SummarizationSetBy = Automatic

	/// Company Code.
	column COMPANYCODE
		dataType: string
		summarizeBy: none
		sourceColumn: COMPANYCODE

		annotation SummarizationSetBy = Automatic

	/// Name of Company Code or Company.
	column COMPANYCODENAME
		dataType: string
		summarizeBy: none
		sourceColumn: COMPANYCODENAME

		annotation SummarizationSetBy = Automatic

	/// Controlling Area.
	column CONTROLLINGAREA
		dataType: string
		summarizeBy: none
		sourceColumn: CONTROLLINGAREA

		annotation SummarizationSetBy = Automatic

	/// Country/Region Key.
	column COUNTRY
		dataType: string
		summarizeBy: none
		sourceColumn: COUNTRY

		annotation SummarizationSetBy = Automatic

	/// Alternative Chart of Accounts.
	column COUNTRYCHARTOFACCOUNTS
		dataType: string
		summarizeBy: none
		sourceColumn: COUNTRYCHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	column CREDITCONTROLAREA
		dataType: string
		summarizeBy: none
		sourceColumn: CREDITCONTROLAREA

		annotation SummarizationSetBy = Automatic

	/// Currency Key.
	column CURRENCY
		dataType: string
		summarizeBy: none
		sourceColumn: CURRENCY

		annotation SummarizationSetBy = Automatic

	/// Indicator: Document Date As the Basis for Tax Determination.
	column DOCDATEISUSEDFORTAXDETN
		dataType: string
		summarizeBy: none
		sourceColumn: DOCDATEISUSEDFORTAXDETN

		annotation SummarizationSetBy = Automatic

	/// Indicator: Extended Withholding Tax Active.
	column EXTENDEDWHLDGTAXISACTIVE
		dataType: string
		summarizeBy: none
		sourceColumn: EXTENDEDWHLDGTAXISACTIVE

		annotation SummarizationSetBy = Automatic

	/// Field Status Variant.
	column FIELDSTATUSVARIANT
		dataType: string
		summarizeBy: none
		sourceColumn: FIELDSTATUSVARIANT

		annotation SummarizationSetBy = Automatic

	/// Financial Management Area.
	column FINANCIALMANAGEMENTAREA
		dataType: string
		summarizeBy: none
		sourceColumn: FINANCIALMANAGEMENTAREA

		annotation SummarizationSetBy = Automatic

	/// Fiscal Year Variant.
	column FISCALYEARVARIANT
		dataType: string
		summarizeBy: none
		sourceColumn: FISCALYEARVARIANT

		annotation SummarizationSetBy = Automatic

	/// Language Key.
	column LANGUAGE
		dataType: string
		summarizeBy: none
		sourceColumn: LANGUAGE

		annotation SummarizationSetBy = Automatic

	/// Output Tax Code for Non-Taxable Transactions.
	column NONTAXABLETRANSACTIONTAXCODE
		dataType: string
		summarizeBy: none
		sourceColumn: NONTAXABLETRANSACTIONTAXCODE

		annotation SummarizationSetBy = Automatic

	/// Taxes on Sales/Purchases Group.
	column TAXABLEENTITY
		dataType: string
		summarizeBy: none
		sourceColumn: TAXABLEENTITY

		annotation SummarizationSetBy = Automatic

	/// Tax Reporting Date Active in Documents.
	column TAXRPTGDATEISACTIVE
		dataType: string
		summarizeBy: none
		sourceColumn: TAXRPTGDATEISACTIVE

		annotation SummarizationSetBy = Automatic

	/// VAT Registration Number.
	column VATREGISTRATION
		dataType: string
		summarizeBy: none
		sourceColumn: VATREGISTRATION

		annotation SummarizationSetBy = Automatic

	partition COMPANYCODE-66f952d6-2ccf-4469-b2a8-7ced999f9ea1 = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_I_COMPANYCODE = Source{[Schema=Schema_Name,Item="I_COMPANYCODE"]}[Data]
				in
				    dmgold_I_COMPANYCODE

	annotation PBI_ResultType = Table
````

### COSTCENTER

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/COSTCENTER.tmdl). 13 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Cost center dimension for expense tracking and control
table COSTCENTER

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		sourceProviderType: datetime2
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column COMPANYCODE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: COMPANYCODE

		annotation SummarizationSetBy = Automatic

	column CONTROLLINGAREA
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CONTROLLINGAREA

		annotation SummarizationSetBy = Automatic

	column COSTCENTER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: COSTCENTER

		annotation SummarizationSetBy = Automatic

	column COSTCENTERCATEGORY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: COSTCENTERCATEGORY

		annotation SummarizationSetBy = Automatic

	column COSTCENTERCURRENCY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: COSTCENTERCURRENCY

		annotation SummarizationSetBy = Automatic

	column COSTCENTERSTANDARDHIERAREA
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: COSTCENTERSTANDARDHIERAREA

		annotation SummarizationSetBy = Automatic

	column LANGUAGE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: LANGUAGE

		annotation SummarizationSetBy = Automatic

	column PLANT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PLANT

		annotation SummarizationSetBy = Automatic

	column VALIDITYENDDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: VALIDITYENDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column VALIDITYSTARTDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: VALIDITYSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	partition COSTCENTER = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dbo_vCOSTCENTER = Source{[Schema=Schema_Name,Item="vCOSTCENTER"]}[Data],
				  #"Choose columns" = Table.SelectColumns(dbo_vCOSTCENTER, {"Key", "_UpdateTimeStamp", "_SystemName", "COMPANYCODE", "CONTROLLINGAREA", "COSTCENTER", "COSTCENTERCATEGORY", "COSTCENTERCURRENCY", "COSTCENTERSTANDARDHIERAREA", "LANGUAGE", "PLANT", "VALIDITYENDDATE", "VALIDITYSTARTDATE"})
				in
				    #"Choose columns"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### COSTCENTERTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/COSTCENTERTEXT.tmdl). 8 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for cost center entries
table COSTCENTERTEXT

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column CONTROLLINGAREA
		dataType: string
		summarizeBy: none
		sourceColumn: CONTROLLINGAREA

		annotation SummarizationSetBy = Automatic

	column COSTCENTER
		dataType: string
		summarizeBy: none
		sourceColumn: COSTCENTER

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	partition COSTCENTERTEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwCOSTCENTERTEXT = Source{[Schema=Schema_Name,Item="vtCOSTCENTERTEXT"]}[Data],
				    #"Columns removed by Measure Killer"= Table.RemoveColumns(dmgold_vwCOSTCENTERTEXT,{"RU","ZH","RO","LV","PL","KK","LT","SV","ET","AR","HU","NL","TH","HI","DA","HR","JA","TR","NO","PT","EL","KO","ZF","IT","BG","CS","VI","HE","SL","UK","SK","FI","SH","CA"})
				in
				    #"Columns removed by Measure Killer"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### CUSTOMER

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/CUSTOMER.tmdl). 116 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Customer dimension with customer attributes and classifications
table CUSTOMER

	/// Primary Key for the table.
	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	/// Timestamp indicating last update time in silver lakehouse.
	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		sourceProviderType: datetime2
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	/// Name of the source system.
	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: nvarchar(4000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	/// Address.
	column ADDRESSID
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: ADDRESSID

		annotation SummarizationSetBy = Automatic

	/// Indicator: Is an alternative payer allowed in document?.
	column ALTERNATIVEPAYEEISALLOWED
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ALTERNATIVEPAYEEISALLOWED

		annotation SummarizationSetBy = Automatic

	/// Account Number of an Alternative Payer.
	column ALTERNATIVEPAYERACCOUNT
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: ALTERNATIVEPAYERACCOUNT

		annotation SummarizationSetBy = Automatic

	/// City Code.
	column CITYCODE
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: CITYCODE

		annotation SummarizationSetBy = Automatic

	/// City.
	column CITYNAME
		dataType: string
		sourceProviderType: nvarchar(35)
		summarizeBy: none
		sourceColumn: CITYNAME

		annotation SummarizationSetBy = Automatic

	/// Country/Region Key.
	column COUNTRY
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: COUNTRY

		annotation SummarizationSetBy = Automatic

	/// County Code.
	column COUNTY
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: COUNTY

		annotation SummarizationSetBy = Automatic

	/// Customer Number.
	column CUSTOMER
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: CUSTOMER

		annotation SummarizationSetBy = Automatic

	/// Customer Account Group.
	column CUSTOMERACCOUNTGROUP
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: CUSTOMERACCOUNTGROUP

		annotation SummarizationSetBy = Automatic

	/// Customer Classification.
	column CUSTOMERCLASSIFICATION
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: CUSTOMERCLASSIFICATION

		annotation SummarizationSetBy = Automatic

	/// Group Key.
	column CUSTOMERCORPORATEGROUP
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: CUSTOMERCORPORATEGROUP

		annotation SummarizationSetBy = Automatic

	/// Customer Full Name.
	column CUSTOMERFULLNAME
		dataType: string
		sourceProviderType: nvarchar(220)
		summarizeBy: none
		sourceColumn: CUSTOMERFULLNAME

		annotation SummarizationSetBy = Automatic

	/// Name of Customer.
	column CUSTOMERNAME
		dataType: string
		sourceProviderType: nvarchar(80)
		summarizeBy: none
		sourceColumn: CUSTOMERNAME

		annotation SummarizationSetBy = Automatic

	/// Central delivery block for the customer.
	column DELIVERYISBLOCKED
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: DELIVERYISBLOCKED

		annotation SummarizationSetBy = Automatic

	/// Industry Key.
	column INDUSTRY
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: INDUSTRY

		annotation SummarizationSetBy = Automatic

	/// Type of Industry.
	column INDUSTRYTYPE
		dataType: string
		sourceProviderType: nvarchar(30)
		summarizeBy: none
		sourceColumn: INDUSTRYTYPE

		annotation SummarizationSetBy = Automatic

	/// Business Purpose Completed Flag.
	column ISBUSINESSPURPOSECOMPLETED
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISBUSINESSPURPOSECOMPLETED

		annotation SummarizationSetBy = Automatic

	/// Indicator: Competitor.
	column ISCOMPETITOR
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISCOMPETITOR

		annotation SummarizationSetBy = Automatic

	/// Indicator: Is the Account a One-Time Account?.
	column ISONETIMEACCOUNT
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISONETIMEACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Language Key.
	column LANGUAGE
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: LANGUAGE

		annotation SummarizationSetBy = Automatic

	/// Central Order Block for Customer.
	column ORDERISBLOCKEDFORCUSTOMER
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: ORDERISBLOCKEDFORCUSTOMER

		annotation SummarizationSetBy = Automatic

	/// Payment Reason.
	column PAYMENTREASON
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: PAYMENTREASON

		annotation SummarizationSetBy = Automatic

	/// Postal Code.
	column POSTALCODE
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: POSTALCODE

		annotation SummarizationSetBy = Automatic

	/// Central Posting Block.
	column POSTINGISBLOCKED
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: POSTINGISBLOCKED

		annotation SummarizationSetBy = Automatic

	/// Region (State, Province, County).
	column REGION
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: REGION

		annotation SummarizationSetBy = Automatic

	/// Street and House Number.
	column STREETNAME
		dataType: string
		sourceProviderType: nvarchar(35)
		summarizeBy: none
		sourceColumn: STREETNAME

		annotation SummarizationSetBy = Automatic

	/// Account Number of Supplier.
	column SUPPLIER
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: SUPPLIER

		annotation SummarizationSetBy = Automatic

	/// Name of Representative.
	column TAXINVOICEREPRESENTATIVENAME
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: TAXINVOICEREPRESENTATIVENAME

		annotation SummarizationSetBy = Automatic

	/// Tax Jurisdiction.
	column TAXJURISDICTION
		dataType: string
		sourceProviderType: nvarchar(15)
		summarizeBy: none
		sourceColumn: TAXJURISDICTION

		annotation SummarizationSetBy = Automatic

	/// Tax Number Type.
	column TAXNUMBERTYPE
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: TAXNUMBERTYPE

		annotation SummarizationSetBy = Automatic

	/// First telephone number.
	column TELEPHONENUMBER1
		dataType: string
		sourceProviderType: nvarchar(16)
		summarizeBy: none
		sourceColumn: TELEPHONENUMBER1

		annotation SummarizationSetBy = Automatic

	/// Second telephone number.
	column TELEPHONENUMBER2
		dataType: string
		sourceProviderType: nvarchar(16)
		summarizeBy: none
		sourceColumn: TELEPHONENUMBER2

		annotation SummarizationSetBy = Automatic

	/// Company ID of Trading Partner.
	column TRADINGPARTNER
		dataType: string
		sourceProviderType: nvarchar(6)
		summarizeBy: none
		sourceColumn: TRADINGPARTNER

		annotation SummarizationSetBy = Automatic

	/// Train station.
	column TRAINSTATIONNAME
		dataType: string
		sourceProviderType: nvarchar(25)
		summarizeBy: none
		sourceColumn: TRAINSTATIONNAME

		annotation SummarizationSetBy = Automatic

	/// Consolidated Invoicing for Taiwan.
	column TW_COLLVBILLINGISSUPPORTED
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: TW_COLLVBILLINGISSUPPORTED

		annotation SummarizationSetBy = Automatic

	/// Liable for VAT.
	column VATLIABILITY
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: VATLIABILITY

		annotation SummarizationSetBy = Automatic

	/// VAT Registration Number.
	column VATREGISTRATION
		dataType: string
		sourceProviderType: nvarchar(20)
		summarizeBy: none
		sourceColumn: VATREGISTRATION

		annotation SummarizationSetBy = Automatic

	column BILLINGISBLOCKEDFORCUSTOMER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BILLINGISBLOCKEDFORCUSTOMER

		annotation SummarizationSetBy = Automatic

	column NIELSENREGION
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: NIELSENREGION

		annotation SummarizationSetBy = Automatic

	column PAYMENTISBLOCKEDFORCUSTOMER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PAYMENTISBLOCKEDFORCUSTOMER

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLERSET
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLERSET

		annotation SummarizationSetBy = Automatic

	column DISTRICTNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DISTRICTNAME

		annotation SummarizationSetBy = Automatic

	column BPCUSTOMERNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BPCUSTOMERNAME

		annotation SummarizationSetBy = Automatic

	column BPCUSTOMERFULLNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BPCUSTOMERFULLNAME

		annotation SummarizationSetBy = Automatic

	column CREATEDBYUSER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CREATEDBYUSER

		annotation SummarizationSetBy = Automatic

	column CREATIONDATE
		dataType: dateTime
		formatString: Long Date
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: CREATIONDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column AUTHORIZATIONGROUP
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: AUTHORIZATIONGROUP

		annotation SummarizationSetBy = Automatic

	column INTERNATIONALLOCATIONNUMBER1
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: INTERNATIONALLOCATIONNUMBER1

		annotation SummarizationSetBy = Automatic

	column TAXNUMBER1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TAXNUMBER1

		annotation SummarizationSetBy = Automatic

	column TAXNUMBER2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TAXNUMBER2

		annotation SummarizationSetBy = Automatic

	column TAXNUMBER3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TAXNUMBER3

		annotation SummarizationSetBy = Automatic

	column TAXNUMBER4
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TAXNUMBER4

		annotation SummarizationSetBy = Automatic

	column TAXNUMBER5
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TAXNUMBER5

		annotation SummarizationSetBy = Automatic

	column TAXNUMBER6
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TAXNUMBER6

		annotation SummarizationSetBy = Automatic

	column INDUSTRYCODE1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: INDUSTRYCODE1

		annotation SummarizationSetBy = Automatic

	column INDUSTRYCODE2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: INDUSTRYCODE2

		annotation SummarizationSetBy = Automatic

	column INDUSTRYCODE3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: INDUSTRYCODE3

		annotation SummarizationSetBy = Automatic

	column INDUSTRYCODE4
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: INDUSTRYCODE4

		annotation SummarizationSetBy = Automatic

	column INDUSTRYCODE5
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: INDUSTRYCODE5

		annotation SummarizationSetBy = Automatic

	column ORGANIZATIONBPNAME1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ORGANIZATIONBPNAME1

		annotation SummarizationSetBy = Automatic

	column ORGANIZATIONBPNAME2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ORGANIZATIONBPNAME2

		annotation SummarizationSetBy = Automatic

	column SORTFIELD
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SORTFIELD

		annotation SummarizationSetBy = Automatic

	column FAXNUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FAXNUMBER

		annotation SummarizationSetBy = Automatic

	column BR_SUFRAMACODE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BR_SUFRAMACODE

		annotation SummarizationSetBy = Automatic

	column DATAMEDIUMEXCHANGEINDICATOR
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATAMEDIUMEXCHANGEINDICATOR

		annotation SummarizationSetBy = Automatic

	column RESPONSIBLETYPE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: RESPONSIBLETYPE

		annotation SummarizationSetBy = Automatic

	column FISCALADDRESS
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FISCALADDRESS

		annotation SummarizationSetBy = Automatic

	column NFPARTNERISNATURALPERSON
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: NFPARTNERISNATURALPERSON

		annotation SummarizationSetBy = Automatic

	column DELETIONINDICATOR
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DELETIONINDICATOR

		annotation SummarizationSetBy = Automatic

	column DELIVERYDATETYPERULE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DELIVERYDATETYPERULE

		annotation SummarizationSetBy = Automatic

	column EXPRESSTRAINSTATIONNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: EXPRESSTRAINSTATIONNAME

		annotation SummarizationSetBy = Automatic

	column INTERNATIONALLOCATIONNUMBER2
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: INTERNATIONALLOCATIONNUMBER2

		annotation SummarizationSetBy = Automatic

	column INTERNATIONALLOCATIONNUMBER3
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: INTERNATIONALLOCATIONNUMBER3

		annotation SummarizationSetBy = Automatic

	column CUSTOMERHASUNLOADINGPOINT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CUSTOMERHASUNLOADINGPOINT

		annotation SummarizationSetBy = Automatic

	column CUSTOMERWORKINGTIMECALENDAR
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CUSTOMERWORKINGTIMECALENDAR

		annotation SummarizationSetBy = Automatic

	column BUSINESSTYPE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BUSINESSTYPE

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE01
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE01

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE02
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE02

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE03
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE03

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE04
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE04

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE05
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE05

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE06
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE06

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE07
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE07

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE08
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE08

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE09
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE09

		annotation SummarizationSetBy = Automatic

	column FREEDEFINEDATTRIBUTE10
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FREEDEFINEDATTRIBUTE10

		annotation SummarizationSetBy = Automatic

	column CUSTOMERCONDITIONGROUP1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CUSTOMERCONDITIONGROUP1

		annotation SummarizationSetBy = Automatic

	column CUSTOMERCONDITIONGROUP2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CUSTOMERCONDITIONGROUP2

		annotation SummarizationSetBy = Automatic

	column CUSTOMERCONDITIONGROUP3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CUSTOMERCONDITIONGROUP3

		annotation SummarizationSetBy = Automatic

	column CUSTOMERCONDITIONGROUP4
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CUSTOMERCONDITIONGROUP4

		annotation SummarizationSetBy = Automatic

	column CUSTOMERCONDITIONGROUP5
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CUSTOMERCONDITIONGROUP5

		annotation SummarizationSetBy = Automatic

	column ISSALESPROSPECT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ISSALESPROSPECT

		annotation SummarizationSetBy = Automatic

	column ISCONSUMER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ISCONSUMER

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER1

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER2

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER3

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER4
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER4

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER5
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER5

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER6
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER6

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER7
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER7

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER8
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER8

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER9
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER9

		annotation SummarizationSetBy = Automatic

	column DATACONTROLLER10
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DATACONTROLLER10

		annotation SummarizationSetBy = Automatic

	column BUSINESSPARTNERNAME1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BUSINESSPARTNERNAME1

		annotation SummarizationSetBy = Automatic

	column BUSINESSPARTNERNAME2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BUSINESSPARTNERNAME2

		annotation SummarizationSetBy = Automatic

	column BUSINESSPARTNERNAME3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BUSINESSPARTNERNAME3

		annotation SummarizationSetBy = Automatic

	column BUSINESSPARTNERNAME4
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BUSINESSPARTNERNAME4

		annotation SummarizationSetBy = Automatic

	column BPADDRCITYNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BPADDRCITYNAME

		annotation SummarizationSetBy = Automatic

	column BPADDRSTREETNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BPADDRSTREETNAME

		annotation SummarizationSetBy = Automatic

	column ADDRESSSEARCHTERM1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ADDRESSSEARCHTERM1

		annotation SummarizationSetBy = Automatic

	column ADDRESSSEARCHTERM2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ADDRESSSEARCHTERM2

		annotation SummarizationSetBy = Automatic

	column POBOXDEVIATINGCITYNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: POBOXDEVIATINGCITYNAME

		annotation SummarizationSetBy = Automatic

	column BUSINESSPARTNERFORMOFADDRESS
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BUSINESSPARTNERFORMOFADDRESS

		annotation SummarizationSetBy = Automatic

	partition CUSTOMER = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_I_CUSTOMER = Source{[Schema=Schema_Name,Item="I_CUSTOMER"]}[Data]
				in
				    dmgold_I_CUSTOMER

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### DEBITCREDITCODE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/DEBITCREDITCODE.tmdl). 4 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Debit/Credit code dimension for transaction type classification
table DEBITCREDITCODE

	column DEBITCREDITCODE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DEBITCREDITCODE

		annotation SummarizationSetBy = Automatic

	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: General Date
		sourceProviderType: datetime2
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column Key
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	partition DEBITCREDITCODE = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwDEBITCREDITCODETEXT = Source{[Schema=Schema_Name,Item="I_DEBITCREDITCODE"]}[Data]
				in
				    dmgold_vwDEBITCREDITCODETEXT

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Table
````

### DEBITCREDITCODETEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/DEBITCREDITCODETEXT.tmdl). 42 columns; 2 hidden columns; 1 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for debit/credit codes
table DEBITCREDITCODETEXT

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column DEBITCREDITCODE
		dataType: string
		summarizeBy: none
		sourceColumn: DEBITCREDITCODE

		annotation SummarizationSetBy = Automatic

	column ZH
		dataType: string
		summarizeBy: none
		sourceColumn: ZH
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column TH
		dataType: string
		summarizeBy: none
		sourceColumn: TH
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column KO
		dataType: string
		summarizeBy: none
		sourceColumn: KO
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column RO
		dataType: string
		summarizeBy: none
		sourceColumn: RO
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column SL
		dataType: string
		summarizeBy: none
		sourceColumn: SL
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column HR
		dataType: string
		summarizeBy: none
		sourceColumn: HR
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column UK
		dataType: string
		summarizeBy: none
		sourceColumn: UK
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column ET
		dataType: string
		summarizeBy: none
		sourceColumn: ET
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column AR
		dataType: string
		summarizeBy: none
		sourceColumn: AR
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column HE
		dataType: string
		summarizeBy: none
		sourceColumn: HE
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column CA
		dataType: string
		summarizeBy: none
		sourceColumn: CA
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column CS
		dataType: string
		summarizeBy: none
		sourceColumn: CS
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		summarizeBy: none
		sourceColumn: DE
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column SH
		dataType: string
		summarizeBy: none
		sourceColumn: SH
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		summarizeBy: none
		sourceColumn: EN
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		summarizeBy: none
		sourceColumn: FR
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column EL
		dataType: string
		summarizeBy: none
		sourceColumn: EL
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column HU
		dataType: string
		summarizeBy: none
		sourceColumn: HU
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column IT
		dataType: string
		summarizeBy: none
		sourceColumn: IT
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column JA
		dataType: string
		summarizeBy: none
		sourceColumn: JA
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column DA
		dataType: string
		summarizeBy: none
		sourceColumn: DA
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column PL
		dataType: string
		summarizeBy: none
		sourceColumn: PL
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column ZF
		dataType: string
		summarizeBy: none
		sourceColumn: ZF
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column NL
		dataType: string
		summarizeBy: none
		sourceColumn: NL
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column NO
		dataType: string
		summarizeBy: none
		sourceColumn: NO
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column PT
		dataType: string
		summarizeBy: none
		sourceColumn: PT
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column SK
		dataType: string
		summarizeBy: none
		sourceColumn: SK
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column RU
		dataType: string
		summarizeBy: none
		sourceColumn: RU
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		summarizeBy: none
		sourceColumn: ES
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column TR
		dataType: string
		summarizeBy: none
		sourceColumn: TR
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column FI
		dataType: string
		summarizeBy: none
		sourceColumn: FI
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column SV
		dataType: string
		summarizeBy: none
		sourceColumn: SV
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column BG
		dataType: string
		summarizeBy: none
		sourceColumn: BG
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column LT
		dataType: string
		summarizeBy: none
		sourceColumn: LT
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column LV
		dataType: string
		summarizeBy: none
		sourceColumn: LV
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column HI
		dataType: string
		summarizeBy: none
		sourceColumn: HI
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column KK
		dataType: string
		summarizeBy: none
		sourceColumn: KK
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column VI
		dataType: string
		summarizeBy: none
		sourceColumn: VI
		sortByColumn: SortOrder

		annotation SummarizationSetBy = Automatic

	column SortOrder = IF(DEBITCREDITCODETEXT[Key] = 1, 2, 1)
		formatString: 0
		summarizeBy: none

		annotation SummarizationSetBy = Automatic

	partition DEBITCREDITCODETEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwDEBITCREDITCODETEXT = Source{[Schema=Schema_Name,Item="vtDEBITCREDITCODETEXT"]}[Data]
				in
				    dmgold_vwDEBITCREDITCODETEXT

	annotation PBI_ResultType = Table
````

### FISCALPERIODFORVARIANT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/FISCALPERIODFORVARIANT.tmdl). 14 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Fiscal period variant mapping for different accounting calendars
table FISCALPERIODFORVARIANT

	column FISCALYEARVARIANT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FISCALYEARVARIANT

		annotation SummarizationSetBy = Automatic

	column FISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: FISCALYEAR

		annotation SummarizationSetBy = Automatic

	column FISCALPERIOD
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: FISCALPERIOD

		annotation SummarizationSetBy = Automatic

	column FISCALPERIODSTARTDATE
		dataType: dateTime
		formatString: Long Date
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: FISCALPERIODSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column FISCALPERIODENDDATE
		dataType: dateTime
		formatString: Long Date
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: FISCALPERIODENDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column ISSPECIALPERIOD
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ISSPECIALPERIOD

		annotation SummarizationSetBy = Automatic

	column FISCALYEARSTARTDATE
		dataType: dateTime
		formatString: Long Date
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: FISCALYEARSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column FISCALYEARENDDATE
		dataType: dateTime
		formatString: Long Date
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: FISCALYEARENDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column FISCALYEARPERIOD
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: FISCALYEARPERIOD

		annotation SummarizationSetBy = Automatic

	column NEXTFISCALPERIOD
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: NEXTFISCALPERIOD

		annotation SummarizationSetBy = Automatic

	column NEXTFISCALPERIODFISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: NEXTFISCALPERIODFISCALYEAR

		annotation SummarizationSetBy = Automatic

	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: General Date
		sourceProviderType: datetime2
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	partition FISCALPERIODFORVARIANT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dbo_vCOSTCENTER = Source{[Schema=Schema_Name,Item="I_FISCALPERIODFORVARIANT"]}[Data]
				in
				    dbo_vCOSTCENTER

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Table
````

### GLACCOUNTHIERARCHYWTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTHIERARCHYWTEXT.tmdl). 39 columns; 3 hidden columns; 0 calculated columns; 2 measures; m partition; dual mode.

````tmdl
/// GL Account hierarchy with text descriptions for drill-down reporting
table GLACCOUNTHIERARCHYWTEXT

	measure _CurrentLevel = ```
			SWITCH(
			    TRUE(), 
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL9_TEXT]), 9,
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL8_TEXT]), 8, 
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL7_TEXT]), 7, 
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL6_TEXT]), 6,
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL5_TEXT]), 5,
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL4_TEXT]), 4, 
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL3_TEXT]), 3, 
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL2_TEXT]), 2,
			    ISINSCOPE( GLACCOUNTHIERARCHYWTEXT[GLACCOUNT_HIER_LEVEL1_TEXT]), 1
			    )
			```
		formatString: 0

	measure _Show = IF([_CurrentLevel] <= MIN(GLACCOUNTHIERARCHYWTEXT[MAXHIERARCHYLEVEL]),1)
		formatString: 0

	column GLACCOUNTHIERARCHY
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNTHIERARCHY

		annotation SummarizationSetBy = Automatic

	column CHARTOFACCOUNTS
		dataType: string
		summarizeBy: none
		sourceColumn: CHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	column HIERARCHYVERSION
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: HIERARCHYVERSION

		annotation SummarizationSetBy = Automatic

	/// ISO 639-1 two-letter language code.
	column _ISOLanguage
		dataType: string
		isHidden
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _ISOLanguage

		annotation SummarizationSetBy = Automatic

	/// Source SAP system name.
	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column VALIDITYENDDATE
		dataType: dateTime
		formatString: m/d/yyyy
		summarizeBy: none
		sourceColumn: VALIDITYENDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column VALIDITYSTARTDATE
		dataType: dateTime
		formatString: m/d/yyyy
		summarizeBy: none
		sourceColumn: VALIDITYSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column CHILD
		dataType: string
		summarizeBy: none
		sourceColumn: CHILD

		annotation SummarizationSetBy = Automatic

	column PARENT
		dataType: string
		summarizeBy: none
		sourceColumn: PARENT

		annotation SummarizationSetBy = Automatic

	column LEVEL1
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL1

		annotation SummarizationSetBy = Automatic

	column LEVEL1_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL1_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL2
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL2

		annotation SummarizationSetBy = Automatic

	column LEVEL2_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL2_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL3
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL3

		annotation SummarizationSetBy = Automatic

	column LEVEL3_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL3_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL4
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL4

		annotation SummarizationSetBy = Automatic

	column LEVEL4_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL4_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL5
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL5

		annotation SummarizationSetBy = Automatic

	column LEVEL5_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL5_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL6
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL6

		annotation SummarizationSetBy = Automatic

	column LEVEL6_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL6_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL7
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL7

		annotation SummarizationSetBy = Automatic

	column LEVEL7_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL7_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL8
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL8

		annotation SummarizationSetBy = Automatic

	column LEVEL8_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL8_KEY

		annotation SummarizationSetBy = Automatic

	column LEVEL9
		dataType: string
		summarizeBy: none
		sourceColumn: LEVEL9

		annotation SummarizationSetBy = Automatic

	column LEVEL9_KEY
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: LEVEL9_KEY

		annotation SummarizationSetBy = Automatic

	column HIERARCHYPATH
		dataType: string
		summarizeBy: none
		sourceColumn: HIERARCHYPATH

		annotation SummarizationSetBy = Automatic

	column MAXHIERARCHYLEVEL
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: MAXHIERARCHYLEVEL

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_NODE_KEY
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: GLACCOUNT_NODE_KEY

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL1_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL1_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL2_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL2_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL3_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL3_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL4_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL4_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL5_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL5_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL6_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL6_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL7_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL7_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL8_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL8_TEXT

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT_HIER_LEVEL9_TEXT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT_HIER_LEVEL9_TEXT

		annotation SummarizationSetBy = Automatic

	partition GLACCOUNTHIERARCHYWTEXT-9c5b9fb2-f9b7-4322-a461-5cc5bdebffd9 = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_GLACCOUNTHIERARCHYWTEXT1 = Source{[Schema=Schema_Name,Item="vGLACCOUNTHIERARCHYWTEXT"]}[Data]
				in
				    dmgold_GLACCOUNTHIERARCHYWTEXT1

	annotation PBI_ResultType = Table
````

### GLACCOUNTINCHARTOFACCOUNTS

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTINCHARTOFACCOUNTS.tmdl). 25 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Mapping table linking GL accounts to chart of accounts
table GLACCOUNTINCHARTOFACCOUNTS

	/// Primary Key for the table.
	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = User

	/// Timestamp indicating last update time in silver lakehouse.
	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	/// Name of the source system.
	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	/// Indicator: Account Is Blocked for Creation ?.
	column ACCOUNTISBLOCKEDFORCREATION
		dataType: string
		summarizeBy: none
		sourceColumn: ACCOUNTISBLOCKEDFORCREATION

		annotation SummarizationSetBy = Automatic

	/// Indicator: Account Blocked for Planning ?.
	column ACCOUNTISBLOCKEDFORPLANNING
		dataType: string
		summarizeBy: none
		sourceColumn: ACCOUNTISBLOCKEDFORPLANNING

		annotation SummarizationSetBy = Automatic

	/// Indicator: Is Account Blocked for Posting?.
	column ACCOUNTISBLOCKEDFORPOSTING
		dataType: string
		summarizeBy: none
		sourceColumn: ACCOUNTISBLOCKEDFORPOSTING

		annotation SummarizationSetBy = Automatic

	/// Indicator: Account Marked for Deletion?.
	column ACCOUNTISMARKEDFORDELETION
		dataType: string
		summarizeBy: none
		sourceColumn: ACCOUNTISMARKEDFORDELETION

		annotation SummarizationSetBy = Automatic

	/// Bank Reconciliation Account.
	column BANKRECONCILIATIONACCOUNT
		dataType: string
		summarizeBy: none
		sourceColumn: BANKRECONCILIATIONACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Chart of Accounts.
	column CHARTOFACCOUNTS
		dataType: string
		summarizeBy: none
		sourceColumn: CHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// Group Account Number.
	column CORPORATEGROUPACCOUNT
		dataType: string
		summarizeBy: none
		sourceColumn: CORPORATEGROUPACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Group Chart of Accts.
	column CORPORATEGROUPCHARTOFACCOUNTS
		dataType: string
		summarizeBy: none
		sourceColumn: CORPORATEGROUPCHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// Name of Person who Created the Object.
	column CREATEDBYUSER
		dataType: string
		summarizeBy: none
		sourceColumn: CREATEDBYUSER

		annotation SummarizationSetBy = Automatic

	/// Record Created On.
	column CREATIONDATE
		dataType: dateTime
		formatString: m/d/yyyy
		summarizeBy: none
		sourceColumn: CREATIONDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Functional Area.
	column FUNCTIONALAREA
		dataType: string
		summarizeBy: none
		sourceColumn: FUNCTIONALAREA

		annotation SummarizationSetBy = Automatic

	/// G/L Account Number.
	column GLACCOUNT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT

		annotation SummarizationSetBy = Automatic

	/// G/L Account Number.
	column GLACCOUNTEXTERNAL
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNTEXTERNAL

		annotation SummarizationSetBy = Automatic

	/// G/L Account Group.
	column GLACCOUNTGROUP
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNTGROUP

		annotation SummarizationSetBy = Automatic

	/// Subtype of a GL Account.
	column GLACCOUNTSUBTYPE
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNTSUBTYPE

		annotation SummarizationSetBy = Automatic

	/// Type of a General Ledger Account.
	column GLACCOUNTTYPE
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNTTYPE

		annotation SummarizationSetBy = Automatic

	/// Indicator: Account is a balance sheet account?.
	column ISBALANCESHEETACCOUNT
		dataType: string
		summarizeBy: none
		sourceColumn: ISBALANCESHEETACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Indicator: Account is a balance sheet account?.
	column ISPROFITLOSSACCOUNT
		dataType: string
		summarizeBy: none
		sourceColumn: ISPROFITLOSSACCOUNT

		annotation SummarizationSetBy = Automatic

	/// UTC Time Stamp in Short Form (YYYYMMDDhhmmss).
	column LASTCHANGEDATETIME
		dataType: double
		sourceProviderType: decimal(15, 0)
		summarizeBy: none
		sourceColumn: LASTCHANGEDATETIME

		annotation SummarizationSetBy = User

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Company ID of Trading Partner.
	column PARTNERCOMPANY
		dataType: string
		summarizeBy: none
		sourceColumn: PARTNERCOMPANY

		annotation SummarizationSetBy = Automatic

	/// P&L statement account type.
	column PROFITLOSSACCOUNTTYPE
		dataType: string
		summarizeBy: none
		sourceColumn: PROFITLOSSACCOUNTTYPE

		annotation SummarizationSetBy = Automatic

	/// Number of the Sample Account.
	column SAMPLEGLACCOUNT
		dataType: string
		summarizeBy: none
		sourceColumn: SAMPLEGLACCOUNT

		annotation SummarizationSetBy = Automatic

	partition GLACCOUNTINCHARTOFACCOUNTS-59ea94a8-ffa9-431d-a173-692e0b0dd494 = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_I_GLACCOUNTINCHARTOFACCOUNTS = Source{[Schema=Schema_Name,Item="I_GLACCOUNTINCHARTOFACCOUNTS"]}[Data]
				in
				    dmgold_I_GLACCOUNTINCHARTOFACCOUNTS

	annotation PBI_ResultType = Table
````

### GLACCOUNTINCHARTOFACCOUNTSTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTINCHARTOFACCOUNTSTEXT.tmdl). 41 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for GL accounts in chart of accounts
table GLACCOUNTINCHARTOFACCOUNTSTEXT

	column Key
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column GLACCOUNT
		dataType: string
		summarizeBy: none
		sourceColumn: GLACCOUNT

		annotation SummarizationSetBy = Automatic

	column ZH
		dataType: string
		summarizeBy: none
		sourceColumn: ZH

		annotation SummarizationSetBy = Automatic

	column TH
		dataType: string
		summarizeBy: none
		sourceColumn: TH

		annotation SummarizationSetBy = Automatic

	column KO
		dataType: string
		summarizeBy: none
		sourceColumn: KO

		annotation SummarizationSetBy = Automatic

	column RO
		dataType: string
		summarizeBy: none
		sourceColumn: RO

		annotation SummarizationSetBy = Automatic

	column SL
		dataType: string
		summarizeBy: none
		sourceColumn: SL

		annotation SummarizationSetBy = Automatic

	column HR
		dataType: string
		summarizeBy: none
		sourceColumn: HR

		annotation SummarizationSetBy = Automatic

	column UK
		dataType: string
		summarizeBy: none
		sourceColumn: UK

		annotation SummarizationSetBy = Automatic

	column ET
		dataType: string
		summarizeBy: none
		sourceColumn: ET

		annotation SummarizationSetBy = Automatic

	column AR
		dataType: string
		summarizeBy: none
		sourceColumn: AR

		annotation SummarizationSetBy = Automatic

	column HE
		dataType: string
		summarizeBy: none
		sourceColumn: HE

		annotation SummarizationSetBy = Automatic

	column CA
		dataType: string
		summarizeBy: none
		sourceColumn: CA

		annotation SummarizationSetBy = Automatic

	column CS
		dataType: string
		summarizeBy: none
		sourceColumn: CS

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column SH
		dataType: string
		summarizeBy: none
		sourceColumn: SH

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column EL
		dataType: string
		summarizeBy: none
		sourceColumn: EL

		annotation SummarizationSetBy = Automatic

	column HU
		dataType: string
		summarizeBy: none
		sourceColumn: HU

		annotation SummarizationSetBy = Automatic

	column IT
		dataType: string
		summarizeBy: none
		sourceColumn: IT

		annotation SummarizationSetBy = Automatic

	column JA
		dataType: string
		summarizeBy: none
		sourceColumn: JA

		annotation SummarizationSetBy = Automatic

	column DA
		dataType: string
		summarizeBy: none
		sourceColumn: DA

		annotation SummarizationSetBy = Automatic

	column PL
		dataType: string
		summarizeBy: none
		sourceColumn: PL

		annotation SummarizationSetBy = Automatic

	column ZF
		dataType: string
		summarizeBy: none
		sourceColumn: ZF

		annotation SummarizationSetBy = Automatic

	column NL
		dataType: string
		summarizeBy: none
		sourceColumn: NL

		annotation SummarizationSetBy = Automatic

	column NO
		dataType: string
		summarizeBy: none
		sourceColumn: NO

		annotation SummarizationSetBy = Automatic

	column PT
		dataType: string
		summarizeBy: none
		sourceColumn: PT

		annotation SummarizationSetBy = Automatic

	column SK
		dataType: string
		summarizeBy: none
		sourceColumn: SK

		annotation SummarizationSetBy = Automatic

	column RU
		dataType: string
		summarizeBy: none
		sourceColumn: RU

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	column TR
		dataType: string
		summarizeBy: none
		sourceColumn: TR

		annotation SummarizationSetBy = Automatic

	column FI
		dataType: string
		summarizeBy: none
		sourceColumn: FI

		annotation SummarizationSetBy = Automatic

	column SV
		dataType: string
		summarizeBy: none
		sourceColumn: SV

		annotation SummarizationSetBy = Automatic

	column BG
		dataType: string
		summarizeBy: none
		sourceColumn: BG

		annotation SummarizationSetBy = Automatic

	column LT
		dataType: string
		summarizeBy: none
		sourceColumn: LT

		annotation SummarizationSetBy = Automatic

	column LV
		dataType: string
		summarizeBy: none
		sourceColumn: LV

		annotation SummarizationSetBy = Automatic

	column HI
		dataType: string
		summarizeBy: none
		sourceColumn: HI

		annotation SummarizationSetBy = Automatic

	column KK
		dataType: string
		summarizeBy: none
		sourceColumn: KK

		annotation SummarizationSetBy = Automatic

	column VI
		dataType: string
		summarizeBy: none
		sourceColumn: VI

		annotation SummarizationSetBy = Automatic

	partition GLACCOUNTINCHARTOFACCOUNTSTEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwGLACCOUNTINCHARTOFACCOUNTSTEXT = Source{[Schema=Schema_Name,Item="vtGLACCOUNTINCHARTOFACCOUNTSTEXT"]}[Data]
				in
				    dmgold_vwGLACCOUNTINCHARTOFACCOUNTSTEXT

	annotation PBI_ResultType = Table
````

### GLACCOUNTLINEITEMRAWDATA

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/GLACCOUNTLINEITEMRAWDATA.tmdl). 428 columns; 32 hidden columns; 0 calculated columns; 0 measures; m partition; directQuery mode.

````tmdl
/// Main fact table containing raw GL account line item transactions with amounts, dates, and dimensional attributes
table GLACCOUNTLINEITEMRAWDATA

	column _key_ICONTROLLINGAREA
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ICONTROLLINGAREA

		annotation SummarizationSetBy = User

	column _key_ICUSTOMER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ICUSTOMER

		annotation SummarizationSetBy = User

	column _key_IPRODUCTGROUP2
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IPRODUCTGROUP2

		annotation SummarizationSetBy = User

	column _key_ISUPPLIER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ISUPPLIER

		annotation SummarizationSetBy = User

	column _key_IPRODUCT
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IPRODUCT

		annotation SummarizationSetBy = User

	column _key_IPLANT
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IPLANT

		annotation SummarizationSetBy = User

	column _key_IBUSINESSAREA
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IBUSINESSAREA

		annotation SummarizationSetBy = User

	column _key_ICHARTOFACCOUNTS
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ICHARTOFACCOUNTS

		annotation SummarizationSetBy = User

	column _key_IEQUIPMENT
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IEQUIPMENT

		annotation SummarizationSetBy = User

	column _key_IASSETCLASS
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IASSETCLASS

		annotation SummarizationSetBy = User

	column _key_ILEDGER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ILEDGER

		annotation SummarizationSetBy = User

	column _key_IASSETTRANSACTIONTYPE
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IASSETTRANSACTIONTYPE

		annotation SummarizationSetBy = User

	column _key_IFISCALYEARVARIANT
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IFISCALYEARVARIANT

		annotation SummarizationSetBy = User

	column _key_IFISCALYEARFORCOMPANYCODE
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IFISCALYEARFORCOMPANYCODE

		annotation SummarizationSetBy = User

	column _key_IGLOBALCOMPANYCompany
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IGLOBALCOMPANYCompany

		annotation SummarizationSetBy = User

	column _key_IGLOBALCOMPANYPartnerCompany
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IGLOBALCOMPANYPartnerCompany

		annotation SummarizationSetBy = User

	column _key_IACCOUNTINGDOCUMENTTYPE
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IACCOUNTINGDOCUMENTTYPE

		annotation SummarizationSetBy = User

	column _key_IFUNCTIONALAREA
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IFUNCTIONALAREA

		annotation SummarizationSetBy = User

	column _key_ISEGMENT
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ISEGMENT

		annotation SummarizationSetBy = User

	column _key_ICOMPANYCODE
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ICOMPANYCODE

		annotation SummarizationSetBy = User

	column _key_IGLACCOUNTINCHARTOFACCOUNTS
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IGLACCOUNTINCHARTOFACCOUNTS

		annotation SummarizationSetBy = User

	column _key_IDEBITCREDITCODE
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IDEBITCREDITCODE

		annotation SummarizationSetBy = User

	column _key_IPROFITCENTER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IPROFITCENTER

		annotation SummarizationSetBy = User

	column _key_ICOSTCENTER
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ICOSTCENTER

		annotation SummarizationSetBy = User

	column _key_IFUNCTIONALLOCATION
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IFUNCTIONALLOCATION

		annotation SummarizationSetBy = User

	/// Name of the source system.
	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	/// Journal Entry.
	column ACCOUNTINGDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCOUNTINGDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Company Code.
	column COMPANYCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COMPANYCODE

		annotation SummarizationSetBy = Automatic

	/// Fiscal Year.
	column FISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: FISCALYEAR

		annotation SummarizationSetBy = User

	/// Fiscal Year Variant.
	column FISCALYEARVARIANT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FISCALYEARVARIANT

		annotation SummarizationSetBy = Automatic

	/// General Ledger Journal Entry Line Item.
	column LEDGERGLLINEITEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: LEDGERGLLINEITEM

		annotation SummarizationSetBy = Automatic

	/// Source Ledger.
	column SOURCELEDGER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SOURCELEDGER

		annotation SummarizationSetBy = Automatic

	/// Debit/Credit Code.
	column DEBITCREDITCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: DEBITCREDITCODE

		annotation SummarizationSetBy = Automatic

	/// Chart of Accounts.
	column CHARTOFACCOUNTS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// G/L Account.
	column GLACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GLACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Company.
	column COMPANY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COMPANY

		annotation SummarizationSetBy = Automatic

	/// Segment for Segmental Reporting.
	column SEGMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SEGMENT

		annotation SummarizationSetBy = Automatic

	/// Functional Area.
	column FUNCTIONALAREA
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FUNCTIONALAREA

		annotation SummarizationSetBy = Automatic

	/// Journal Entry Type.
	column ACCOUNTINGDOCUMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCOUNTINGDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// WBS Element Internal ID.
	column WBSELEMENTINTERNALID
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: WBSELEMENTINTERNALID

		annotation SummarizationSetBy = Automatic

	/// Fixed Asset.
	column MASTERFIXEDASSET
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MASTERFIXEDASSET

		annotation SummarizationSetBy = Automatic

	/// Asset Transaction Type.
	column ASSETTRANSACTIONTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ASSETTRANSACTIONTYPE

		annotation SummarizationSetBy = Automatic

	/// Asset Subnumber.
	column FIXEDASSET
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FIXEDASSET

		annotation SummarizationSetBy = Automatic

	/// Asset Class.
	column ASSETCLASS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ASSETCLASS

		annotation SummarizationSetBy = Automatic

	/// WBS Element.
	column WBSELEMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: WBSELEMENT

		annotation SummarizationSetBy = Automatic

	/// Equipment Number.
	column EQUIPMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: EQUIPMENT

		annotation SummarizationSetBy = Automatic

	/// Functional Location.
	column FUNCTIONALLOCATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FUNCTIONALLOCATION

		annotation SummarizationSetBy = Automatic

	/// Business Area.
	column BUSINESSAREA
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BUSINESSAREA

		annotation SummarizationSetBy = Automatic

	/// Plant.
	column PLANT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PLANT

		annotation SummarizationSetBy = Automatic

	/// Product Number.
	column PRODUCT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PRODUCT

		annotation SummarizationSetBy = Automatic

	/// Supplier.
	column SUPPLIER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SUPPLIER

		annotation SummarizationSetBy = Automatic

	/// Product Group.
	column PRODUCTGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PRODUCTGROUP

		annotation SummarizationSetBy = Automatic

	/// Customer Number.
	column CUSTOMER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUSTOMER

		annotation SummarizationSetBy = Automatic

	/// Controlling Area.
	column CONTROLLINGAREA
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONTROLLINGAREA

		annotation SummarizationSetBy = Automatic

	/// Base Unit of Measure.
	column BASEUNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BASEUNIT

		annotation SummarizationSetBy = Automatic

	/// Balance Transaction Currency.
	column BALANCETRANSACTIONCURRENCY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BALANCETRANSACTIONCURRENCY

		annotation SummarizationSetBy = Automatic

	/// Transaction Currency.
	column TRANSACTIONCURRENCY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: TRANSACTIONCURRENCY

		annotation SummarizationSetBy = Automatic

	/// Company Code Currency.
	column COMPANYCODECURRENCY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COMPANYCODECURRENCY

		annotation SummarizationSetBy = Automatic

	/// Global Currency.
	column GLOBALCURRENCY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GLOBALCURRENCY

		annotation SummarizationSetBy = Automatic

	/// Functional Currency.
	column FUNCTIONALCURRENCY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FUNCTIONALCURRENCY

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 1.
	column FREEDEFINEDCURRENCY1
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY1

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 2.
	column FREEDEFINEDCURRENCY2
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY2

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 3.
	column FREEDEFINEDCURRENCY3
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY3

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 4.
	column FREEDEFINEDCURRENCY4
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY4

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 5.
	column FREEDEFINEDCURRENCY5
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY5

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 6.
	column FREEDEFINEDCURRENCY6
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY6

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 7.
	column FREEDEFINEDCURRENCY7
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY7

		annotation SummarizationSetBy = Automatic

	/// Freely Defined Currency 8.
	column FREEDEFINEDCURRENCY8
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FREEDEFINEDCURRENCY8

		annotation SummarizationSetBy = Automatic

	/// CO Object Currency.
	column CONTROLLINGOBJECTCURRENCY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONTROLLINGOBJECTCURRENCY

		annotation SummarizationSetBy = Automatic

	/// Grant currency.
	column GRANTCURRENCY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GRANTCURRENCY

		annotation SummarizationSetBy = Automatic

	/// Foreign key reference to the fiscal period for the fiscal year variant.
	column _key_IFISCALPERIODFORVARIANT
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IFISCALPERIODFORVARIANT

		annotation SummarizationSetBy = User

	/// Fiscal Year of Ledger.
	column LEDGERFISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: LEDGERFISCALYEAR

		annotation SummarizationSetBy = Automatic

	/// Record Type.
	column GLRECORDTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GLRECORDTYPE

		annotation SummarizationSetBy = Automatic

	/// Shifted Fiscal Year Consecutive ID.
	column JRNLENTRALTVFYCONSECUTIVEID
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JRNLENTRALTVFYCONSECUTIVEID

		annotation SummarizationSetBy = Automatic

	/// Financial Transaction Type.
	column FINANCIALTRANSACTIONTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FINANCIALTRANSACTIONTYPE

		annotation SummarizationSetBy = Automatic

	/// Transaction Type for General Ledger.
	column GLBUSINESSTRANSACTIONTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GLBUSINESSTRANSACTIONTYPE

		annotation SummarizationSetBy = Automatic

	/// Business Transaction Category.
	column BUSINESSTRANSACTIONCATEGORY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BUSINESSTRANSACTIONCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Business Transaction Type.
	column BUSINESSTRANSACTIONTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BUSINESSTRANSACTIONTYPE

		annotation SummarizationSetBy = Automatic

	/// Financial Closing Step.
	column FINANCIALCLOSINGSTEP
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: FINANCIALCLOSINGSTEP

		annotation SummarizationSetBy = Automatic

	/// CO Business Transaction.
	column CONTROLLINGBUSTRANSACTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONTROLLINGBUSTRANSACTYPE

		annotation SummarizationSetBy = Automatic

	/// Reference Document Type.
	column REFERENCEDOCUMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REFERENCEDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Logical System.
	column LOGICALSYSTEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: LOGICALSYSTEM

		annotation SummarizationSetBy = Automatic

	/// Reference Document Context.
	column REFERENCEDOCUMENTCONTEXT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REFERENCEDOCUMENTCONTEXT

		annotation SummarizationSetBy = Automatic

	/// Reference Doc. Number.
	column REFERENCEDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REFERENCEDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Reference Document Item.
	column REFERENCEDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: REFERENCEDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Reference Document Item Group.
	column REFERENCEDOCUMENTITEMGROUP
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: REFERENCEDOCUMENTITEMGROUP

		annotation SummarizationSetBy = Automatic

	/// Partial Document to be balanced to zero.
	column TRANSACTIONSUBITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: TRANSACTIONSUBITEM

		annotation SummarizationSetBy = Automatic

	/// Indicator: Item is Reversing Another Item.
	column ISREVERSAL
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ISREVERSAL

		annotation SummarizationSetBy = Automatic

	/// Indicator: Item is Reversed.
	column ISREVERSED
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ISREVERSED

		annotation SummarizationSetBy = Automatic

	/// Reversal Reference Document Context.
	column REVERSALREFERENCEDOCUMENTCNTXT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REVERSALREFERENCEDOCUMENTCNTXT

		annotation SummarizationSetBy = Automatic

	/// Reversal Reference Document.
	column REVERSALREFERENCEDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REVERSALREFERENCEDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Reversal Transaction Sub Item.
	column REVERSALTRANSACTIONSUBITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: REVERSALTRANSACTIONSUBITEM

		annotation SummarizationSetBy = Automatic

	/// Indicator: Item is Settling or Transferring Another Item.
	column ISSETTLEMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ISSETTLEMENT

		annotation SummarizationSetBy = Automatic

	/// Indicator: Line Item is Settled or Transferred.
	column ISSETTLED
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ISSETTLED

		annotation SummarizationSetBy = Automatic

	/// Predecessor Reference Document Type.
	column PREDECESSORREFERENCEDOCTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PREDECESSORREFERENCEDOCTYPE

		annotation SummarizationSetBy = Automatic

	/// Predecessor Reference Document Context.
	column PREDECESSORREFERENCEDOCCNTXT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PREDECESSORREFERENCEDOCCNTXT

		annotation SummarizationSetBy = Automatic

	/// Predecessor Reference Document.
	column PREDECESSORREFERENCEDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PREDECESSORREFERENCEDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Predecessor Reference Document Item.
	column PREDECESSORREFERENCEDOCITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PREDECESSORREFERENCEDOCITEM

		annotation SummarizationSetBy = Automatic

	/// Preceding Journal Entry Company Code.
	column PRDCSSRJOURNALENTRYCOMPANYCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PRDCSSRJOURNALENTRYCOMPANYCODE

		annotation SummarizationSetBy = Automatic

	/// Preceding Journal Entry Fiscal Year.
	column PRDCSSRJOURNALENTRYFISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PRDCSSRJOURNALENTRYFISCALYEAR

		annotation SummarizationSetBy = Automatic

	/// Preceding Journal Entry Document Number.
	column PREDECESSORJOURNALENTRY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PREDECESSORJOURNALENTRY

		annotation SummarizationSetBy = Automatic

	/// Preceding Journal Entry Line Item.
	column PREDECESSORJOURNALENTRYITEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PREDECESSORJOURNALENTRYITEM

		annotation SummarizationSetBy = Automatic

	/// Source Reference Document Type.
	column SOURCEREFERENCEDOCUMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SOURCEREFERENCEDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Source Logical System.
	column SOURCELOGICALSYSTEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SOURCELOGICALSYSTEM

		annotation SummarizationSetBy = Automatic

	/// Source Reference Document Context.
	column SOURCEREFERENCEDOCUMENTCNTXT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SOURCEREFERENCEDOCUMENTCNTXT

		annotation SummarizationSetBy = Automatic

	/// Source Reference Document.
	column SOURCEREFERENCEDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SOURCEREFERENCEDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Source Reference Document Item.
	column SOURCEREFERENCEDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: SOURCEREFERENCEDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Source Reference Document Subitem.
	column SOURCEREFERENCEDOCSUBITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: SOURCEREFERENCEDOCSUBITEM

		annotation SummarizationSetBy = Automatic

	/// Indicator: Is Commitment.
	column ISCOMMITMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ISCOMMITMENT

		annotation SummarizationSetBy = Automatic

	/// Journal Entry Item Obsolete Reason.
	column JRNLENTRYITEMOBSOLETEREASON
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JRNLENTRYITEMOBSOLETEREASON

		annotation SummarizationSetBy = Automatic

	/// Journal Entry Is Secondary Entry.
	column JOURNALENTRYISSECONDARYENTRY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOURNALENTRYISSECONDARYENTRY

		annotation SummarizationSetBy = Automatic

	/// Orgl Change.
	column ORGANIZATIONALCHANGE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORGANIZATIONALCHANGE

		annotation SummarizationSetBy = Automatic

	/// Cost Center.
	column COSTCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COSTCENTER

		annotation SummarizationSetBy = Automatic

	/// Profit Center.
	column PROFITCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PROFITCENTER

		annotation SummarizationSetBy = Automatic

	/// Partner Cost Center.
	column PARTNERCOSTCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERCOSTCENTER

		annotation SummarizationSetBy = Automatic

	/// Partner Profit Center.
	column PARTNERPROFITCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERPROFITCENTER

		annotation SummarizationSetBy = Automatic

	/// Partner Functional Area.
	column PARTNERFUNCTIONALAREA
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERFUNCTIONALAREA

		annotation SummarizationSetBy = Automatic

	/// Partner Business Area.
	column PARTNERBUSINESSAREA
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERBUSINESSAREA

		annotation SummarizationSetBy = Automatic

	/// Company ID of Trading Partner.
	column PARTNERCOMPANY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERCOMPANY

		annotation SummarizationSetBy = Automatic

	/// Partner Segment for Segmental Reporting.
	column PARTNERSEGMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERSEGMENT

		annotation SummarizationSetBy = Automatic

	/// Amount in Balance Transaction Currency.
	column AMOUNTINBALANCETRANSACCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINBALANCETRANSACCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Transaction Currency.
	column AMOUNTINTRANSACTIONCURRENCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINTRANSACTIONCURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Company Code Currency.
	column AMOUNTINCOMPANYCODECURRENCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINCOMPANYCODECURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Global Currency.
	column AMOUNTINGLOBALCURRENCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINGLOBALCURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Functional Currency.
	column AMOUNTINFUNCTIONALCURRENCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFUNCTIONALCURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 1.
	column AMOUNTINFREEDEFINEDCURRENCY1
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY1

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 2.
	column AMOUNTINFREEDEFINEDCURRENCY2
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY2

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 3.
	column AMOUNTINFREEDEFINEDCURRENCY3
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY3

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 4.
	column AMOUNTINFREEDEFINEDCURRENCY4
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY4

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 5.
	column AMOUNTINFREEDEFINEDCURRENCY5
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY5

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 6.
	column AMOUNTINFREEDEFINEDCURRENCY6
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY6

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 7.
	column AMOUNTINFREEDEFINEDCURRENCY7
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY7

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Freely Defined Currency 8.
	column AMOUNTINFREEDEFINEDCURRENCY8
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINFREEDEFINEDCURRENCY8

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Fixed Amount in Global Currency.
	column FIXEDAMOUNTINGLOBALCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: FIXEDAMOUNTINGLOBALCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Group Valuation Fixed Amount in Global Currency.
	column GRPVALNFIXEDAMTINGLOBCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: GRPVALNFIXEDAMTINGLOBCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Profit Center Valuation Fixed Amount in Global Currency.
	column PRFTCTRVALNFXDAMTINGLOBCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: PRFTCTRVALNFXDAMTINGLOBCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Fixed Amount in Company Currency.
	column FIXEDAMOUNTINCOCODECRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: FIXEDAMOUNTINCOCODECRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Fixed Amount in Transaction Currency.
	column FIXEDAMOUNTINTRANSCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: FIXEDAMOUNTINTRANSCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Total Price Variance in Global Currency.
	column TOTALPRICEVARCINGLOBALCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: TOTALPRICEVARCINGLOBALCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Group Valuation Total Price Variance in Global Currency.
	column GRPVALNTOTPRCVARCINGLOBCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: GRPVALNTOTPRCVARCINGLOBCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Profit Center Valuation Total Price Variance in Global Cur..
	column PRFTCTRVALNTOTPRCVARCINGLBCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: PRFTCTRVALNTOTPRCVARCINGLBCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Fixed Price Variance in Global Currency.
	column FIXEDPRICEVARCINGLOBALCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: FIXEDPRICEVARCINGLOBALCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Group Valuation Fixed Price Variance in Global Currency.
	column GRPVALNFIXEDPRCVARCINGLOBCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: GRPVALNFIXEDPRCVARCINGLOBCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Profit Center Valuation Fixed Price Variance in Global Cur..
	column PRFTCTRVALNFXDPRCVARCINGLBCRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: PRFTCTRVALNFXDPRCVARCINGLBCRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Amount in Object Currency.
	column AMOUNTINOBJECTCURRENCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINOBJECTCURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Grant Amount in Grant Currency.
	column AMOUNTINGRANTCURRENCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: AMOUNTINGRANTCURRENCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Quantity.
	column QUANTITY
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: QUANTITY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Fixed Quantity.
	column FIXEDQUANTITY
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: FIXEDQUANTITY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Cost Source Unit.
	column COSTSOURCEUNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COSTSOURCEUNIT

		annotation SummarizationSetBy = Automatic

	/// Valuation Quantity.
	column VALUATIONQUANTITY
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: VALUATIONQUANTITY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Valuation Fixed Quantity.
	column VALUATIONFIXEDQUANTITY
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: VALUATIONFIXEDQUANTITY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Unit of Measure for Reference Quantity.
	column REFERENCEQUANTITYUNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REFERENCEQUANTITYUNIT

		annotation SummarizationSetBy = Automatic

	/// Reference quantity.
	column REFERENCEQUANTITY
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: REFERENCEQUANTITY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Additional Quantity 1 Unit.
	column ADDITIONALQUANTITY1UNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ADDITIONALQUANTITY1UNIT

		annotation SummarizationSetBy = Automatic

	/// Additional Quantity 1.
	column ADDITIONALQUANTITY1
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: ADDITIONALQUANTITY1

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Additional Quantity 2 Unit.
	column ADDITIONALQUANTITY2UNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ADDITIONALQUANTITY2UNIT

		annotation SummarizationSetBy = Automatic

	/// Additional Quantity 2.
	column ADDITIONALQUANTITY2
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: ADDITIONALQUANTITY2

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Additional Quantity 3 Unit.
	column ADDITIONALQUANTITY3UNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ADDITIONALQUANTITY3UNIT

		annotation SummarizationSetBy = Automatic

	/// Additional Quantity 3.
	column ADDITIONALQUANTITY3
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: ADDITIONALQUANTITY3

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Fiscal Period.
	column FISCALPERIOD
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: FISCALPERIOD

		annotation SummarizationSetBy = User

	/// Fiscal Year Period.
	column FISCALYEARPERIOD
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: FISCALYEARPERIOD

		annotation SummarizationSetBy = Automatic

	/// Posting Date.
	column POSTINGDATE
		dataType: dateTime
		formatString: mm/dd/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: POSTINGDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

		annotation PBI_FormatHint = {"isDateTimeCustom":true}

	/// Journal Entry Date.
	column DOCUMENTDATE
		dataType: dateTime
		formatString: mm/dd/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: DOCUMENTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

		annotation PBI_FormatHint = {"isDateTimeCustom":true}

	/// Journal Entry Posting View Item.
	column ACCOUNTINGDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: ACCOUNTINGDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Assignment Reference.
	column ASSIGNMENTREFERENCE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ASSIGNMENTREFERENCE

		annotation SummarizationSetBy = Automatic

	/// Journal Entry Category.
	column ACCOUNTINGDOCUMENTCATEGORY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCOUNTINGDOCUMENTCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Posting Key.
	column POSTINGKEY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: POSTINGKEY

		annotation SummarizationSetBy = Automatic

	/// Transaction Key.
	column TRANSACTIONTYPEDETERMINATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: TRANSACTIONTYPEDETERMINATION

		annotation SummarizationSetBy = Automatic

	/// Subledger-Specific Line Item Type.
	column SUBLEDGERACCTLINEITEMTYPE
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: SUBLEDGERACCTLINEITEMTYPE

		annotation SummarizationSetBy = Automatic

	/// User that created the journal entry.
	column ACCOUNTINGDOCCREATEDBYUSER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCOUNTINGDOCCREATEDBYUSER

		annotation SummarizationSetBy = Automatic

	/// Last Change Date Time.
	column LASTCHANGEDATETIME
		dataType: double
		sourceProviderType: decimal(15, 0)
		summarizeBy: none
		sourceColumn: LASTCHANGEDATETIME

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Creation Date Time.
	column CREATIONDATETIME
		dataType: double
		sourceProviderType: decimal(15, 0)
		summarizeBy: none
		sourceColumn: CREATIONDATETIME

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Creation Date.
	column CREATIONDATE
		dataType: dateTime
		formatString: mm/dd/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: CREATIONDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

		annotation PBI_FormatHint = {"isDateTimeCustom":true}

	/// Elimination Profit Center.
	column ELIMINATIONPROFITCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ELIMINATIONPROFITCENTER

		annotation SummarizationSetBy = Automatic

	/// Type of Origin Object.
	column ORIGINOBJECTTYPE
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: ORIGINOBJECTTYPE

		annotation SummarizationSetBy = Automatic

	/// Type of a General Ledger Account.
	column GLACCOUNTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GLACCOUNTTYPE

		annotation SummarizationSetBy = Automatic

	/// Alternative G/L Account Number In Company Code.
	column ALTERNATIVEGLACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ALTERNATIVEGLACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Alternative Chart of Accounts for Country/Region.
	column COUNTRYCHARTOFACCOUNTS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COUNTRYCHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// Item changed by document splitting.
	column ITEMISSPLIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ITEMISSPLIT

		annotation SummarizationSetBy = Automatic

	/// Consolidation Unit.
	column CONSOLIDATIONUNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONSOLIDATIONUNIT

		annotation SummarizationSetBy = Automatic

	/// Partner Consolidation Unit.
	column PARTNERCONSOLIDATIONUNIT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERCONSOLIDATIONUNIT

		annotation SummarizationSetBy = Automatic

	/// Consolidation Chart of Accounts.
	column CONSOLIDATIONCHARTOFACCOUNTS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONSOLIDATIONCHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// Consolidation Financial Statement Item.
	column CNSLDTNFINANCIALSTATEMENTITEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CNSLDTNFINANCIALSTATEMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Consolidation Subitem Category.
	column CNSLDTNSUBITEMCATEGORY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CNSLDTNSUBITEMCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Consolidation Subitem.
	column CNSLDTNSUBITEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CNSLDTNSUBITEM

		annotation SummarizationSetBy = Automatic

	/// Invoice Reference.
	column INVOICEREFERENCE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: INVOICEREFERENCE

		annotation SummarizationSetBy = Automatic

	/// Invoice Reference Fiscal Year.
	column INVOICEREFERENCEFISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: INVOICEREFERENCEFISCALYEAR

		annotation SummarizationSetBy = Automatic

	/// Follow-On Document Type.
	column FOLLOWONDOCUMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FOLLOWONDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Invoice Item Reference.
	column INVOICEITEMREFERENCE
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: INVOICEITEMREFERENCE

		annotation SummarizationSetBy = Automatic

	/// Category of Reference Purchase Order.
	column REFERENCEPURCHASEORDERCATEGORY
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: REFERENCEPURCHASEORDERCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Purchasing Document.
	column PURCHASINGDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PURCHASINGDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Purchasing Document Item.
	column PURCHASINGDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PURCHASINGDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Account Assignment Number.
	column ACCOUNTASSIGNMENTNUMBER
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: ACCOUNTASSIGNMENTNUMBER

		annotation SummarizationSetBy = Automatic

	/// Item Text.
	column DOCUMENTITEMTEXT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: DOCUMENTITEMTEXT

		annotation SummarizationSetBy = Automatic

	/// Sales Document.
	column SALESDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SALESDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Sales Document Item.
	column SALESDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: SALESDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Date on which services are rendered.
	column SERVICESRENDEREDDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: SERVICESRENDEREDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Billing Period of Performance Start Date.
	column PERFORMANCEPERIODSTARTDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: PERFORMANCEPERIODSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Billing Period of Performance End Date.
	column PERFORMANCEPERIODENDDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: PERFORMANCEPERIODENDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Condition Contract.
	column CONDITIONCONTRACT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONDITIONCONTRACT

		annotation SummarizationSetBy = Automatic

	/// Translation Date.
	column EXCHANGERATEDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: EXCHANGERATEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Account Type.
	column FINANCIALACCOUNTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FINANCIALACCOUNTTYPE

		annotation SummarizationSetBy = Automatic

	/// Special G/L Indicator.
	column SPECIALGLCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SPECIALGLCODE

		annotation SummarizationSetBy = Automatic

	/// Tax on Sales/Purchases Code.
	column TAXCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: TAXCODE

		annotation SummarizationSetBy = Automatic

	/// Tax Reporting Country/Region.
	column TAXCOUNTRY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: TAXCOUNTRY

		annotation SummarizationSetBy = Automatic

	/// House Bank Key.
	column HOUSEBANK
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: HOUSEBANK

		annotation SummarizationSetBy = Automatic

	/// House Bank Account.
	column HOUSEBANKACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: HOUSEBANKACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Managed on an Open Item Basis.
	column ISOPENITEMMANAGED
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ISOPENITEMMANAGED

		annotation SummarizationSetBy = Automatic

	/// Clearing Date.
	column CLEARINGDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: CLEARINGDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Fiscal Year of Clearing Journal Entry (Deprecated).
	column CLEARINGDOCFISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: CLEARINGDOCFISCALYEAR

		annotation SummarizationSetBy = Automatic

	/// Clearing Journal Entry (Deprecated).
	column CLEARINGACCOUNTINGDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CLEARINGACCOUNTINGDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Fiscal Year of Clearing Journal Entry.
	column CLEARINGJOURNALENTRYFISCALYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: CLEARINGJOURNALENTRYFISCALYEAR

		annotation SummarizationSetBy = Automatic

	/// Clearing Journal Entry.
	column CLEARINGJOURNALENTRY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CLEARINGJOURNALENTRY

		annotation SummarizationSetBy = Automatic

	/// Value Date.
	column VALUEDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: VALUEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// General Ledger Aging Scope.
	column GENERALLEDGERAGINGSCOPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GENERALLEDGERAGINGSCOPE

		annotation SummarizationSetBy = Automatic

	/// General Ledger Aging Increment.
	column GENERALLEDGERAGINGINCREMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GENERALLEDGERAGINGINCREMENT

		annotation SummarizationSetBy = Automatic

	/// Asset Depreciation Area (Real or Derived).
	column ASSETDEPRECIATIONAREA
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: ASSETDEPRECIATIONAREA

		annotation SummarizationSetBy = Automatic

	/// Asset Value Date.
	column ASSETVALUEDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: ASSETVALUEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Transaction Type Category.
	column ASSETACCTTRANSCLASSFCTN
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ASSETACCTTRANSCLASSFCTN

		annotation SummarizationSetBy = Automatic

	/// Fiscal Period of Depreciation.
	column DEPRECIATIONFISCALPERIOD
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: DEPRECIATIONFISCALPERIOD

		annotation SummarizationSetBy = Automatic

	/// Group Asset.
	column GROUPMASTERFIXEDASSET
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GROUPMASTERFIXEDASSET

		annotation SummarizationSetBy = Automatic

	/// Group Asset Subnumber.
	column GROUPFIXEDASSET
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GROUPFIXEDASSET

		annotation SummarizationSetBy = Automatic

	/// Partner Master Fixed Asset.
	column PARTNERMASTERFIXEDASSET
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERMASTERFIXEDASSET

		annotation SummarizationSetBy = Automatic

	/// Partner Fixed Asset.
	column PARTNERFIXEDASSET
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERFIXEDASSET

		annotation SummarizationSetBy = Automatic

	/// Cost Estimate.
	column COSTESTIMATE
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: COSTESTIMATE

		annotation SummarizationSetBy = Automatic

	/// Inventory Special Stock Valuation Type.
	column INVENTORYSPECIALSTOCKVALNTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: INVENTORYSPECIALSTOCKVALNTYPE

		annotation SummarizationSetBy = Automatic

	/// Is Supplier Stock Valuation.
	column ISSUPPLIERSTOCKVALUATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ISSUPPLIERSTOCKVALUATION

		annotation SummarizationSetBy = Automatic

	/// Inventory Special Stock Type.
	column INVENTORYSPECIALSTOCKTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: INVENTORYSPECIALSTOCKTYPE

		annotation SummarizationSetBy = Automatic

	/// Inventory Special Stock Sales Document.
	column INVENTORYSPCLSTKSALESDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: INVENTORYSPCLSTKSALESDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Inventory Special Stock Sales Document Item.
	column INVENTORYSPCLSTKSALESDOCITM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: INVENTORYSPCLSTKSALESDOCITM

		annotation SummarizationSetBy = Automatic

	/// Inventory Special Stock WBS Element Internal ID.
	column INVTRYSPCLSTOCKWBSELMNTINTID
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: INVTRYSPCLSTOCKWBSELMNTINTID

		annotation SummarizationSetBy = Automatic

	/// Inventory Special Stock WBS Element.
	column INVENTORYSPCLSTOCKWBSELEMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: INVENTORYSPCLSTOCKWBSELEMENT

		annotation SummarizationSetBy = Automatic

	/// Supplier of Inventory Special Stock.
	column INVENTORYSPECIALSTOCKSUPPLIER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: INVENTORYSPECIALSTOCKSUPPLIER

		annotation SummarizationSetBy = Automatic

	/// Inventory Valuation Type.
	column INVENTORYVALUATIONTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: INVENTORYVALUATIONTYPE

		annotation SummarizationSetBy = Automatic

	/// Valuation Area.
	column VALUATIONAREA
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: VALUATIONAREA

		annotation SummarizationSetBy = Automatic

	/// Material Ledger Process Type (Procurement/Consumption).
	column MATERIALLEDGERPROCESSTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MATERIALLEDGERPROCESSTYPE

		annotation SummarizationSetBy = Automatic

	/// Category in Material Ledger Update Structure.
	column MATERIALLEDGERCATEGORY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MATERIALLEDGERCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Sales Price Amount in Company Code Currency.
	column SLSPRICEAMOUNTINCOCODECRCY
		dataType: decimal
		sourceProviderType: decimal(23, 2)
		summarizeBy: none
		sourceColumn: SLSPRICEAMOUNTINCOCODECRCY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Product Price Control Indicator.
	column PRODUCTPRICECONTROL
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PRODUCTPRICECONTROL

		annotation SummarizationSetBy = Automatic

	/// Company Code in Sender System.
	column SENDERCOMPANYCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SENDERCOMPANYCODE

		annotation SummarizationSetBy = Automatic

	/// Sender G/L Account.
	column SENDERGLACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SENDERGLACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Sender Account Assignment.
	column SENDERACCOUNTASSIGNMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SENDERACCOUNTASSIGNMENT

		annotation SummarizationSetBy = Automatic

	/// Account Assignment Type in Sender System.
	column SENDERACCOUNTASSIGNMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SENDERACCOUNTASSIGNMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Controlling Object.
	column CONTROLLINGOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONTROLLINGOBJECT

		annotation SummarizationSetBy = Automatic

	/// Origin Group as Subdivision of Cost Element.
	column COSTORIGINGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COSTORIGINGROUP

		annotation SummarizationSetBy = Automatic

	/// Origin Sender Object.
	column ORIGINSENDEROBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINSENDEROBJECT

		annotation SummarizationSetBy = Automatic

	/// Controlling Debit Credit Code.
	column CONTROLLINGDEBITCREDITCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONTROLLINGDEBITCREDITCODE

		annotation SummarizationSetBy = Automatic

	/// Debit/Credit Indicator (Origin).
	column ORIGINCTRLGDEBITCREDITCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINCTRLGDEBITCREDITCODE

		annotation SummarizationSetBy = Automatic

	/// Controlling Object Debit Type.
	column CONTROLLINGOBJECTDEBITTYPE
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: CONTROLLINGOBJECTDEBITTYPE

		annotation SummarizationSetBy = Automatic

	/// Indicator: Quantity Is Incomplete.
	column QUANTITYISINCOMPLETE
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: QUANTITYISINCOMPLETE

		annotation SummarizationSetBy = Automatic

	/// Offsetting Account.
	column OFFSETTINGACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: OFFSETTINGACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Offsetting Account Type.
	column OFFSETTINGACCOUNTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: OFFSETTINGACCOUNTTYPE

		annotation SummarizationSetBy = Automatic

	/// Offsetting Chart of Accounts.
	column OFFSETTINGCHARTOFACCOUNTS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: OFFSETTINGCHARTOFACCOUNTS

		annotation SummarizationSetBy = Automatic

	/// Indicator: Line Item is Completed.
	column LINEITEMISCOMPLETED
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: LINEITEMISCOMPLETED

		annotation SummarizationSetBy = Automatic

	/// Personnel Number.
	column PERSONNELNUMBER
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PERSONNELNUMBER

		annotation SummarizationSetBy = Automatic

	/// Controlling Object Class.
	column CONTROLLINGOBJECTCLASS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CONTROLLINGOBJECTCLASS

		annotation SummarizationSetBy = Automatic

	/// Partner Company Code.
	column PARTNERCOMPANYCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERCOMPANYCODE

		annotation SummarizationSetBy = Automatic

	/// Partner Controlling Object Class.
	column PARTNERCONTROLLINGOBJECTCLASS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERCONTROLLINGOBJECTCLASS

		annotation SummarizationSetBy = Automatic

	/// Origin Profit Center.
	column ORIGINPROFITCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINPROFITCENTER

		annotation SummarizationSetBy = Automatic

	/// Origin Order.
	column ORIGINORDER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINORDER

		annotation SummarizationSetBy = Automatic

	/// Origin Cost Center Activity Type.
	column ORIGINCOSTCTRACTIVITYTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINCOSTCTRACTIVITYTYPE

		annotation SummarizationSetBy = Automatic

	/// Origin Cost Center.
	column ORIGINCOSTCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINCOSTCENTER

		annotation SummarizationSetBy = Automatic

	/// Origin Product.
	column ORIGINPRODUCT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINPRODUCT

		annotation SummarizationSetBy = Automatic

	/// Origin G/L Account of a Variance.
	column VARIANCEORIGINGLACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: VARIANCEORIGINGLACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Account Assignment.
	column ACCOUNTASSIGNMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCOUNTASSIGNMENT

		annotation SummarizationSetBy = Automatic

	/// Account Assignment Type.
	column ACCOUNTASSIGNMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCOUNTASSIGNMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Activity Type.
	column COSTCTRACTIVITYTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COSTCTRACTIVITYTYPE

		annotation SummarizationSetBy = Automatic

	/// Order ID.
	column ORDERID
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORDERID

		annotation SummarizationSetBy = Automatic

	/// Order Category.
	column ORDERCATEGORY
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: ORDERCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Partner WBS Element Internal ID.
	column PARTNERWBSELEMENTINTERNALID
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PARTNERWBSELEMENTINTERNALID

		annotation SummarizationSetBy = Automatic

	/// Partner WBS Element.
	column PARTNERWBSELEMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERWBSELEMENT

		annotation SummarizationSetBy = Automatic

	/// Project Internal ID.
	column PROJECTINTERNALID
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PROJECTINTERNALID

		annotation SummarizationSetBy = Automatic

	/// Project.
	column PROJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PROJECT

		annotation SummarizationSetBy = Automatic

	/// Partner Project Internal ID.
	column PARTNERPROJECTINTERNALID
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PARTNERPROJECTINTERNALID

		annotation SummarizationSetBy = Automatic

	/// Partner Project.
	column PARTNERPROJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERPROJECT

		annotation SummarizationSetBy = Automatic

	/// Operating Concern.
	column OPERATINGCONCERN
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: OPERATINGCONCERN

		annotation SummarizationSetBy = Automatic

	/// Network Number for Account Assignment.
	column PROJECTNETWORK
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PROJECTNETWORK

		annotation SummarizationSetBy = Automatic

	/// Related Network Activity.
	column RELATEDNETWORKACTIVITY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: RELATEDNETWORKACTIVITY

		annotation SummarizationSetBy = Automatic

	/// Business Process.
	column BUSINESSPROCESS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BUSINESSPROCESS

		annotation SummarizationSetBy = Automatic

	/// Cost Object.
	column COSTOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COSTOBJECT

		annotation SummarizationSetBy = Automatic

	/// Billable Control.
	column BILLABLECONTROL
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BILLABLECONTROL

		annotation SummarizationSetBy = Automatic

	/// Cost Analysis Resource.
	column COSTANALYSISRESOURCE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: COSTANALYSISRESOURCE

		annotation SummarizationSetBy = Automatic

	/// Customer Service Notification.
	column CUSTOMERSERVICENOTIFICATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUSTOMERSERVICENOTIFICATION

		annotation SummarizationSetBy = Automatic

	/// Service Document Type.
	column SERVICEDOCUMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SERVICEDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Service Document ID.
	column SERVICEDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SERVICEDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Service Document Item ID.
	column SERVICEDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: SERVICEDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Partner Service Document Type.
	column PARTNERSERVICEDOCUMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERSERVICEDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Partner Service Document.
	column PARTNERSERVICEDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERSERVICEDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Partner Service Document Item.
	column PARTNERSERVICEDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PARTNERSERVICEDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Service Contract Type.
	column SERVICECONTRACTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SERVICECONTRACTTYPE

		annotation SummarizationSetBy = Automatic

	/// Service Contract ID.
	column SERVICECONTRACT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SERVICECONTRACT

		annotation SummarizationSetBy = Automatic

	/// Service Contract Item ID.
	column SERVICECONTRACTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: SERVICECONTRACTITEM

		annotation SummarizationSetBy = Automatic

	/// Solution Order.
	column BUSINESSSOLUTIONORDER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BUSINESSSOLUTIONORDER

		annotation SummarizationSetBy = Automatic

	/// Solution Order Item.
	column BUSINESSSOLUTIONORDERITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: BUSINESSSOLUTIONORDERITEM

		annotation SummarizationSetBy = Automatic

	/// Provider Contract.
	column PROVIDERCONTRACT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PROVIDERCONTRACT

		annotation SummarizationSetBy = Automatic

	/// Provider Contract Item.
	column PROVIDERCONTRACTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PROVIDERCONTRACTITEM

		annotation SummarizationSetBy = Automatic

	/// Revenue Accounting Contract.
	column REVENUEACCOUNTINGCONTRACT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REVENUEACCOUNTINGCONTRACT

		annotation SummarizationSetBy = Automatic

	/// Performance Obligation.
	column PERFORMANCEOBLIGATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PERFORMANCEOBLIGATION

		annotation SummarizationSetBy = Automatic

	/// Overtime Category.
	column TIMESHEETOVERTIMECATEGORY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: TIMESHEETOVERTIMECATEGORY

		annotation SummarizationSetBy = Automatic

	/// Partner Account Assignment.
	column PARTNERACCOUNTASSIGNMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERACCOUNTASSIGNMENT

		annotation SummarizationSetBy = Automatic

	/// Partner Account Assignment Type.
	column PARTNERACCOUNTASSIGNMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERACCOUNTASSIGNMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Plan Item.
	column WORKPACKAGE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: WORKPACKAGE

		annotation SummarizationSetBy = Automatic

	/// Work Item ID.
	column WORKITEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: WORKITEM

		annotation SummarizationSetBy = Automatic

	/// Partner Cost Center Activity Type.
	column PARTNERCOSTCTRACTIVITYTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERCOSTCTRACTIVITYTYPE

		annotation SummarizationSetBy = Automatic

	/// Partner Order.
	column PARTNERORDER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERORDER

		annotation SummarizationSetBy = Automatic

	/// Partner Order Category.
	column PARTNERORDERCATEGORY
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PARTNERORDERCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Partner Sales Document.
	column PARTNERSALESDOCUMENT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERSALESDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Partner Sales Document Item.
	column PARTNERSALESDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PARTNERSALESDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Partner Project Network.
	column PARTNERPROJECTNETWORK
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERPROJECTNETWORK

		annotation SummarizationSetBy = Automatic

	/// Partner Project Network Activity.
	column PARTNERPROJECTNETWORKACTIVITY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERPROJECTNETWORKACTIVITY

		annotation SummarizationSetBy = Automatic

	/// Partner Business Process.
	column PARTNERBUSINESSPROCESS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERBUSINESSPROCESS

		annotation SummarizationSetBy = Automatic

	/// Partner Cost Object.
	column PARTNERCOSTOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERCOSTOBJECT

		annotation SummarizationSetBy = Automatic

	/// Controlling Document Item.
	column CONTROLLINGDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: CONTROLLINGDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Variance Origin Group.
	column VARIANCEORIGINGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: VARIANCEORIGINGROUP

		annotation SummarizationSetBy = Automatic

	/// Billing Type.
	column BILLINGDOCUMENTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BILLINGDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Sales Organization.
	column SALESORGANIZATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SALESORGANIZATION

		annotation SummarizationSetBy = Automatic

	/// Distribution Channel.
	column DISTRIBUTIONCHANNEL
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: DISTRIBUTIONCHANNEL

		annotation SummarizationSetBy = Automatic

	/// Division.
	column ORGANIZATIONDIVISION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORGANIZATIONDIVISION

		annotation SummarizationSetBy = Automatic

	/// Product Sold.
	column SOLDPRODUCT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SOLDPRODUCT

		annotation SummarizationSetBy = Automatic

	/// Product Sold Group.
	column SOLDPRODUCTGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SOLDPRODUCTGROUP

		annotation SummarizationSetBy = Automatic

	/// Customer Group.
	column CUSTOMERGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUSTOMERGROUP

		annotation SummarizationSetBy = Automatic

	/// Customer or Supplier Country/Region.
	column CUSTOMERSUPPLIERCOUNTRY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUSTOMERSUPPLIERCOUNTRY

		annotation SummarizationSetBy = Automatic

	/// Customer Supplier Industry.
	column CUSTOMERSUPPLIERINDUSTRY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUSTOMERSUPPLIERINDUSTRY

		annotation SummarizationSetBy = Automatic

	/// Sales District.
	column SALESDISTRICT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SALESDISTRICT

		annotation SummarizationSetBy = Automatic

	/// Bill-to Party.
	column BILLTOPARTY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BILLTOPARTY

		annotation SummarizationSetBy = Automatic

	/// Ship-to Party.
	column SHIPTOPARTY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SHIPTOPARTY

		annotation SummarizationSetBy = Automatic

	/// Customer Supplier Corporate Group.
	column CUSTOMERSUPPLIERCORPORATEGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUSTOMERSUPPLIERCORPORATEGROUP

		annotation SummarizationSetBy = Automatic

	/// Cash Origin Company Code.
	column CASHLEDGERCOMPANYCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CASHLEDGERCOMPANYCODE

		annotation SummarizationSetBy = Automatic

	/// Cash Origin Account.
	column CASHLEDGERACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CASHLEDGERACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Financial Management Area.
	column FINANCIALMANAGEMENTAREA
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FINANCIALMANAGEMENTAREA

		annotation SummarizationSetBy = Automatic

	/// Funds Management Center.
	column FUNDSCENTER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FUNDSCENTER

		annotation SummarizationSetBy = Automatic

	/// Funded Program.
	column FUNDEDPROGRAM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FUNDEDPROGRAM

		annotation SummarizationSetBy = Automatic

	/// Fund.
	column FUND
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FUND

		annotation SummarizationSetBy = Automatic

	/// Grant.
	column GRANTID
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GRANTID

		annotation SummarizationSetBy = Automatic

	/// Budget Period.
	column BUDGETPERIOD
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: BUDGETPERIOD

		annotation SummarizationSetBy = Automatic

	/// Partner Fund.
	column PARTNERFUND
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERFUND

		annotation SummarizationSetBy = Automatic

	/// Partner Grant.
	column PARTNERGRANT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERGRANT

		annotation SummarizationSetBy = Automatic

	/// FM: Partner Budget Period.
	column PARTNERBUDGETPERIOD
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERBUDGETPERIOD

		annotation SummarizationSetBy = Automatic

	/// Budget Account.
	column PUBSECBUDGETACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PUBSECBUDGETACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Budget Account Company Code.
	column PUBSECBUDGETACCOUNTCOCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PUBSECBUDGETACCOUNTCOCODE

		annotation SummarizationSetBy = Automatic

	/// Budget Consumption Date.
	column PUBSECBUDGETCNSMPNDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: PUBSECBUDGETCNSMPNDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// CC Fiscal Period for Budget Consumption Date.
	column PUBSECBUDGETCNSMPNFSCLPERIOD
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PUBSECBUDGETCNSMPNFSCLPERIOD

		annotation SummarizationSetBy = Automatic

	/// CC Fiscal Year for Budget Consumption Date.
	column PUBSECBUDGETCNSMPNFSCLYEAR
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PUBSECBUDGETCNSMPNFSCLYEAR

		annotation SummarizationSetBy = Automatic

	/// Budget-Relevant Indicator.
	column PUBSECBUDGETISRELEVANT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PUBSECBUDGETISRELEVANT

		annotation SummarizationSetBy = Automatic

	/// Budget Consumption Type.
	column PUBSECBUDGETCNSMPNTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PUBSECBUDGETCNSMPNTYPE

		annotation SummarizationSetBy = Automatic

	/// Budget Consumption Amount Type.
	column PUBSECBUDGETCNSMPNAMTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PUBSECBUDGETCNSMPNAMTTYPE

		annotation SummarizationSetBy = Automatic

	/// Sponsored Program.
	column SPONSOREDPROGRAM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SPONSOREDPROGRAM

		annotation SummarizationSetBy = Automatic

	/// Sponsored Class.
	column SPONSOREDCLASS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SPONSOREDCLASS

		annotation SummarizationSetBy = Automatic

	/// Budget Validity Number.
	column GTEEMBUDGETVALIDITYNUMBER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: GTEEMBUDGETVALIDITYNUMBER

		annotation SummarizationSetBy = Automatic

	/// Joint Venture.
	column JOINTVENTURE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOINTVENTURE

		annotation SummarizationSetBy = Automatic

	/// Joint Venture Equity Group.
	column JOINTVENTUREEQUITYGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOINTVENTUREEQUITYGROUP

		annotation SummarizationSetBy = Automatic

	/// Joint Venture Cost Recovery Code.
	column JOINTVENTURECOSTRECOVERYCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOINTVENTURECOSTRECOVERYCODE

		annotation SummarizationSetBy = Automatic

	/// Joint Venture Partner.
	column JOINTVENTUREPARTNER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOINTVENTUREPARTNER

		annotation SummarizationSetBy = Automatic

	/// Joint Venture Billing Type.
	column JOINTVENTUREBILLINGTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOINTVENTUREBILLINGTYPE

		annotation SummarizationSetBy = Automatic

	/// Joint Venture Equity Type.
	column JOINTVENTUREEQUITYTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOINTVENTUREEQUITYTYPE

		annotation SummarizationSetBy = Automatic

	/// Joint Venture Production Date.
	column JOINTVENTUREPRODUCTIONDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: JOINTVENTUREPRODUCTIONDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Joint Venture Billing Date.
	column JOINTVENTUREBILLINGDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: JOINTVENTUREBILLINGDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Joint Venture Operational Date.
	column JOINTVENTUREOPERATIONALDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: JOINTVENTUREOPERATIONALDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Cutback Run.
	column CUTBACKRUN
		dataType: decimal
		sourceProviderType: decimal(21, 7)
		summarizeBy: none
		sourceColumn: CUTBACKRUN

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Joint Venture Accounting Activity.
	column JOINTVENTUREACCOUNTINGACTIVITY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JOINTVENTUREACCOUNTINGACTIVITY

		annotation SummarizationSetBy = Automatic

	/// Partner Venture.
	column PARTNERVENTURE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNERVENTURE

		annotation SummarizationSetBy = Automatic

	/// Partner Equity Group.
	column PARTNEREQUITYGROUP
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: PARTNEREQUITYGROUP

		annotation SummarizationSetBy = Automatic

	/// Sender Cost Recovery Code.
	column SENDERCOSTRECOVERYCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SENDERCOSTRECOVERYCODE

		annotation SummarizationSetBy = Automatic

	/// Cutback Account.
	column CUTBACKACCOUNT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUTBACKACCOUNT

		annotation SummarizationSetBy = Automatic

	/// Cutback Cost Object.
	column CUTBACKCOSTOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CUTBACKCOSTOBJECT

		annotation SummarizationSetBy = Automatic

	/// RE Business Entity.
	column REBUSINESSENTITY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REBUSINESSENTITY

		annotation SummarizationSetBy = Automatic

	/// Real Estate Building.
	column REALESTATEBUILDING
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REALESTATEBUILDING

		annotation SummarizationSetBy = Automatic

	/// Real Estate Property.
	column REALESTATEPROPERTY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REALESTATEPROPERTY

		annotation SummarizationSetBy = Automatic

	/// RE Rental Object.
	column RERENTALOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: RERENTALOBJECT

		annotation SummarizationSetBy = Automatic

	/// Real Estate Contract.
	column REALESTATECONTRACT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REALESTATECONTRACT

		annotation SummarizationSetBy = Automatic

	/// RE Service Charge Key.
	column RESERVICECHARGEKEY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: RESERVICECHARGEKEY

		annotation SummarizationSetBy = Automatic

	/// RE Settlement Unit.
	column RESETTLEMENTUNITID
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: RESETTLEMENTUNITID

		annotation SummarizationSetBy = Automatic

	/// Settlement Reference Date.
	column SETTLEMENTREFERENCEDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: SETTLEMENTREFERENCEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// RE Partner Business Entity.
	column REPARTNERBUSINESSENTITY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REPARTNERBUSINESSENTITY

		annotation SummarizationSetBy = Automatic

	/// Real Estate Partner Building.
	column REALESTATEPARTNERBUILDING
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REALESTATEPARTNERBUILDING

		annotation SummarizationSetBy = Automatic

	/// Real Estate Partner Property.
	column REALESTATEPARTNERPROPERTY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REALESTATEPARTNERPROPERTY

		annotation SummarizationSetBy = Automatic

	/// RE Partner Rental Object.
	column REPARTNERRENTALOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REPARTNERRENTALOBJECT

		annotation SummarizationSetBy = Automatic

	/// Real Estate Partner Contract.
	column REALESTATEPARTNERCONTRACT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REALESTATEPARTNERCONTRACT

		annotation SummarizationSetBy = Automatic

	/// RE Partner Service Charge Key.
	column REPARTNERSERVICECHARGEKEY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REPARTNERSERVICECHARGEKEY

		annotation SummarizationSetBy = Automatic

	/// RE Partner Settlement Unit.
	column REPARTNERSETTLEMENTUNITID
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: REPARTNERSETTLEMENTUNITID

		annotation SummarizationSetBy = Automatic

	/// Partner Reference Date for Settlement.
	column PARTNERSETTLEMENTREFERENCEDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: PARTNERSETTLEMENTREFERENCEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Type of the Accrual Object.
	column ACCRUALOBJECTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCRUALOBJECTTYPE

		annotation SummarizationSetBy = Automatic

	/// Logical System of the Accrual Object.
	column ACCRUALOBJECTLOGICALSYSTEM
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCRUALOBJECTLOGICALSYSTEM

		annotation SummarizationSetBy = Automatic

	/// Identifier of the Accrual Object.
	column ACCRUALOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCRUALOBJECT

		annotation SummarizationSetBy = Automatic

	/// Identifier of the Accrual Subobject.
	column ACCRUALSUBOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCRUALSUBOBJECT

		annotation SummarizationSetBy = Automatic

	/// Type of the Item of the Accrual Subobject.
	column ACCRUALITEMTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCRUALITEMTYPE

		annotation SummarizationSetBy = Automatic

	/// Accrual Reference Object.
	column ACCRUALREFERENCEOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ACCRUALREFERENCEOBJECT

		annotation SummarizationSetBy = Automatic

	/// Accrual Value Date.
	column ACCRUALVALUEDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: ACCRUALVALUEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Financial Valuation Object Type.
	column FINANCIALVALUATIONOBJECTTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FINANCIALVALUATIONOBJECTTYPE

		annotation SummarizationSetBy = Automatic

	/// Financial Valuation Object.
	column FINANCIALVALUATIONOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FINANCIALVALUATIONOBJECT

		annotation SummarizationSetBy = Automatic

	/// Financial Valuation Subobject.
	column FINANCIALVALUATIONSUBOBJECT
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: FINANCIALVALUATIONSUBOBJECT

		annotation SummarizationSetBy = Automatic

	/// Net Due Date.
	column NETDUEDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: NETDUEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Credit Risk Class.
	column CREDITRISKCLASS
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: CREDITRISKCLASS

		annotation SummarizationSetBy = Automatic

	/// Object ID of the resource.
	column WORKCENTERINTERNALID
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: WORKCENTERINTERNALID

		annotation SummarizationSetBy = Automatic

	/// Order Operation.
	column ORDEROPERATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORDEROPERATION

		annotation SummarizationSetBy = Automatic

	/// Number of Order Item.
	column ORDERITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: ORDERITEM

		annotation SummarizationSetBy = Automatic

	/// Partner Order Item Number.
	column PARTNERORDERITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PARTNERORDERITEM

		annotation SummarizationSetBy = Automatic

	/// Order Suboperation.
	column ORDERSUBOPERATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORDERSUBOPERATION

		annotation SummarizationSetBy = Automatic

	/// Assembly.
	column ASSEMBLY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ASSEMBLY

		annotation SummarizationSetBy = Automatic

	/// Maintenance activity type.
	column MAINTENANCEACTIVITYTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MAINTENANCEACTIVITYTYPE

		annotation SummarizationSetBy = Automatic

	/// Maintenance order planning indicator.
	column MAINTENANCEORDERPLANNINGCODE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MAINTENANCEORDERPLANNINGCODE

		annotation SummarizationSetBy = Automatic

	/// Priority Type.
	column MAINTPRIORITYTYPE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MAINTPRIORITYTYPE

		annotation SummarizationSetBy = Automatic

	/// Priority.
	column MAINTPRIORITY
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MAINTPRIORITY

		annotation SummarizationSetBy = Automatic

	/// Number of Superior Order.
	column SUPERIORORDER
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: SUPERIORORDER

		annotation SummarizationSetBy = Automatic

	/// Planned Parts/Work.
	column MAINTENANCEORDERISPLANNED
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: MAINTENANCEORDERISPLANNED

		annotation SummarizationSetBy = Automatic

	/// Origin Order Operation.
	column ORIGINORDEROPERATION
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: ORIGINORDEROPERATION

		annotation SummarizationSetBy = Automatic

	/// Journal Entry Item Migration Source.
	column JRNLENTRYITEMMIGRATIONSOURCE
		dataType: string
		sourceProviderType: nvarchar(100)
		summarizeBy: none
		sourceColumn: JRNLENTRYITEMMIGRATIONSOURCE

		annotation SummarizationSetBy = Automatic

	/// Timestamp of the most recent source or ETL update.
	column _UpdateTimeStamp
		dataType: string
		isHidden
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	column _key_IWBSELEMENTDATA_2
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_IWBSELEMENTDATA_2

		annotation SummarizationSetBy = Automatic

	column _key_ICOSTCTRACTIVITYTYPE
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ICOSTCTRACTIVITYTYPE

		annotation SummarizationSetBy = Automatic

	column _key_ICUSTOMERGROUP
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: _key_ICUSTOMERGROUP

		annotation SummarizationSetBy = Automatic

	/// Reversal Reference Document Type.
	column REVERSALREFERENCEDOCUMENTTYPE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: REVERSALREFERENCEDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	/// Incomplete Summable Valuation Quantity Unit.
	column INCMPLTSUMMABLEVALNQTYUNT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: INCMPLTSUMMABLEVALNQTYUNT

		annotation SummarizationSetBy = Automatic

	/// Incomplete Summable Valuation Quantity.
	column INCMPLTSUMMABLEVALNQTY
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: INCMPLTSUMMABLEVALNQTY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Incomplete Summable Valuation Fix Quantity.
	column INCMPLTSUMMABLEVALNFXDQTY
		dataType: decimal
		sourceProviderType: decimal(23, 3)
		summarizeBy: none
		sourceColumn: INCMPLTSUMMABLEVALNFXDQTY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Journal Entry Item Category.
	column JOURNALENTRYITEMCATEGORY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: JOURNALENTRYITEMCATEGORY

		annotation SummarizationSetBy = Automatic

	/// Statistical Account Assignment Type 1.
	column STSTCLACCOUNTASSIGNMENTTYPE1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: STSTCLACCOUNTASSIGNMENTTYPE1

		annotation SummarizationSetBy = Automatic

	/// Statistical Account Assignment Type 2.
	column STSTCLACCOUNTASSIGNMENTTYPE2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: STSTCLACCOUNTASSIGNMENTTYPE2

		annotation SummarizationSetBy = Automatic

	/// Statistical Account Assignment Type 3.
	column STSTCLACCOUNTASSIGNMENTTYPE3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: STSTCLACCOUNTASSIGNMENTTYPE3

		annotation SummarizationSetBy = Automatic

	/// Commitment Item.
	column COMMITMENTITEM
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: COMMITMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Earmarked Funds Document.
	column EARMARKEDFUNDSDOCUMENT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: EARMARKEDFUNDSDOCUMENT

		annotation SummarizationSetBy = Automatic

	/// Earmarked Funds Document Item.
	column EARMARKEDFUNDSDOCUMENTITEM
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: EARMARKEDFUNDSDOCUMENTITEM

		annotation SummarizationSetBy = Automatic

	/// Financial Services Product Group.
	column FINANCIALSERVICESPRODUCTGROUP
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FINANCIALSERVICESPRODUCTGROUP

		annotation SummarizationSetBy = Automatic

	/// Financial Services Branch.
	column FINANCIALSERVICESBRANCH
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FINANCIALSERVICESBRANCH

		annotation SummarizationSetBy = Automatic

	/// Financial Data Source.
	column FINANCIALDATASOURCE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FINANCIALDATASOURCE

		annotation SummarizationSetBy = Automatic

	column ACCOUNTINGNOTIFICATIONUUID
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ACCOUNTINGNOTIFICATIONUUID

		annotation SummarizationSetBy = Automatic

	column JRNLPERIODENDCLOSINGRUNLOGUUID
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: JRNLPERIODENDCLOSINGRUNLOGUUID

		annotation SummarizationSetBy = Automatic

	/// Deletion indicator used by ETL or data processing logic.
	column _DELETE
		dataType: string
		isHidden
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: _DELETE

		annotation SummarizationSetBy = Automatic

	partition GLACCOUNTLINEITEMRAWDATA-3273179a-ff41-4971-b56e-213d0ceda9ef = m
		mode: directQuery
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_I_GLACCOUNTLINEITEMRAWDATA = Source{[Schema=Schema_Name,Item="I_GLACCOUNTLINEITEMRAWDATA"]}[Data]
				in
				    dmgold_I_GLACCOUNTLINEITEMRAWDATA

	annotation PBI_ResultType = Table
````

### LEDGER

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/LEDGER.tmdl). 12 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Ledger dimension containing financial ledger information
table LEDGER

	/// Primary Key for the table.
	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = User

	/// Timestamp indicating last update time in silver lakehouse.
	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	/// Name of the source system.
	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	/// Valuation View.
	column ACCOUNTINGVALUATIONVIEW
		dataType: string
		summarizeBy: none
		sourceColumn: ACCOUNTINGVALUATIONVIEW

		annotation SummarizationSetBy = Automatic

	/// Extension Ledger Type.
	column EXTENSIONLEDGERTYPE
		dataType: string
		summarizeBy: none
		sourceColumn: EXTENSIONLEDGERTYPE

		annotation SummarizationSetBy = Automatic

	/// Indicator: Leading Ledger.
	column ISLEADINGLEDGER
		dataType: string
		summarizeBy: none
		sourceColumn: ISLEADINGLEDGER

		annotation SummarizationSetBy = Automatic

	/// Ledger in General Ledger Accounting.
	column LEDGER
		dataType: string
		summarizeBy: none
		sourceColumn: LEDGER

		annotation SummarizationSetBy = Automatic

	/// Owner application.
	column LEDGERAPPLICATION
		dataType: string
		summarizeBy: none
		sourceColumn: LEDGERAPPLICATION

		annotation SummarizationSetBy = Automatic

	/// Subapplication.
	column LEDGERSUBAPPLICATION
		dataType: string
		summarizeBy: none
		sourceColumn: LEDGERSUBAPPLICATION

		annotation SummarizationSetBy = Automatic

	/// Ledger Type.
	column LEDGERTYPE
		dataType: string
		summarizeBy: none
		sourceColumn: LEDGERTYPE

		annotation SummarizationSetBy = Automatic

	/// Fallback Ledger.
	column REFERENCELEDGER
		dataType: string
		summarizeBy: none
		sourceColumn: REFERENCELEDGER

		annotation SummarizationSetBy = Automatic

	/// Technical ledger.
	column TECHNICALLEDGER
		dataType: string
		summarizeBy: none
		sourceColumn: TECHNICALLEDGER

		annotation SummarizationSetBy = Automatic

	partition LEDGER-4cb6c72e-e1d9-47c9-bb24-2ff54313a83d = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_I_LEDGER = Source{[Schema=Schema_Name,Item="I_LEDGER"]}[Data]
				in
				    dmgold_I_LEDGER

	annotation PBI_ResultType = Table
````

### LEDGERTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/LEDGERTEXT.tmdl). 41 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for ledger entries
table LEDGERTEXT

	column Key
		dataType: int64
		isHidden
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column LEDGER
		dataType: string
		summarizeBy: none
		sourceColumn: LEDGER

		annotation SummarizationSetBy = Automatic

	column ZH
		dataType: string
		summarizeBy: none
		sourceColumn: ZH

		annotation SummarizationSetBy = Automatic

	column TH
		dataType: string
		summarizeBy: none
		sourceColumn: TH

		annotation SummarizationSetBy = Automatic

	column KO
		dataType: string
		summarizeBy: none
		sourceColumn: KO

		annotation SummarizationSetBy = Automatic

	column RO
		dataType: string
		summarizeBy: none
		sourceColumn: RO

		annotation SummarizationSetBy = Automatic

	column SL
		dataType: string
		summarizeBy: none
		sourceColumn: SL

		annotation SummarizationSetBy = Automatic

	column HR
		dataType: string
		summarizeBy: none
		sourceColumn: HR

		annotation SummarizationSetBy = Automatic

	column UK
		dataType: string
		summarizeBy: none
		sourceColumn: UK

		annotation SummarizationSetBy = Automatic

	column ET
		dataType: string
		summarizeBy: none
		sourceColumn: ET

		annotation SummarizationSetBy = Automatic

	column AR
		dataType: string
		summarizeBy: none
		sourceColumn: AR

		annotation SummarizationSetBy = Automatic

	column HE
		dataType: string
		summarizeBy: none
		sourceColumn: HE

		annotation SummarizationSetBy = Automatic

	column CA
		dataType: string
		summarizeBy: none
		sourceColumn: CA

		annotation SummarizationSetBy = Automatic

	column CS
		dataType: string
		summarizeBy: none
		sourceColumn: CS

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column SH
		dataType: string
		summarizeBy: none
		sourceColumn: SH

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column EL
		dataType: string
		summarizeBy: none
		sourceColumn: EL

		annotation SummarizationSetBy = Automatic

	column HU
		dataType: string
		summarizeBy: none
		sourceColumn: HU

		annotation SummarizationSetBy = Automatic

	column IT
		dataType: string
		summarizeBy: none
		sourceColumn: IT

		annotation SummarizationSetBy = Automatic

	column JA
		dataType: string
		summarizeBy: none
		sourceColumn: JA

		annotation SummarizationSetBy = Automatic

	column DA
		dataType: string
		summarizeBy: none
		sourceColumn: DA

		annotation SummarizationSetBy = Automatic

	column PL
		dataType: string
		summarizeBy: none
		sourceColumn: PL

		annotation SummarizationSetBy = Automatic

	column ZF
		dataType: string
		summarizeBy: none
		sourceColumn: ZF

		annotation SummarizationSetBy = Automatic

	column NL
		dataType: string
		summarizeBy: none
		sourceColumn: NL

		annotation SummarizationSetBy = Automatic

	column NO
		dataType: string
		summarizeBy: none
		sourceColumn: NO

		annotation SummarizationSetBy = Automatic

	column PT
		dataType: string
		summarizeBy: none
		sourceColumn: PT

		annotation SummarizationSetBy = Automatic

	column SK
		dataType: string
		summarizeBy: none
		sourceColumn: SK

		annotation SummarizationSetBy = Automatic

	column RU
		dataType: string
		summarizeBy: none
		sourceColumn: RU

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	column TR
		dataType: string
		summarizeBy: none
		sourceColumn: TR

		annotation SummarizationSetBy = Automatic

	column FI
		dataType: string
		summarizeBy: none
		sourceColumn: FI

		annotation SummarizationSetBy = Automatic

	column SV
		dataType: string
		summarizeBy: none
		sourceColumn: SV

		annotation SummarizationSetBy = Automatic

	column BG
		dataType: string
		summarizeBy: none
		sourceColumn: BG

		annotation SummarizationSetBy = Automatic

	column LT
		dataType: string
		summarizeBy: none
		sourceColumn: LT

		annotation SummarizationSetBy = Automatic

	column LV
		dataType: string
		summarizeBy: none
		sourceColumn: LV

		annotation SummarizationSetBy = Automatic

	column HI
		dataType: string
		summarizeBy: none
		sourceColumn: HI

		annotation SummarizationSetBy = Automatic

	column KK
		dataType: string
		summarizeBy: none
		sourceColumn: KK

		annotation SummarizationSetBy = Automatic

	column VI
		dataType: string
		summarizeBy: none
		sourceColumn: VI

		annotation SummarizationSetBy = Automatic

	partition LEDGERTEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwLEDGERTEXT = Source{[Schema=Schema_Name,Item="vtLEDGERTEXT"]}[Data]
				in
				    dmgold_vwLEDGERTEXT

	annotation PBI_ResultType = Table
````

### PRODUCT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PRODUCT.tmdl). 152 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Product dimension with product details, categories, and hierarchies
table PRODUCT

	/// Timestamp indicating last update time in silver lakehouse.
	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		sourceProviderType: datetime2
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	/// Name of the source system.
	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: nvarchar(4000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	/// Product Category.
	column ARTICLECATEGORY
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: ARTICLECATEGORY

		annotation SummarizationSetBy = Automatic

	/// Assortment List Type.
	column ASSORTMENTLISTTYPE
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ASSORTMENTLISTTYPE

		annotation SummarizationSetBy = Automatic

	/// Base Unit of Measure.
	column BASEUNIT
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: BASEUNIT

		annotation SummarizationSetBy = Automatic

	/// Comparison price unit.
	column COMPARISONPRICEQUANTITY
		dataType: decimal
		sourceProviderType: decimal(5, 0)
		summarizeBy: none
		sourceColumn: COMPARISONPRICEQUANTITY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Competitor.
	column COMPETITORID
		dataType: string
		sourceProviderType: nvarchar(10)
		summarizeBy: none
		sourceColumn: COMPETITORID

		annotation SummarizationSetBy = Automatic

	/// Country/Region of Origin of Material (Non-Preferential Ori.).
	column COUNTRYOFORIGIN
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: COUNTRYOFORIGIN

		annotation SummarizationSetBy = Automatic

	/// Cross-Plant Configurable Product.
	column CROSSPLANTCONFIGURABLEPRODUCT
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: CROSSPLANTCONFIGURABLEPRODUCT

		annotation SummarizationSetBy = Automatic

	/// Cross-Plant Product Status.
	column CROSSPLANTSTATUS
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: CROSSPLANTSTATUS

		annotation SummarizationSetBy = Automatic

	/// Date from which the cross-plant material status is valid.
	column CROSSPLANTSTATUSVALIDITYDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: CROSSPLANTSTATUSVALIDITYDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Dangerous Goods Indicator Profile.
	column DANGEROUSGOODSINDPROFILE
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: DANGEROUSGOODSINDPROFILE

		annotation SummarizationSetBy = Automatic

	/// Division.
	column DIVISION
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: DIVISION

		annotation SummarizationSetBy = Automatic

	/// External Product Group.
	column EXTERNALPRODUCTGROUP
		dataType: string
		sourceProviderType: nvarchar(18)
		summarizeBy: none
		sourceColumn: EXTERNALPRODUCTGROUP

		annotation SummarizationSetBy = Automatic

	/// Gross contents.
	column GROSSCONTENT
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: GROSSCONTENT

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Gross Weight.
	column GROSSWEIGHT
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: GROSSWEIGHT

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Empties Bill of Material.
	column HASEMPTIESBOM
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: HASEMPTIESBOM

		annotation SummarizationSetBy = Automatic

	/// Indicator: Contains Non-Textile Parts of Animal Origin.
	column HASTEXTILEPARTSWTHANIMALORIGIN
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: HASTEXTILEPARTSWTHANIMALORIGIN

		annotation SummarizationSetBy = Automatic

	/// Industry.
	column INDUSTRYSECTOR
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: INDUSTRYSECTOR

		annotation SummarizationSetBy = Automatic

	/// Industry Standard Description (such as ANSI or ISO).
	column INDUSTRYSTANDARDNAME
		dataType: string
		sourceProviderType: nvarchar(18)
		summarizeBy: none
		sourceColumn: INDUSTRYSTANDARDNAME

		annotation SummarizationSetBy = Automatic

	/// Draft - Indicator - Is active document.
	column ISACTIVEENTITY
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISACTIVEENTITY

		annotation SummarizationSetBy = Automatic

	/// Approved Batch Record Required.
	column ISAPPROVEDBATCHRECORDREQD
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISAPPROVEDBATCHRECORDREQD

		annotation SummarizationSetBy = Automatic

	/// Batch Management Requirement Indicator.
	column ISBATCHMANAGEMENTREQUIRED
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISBATCHMANAGEMENTREQUIRED

		annotation SummarizationSetBy = Automatic

	/// Chemical Compliance Relevance Indicator.
	column ISCHEMICALCOMPLIANCERELEVANT
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISCHEMICALCOMPLIANCERELEVANT

		annotation SummarizationSetBy = Automatic

	/// Deletion Indicator.
	column ISMARKEDFORDELETION
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISMARKEDFORDELETION

		annotation SummarizationSetBy = Automatic

	/// Pilferable.
	column ISPILFERABLE
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISPILFERABLE

		annotation SummarizationSetBy = Automatic

	/// Relevant for Hazardous Substances.
	column ISRELEVANTFORHZDSSUBSTANCES
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: ISRELEVANTFORHZDSSUBSTANCES

		annotation SummarizationSetBy = Automatic

	/// General item category group.
	column ITEMCATEGORYGROUP
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: ITEMCATEGORYGROUP

		annotation SummarizationSetBy = Automatic

	/// Low-Level Code.
	column LOWLEVELCODE
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: LOWLEVELCODE

		annotation SummarizationSetBy = Automatic

	/// Volume.
	column MATERIALVOLUME
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: MATERIALVOLUME

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Net Weight.
	column NETWEIGHT
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: NETWEIGHT

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	/// Material Group: Packaging Materials.
	column PACKAGINGMATERIALGROUP
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: PACKAGINGMATERIALGROUP

		annotation SummarizationSetBy = Automatic

	/// Preferred Alternative UoM for Warehouse Operations.
	column PREFERREDUNITOFMEASURE
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: PREFERREDUNITOFMEASURE

		annotation SummarizationSetBy = Automatic

	/// Procurement rule.
	column PROCUREMENTRULE
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: PROCUREMENTRULE

		annotation SummarizationSetBy = Automatic

	/// Environmentally Relevant.
	column PRODISENVIRONMENTALLYRELEVANT
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: PRODISENVIRONMENTALLYRELEVANT

		annotation SummarizationSetBy = Automatic

	/// Product Number.
	column PRODUCT
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: PRODUCT

		annotation SummarizationSetBy = Automatic

	/// Product Category.
	column PRODUCTCATEGORY
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: PRODUCTCATEGORY

		annotation SummarizationSetBy = Automatic

	/// External Representation of Material Number.
	column PRODUCTEXTERNALID
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: PRODUCTEXTERNALID

		annotation SummarizationSetBy = Automatic

	/// Product Group.
	column PRODUCTGROUP
		dataType: string
		sourceProviderType: nvarchar(9)
		summarizeBy: none
		sourceColumn: PRODUCTGROUP

		annotation SummarizationSetBy = Automatic

	/// Product Hierarchy.
	column PRODUCTHIERARCHY
		dataType: string
		sourceProviderType: nvarchar(18)
		summarizeBy: none
		sourceColumn: PRODUCTHIERARCHY

		annotation SummarizationSetBy = Automatic

	/// Product is Configurable.
	column PRODUCTISCONFIGURABLE
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: PRODUCTISCONFIGURABLE

		annotation SummarizationSetBy = Automatic

	/// Indicator: Highly Viscous.
	column PRODUCTISHIGHLYVISCOUS
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: PRODUCTISHIGHLYVISCOUS

		annotation SummarizationSetBy = Automatic

	/// Unit of Dimension for Length/Width/Height.
	column PRODUCTMEASUREMENTUNIT
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: PRODUCTMEASUREMENTUNIT

		annotation SummarizationSetBy = Automatic

	/// Indicator: Use of Season.
	column PRODUCTSEASONUSAGECATEGORY
		dataType: string
		sourceProviderType: nvarchar(1)
		summarizeBy: none
		sourceColumn: PRODUCTSEASONUSAGECATEGORY

		annotation SummarizationSetBy = Automatic

	/// Global Trade Item Number (EAN/UPC/GTIN).
	column PRODUCTSTANDARDID
		dataType: string
		sourceProviderType: nvarchar(18)
		summarizeBy: none
		sourceColumn: PRODUCTSTANDARDID

		annotation SummarizationSetBy = Automatic

	/// Product Type.
	column PRODUCTTYPE
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: PRODUCTTYPE

		annotation SummarizationSetBy = Automatic

	/// Deletion date.
	column PRODUCTVALIDENDDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: PRODUCTVALIDENDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Valid-From Date.
	column PRODUCTVALIDSTARTDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: PRODUCTVALIDSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Purchase Order Unit of Measure.
	column PURCHASEORDERQUANTITYUNIT
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: PURCHASEORDERQUANTITYUNIT

		annotation SummarizationSetBy = Automatic

	/// Material Number of a Sales Material.
	column SALESPRODUCT
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: SALESPRODUCT

		annotation SummarizationSetBy = Automatic

	/// Cross-Distribution-Chain Material Status.
	column SALESSTATUS
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: SALESSTATUS

		annotation SummarizationSetBy = Automatic

	/// Date from which the X-distr.-chain material status is valid.
	column SALESSTATUSVALIDITYDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: SALESSTATUSVALIDITYDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Serial Number Profile.
	column SERIALIDENTIFIERASSGMTPROFILE
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: SERIALIDENTIFIERASSGMTPROFILE

		annotation SummarizationSetBy = Automatic

	/// Size/dimensions.
	column SIZEORDIMENSIONTEXT
		dataType: string
		sourceProviderType: nvarchar(32)
		summarizeBy: none
		sourceColumn: SIZEORDIMENSIONTEXT

		annotation SummarizationSetBy = Automatic

	/// Valid-From Date.
	column VALIDITYSTARTDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: VALIDITYSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	/// Volume Unit.
	column VOLUMEUNIT
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: VOLUMEUNIT

		annotation SummarizationSetBy = Automatic

	/// Warehouse Material Group.
	column WAREHOUSEPRODUCTGROUP
		dataType: string
		sourceProviderType: nvarchar(4)
		summarizeBy: none
		sourceColumn: WAREHOUSEPRODUCTGROUP

		annotation SummarizationSetBy = Automatic

	/// Warehouse Storage Condition.
	column WAREHOUSESTORAGECONDITION
		dataType: string
		sourceProviderType: nvarchar(2)
		summarizeBy: none
		sourceColumn: WAREHOUSESTORAGECONDITION

		annotation SummarizationSetBy = Automatic

	/// Unit of Weight.
	column WEIGHTUNIT
		dataType: string
		sourceProviderType: nvarchar(3)
		summarizeBy: none
		sourceColumn: WEIGHTUNIT

		annotation SummarizationSetBy = Automatic

	column Key
		dataType: int64
		isHidden
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column PRODUCTOID
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTOID

		annotation SummarizationSetBy = Automatic

	column CREATIONDATE
		dataType: dateTime
		formatString: Long Date
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: CREATIONDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column CREATIONTIME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CREATIONTIME

		annotation SummarizationSetBy = Automatic

	column CREATIONDATETIME
		dataType: double
		sourceProviderType: decimal(21, 7)
		summarizeBy: none
		sourceColumn: CREATIONDATETIME

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column CREATEDBYUSER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CREATEDBYUSER

		annotation SummarizationSetBy = Automatic

	column LASTCHANGEDATE
		dataType: dateTime
		formatString: Long Date
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: LASTCHANGEDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column LASTCHANGEDBYUSER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: LASTCHANGEDBYUSER

		annotation SummarizationSetBy = Automatic

	column PRODUCTOLDID
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTOLDID

		annotation SummarizationSetBy = Automatic

	column SOURCEOFSUPPLY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SOURCEOFSUPPLY

		annotation SummarizationSetBy = Automatic

	column VARBLPURORDUNITISACTIVE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: VARBLPURORDUNITISACTIVE

		annotation SummarizationSetBy = Automatic

	column TRANSPORTATIONGROUP
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TRANSPORTATIONGROUP

		annotation SummarizationSetBy = Automatic

	column AUTHORIZATIONGROUP
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: AUTHORIZATIONGROUP

		annotation SummarizationSetBy = Automatic

	column ANPCODE
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: ANPCODE

		annotation SummarizationSetBy = Automatic

	column BRAND
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BRAND

		annotation SummarizationSetBy = Automatic

	column PRODNOINGENPRODINPREPACKPROD
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODNOINGENPRODINPREPACKPROD

		annotation SummarizationSetBy = Automatic

	column INTERNATIONALARTICLENUMBERCAT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: INTERNATIONALARTICLENUMBERCAT

		annotation SummarizationSetBy = Automatic

	column SERIALNOEXPLICITNESSLEVEL
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SERIALNOEXPLICITNESSLEVEL

		annotation SummarizationSetBy = Automatic

	column PRODUCTMANUFACTURERNUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTMANUFACTURERNUMBER

		annotation SummarizationSetBy = Automatic

	column MANUFACTURERNUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: MANUFACTURERNUMBER

		annotation SummarizationSetBy = Automatic

	column MANUFACTURERPARTPROFILE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: MANUFACTURERPARTPROFILE

		annotation SummarizationSetBy = Automatic

	column QLTYMGMTINPROCMTISACTIVE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: QLTYMGMTINPROCMTISACTIVE

		annotation SummarizationSetBy = Automatic

	column HANDLINGINDICATOR
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: HANDLINGINDICATOR

		annotation SummarizationSetBy = Automatic

	column STANDARDHANDLINGUNITTYPE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: STANDARDHANDLINGUNITTYPE

		annotation SummarizationSetBy = Automatic

	column SERIALNUMBERPROFILE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SERIALNUMBERPROFILE

		annotation SummarizationSetBy = Automatic

	column ADJUSTMENTPROFILE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: ADJUSTMENTPROFILE

		annotation SummarizationSetBy = Automatic

	column QUARANTINEPERIOD
		dataType: decimal
		sourceProviderType: decimal(17, 0)
		summarizeBy: none
		sourceColumn: QUARANTINEPERIOD

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column TIMEUNITFORQUARANTINEPERIOD
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TIMEUNITFORQUARANTINEPERIOD

		annotation SummarizationSetBy = Automatic

	column QUALITYINSPECTIONGROUP
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: QUALITYINSPECTIONGROUP

		annotation SummarizationSetBy = Automatic

	column HANDLINGUNITTYPE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: HANDLINGUNITTYPE

		annotation SummarizationSetBy = Automatic

	column HASVARIABLETAREWEIGHT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: HASVARIABLETAREWEIGHT

		annotation SummarizationSetBy = Automatic

	column MAXIMUMPACKAGINGLENGTH
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: MAXIMUMPACKAGINGLENGTH

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column MAXIMUMPACKAGINGWIDTH
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: MAXIMUMPACKAGINGWIDTH

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column MAXIMUMPACKAGINGHEIGHT
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: MAXIMUMPACKAGINGHEIGHT

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column MAXIMUMCAPACITY
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: MAXIMUMCAPACITY

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column OVERCAPACITYTOLERANCE
		dataType: decimal
		sourceProviderType: decimal(17, 1)
		summarizeBy: none
		sourceColumn: OVERCAPACITYTOLERANCE

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column UNITFORMAXPACKAGINGDIMENSIONS
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: UNITFORMAXPACKAGINGDIMENSIONS

		annotation SummarizationSetBy = Automatic

	column BASEUNITSPECIFICPRODUCTLENGTH
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: BASEUNITSPECIFICPRODUCTLENGTH

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column BASEUNITSPECIFICPRODUCTWIDTH
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: BASEUNITSPECIFICPRODUCTWIDTH

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column BASEUNITSPECIFICPRODUCTHEIGHT
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: BASEUNITSPECIFICPRODUCTHEIGHT

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column CONTENTUNIT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CONTENTUNIT

		annotation SummarizationSetBy = Automatic

	column NETCONTENT
		dataType: decimal
		sourceProviderType: decimal(17, 3)
		summarizeBy: none
		sourceColumn: NETCONTENT

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column CHANGENUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CHANGENUMBER

		annotation SummarizationSetBy = Automatic

	column MATERIALREVISIONLEVEL
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: MATERIALREVISIONLEVEL

		annotation SummarizationSetBy = Automatic

	column LASTCHANGEDATETIME
		dataType: double
		sourceProviderType: decimal(21, 7)
		summarizeBy: none
		sourceColumn: LASTCHANGEDATETIME

		annotation SummarizationSetBy = Automatic

		annotation PBI_FormatHint = {"isGeneralNumber":true}

	column LASTCHANGETIME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: LASTCHANGETIME

		annotation SummarizationSetBy = Automatic

	column PRODSUPCHNMGMTUUID22
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODSUPCHNMGMTUUID22

		annotation SummarizationSetBy = Automatic

	column PRODUCTDOCUMENTCHANGENUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTDOCUMENTCHANGENUMBER

		annotation SummarizationSetBy = Automatic

	column PRODUCTDOCUMENTPAGECOUNT
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PRODUCTDOCUMENTPAGECOUNT

		annotation SummarizationSetBy = Automatic

	column PRODUCTDOCUMENTPAGENUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTDOCUMENTPAGENUMBER

		annotation SummarizationSetBy = Automatic

	column OWNINVENTORYMANAGEDPRODUCT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: OWNINVENTORYMANAGEDPRODUCT

		annotation SummarizationSetBy = Automatic

	column DOCUMENTISCREATEDBYCAD
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DOCUMENTISCREATEDBYCAD

		annotation SummarizationSetBy = Automatic

	column PRODUCTIONORINSPECTIONMEMOTXT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTIONORINSPECTIONMEMOTXT

		annotation SummarizationSetBy = Automatic

	column PRODUCTIONMEMOPAGEFORMAT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTIONMEMOPAGEFORMAT

		annotation SummarizationSetBy = Automatic

	column GLOBALTRADEITEMNUMBERVARIANT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: GLOBALTRADEITEMNUMBERVARIANT

		annotation SummarizationSetBy = Automatic

	column TRANSPORTISINBULK
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: TRANSPORTISINBULK

		annotation SummarizationSetBy = Automatic

	column PRODALLOCDETNPROCEDURE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODALLOCDETNPROCEDURE

		annotation SummarizationSetBy = Automatic

	column PRODEFFCTYPARAMVALSAREASSIGNED
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODEFFCTYPARAMVALSAREASSIGNED

		annotation SummarizationSetBy = Automatic

	column LABORATORYORDESIGNOFFICE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: LABORATORYORDESIGNOFFICE

		annotation SummarizationSetBy = Automatic

	column PRODUCTISLOCKED
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTISLOCKED

		annotation SummarizationSetBy = Automatic

	column DISCOUNTINKINDELIGIBILITY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DISCOUNTINKINDELIGIBILITY

		annotation SummarizationSetBy = Automatic

	column SMARTFORMNAME
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SMARTFORMNAME

		annotation SummarizationSetBy = Automatic

	column PACKINGREFERENCEPRODUCT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PACKINGREFERENCEPRODUCT

		annotation SummarizationSetBy = Automatic

	column BASICMATERIAL
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: BASICMATERIAL

		annotation SummarizationSetBy = Automatic

	column PRODUCTDOCUMENTNUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTDOCUMENTNUMBER

		annotation SummarizationSetBy = Automatic

	column PRODUCTDOCUMENTVERSION
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTDOCUMENTVERSION

		annotation SummarizationSetBy = Automatic

	column PRODUCTDOCUMENTTYPE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTDOCUMENTTYPE

		annotation SummarizationSetBy = Automatic

	column PRODUCTDOCUMENTPAGEFORMAT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTDOCUMENTPAGEFORMAT

		annotation SummarizationSetBy = Automatic

	column PRODUCTCONFIGURATION
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PRODUCTCONFIGURATION

		annotation SummarizationSetBy = Automatic

	column SEGMENTATIONSTRATEGY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SEGMENTATIONSTRATEGY

		annotation SummarizationSetBy = Automatic

	column SEGMENTATIONISRELEVANT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SEGMENTATIONISRELEVANT

		annotation SummarizationSetBy = Automatic

	column PRODUCTCOMPOSITIONISRELEVANT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTCOMPOSITIONISRELEVANT

		annotation SummarizationSetBy = Automatic

	column MANUFACTURERBOOKPARTNUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: MANUFACTURERBOOKPARTNUMBER

		annotation SummarizationSetBy = Automatic

	column LOGISTICALPRODUCTCATEGORY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: LOGISTICALPRODUCTCATEGORY

		annotation SummarizationSetBy = Automatic

	column PRODCHARC1INTERNALNUMBER
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PRODCHARC1INTERNALNUMBER

		annotation SummarizationSetBy = Automatic

	column PRODCHARC2INTERNALNUMBER
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PRODCHARC2INTERNALNUMBER

		annotation SummarizationSetBy = Automatic

	column PRODCHARC3INTERNALNUMBER
		dataType: int64
		formatString: 0
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: PRODCHARC3INTERNALNUMBER

		annotation SummarizationSetBy = Automatic

	column PRODUCTCHARACTERISTIC1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTCHARACTERISTIC1

		annotation SummarizationSetBy = Automatic

	column PRODUCTCHARACTERISTIC2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTCHARACTERISTIC2

		annotation SummarizationSetBy = Automatic

	column PRODUCTCHARACTERISTIC3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTCHARACTERISTIC3

		annotation SummarizationSetBy = Automatic

	column MAINTENANCESTATUS
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: MAINTENANCESTATUS

		annotation SummarizationSetBy = Automatic

	column FASHIONPRODINFORMATIONFIELD1
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FASHIONPRODINFORMATIONFIELD1

		annotation SummarizationSetBy = Automatic

	column FASHIONPRODINFORMATIONFIELD2
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FASHIONPRODINFORMATIONFIELD2

		annotation SummarizationSetBy = Automatic

	column FASHIONPRODINFORMATIONFIELD3
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: FASHIONPRODINFORMATIONFIELD3

		annotation SummarizationSetBy = Automatic

	column DFSAMMUNITIONGROUPCODE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSAMMUNITIONGROUPCODE

		annotation SummarizationSetBy = Automatic

	column DFSRICIDENTIFIER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSRICIDENTIFIER

		annotation SummarizationSetBy = Automatic

	column DFSPRODUCTSENSITIVITY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSPRODUCTSENSITIVITY

		annotation SummarizationSetBy = Automatic

	column DFSMANUFACTURERPARTLONGNUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSMANUFACTURERPARTLONGNUMBER

		annotation SummarizationSetBy = Automatic

	column DFSMATLCONDITIONMGMT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSMATLCONDITIONMGMT

		annotation SummarizationSetBy = Automatic

	column DFSRETURNDELIVERY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSRETURNDELIVERY

		annotation SummarizationSetBy = Automatic

	column DFSLOGISTICSLEVEL
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSLOGISTICSLEVEL

		annotation SummarizationSetBy = Automatic

	column DFSNATIONALITEMIDNNUMBER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: DFSNATIONALITEMIDNNUMBER

		annotation SummarizationSetBy = Automatic

	column PRODUCTUUID
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PRODUCTUUID

		annotation SummarizationSetBy = Automatic

	partition PRODUCT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_I_PRODUCT = Source{[Schema=Schema_Name,Item="I_PRODUCT"]}[Data]
				in
				    dmgold_I_PRODUCT

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### PRODUCTGROUP2TEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PRODUCTGROUP2TEXT.tmdl). 7 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for product group level 2
table PRODUCTGROUP2TEXT

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: nvarchar(4000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column PRODUCTGROUP
		dataType: string
		sourceProviderType: nvarchar(9)
		summarizeBy: none
		sourceColumn: PRODUCTGROUP

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		sourceProviderType: nvarchar(20)
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		sourceProviderType: nvarchar(20)
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		sourceProviderType: nvarchar(20)
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		sourceProviderType: nvarchar(20)
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	partition PRODUCTGROUP2TEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vtPRODUCTGROUP_2TEXT = Source{[Schema=Schema_Name,Item="vtPRODUCTGROUP_2TEXT"]}[Data],
				    #"Columns removed by Measure Killer"= Table.RemoveColumns(dmgold_vtPRODUCTGROUP_2TEXT,{"ZH","RO","LT","LV","PL","KK","AR","SV","ET","HU","TH","NL","HI","DA","HR","JA","TR","NO","PT","EL","KO","CS","IT","ZF","VI","HE","UK","SL","SK","FI","SH","CA","BG","RU"})
				in
				    #"Columns removed by Measure Killer"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### PRODUCTTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PRODUCTTEXT.tmdl). 6 columns; 1 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for product entries
table PRODUCTTEXT

	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: nvarchar(4000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column PRODUCT
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: PRODUCT

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		sourceProviderType: nvarchar(40)
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	partition PRODUCTTEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vtPRODUCTTEXT = Source{[Schema=Schema_Name,Item="vtPRODUCTTEXT"]}[Data],
				    #"Columns removed by Measure Killer"= Table.RemoveColumns(dmgold_vtPRODUCTTEXT,{"RU","ZH","RO","LT","Key","LV","PL","KK","AR","SV","ET","HU","TH","NL","HI","DA","HR","BG","JA","TR","NO","PT","EL","KO","ZF","IT","CS","VI","HE","SL","UK","SK","FI","SH","CA"})
				in
				    #"Columns removed by Measure Killer"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### PROFITCENTER

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PROFITCENTER.tmdl). 9 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Profit center dimension for cost allocation and profitability analysis
table PROFITCENTER

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: m/d/yyyy
		sourceProviderType: datetime2
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column CONTROLLINGAREA
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: CONTROLLINGAREA

		annotation SummarizationSetBy = Automatic

	column LANGUAGE
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: LANGUAGE

		annotation SummarizationSetBy = Automatic

	column PROFITCENTER
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PROFITCENTER

		annotation SummarizationSetBy = Automatic

	column PROFITCENTERSTANDARDHIERARCHY
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: PROFITCENTERSTANDARDHIERARCHY

		annotation SummarizationSetBy = Automatic

	column VALIDITYSTARTDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: VALIDITYSTARTDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	column VALIDITYENDDATE
		dataType: dateTime
		formatString: m/d/yyyy
		sourceProviderType: date
		summarizeBy: none
		sourceColumn: VALIDITYENDDATE

		annotation SummarizationSetBy = Automatic

		annotation UnderlyingDateTimeDataType = Date

	partition PROFITCENTER = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dbo_vPROFITCENTER = Source{[Schema=Schema_Name,Item="vPROFITCENTER"]}[Data],
				  #"Choose columns" = Table.SelectColumns(dbo_vPROFITCENTER, {"Key", "_UpdateTimeStamp", "_SystemName", "CONTROLLINGAREA", "LANGUAGE", "PROFITCENTER", "PROFITCENTERSTANDARDHIERARCHY", "VALIDITYSTARTDATE", "VALIDITYENDDATE"})
				in
				    #"Choose columns"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### PROFITCENTERTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/PROFITCENTERTEXT.tmdl). 8 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for profit center entries
table PROFITCENTERTEXT

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column CONTROLLINGAREA
		dataType: string
		summarizeBy: none
		sourceColumn: CONTROLLINGAREA

		annotation SummarizationSetBy = Automatic

	column PROFITCENTER
		dataType: string
		summarizeBy: none
		sourceColumn: PROFITCENTER

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	partition PROFITCENTERTEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwPROFITCENTERTEXT = Source{[Schema=Schema_Name,Item="vtPROFITCENTERTEXT"]}[Data],
				    #"Columns removed by Measure Killer"= Table.RemoveColumns(dmgold_vwPROFITCENTERTEXT,{"CS","VI","HE","SL","UK","SK","FI","SH","CA","BG","RU","ZH","RO","LT","LV","PL","KK","AR","SV","ET","HU","TH","NL","ZF","HI","DA","HR","JA","TR","NO","PT","EL","KO","IT"})
				in
				    #"Columns removed by Measure Killer"

	annotation PBI_ResultType = Table

	annotation PBI_NavigationStepName = Navigation
````

### SAPLANGUAGE

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/SAPLANGUAGE.tmdl). 5 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
table SAPLANGUAGE

	column LANGUAGE
		dataType: string
		summarizeBy: none
		sourceColumn: LANGUAGE

		annotation SummarizationSetBy = Automatic

	column _ISOLanguage
		dataType: string
		isHidden
		isKey
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _ISOLanguage

		annotation SummarizationSetBy = Automatic

	column LANGUAGENAME
		dataType: string
		summarizeBy: none
		sourceColumn: LANGUAGENAME

		annotation SummarizationSetBy = Automatic

	column LANGUAGECODE
		dataType: string
		summarizeBy: none
		sourceColumn: LANGUAGECODE

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	partition SAPLANGUAGE = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwSAPLANGUAGE = Source{[Schema=Schema_Name,Item="SAPLANGUAGE"]}[Data],
				    #"Filtered Rows" = Table.SelectRows(dmgold_vwSAPLANGUAGE, each ([_ISOLanguage] = "DE" or [_ISOLanguage] = "EN" or [_ISOLanguage] = "ES" or [_ISOLanguage] = "FR"))
				in
				    #"Filtered Rows"

	annotation PBI_ResultType = Table
````

### SEGMENT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/SEGMENT.tmdl). 4 columns; 3 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Business segment dimension for financial reporting
table SEGMENT

	column SEGMENT
		dataType: string
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: SEGMENT

		annotation SummarizationSetBy = Automatic

	column _UpdateTimeStamp
		dataType: dateTime
		isHidden
		formatString: General Date
		sourceProviderType: datetime2
		summarizeBy: none
		sourceColumn: _UpdateTimeStamp

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		sourceProviderType: varchar(8000)
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		sourceProviderType: int
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	partition SEGMENT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwSEGMENTTEXT = Source{[Schema=Schema_Name,Item="I_SEGMENT"]}[Data]
				in
				    dmgold_vwSEGMENTTEXT

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Table
````

### SEGMENTTEXT

[Source TMDL](../Record_to_Report_Financial_Insights.SemanticModel/definition/tables/SEGMENTTEXT.tmdl). 41 columns; 2 hidden columns; 0 calculated columns; 0 measures; m partition; dual mode.

````tmdl
/// Text descriptions for segment entries
table SEGMENTTEXT

	column Key
		dataType: int64
		isHidden
		isKey
		formatString: 0
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: Key

		annotation SummarizationSetBy = Automatic

	column _SystemName
		dataType: string
		isHidden
		isAvailableInMdx: false
		summarizeBy: none
		sourceColumn: _SystemName

		annotation SummarizationSetBy = Automatic

	column SEGMENT
		dataType: string
		summarizeBy: none
		sourceColumn: SEGMENT

		annotation SummarizationSetBy = Automatic

	column ZH
		dataType: string
		summarizeBy: none
		sourceColumn: ZH

		annotation SummarizationSetBy = Automatic

	column TH
		dataType: string
		summarizeBy: none
		sourceColumn: TH

		annotation SummarizationSetBy = Automatic

	column KO
		dataType: string
		summarizeBy: none
		sourceColumn: KO

		annotation SummarizationSetBy = Automatic

	column RO
		dataType: string
		summarizeBy: none
		sourceColumn: RO

		annotation SummarizationSetBy = Automatic

	column SL
		dataType: string
		summarizeBy: none
		sourceColumn: SL

		annotation SummarizationSetBy = Automatic

	column HR
		dataType: string
		summarizeBy: none
		sourceColumn: HR

		annotation SummarizationSetBy = Automatic

	column UK
		dataType: string
		summarizeBy: none
		sourceColumn: UK

		annotation SummarizationSetBy = Automatic

	column ET
		dataType: string
		summarizeBy: none
		sourceColumn: ET

		annotation SummarizationSetBy = Automatic

	column AR
		dataType: string
		summarizeBy: none
		sourceColumn: AR

		annotation SummarizationSetBy = Automatic

	column HE
		dataType: string
		summarizeBy: none
		sourceColumn: HE

		annotation SummarizationSetBy = Automatic

	column CA
		dataType: string
		summarizeBy: none
		sourceColumn: CA

		annotation SummarizationSetBy = Automatic

	column CS
		dataType: string
		summarizeBy: none
		sourceColumn: CS

		annotation SummarizationSetBy = Automatic

	column DE
		dataType: string
		summarizeBy: none
		sourceColumn: DE

		annotation SummarizationSetBy = Automatic

	column SH
		dataType: string
		summarizeBy: none
		sourceColumn: SH

		annotation SummarizationSetBy = Automatic

	column EN
		dataType: string
		summarizeBy: none
		sourceColumn: EN

		annotation SummarizationSetBy = Automatic

	column FR
		dataType: string
		summarizeBy: none
		sourceColumn: FR

		annotation SummarizationSetBy = Automatic

	column EL
		dataType: string
		summarizeBy: none
		sourceColumn: EL

		annotation SummarizationSetBy = Automatic

	column HU
		dataType: string
		summarizeBy: none
		sourceColumn: HU

		annotation SummarizationSetBy = Automatic

	column IT
		dataType: string
		summarizeBy: none
		sourceColumn: IT

		annotation SummarizationSetBy = Automatic

	column JA
		dataType: string
		summarizeBy: none
		sourceColumn: JA

		annotation SummarizationSetBy = Automatic

	column DA
		dataType: string
		summarizeBy: none
		sourceColumn: DA

		annotation SummarizationSetBy = Automatic

	column PL
		dataType: string
		summarizeBy: none
		sourceColumn: PL

		annotation SummarizationSetBy = Automatic

	column ZF
		dataType: string
		summarizeBy: none
		sourceColumn: ZF

		annotation SummarizationSetBy = Automatic

	column NL
		dataType: string
		summarizeBy: none
		sourceColumn: NL

		annotation SummarizationSetBy = Automatic

	column NO
		dataType: string
		summarizeBy: none
		sourceColumn: NO

		annotation SummarizationSetBy = Automatic

	column PT
		dataType: string
		summarizeBy: none
		sourceColumn: PT

		annotation SummarizationSetBy = Automatic

	column SK
		dataType: string
		summarizeBy: none
		sourceColumn: SK

		annotation SummarizationSetBy = Automatic

	column RU
		dataType: string
		summarizeBy: none
		sourceColumn: RU

		annotation SummarizationSetBy = Automatic

	column ES
		dataType: string
		summarizeBy: none
		sourceColumn: ES

		annotation SummarizationSetBy = Automatic

	column TR
		dataType: string
		summarizeBy: none
		sourceColumn: TR

		annotation SummarizationSetBy = Automatic

	column FI
		dataType: string
		summarizeBy: none
		sourceColumn: FI

		annotation SummarizationSetBy = Automatic

	column SV
		dataType: string
		summarizeBy: none
		sourceColumn: SV

		annotation SummarizationSetBy = Automatic

	column BG
		dataType: string
		summarizeBy: none
		sourceColumn: BG

		annotation SummarizationSetBy = Automatic

	column LT
		dataType: string
		summarizeBy: none
		sourceColumn: LT

		annotation SummarizationSetBy = Automatic

	column LV
		dataType: string
		summarizeBy: none
		sourceColumn: LV

		annotation SummarizationSetBy = Automatic

	column HI
		dataType: string
		summarizeBy: none
		sourceColumn: HI

		annotation SummarizationSetBy = Automatic

	column KK
		dataType: string
		summarizeBy: none
		sourceColumn: KK

		annotation SummarizationSetBy = Automatic

	column VI
		dataType: string
		summarizeBy: none
		sourceColumn: VI

		annotation SummarizationSetBy = Automatic

	partition SEGMENTTEXT = m
		mode: dual
		source =
				let
				    Source = Sql.Database(Server, Database),
				    dmgold_vwSEGMENTTEXT = Source{[Schema=Schema_Name,Item="vtSEGMENTTEXT"]}[Data]
				in
				    dmgold_vwSEGMENTTEXT

	annotation PBI_ResultType = Table
````

## Report page and visual inventory

### Trial Balance — e9a0daa552c5be7f88d0

[Page definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/page.json). 1280 × 900; FitToPage; 21 visual containers. Active authoring page: True.

Page configuration (including all page-level filtering, drillthrough and interaction metadata if authored):

```json
{"$schema":"https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json","name":"e9a0daa552c5be7f88d0","displayName":"Trial Balance","displayOption":"FitToPage","height":900,"width":1280}
```

| Container | Type | Authored labels | Bound fields / measures |
|---|---|---|---|
| [071471fa20a68fa054f9](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/071471fa20a68fa054f9/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Field' |  |
| [1e7cb142cc39d2ed9a8b](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/1e7cb142cc39d2ed9a8b/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Trial Balance |  |
| [29eb14c3ea3fbdde208c](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/29eb14c3ea3fbdde208c/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS; Column: _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS |
| [2bad24393298c417e966](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/2bad24393298c417e966/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=ProfitCenterText; .visual.objects.header[0].properties.text='Profit Center' | queryRef: PROFITCENTERTEXT.EN; Column: PROFITCENTERTEXT.EN; Column: _PROFITCENTERTEXT.FIELD_PARAM_PROFITCENTERTEXT; Column: PROFITCENTERTEXT.DE; Column: p.DE |
| [2c604992f5e3ae683475](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/2c604992f5e3ae683475/visual.json) | pivotTable | .visual.query.queryState.Columns.projections[0].displayName=Transaction Currency; .visual.query.queryState.Columns.projections[1].displayName=Debit/Credit; .visual.query.queryState.Rows.projections[1].displayName=GL Account Name; .visual.query.queryState.Rows.projections[2].displayName=GLACCOUNTGROUP; .visual.query.queryState.Rows.projections[3].displayName=PROFITCENTER; .visual.query.queryState.Rows.projections[4].displayName=COSTCENTER; .visual.query.queryState.Rows.projections[5].displayName=COMPANYCODE; .visual.query.queryState.Rows.projections[6].displayName=PARTNERCOMPANYCODE; .visual.query.queryState.Rows.projections[7].displayName=TAXCODE; .visual.query.queryState.Rows.projections[8].displayName=TAXCOUNTRY; .visual.query.queryState.Values.projections[0].displayName=Current Period; .visual.visualContainerObjects.title[0].properties.text='Accounting Documents' | queryRef: AGGR_H.TRANSACTIONCURRENCY; Column: AGGR_H.TRANSACTIONCURRENCY; queryRef: DEBITCREDITCODETEXT.EN; Column: DEBITCREDITCODETEXT.EN; Column: _DEBITCREDITCODETEXT.FIELD_PARAM_DEBITCREDITCODETEXT; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; queryRef: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; Column: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; queryRef: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; Column: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; queryRef: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP; Column: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP; queryRef: PROFITCENTER.PROFITCENTER; Column: PROFITCENTER.PROFITCENTER; queryRef: COSTCENTER.COSTCENTER; Column: COSTCENTER.COSTCENTER; queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; queryRef: AGGR_H.PARTNERCOMPANYCODE; Column: AGGR_H.PARTNERCOMPANYCODE; queryRef: AGGR_H.TAXCODE; Column: AGGR_H.TAXCODE; queryRef: AGGR_H.TAXCOUNTRY; Column: AGGR_H.TAXCOUNTRY; Column: _GLACCOUNTINCHARTOFACCOUNTSTEXT.FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT; Column: _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS; queryRef: _MEASURES_AGGR_H.AGGR_TRANSACTION_CURRENT_PERIOD; Measure: _MEASURES_AGGR_H.AGGR_TRANSACTION_CURRENT_PERIOD; Column: _FIELD_PARAM_AGGR_CURRENT_PERIOD._FIELD_PARAM_AGGR_CURRENT_PERIOD |
| [30dc55055ac2bf1ea64f](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/30dc55055ac2bf1ea64f/visual.json) | slicer | .visual.objects.header[0].properties.text='Company Code' | queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; Column: c.COMPANYCODE |
| [3dff14b0eeb3d263ba11](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/3dff14b0eeb3d263ba11/visual.json) | slicer | .visual.objects.header[0].properties.text='Chart of Accounts' | queryRef: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: c.CHARTOFACCOUNTS |
| [4a363851dc01936570f6](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/4a363851dc01936570f6/visual.json) | shape |  |  |
| [61b8785993f0d57184b4](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/61b8785993f0d57184b4/visual.json) | shape |  |  |
| [6e5c044ea8884a73a1d1](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/6e5c044ea8884a73a1d1/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; Column: _._FIELD_PARAM_AGGR_CURRENCY Fields; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY Fields |
| [7c8ff2db5502611b2026](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/7c8ff2db5502611b2026/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Currency' |  |
| [982c4839be4e90a98844](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/982c4839be4e90a98844/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Period' | queryRef: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: f.FISCALPERIOD |
| [98983ca3ee513b135c63](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/98983ca3ee513b135c63/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=LedgerText; .visual.objects.header[0].properties.text='Ledger'; .visual.visualContainerObjects.title[0].properties.text='Slicer' | queryRef: LEDGERTEXT.EN; Column: LEDGERTEXT.EN; Column: _LEDGERTEXT.FIELD_PARAM_LEDGERTEXT; Column: l.DE; Column: LEDGERTEXT.DE |
| [ae1821b4ca8b903737c0](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/ae1821b4ca8b903737c0/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: SAPLANGUAGE.LANGUAGENAME; Column: SAPLANGUAGE.LANGUAGENAME; queryRef: SAPLANGUAGE._ISOLanguage; Column: SAPLANGUAGE._ISOLanguage; Column: s.LANGUAGENAME |
| [b6e1776ae707ba3ee673](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/b6e1776ae707ba3ee673/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Language' |  |
| [b9a33edd87444d1950a8](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/b9a33edd87444d1950a8/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Year' | queryRef: FISCALPERIODFORVARIANT.FISCALYEAR; Column: FISCALPERIODFORVARIANT.FISCALYEAR; Column: f.FISCALYEAR |
| [c7bf94f96ab0d0267d6a](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/c7bf94f96ab0d0267d6a/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=SegmentText; .visual.objects.header[0].properties.text='Segment' | queryRef: SEGMENTTEXT.EN; Column: SEGMENTTEXT.EN; Column: _SEGMENTTEXT.FIELD_PARAM_SEGMENTTEXT; Column: ISOLANGUAGE.LANGUAGECODE |
| [d3b976149ea2c21c58e0](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/d3b976149ea2c21c58e0/visual.json) | shape |  |  |
| [da2b1fc60510eb829f7c](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/da2b1fc60510eb829f7c/visual.json) | image |  |  |
| [ddbdf463cbb627e27195](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/ddbdf463cbb627e27195/visual.json) | shape |  |  |
| [e483aece8ca6ffcff19a](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/e483aece8ca6ffcff19a/visual.json) | visualGroup | .visualGroup.displayName=Group 1 |  |

#### 071471fa20a68fa054f9 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/071471fa20a68fa054f9/visual.json). Position: `{"x":980,"y":112,"z":15000,"height":15.99536,"width":73.9814,"tabOrder":14000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Field'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 1e7cb142cc39d2ed9a8b — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/1e7cb142cc39d2ed9a8b/visual.json). Position: `{"x":65.71428571428572,"y":24.28571428571429,"z":7000,"height":35.714285714285715,"width":260,"tabOrder":7000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Trial Balance","textStyle":{"fontFamily":"Segoe (Bold)","fontSize":"14pt"}}]}]}}]},"drillFilterOtherVisuals":true}}
```

#### 29eb14c3ea3fbdde208c — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/29eb14c3ea3fbdde208c/visual.json). Position: `{"x":1046,"y":96,"z":14000,"height":50,"width":195.9954,"tabOrder":13000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"Property":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"queryRef":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS","nativeQueryRef":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"false"}}},"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 2bad24393298c417e966 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/2bad24393298c417e966/visual.json). Position: `{"x":14.444444444444445,"y":510,"z":17000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":16000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"EN"}},"queryRef":"PROFITCENTERTEXT.EN","nativeQueryRef":"ProfitCenterText","active":true,"displayName":"ProfitCenterText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_PROFITCENTERTEXT"}},"Property":"FIELD_PARAM_PROFITCENTERTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Profit Center'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"ProfitCenter","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"5047aab52c695354d682","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"p","Entity":"PROFITCENTERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"p"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]},"howCreated":"User"}]}}
```

#### 2c604992f5e3ae683475 — pivotTable

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/2c604992f5e3ae683475/visual.json). Position: `{"x":237.5,"y":146.25,"z":10000,"height":723.75,"width":1005,"tabOrder":9000}`.

```json
{"visual":{"visualType":"pivotTable","query":{"queryState":{"Columns":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TRANSACTIONCURRENCY"}},"queryRef":"AGGR_H.TRANSACTIONCURRENCY","nativeQueryRef":"Transaction Currency","active":true,"displayName":"Transaction Currency"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"queryRef":"DEBITCREDITCODETEXT.EN","nativeQueryRef":"Debit/Credit","active":false,"displayName":"Debit/Credit"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_DEBITCREDITCODETEXT"}},"Property":"FIELD_PARAM_DEBITCREDITCODETEXT"}},"index":1,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}},"index":0,"length":1}]},"Rows":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT","nativeQueryRef":"GLACCOUNT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTSTEXT.EN","nativeQueryRef":"GL Account Name","active":true,"displayName":"GL Account Name"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNTGROUP"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP","nativeQueryRef":"GLACCOUNTGROUP","active":true,"displayName":"GLACCOUNTGROUP"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}},"queryRef":"PROFITCENTER.PROFITCENTER","nativeQueryRef":"PROFITCENTER","active":true,"displayName":"PROFITCENTER"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}},"queryRef":"COSTCENTER.COSTCENTER","nativeQueryRef":"COSTCENTER","active":false,"displayName":"COSTCENTER"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":false,"displayName":"COMPANYCODE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"PARTNERCOMPANYCODE"}},"queryRef":"AGGR_H.PARTNERCOMPANYCODE","nativeQueryRef":"PARTNERCOMPANYCODE","active":false,"displayName":"PARTNERCOMPANYCODE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCODE"}},"queryRef":"AGGR_H.TAXCODE","nativeQueryRef":"TAXCODE","active":false,"displayName":"TAXCODE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCOUNTRY"}},"queryRef":"AGGR_H.TAXCOUNTRY","nativeQueryRef":"TAXCOUNTRY","active":false,"displayName":"TAXCOUNTRY"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"index":1,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"Property":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"index":2,"length":7}]},"Values":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_CURRENT_PERIOD"}},"queryRef":"_MEASURES_AGGR_H.AGGR_TRANSACTION_CURRENT_PERIOD","nativeQueryRef":"Current Period","displayName":"Current Period"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENT_PERIOD"}},"Property":"_FIELD_PARAM_AGGR_CURRENT_PERIOD"}},"index":0,"length":1}]}}},"expansionStates":[{"roles":["Rows"],"levels":[{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT"],"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTSTEXT.EN"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}}],"isPinned":true},{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNTGROUP"}}],"isPinned":true},{"queryRefs":["PROFITCENTER.PROFITCENTER"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}}],"isPinned":true},{"queryRefs":["COSTCENTER.COSTCENTER"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}}],"isPinned":true},{"queryRefs":["COMPANYCODE.COMPANYCODE"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}}],"isPinned":true},{"queryRefs":["AGGR_H.PARTNERCOMPANYCODE"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"PARTNERCOMPANYCODE"}}],"isPinned":true},{"queryRefs":["AGGR_H.TAXCODE"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCODE"}}],"isPinned":true},{"queryRefs":["AGGR_H.TAXCOUNTRY"],"isCollapsed":true,"isPinned":true}],"root":{"children":[{"identityValues":[{"Literal":{"Value":"'0011001000'"}}],"children":[{"identityValues":[{"Literal":{"Value":"'Bank1 Main Account'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'FIN.'"}}],"isToggled":true}]}]}]}}],"objects":{"columnHeaders":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"9D"}}},"wordWrap":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"4D"}}}}}],"grid":[{"properties":{"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}},"gridHorizontal":{"expr":{"Literal":{"Value":"true"}}},"gridHorizontalWeight":{"expr":{"Literal":{"Value":"5D"}}},"gridHorizontalColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"rowPadding":{"expr":{"Literal":{"Value":"6D"}}},"gridVertical":{"expr":{"Literal":{"Value":"true"}}},"outlineStyle":{"expr":{"Literal":{"Value":"4D"}}}}}],"general":[{"properties":{"layout":{"expr":{"Literal":{"Value":"'Outline'"}}}}}],"values":[{"properties":{"wordWrap":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"12D"}}}}}],"subTotals":[{"properties":{"perColumnLevel":{"expr":{"Literal":{"Value":"true"}}},"perRowLevel":{"expr":{"Literal":{"Value":"false"}}},"columnSubtotals":{"expr":{"Literal":{"Value":"true"}}},"rowSubtotals":{"expr":{"Literal":{"Value":"true"}}},"rowSubtotalsPosition":{"expr":{"Literal":{"Value":"'Top'"}}}}},{"properties":{"levelSubtotalEnabled":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT"}},{"properties":{"levelSubtotalEnabled":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY"}}],"rowHeaders":[{"properties":{"showExpandCollapseButtons":{"expr":{"Literal":{"Value":"true"}}}}}],"columnWidth":[{"properties":{"value":{"expr":{"Literal":{"Value":"79.7810899389317D"}}}},"selector":{"data":[{"scopeId":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TRANSACTIONCURRENCY"}},"Right":{"Literal":{"Value":"'EUR'"}}}}}]}},{"properties":{"value":{"expr":{"Literal":{"Value":"95.04830364281592D"}}}},"selector":{"data":[{"scopeId":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TRANSACTIONCURRENCY"}},"Right":{"Literal":{"Value":"'AUD'"}}}}}]}},{"properties":{"value":{"expr":{"Literal":{"Value":"103.85671641791045D"}}}},"selector":{"metadata":"GLACCOUNTINCHARTOFACCOUNTSTEXT.EN"}},{"properties":{"value":{"expr":{"Literal":{"Value":"83.84776119402986D"}}}},"selector":{"metadata":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP"}},{"properties":{"value":{"expr":{"Literal":{"Value":"155.16364463676976D"}}}},"selector":{"metadata":"PROFITCENTER.PROFITCENTER"}},{"properties":{"value":{"expr":{"Literal":{"Value":"52.9044776119403D"}}}},"selector":{"metadata":"AGGR_H.TAXCOUNTRY"}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Accounting Documents'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}]},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"dfecd523a906078b5016","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"type":"Categorical","objects":{"general":[{"properties":{"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}]}},{"name":"cdde8ce05a4d659d65ee","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TRANSACTIONCURRENCY"}},"type":"Categorical"},{"name":"ec0ad040d670ee350d13","field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"type":"Categorical"},{"name":"a6fbb1b5cecb974522c6","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}},"type":"Categorical"},{"name":"aa02afb537a0a2cdca96","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNTGROUP"}},"type":"Categorical"},{"name":"fb74b8a9b26036aa127c","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}},"type":"Categorical"},{"name":"f0a647ab0075b00c02eb","field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}},"type":"Categorical"},{"name":"f9848b8ad8327631a6b0","field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"type":"Categorical"},{"name":"448491307c7ae1a931c2","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"PARTNERCOMPANYCODE"}},"type":"Categorical"},{"name":"10ab352e6710610c6e15","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCODE"}},"type":"Categorical"},{"name":"0cd4bc4950289a3c088a","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCOUNTRY"}},"type":"Categorical"},{"name":"1b6cb2f6b550d8da46bd","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_CURRENT_PERIOD"}},"type":"Advanced"}]}}
```

#### 30dc55055ac2bf1ea64f — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/30dc55055ac2bf1ea64f/visual.json). Position: `{"x":14.285714285714286,"y":165.71428571428572,"z":4000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":4000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Company Code'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"COMPANYCODE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"COMPANYCODE"}}],"Values":[[{"Literal":{"Value":"'1710'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"COMPANYCODE","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 3dff14b0eeb3d263ba11 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/3dff14b0eeb3d263ba11/visual.json). Position: `{"x":14.285714285714286,"y":234.2857142857143,"z":11000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":10000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CHARTOFACCOUNTS"}},"Property":"CHARTOFACCOUNTS"}},"queryRef":"CHARTOFACCOUNTS.CHARTOFACCOUNTS","nativeQueryRef":"CHARTOFACCOUNTS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Chart of Accounts'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}},"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"CHARTOFACCOUNTS","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"CHARTOFACCOUNTS"}}],"Values":[[{"Literal":{"Value":"'YCOA'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"CHARTOFACCOUNTS","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 4a363851dc01936570f6 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/4a363851dc01936570f6/visual.json). Position: `{"x":0,"y":0,"z":0,"height":82,"width":1280}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 61b8785993f0d57184b4 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/61b8785993f0d57184b4/visual.json). Position: `{"x":0.5,"y":0,"z":8000,"height":34,"width":34}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}}],"outline":[{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}},"radius":{"expr":{"Literal":{"Value":"4D"}}}}}],"lockAspect":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"e483aece8ca6ffcff19a","howCreated":"InsertVisualButton"}
```

#### 6e5c044ea8884a73a1d1 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/6e5c044ea8884a73a1d1/visual.json). Position: `{"x":771.9518576661434,"y":16.74515960230246,"z":12000,"height":50.23547880690738,"width":195.9183673469388,"tabOrder":11000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}},"queryRef":"_FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY","nativeQueryRef":"_FIELD_PARAM_AGGR_CURRENCY","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"_","Entity":"_FIELD_PARAM_AGGR_CURRENCY","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"_"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY Fields"}}],"Values":[[{"Literal":{"Value":"'''AGGR_H''[TRANSACTIONCURRENCY]'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'''AGGR_H''[TRANSACTIONCURRENCY]'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY Fields"}}}]},"valueMap":[{"0":"Transaction Currency"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 7c8ff2db5502611b2026 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/7c8ff2db5502611b2026/visual.json). Position: `{"x":689.9005756148614,"y":33.49031920460492,"z":13000,"height":20.07861852433281,"width":100.47095761381476,"tabOrder":12000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Currency'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 982c4839be4e90a98844 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/982c4839be4e90a98844/visual.json). Position: `{"x":14.285714285714286,"y":372.8571428571429,"z":3000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":3000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALPERIOD"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALPERIOD","nativeQueryRef":"FISCALPERIOD1","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Period'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALPERIOD"}}],"Values":[[{"Literal":{"Value":"2L"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALPERIOD","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 98983ca3ee513b135c63 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/98983ca3ee513b135c63/visual.json). Position: `{"x":15.070643642072215,"y":105.4945054945055,"z":16000,"height":60.27487179487179,"width":197.58953427524858,"tabOrder":15000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"EN"}},"queryRef":"LEDGERTEXT.EN","nativeQueryRef":"LedgerText","active":false,"displayName":"LedgerText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_LEDGERTEXT"}},"Property":"FIELD_PARAM_LEDGERTEXT"}},"index":0,"length":4}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}},"filter":{"filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}}],"Values":[[{"Literal":{"Value":"'Ledger 0L'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'Ledger 0L'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}}]},"valueMap":[{"0":"Ledger 0L"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Ledger'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}}}}],"title":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Slicer'"}}}}}]},"syncGroup":{"groupName":"Ledger","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"7ed0f4b41e94f9227537","field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]}}]}}
```

#### ae1821b4ca8b903737c0 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/ae1821b4ca8b903737c0/visual.json). Position: `{"x":1066.25,"y":16.25,"z":5000,"height":50,"width":196.25,"tabOrder":5000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}},"queryRef":"SAPLANGUAGE.LANGUAGENAME","nativeQueryRef":"LANGUAGENAME","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"_ISOLanguage"}},"queryRef":"SAPLANGUAGE._ISOLanguage","nativeQueryRef":"_ISOLanguage","active":false}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"s","Entity":"SAPLANGUAGE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"s"}},"Property":"LANGUAGENAME"}}],"Values":[[{"Literal":{"Value":"'English'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'English'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}}]},"valueMap":[{"0":"English"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"LANGUAGENAME","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### b6e1776ae707ba3ee673 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/b6e1776ae707ba3ee673/visual.json). Position: `{"x":982.9408686551544,"y":33.49031920460492,"z":6000,"height":20.07861852433281,"width":98.78488749345892,"tabOrder":6000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Language'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### b9a33edd87444d1950a8 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/b9a33edd87444d1950a8/visual.json). Position: `{"x":14.285714285714286,"y":302.8571428571429,"z":2000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":2000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALYEAR","nativeQueryRef":"FISCALYEAR","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Year'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}}],"Values":[[{"Literal":{"Value":"2016L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALYEAR","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"420b0605276736284725","field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":1,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}},"Right":{"Literal":{"Value":"2015L"}}}}}]}}]}}
```

#### c7bf94f96ab0d0267d6a — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/c7bf94f96ab0d0267d6a/visual.json). Position: `{"x":15.555555555555555,"y":442.22222222222223,"z":18000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":17000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"EN"}},"queryRef":"SEGMENTTEXT.EN","nativeQueryRef":"SegmentText","active":true,"displayName":"SegmentText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_SEGMENTTEXT"}},"Property":"FIELD_PARAM_SEGMENTTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Segment'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"pendingChangesIcon":[{"properties":{"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"syncGroup":{"groupName":"Segment","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"a2125af5969106a6fcf7","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### d3b976149ea2c21c58e0 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/d3b976149ea2c21c58e0/visual.json). Position: `{"x":225.71428571428572,"y":97.14285714285715,"z":9000,"height":787.1428571428572,"width":1040,"tabOrder":8000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### da2b1fc60510eb829f7c — image

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/da2b1fc60510eb829f7c/visual.json). Position: `{"x":0,"y":3.25,"z":42001,"height":27.25,"width":34.25,"tabOrder":1000}`.

```json
{"visual":{"visualType":"image","objects":{"general":[{"properties":{"imageUrl":{"expr":{"ResourcePackageItem":{"PackageName":"RegisteredResources","PackageType":1,"ItemName":"Data_Bar_Vertical_Highlight26202892008048195.png"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"e483aece8ca6ffcff19a","howCreated":"InsertVisualButton"}
```

#### ddbdf463cbb627e27195 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/ddbdf463cbb627e27195/visual.json). Position: `{"x":15,"y":97.5,"z":1000,"height":787.5,"width":195,"tabOrder":1000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### e483aece8ca6ffcff19a — visualGroup

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e9a0daa552c5be7f88d0/visuals/e483aece8ca6ffcff19a/visual.json). Position: `{"x":15.5,"y":24,"z":8000,"height":34,"width":34.5,"tabOrder":18000}`.

```json
{"visualGroup":{"displayName":"Group 1","groupMode":"ScaleMode"}}
```

### YTD Trial Balance — 29205fb9a9b601d02447

[Page definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/page.json). 1280 × 900; FitToWidth; 21 visual containers. Active authoring page: False.

Page configuration (including all page-level filtering, drillthrough and interaction metadata if authored):

```json
{"$schema":"https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json","name":"29205fb9a9b601d02447","displayName":"YTD Trial Balance","displayOption":"FitToWidth","height":900,"width":1280}
```

| Container | Type | Authored labels | Bound fields / measures |
|---|---|---|---|
| [184e0ee991bd10a1990f](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/184e0ee991bd10a1990f/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Period' | queryRef: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: f.FISCALPERIOD |
| [1ac6cedbdc1c47706d0e](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/1ac6cedbdc1c47706d0e/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Year' | queryRef: FISCALPERIODFORVARIANT.FISCALYEAR; Column: FISCALPERIODFORVARIANT.FISCALYEAR; Column: f.FISCALYEAR |
| [2461f38afb2e7b671d20](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/2461f38afb2e7b671d20/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=SegmentText; .visual.objects.header[0].properties.text='Segment' | queryRef: SEGMENTTEXT.EN; Column: SEGMENTTEXT.EN; Column: _SEGMENTTEXT.FIELD_PARAM_SEGMENTTEXT; Column: ISOLANGUAGE.LANGUAGECODE |
| [328394ecc789d33226cb](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/328394ecc789d33226cb/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; Column: _._FIELD_PARAM_AGGR_CURRENCY Fields; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY Fields |
| [37dcc5d87a60c8847e5f](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/37dcc5d87a60c8847e5f/visual.json) | shape |  |  |
| [590237481b3e517c91a8](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/590237481b3e517c91a8/visual.json) | slicer | .visual.objects.header[0].properties.text='Chart of Accounts' | queryRef: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: c.CHARTOFACCOUNTS |
| [68028e6dc9134ac57981](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/68028e6dc9134ac57981/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Language' |  |
| [689c83b11556bf76ff92](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/689c83b11556bf76ff92/visual.json) | shape |  |  |
| [727966b781f975f7cb57](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/727966b781f975f7cb57/visual.json) | shape |  |  |
| [99f33e48f5863153f6fb](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/99f33e48f5863153f6fb/visual.json) | pivotTable | .visual.query.queryState.Columns.projections[0].displayName=Transaction Currency; .visual.query.queryState.Columns.projections[1].displayName=Debit/Credit; .visual.query.queryState.Rows.projections[1].displayName=GL Account Name; .visual.query.queryState.Rows.projections[2].displayName=GLACCOUNTGROUP; .visual.query.queryState.Rows.projections[3].displayName=PROFITCENTER; .visual.query.queryState.Rows.projections[4].displayName=COSTCENTER; .visual.query.queryState.Rows.projections[5].displayName=COMPANYCODE; .visual.query.queryState.Rows.projections[6].displayName=PARTNERCOMPANYCODE; .visual.query.queryState.Rows.projections[7].displayName=TAXCODE; .visual.query.queryState.Rows.projections[8].displayName=TAXCOUNTRY; .visual.query.queryState.Values.projections[0].displayName=Opening Balance; .visual.query.queryState.Values.projections[1].displayName=Current Period; .visual.query.queryState.Values.projections[2].displayName=Closing Balance; .visual.visualContainerObjects.title[0].properties.text='Accounting Documents' | queryRef: AGGR_H.TRANSACTIONCURRENCY; Column: AGGR_H.TRANSACTIONCURRENCY; queryRef: DEBITCREDITCODETEXT.EN; Column: DEBITCREDITCODETEXT.EN; Column: _DEBITCREDITCODETEXT.FIELD_PARAM_DEBITCREDITCODETEXT; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; queryRef: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; Column: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; queryRef: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; Column: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; queryRef: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP; Column: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP; queryRef: PROFITCENTER.PROFITCENTER; Column: PROFITCENTER.PROFITCENTER; queryRef: COSTCENTER.COSTCENTER; Column: COSTCENTER.COSTCENTER; queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; queryRef: AGGR_H.PARTNERCOMPANYCODE; Column: AGGR_H.PARTNERCOMPANYCODE; queryRef: AGGR_H.TAXCODE; Column: AGGR_H.TAXCODE; queryRef: AGGR_H.TAXCOUNTRY; Column: AGGR_H.TAXCOUNTRY; Column: _GLACCOUNTINCHARTOFACCOUNTSTEXT.FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT; Column: _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS; queryRef: _MEASURES_AGGR_H.AGGR_TRANSACTION_OPENING_BALANCE; Measure: _MEASURES_AGGR_H.AGGR_TRANSACTION_OPENING_BALANCE; queryRef: _MEASURES_AGGR_H.AGGR_TRANSACTION_CURRENT_PERIOD; Measure: _MEASURES_AGGR_H.AGGR_TRANSACTION_CURRENT_PERIOD; queryRef: _MEASURES_AGGR_H.AGGR_TRANSACTION_CLOSING_BALANCE; Measure: _MEASURES_AGGR_H.AGGR_TRANSACTION_CLOSING_BALANCE; Column: _FIELD_PARAM_AGGR_OPENING_BALANCE._FIELD_PARAM_AGGR_OPENING_BALANCE; Column: _FIELD_PARAM_AGGR_CURRENT_PERIOD._FIELD_PARAM_AGGR_CURRENT_PERIOD; Column: _FIELD_PARAM_AGGR_CLOSING_BALANCE._FIELD_PARAM_AGGR_CLOSING_BALANCE |
| [a26252c5422a2dec521a](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/a26252c5422a2dec521a/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS; Column: _FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS |
| [a3e1ab58a721296f50ee](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/a3e1ab58a721296f50ee/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=YTD Trial Balance |  |
| [c06e4239444d9f5c858b](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/c06e4239444d9f5c858b/visual.json) | slicer | .visual.objects.header[0].properties.text='Company Code' | queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; Column: c.COMPANYCODE |
| [d13eeae93a65a7f311bf](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/d13eeae93a65a7f311bf/visual.json) | visualGroup | .visualGroup.displayName=Group 1 |  |
| [d2a30d331a67626b1cba](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/d2a30d331a67626b1cba/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Currency' |  |
| [e10a2000a6e115f309c6](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e10a2000a6e115f309c6/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=LedgerText; .visual.objects.header[0].properties.text='Ledger'; .visual.visualContainerObjects.title[0].properties.text='Slicer' | queryRef: LEDGERTEXT.EN; Column: LEDGERTEXT.EN; Column: _LEDGERTEXT.FIELD_PARAM_LEDGERTEXT; Column: l.DE; Column: LEDGERTEXT.DE |
| [e3900963152a42665296](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e3900963152a42665296/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: SAPLANGUAGE.LANGUAGENAME; Column: SAPLANGUAGE.LANGUAGENAME; queryRef: SAPLANGUAGE._ISOLanguage; Column: SAPLANGUAGE._ISOLanguage; Column: s.LANGUAGENAME |
| [e58083d44409faf86c31](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e58083d44409faf86c31/visual.json) | shape |  |  |
| [e97255934c5329ff4d89](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e97255934c5329ff4d89/visual.json) | image |  |  |
| [eb629890193a94d01114](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/eb629890193a94d01114/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Field' |  |
| [f12ad8ee4155a123ec30](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/f12ad8ee4155a123ec30/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=ProfitCenterText; .visual.objects.header[0].properties.text='Profit Center' | queryRef: PROFITCENTERTEXT.EN; Column: PROFITCENTERTEXT.EN; Column: _PROFITCENTERTEXT.FIELD_PARAM_PROFITCENTERTEXT; Column: PROFITCENTERTEXT.DE; Column: p.DE |

#### 184e0ee991bd10a1990f — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/184e0ee991bd10a1990f/visual.json). Position: `{"x":14.285714285714286,"y":372.8571428571429,"z":3000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":3000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALPERIOD"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALPERIOD","nativeQueryRef":"FISCALPERIOD1","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Period'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALPERIOD"}}],"Values":[[{"Literal":{"Value":"2L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALPERIOD","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 1ac6cedbdc1c47706d0e — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/1ac6cedbdc1c47706d0e/visual.json). Position: `{"x":14.285714285714286,"y":302.8571428571429,"z":2000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":2000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALYEAR","nativeQueryRef":"FISCALYEAR","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Year'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}}],"Values":[[{"Literal":{"Value":"2016L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALYEAR","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"24c6085e0558d09ccb94","field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":1,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}},"Right":{"Literal":{"Value":"2015L"}}}}}]}}]}}
```

#### 2461f38afb2e7b671d20 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/2461f38afb2e7b671d20/visual.json). Position: `{"x":15.555555555555555,"y":442.22222222222223,"z":18000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":17000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"EN"}},"queryRef":"SEGMENTTEXT.EN","nativeQueryRef":"SegmentText","active":true,"displayName":"SegmentText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_SEGMENTTEXT"}},"Property":"FIELD_PARAM_SEGMENTTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Segment'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"pendingChangesIcon":[{"properties":{"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"syncGroup":{"groupName":"Segment","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"cefa1cd2aef98173df6f","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### 328394ecc789d33226cb — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/328394ecc789d33226cb/visual.json). Position: `{"x":771.9518576661434,"y":16.74515960230246,"z":15000,"height":50.23547880690738,"width":195.9183673469388,"tabOrder":14000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}},"queryRef":"_FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY","nativeQueryRef":"_FIELD_PARAM_AGGR_CURRENCY","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"_","Entity":"_FIELD_PARAM_AGGR_CURRENCY","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"_"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY Fields"}}],"Values":[[{"Literal":{"Value":"'''AGGR_H''[TRANSACTIONCURRENCY]'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'''AGGR_H''[TRANSACTIONCURRENCY]'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY Fields"}}}]},"valueMap":[{"0":"Transaction Currency"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 37dcc5d87a60c8847e5f — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/37dcc5d87a60c8847e5f/visual.json). Position: `{"x":15,"y":97.5,"z":1000,"height":787.5,"width":195,"tabOrder":1000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 590237481b3e517c91a8 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/590237481b3e517c91a8/visual.json). Position: `{"x":14.285714285714286,"y":234.2857142857143,"z":8000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":7000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CHARTOFACCOUNTS"}},"Property":"CHARTOFACCOUNTS"}},"queryRef":"CHARTOFACCOUNTS.CHARTOFACCOUNTS","nativeQueryRef":"CHARTOFACCOUNTS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Chart of Accounts'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"CHARTOFACCOUNTS","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"CHARTOFACCOUNTS"}}],"Values":[[{"Literal":{"Value":"'YCOA'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"CHARTOFACCOUNTS","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 68028e6dc9134ac57981 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/68028e6dc9134ac57981/visual.json). Position: `{"x":982.9408686551544,"y":33.49031920460492,"z":14000,"height":20.07861852433281,"width":98.78488749345892,"tabOrder":13000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Language'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 689c83b11556bf76ff92 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/689c83b11556bf76ff92/visual.json). Position: `{"x":0.5,"y":0,"z":8000,"height":34,"width":34}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}}],"outline":[{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}},"radius":{"expr":{"Literal":{"Value":"4D"}}}}}],"lockAspect":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"d13eeae93a65a7f311bf","howCreated":"InsertVisualButton"}
```

#### 727966b781f975f7cb57 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/727966b781f975f7cb57/visual.json). Position: `{"x":0,"y":0,"z":0,"height":82,"width":1280}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 99f33e48f5863153f6fb — pivotTable

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/99f33e48f5863153f6fb/visual.json). Position: `{"x":238,"y":146,"z":9000,"height":718,"width":1014,"tabOrder":8000}`.

```json
{"visual":{"visualType":"pivotTable","query":{"queryState":{"Columns":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TRANSACTIONCURRENCY"}},"queryRef":"AGGR_H.TRANSACTIONCURRENCY","nativeQueryRef":"Transaction Currency","active":true,"displayName":"Transaction Currency"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"queryRef":"DEBITCREDITCODETEXT.EN","nativeQueryRef":"Debit/Credit","active":false,"displayName":"Debit/Credit"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_DEBITCREDITCODETEXT"}},"Property":"FIELD_PARAM_DEBITCREDITCODETEXT"}},"index":1,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}},"index":0,"length":1}]},"Rows":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT","nativeQueryRef":"GLACCOUNT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTSTEXT.EN","nativeQueryRef":"GL Account Name","active":true,"displayName":"GL Account Name"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNTGROUP"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP","nativeQueryRef":"GLACCOUNTGROUP","active":false,"displayName":"GLACCOUNTGROUP"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}},"queryRef":"PROFITCENTER.PROFITCENTER","nativeQueryRef":"PROFITCENTER","active":false,"displayName":"PROFITCENTER"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}},"queryRef":"COSTCENTER.COSTCENTER","nativeQueryRef":"COSTCENTER","active":false,"displayName":"COSTCENTER"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":false,"displayName":"COMPANYCODE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"PARTNERCOMPANYCODE"}},"queryRef":"AGGR_H.PARTNERCOMPANYCODE","nativeQueryRef":"PARTNERCOMPANYCODE","active":false,"displayName":"PARTNERCOMPANYCODE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCODE"}},"queryRef":"AGGR_H.TAXCODE","nativeQueryRef":"TAXCODE","active":false,"displayName":"TAXCODE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCOUNTRY"}},"queryRef":"AGGR_H.TAXCOUNTRY","nativeQueryRef":"TAXCOUNTRY","active":false,"displayName":"TAXCOUNTRY"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"index":1,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"Property":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"index":2,"length":7}]},"Values":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_OPENING_BALANCE"}},"queryRef":"_MEASURES_AGGR_H.AGGR_TRANSACTION_OPENING_BALANCE","nativeQueryRef":"Opening Balance","displayName":"Opening Balance"},{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_CURRENT_PERIOD"}},"queryRef":"_MEASURES_AGGR_H.AGGR_TRANSACTION_CURRENT_PERIOD","nativeQueryRef":"Current Period","displayName":"Current Period"},{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_CLOSING_BALANCE"}},"queryRef":"_MEASURES_AGGR_H.AGGR_TRANSACTION_CLOSING_BALANCE","nativeQueryRef":"Closing Balance","displayName":"Closing Balance"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_OPENING_BALANCE"}},"Property":"_FIELD_PARAM_AGGR_OPENING_BALANCE"}},"index":0,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENT_PERIOD"}},"Property":"_FIELD_PARAM_AGGR_CURRENT_PERIOD"}},"index":1,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CLOSING_BALANCE"}},"Property":"_FIELD_PARAM_AGGR_CLOSING_BALANCE"}},"index":2,"length":1}]}}},"expansionStates":[{"roles":["Rows"],"levels":[{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTSTEXT.EN"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}}],"isPinned":true},{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNTGROUP"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNTGROUP"}}],"isPinned":true},{"queryRefs":["PROFITCENTER.PROFITCENTER"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}}],"isPinned":true},{"queryRefs":["COSTCENTER.COSTCENTER"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}}],"isPinned":true},{"queryRefs":["COMPANYCODE.COMPANYCODE"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}}],"isPinned":true},{"queryRefs":["AGGR_H.PARTNERCOMPANYCODE"],"isCollapsed":true,"isPinned":true},{"queryRefs":["AGGR_H.TAXCODE"],"isCollapsed":true},{"queryRefs":["AGGR_H.TAXCOUNTRY"],"isCollapsed":true}],"root":{"children":[{"identityValues":[{"Literal":{"Value":"'0011001000'"}}],"children":[{"identityValues":[{"Literal":{"Value":"'Bank1 Main Account'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'FIN.'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'US10_PCC1L'"}}],"children":[{"identityValues":[{"Literal":{"Value":"null"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'1710'"}}],"isToggled":true}]}]}]}]}]},{"identityValues":[{"Literal":{"Value":"'0012100000'"}}],"isToggled":true}]}}],"objects":{"columnHeaders":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"9D"}}},"wordWrap":{"expr":{"Literal":{"Value":"false"}}}}}],"grid":[{"properties":{"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}},"gridHorizontal":{"expr":{"Literal":{"Value":"true"}}},"gridHorizontalWeight":{"expr":{"Literal":{"Value":"5D"}}},"gridHorizontalColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"rowPadding":{"expr":{"Literal":{"Value":"6D"}}},"gridVertical":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"layout":{"expr":{"Literal":{"Value":"'Outline'"}}}}}],"subTotals":[{"properties":{"perColumnLevel":{"expr":{"Literal":{"Value":"false"}}},"columnSubtotals":{"expr":{"Literal":{"Value":"false"}}},"perRowLevel":{"expr":{"Literal":{"Value":"true"}}}}}],"values":[{"properties":{"wordWrap":{"expr":{"Literal":{"Value":"false"}}},"bandedRowHeaders":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Accounting Documents'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}]},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"fd135f64ec3c335f3d75","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"type":"Categorical"},{"name":"5b40432b16b403cfcbe1","field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"type":"Categorical"},{"name":"8364b777ac917f80f504","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}},"type":"Categorical"},{"name":"c56c6e92e0be4724f210","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNTGROUP"}},"type":"Categorical"},{"name":"47b0e07ca460ce7b4d59","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}},"type":"Categorical"},{"name":"f14ebdd8e4f3c13cccfa","field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}},"type":"Categorical"},{"name":"d278bdfc2bdcb8f3652b","field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"type":"Categorical"},{"name":"fe8af29b1d7a50d8fa80","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"PARTNERCOMPANYCODE"}},"type":"Categorical"},{"name":"6f6c5b357db4e1b011ae","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCODE"}},"type":"Categorical"},{"name":"a523002b3ff4808d3b69","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TAXCOUNTRY"}},"type":"Categorical"},{"name":"a4c2f12e9ec1cb156ee7","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"TRANSACTIONCURRENCY"}},"type":"Categorical"},{"name":"07ff80220b2f95a12d44","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_OPENING_BALANCE"}},"type":"Advanced"},{"name":"96c4b5bc9134696b008c","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_CURRENT_PERIOD"}},"type":"Advanced"},{"name":"901818ab697a102eb5d3","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"_MEASURES_AGGR_H"}},"Property":"AGGR_TRANSACTION_CLOSING_BALANCE"}},"type":"Advanced"}]}}
```

#### a26252c5422a2dec521a — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/a26252c5422a2dec521a/visual.json). Position: `{"x":1046,"y":96,"z":10000,"height":50,"width":195.9954,"tabOrder":9000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"Property":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS"}},"queryRef":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS._FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS","nativeQueryRef":"_FIELD_PARAM_AGGR_TRIALBALANCE_FIELDS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"false"}}},"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### a3e1ab58a721296f50ee — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/a3e1ab58a721296f50ee/visual.json). Position: `{"x":65.71428571428572,"y":24.28571428571429,"z":5000,"height":35.714285714285715,"width":260,"tabOrder":5000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"YTD Trial Balance","textStyle":{"fontFamily":"Segoe (Bold)","fontSize":"14pt"}}]}]}}]},"drillFilterOtherVisuals":true}}
```

#### c06e4239444d9f5c858b — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/c06e4239444d9f5c858b/visual.json). Position: `{"x":14.285714285714286,"y":165.71428571428572,"z":4000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":4000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Company Code'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"COMPANYCODE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"COMPANYCODE"}}],"Values":[[{"Literal":{"Value":"'1710'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"COMPANYCODE","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### d13eeae93a65a7f311bf — visualGroup

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/d13eeae93a65a7f311bf/visual.json). Position: `{"x":15.5,"y":24,"z":6000,"height":34,"width":34.5,"tabOrder":18000}`.

```json
{"visualGroup":{"displayName":"Group 1","groupMode":"ScaleMode"}}
```

#### d2a30d331a67626b1cba — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/d2a30d331a67626b1cba/visual.json). Position: `{"x":689.9005756148614,"y":33.49031920460492,"z":16000,"height":20.07861852433281,"width":100.47095761381476,"tabOrder":15000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Currency'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### e10a2000a6e115f309c6 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e10a2000a6e115f309c6/visual.json). Position: `{"x":15.070643642072215,"y":105.4945054945055,"z":12000,"height":60.27487179487179,"width":197.58953427524858,"tabOrder":11000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"EN"}},"queryRef":"LEDGERTEXT.EN","nativeQueryRef":"LedgerText","active":false,"displayName":"LedgerText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_LEDGERTEXT"}},"Property":"FIELD_PARAM_LEDGERTEXT"}},"index":0,"length":4}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}},"filter":{"filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}}],"Values":[[{"Literal":{"Value":"'Ledger 0L'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'Ledger 0L'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}}]},"valueMap":[{"0":"Ledger 0L"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Ledger'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}}}}],"title":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Slicer'"}}}}}]},"syncGroup":{"groupName":"Ledger","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"25ba12c5574cb08e6f4a","field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]}}]}}
```

#### e3900963152a42665296 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e3900963152a42665296/visual.json). Position: `{"x":1066.25,"y":16.25,"z":13000,"height":50,"width":196.25,"tabOrder":12000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}},"queryRef":"SAPLANGUAGE.LANGUAGENAME","nativeQueryRef":"LANGUAGENAME","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"_ISOLanguage"}},"queryRef":"SAPLANGUAGE._ISOLanguage","nativeQueryRef":"_ISOLanguage","active":false}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"s","Entity":"SAPLANGUAGE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"s"}},"Property":"LANGUAGENAME"}}],"Values":[[{"Literal":{"Value":"'English'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'English'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}}]},"valueMap":[{"0":"English"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"LANGUAGENAME","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### e58083d44409faf86c31 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e58083d44409faf86c31/visual.json). Position: `{"x":225.71428571428572,"y":97.14285714285715,"z":7000,"height":787.1428571428572,"width":1040,"tabOrder":6000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### e97255934c5329ff4d89 — image

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/e97255934c5329ff4d89/visual.json). Position: `{"x":0,"y":3.25,"z":42001,"height":27.25,"width":34.25,"tabOrder":1000}`.

```json
{"visual":{"visualType":"image","objects":{"general":[{"properties":{"imageUrl":{"expr":{"ResourcePackageItem":{"PackageName":"RegisteredResources","PackageType":1,"ItemName":"Data_Bar_Vertical_Highlight26202892008048195.png"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"d13eeae93a65a7f311bf","howCreated":"InsertVisualButton"}
```

#### eb629890193a94d01114 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/eb629890193a94d01114/visual.json). Position: `{"x":980,"y":112,"z":11000,"height":15.99536,"width":73.9814,"tabOrder":10000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Field'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### f12ad8ee4155a123ec30 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/29205fb9a9b601d02447/visuals/f12ad8ee4155a123ec30/visual.json). Position: `{"x":15.555555555555555,"y":510,"z":17000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":16000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"EN"}},"queryRef":"PROFITCENTERTEXT.EN","nativeQueryRef":"ProfitCenterText","active":true,"displayName":"ProfitCenterText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_PROFITCENTERTEXT"}},"Property":"FIELD_PARAM_PROFITCENTERTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Profit Center'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"ProfitCenter","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"c6457de37d1b60002e60","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"p","Entity":"PROFITCENTERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"p"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]},"howCreated":"User"}]}}
```

### YTD Financial Statement — bf28c024fb01861a71b5

[Page definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/page.json). 1280 × 900; FitToPage; 20 visual containers. Active authoring page: False.

Page configuration (including all page-level filtering, drillthrough and interaction metadata if authored):

```json
{"$schema":"https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json","name":"bf28c024fb01861a71b5","displayName":"YTD Financial Statement","displayOption":"FitToPage","height":900,"width":1280}
```

| Container | Type | Authored labels | Bound fields / measures |
|---|---|---|---|
| [003210ce3a96cb304855](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/003210ce3a96cb304855/visual.json) | shape |  |  |
| [0a36164a4ae61211b8af](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/0a36164a4ae61211b8af/visual.json) | slicer | .visual.objects.header[0].properties.text='Chart of Accounts' | queryRef: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: c.CHARTOFACCOUNTS |
| [4a6498daebc550a471ab](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/4a6498daebc550a471ab/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Currency' |  |
| [58c27e1fcbadbbe5b2fb](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/58c27e1fcbadbbe5b2fb/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Language' |  |
| [639dfb56abab0f588a4a](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/639dfb56abab0f588a4a/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: SAPLANGUAGE.LANGUAGENAME; Column: SAPLANGUAGE.LANGUAGENAME; queryRef: SAPLANGUAGE._ISOLanguage; Column: SAPLANGUAGE._ISOLanguage; Column: s.LANGUAGENAME |
| [675b671de54ec46caa31](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/675b671de54ec46caa31/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Year' | queryRef: FISCALPERIODFORVARIANT.FISCALYEAR; Column: FISCALPERIODFORVARIANT.FISCALYEAR; Column: f.FISCALYEAR |
| [78bc3bd6fdb14f792ab1](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/78bc3bd6fdb14f792ab1/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Period' | queryRef: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: f.FISCALPERIOD |
| [7cbe2da8c2d5dde0ae0a](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/7cbe2da8c2d5dde0ae0a/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=YTD Financial Statement |  |
| [822616374fa48aafab8f](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/822616374fa48aafab8f/visual.json) | slicer | .visual.objects.header[0].properties.text='Company Code' | queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; Column: c.COMPANYCODE |
| [85916a0a672b27aae9c4](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/85916a0a672b27aae9c4/visual.json) | image |  |  |
| [9836b6b6f8ba5dbee5b0](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/9836b6b6f8ba5dbee5b0/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=SegmentText; .visual.objects.header[0].properties.text='Segment' | queryRef: SEGMENTTEXT.EN; Column: SEGMENTTEXT.EN; Column: _SEGMENTTEXT.FIELD_PARAM_SEGMENTTEXT; Column: ISOLANGUAGE.LANGUAGECODE |
| [998a50853a91425a7b26](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/998a50853a91425a7b26/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=LedgerText; .visual.objects.header[0].properties.text='Ledger'; .visual.visualContainerObjects.title[0].properties.text='Slicer' | queryRef: LEDGERTEXT.EN; Column: LEDGERTEXT.EN; Column: _LEDGERTEXT.FIELD_PARAM_LEDGERTEXT; Column: l.DE; Column: LEDGERTEXT.DE |
| [b295dc684c36334c2cac](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/b295dc684c36334c2cac/visual.json) | shape |  |  |
| [b3238f301ea38b3f425f](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/b3238f301ea38b3f425f/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; Column: _._FIELD_PARAM_AGGR_CURRENCY Fields; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY Fields |
| [be48ebae767cadca9857](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/be48ebae767cadca9857/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=ProfitCenterText; .visual.objects.header[0].properties.text='Profit Center' | queryRef: PROFITCENTERTEXT.EN; Column: PROFITCENTERTEXT.EN; Column: _PROFITCENTERTEXT.FIELD_PARAM_PROFITCENTERTEXT; Column: PROFITCENTERTEXT.DE; Column: p.DE |
| [c10a06d89384aad6b615](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/c10a06d89384aad6b615/visual.json) | shape |  |  |
| [c614661e9e338d8aa46b](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/c614661e9e338d8aa46b/visual.json) | visualGroup | .visualGroup.displayName=Group 1 |  |
| [cec7836f9dbcae9f25a7](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/cec7836f9dbcae9f25a7/visual.json) | slicer | .visual.objects.header[0].properties.text='GL Hierarchy' | queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY; queryRef: GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION; Column: GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION; Column: g.GLACCOUNTHIERARCHY; Column: ISOLANGUAGE.LANGUAGECODE |
| [e53fc44ec2db63eb3626](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/e53fc44ec2db63eb3626/visual.json) | pivotTable | .visual.query.queryState.Columns.projections[0].displayName=Company Code Currency; .visual.query.queryState.Columns.projections[1].displayName=Debit/Credit; .visual.query.queryState.Values.projections[0].displayName=Opening Balance; .visual.query.queryState.Values.projections[1].displayName=Current Period; .visual.query.queryState.Values.projections[2].displayName=Closing Balance; .visual.visualContainerObjects.title[0].properties.text='Accounting Documents' | queryRef: AGGR_H.COMPANYCODECURRENCY; Column: AGGR_H.COMPANYCODECURRENCY; queryRef: DEBITCREDITCODETEXT.EN; Column: DEBITCREDITCODETEXT.EN; Column: _DEBITCREDITCODETEXT.FIELD_PARAM_DEBITCREDITCODETEXT; Column: _FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL1_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL1_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL2_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL2_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL3_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL3_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL4_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL4_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL5_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL5_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL6_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL6_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL7_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL7_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL8_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL8_TEXT; queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL9_TEXT; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL9_TEXT; queryRef: __MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_OPENING_BALANCE; Measure: __MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_OPENING_BALANCE; queryRef: __MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_CURRENT_PERIOD; Measure: __MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_CURRENT_PERIOD; queryRef: __MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_CLOSING_BALANCE; Measure: __MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_CLOSING_BALANCE; Column: _FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE.FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE; Column: _FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD.FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD; Column: _FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE.FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE |
| [f88b044ec9f7a920f4fd](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/f88b044ec9f7a920f4fd/visual.json) | shape |  |  |

#### 003210ce3a96cb304855 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/003210ce3a96cb304855/visual.json). Position: `{"x":0.5,"y":0,"z":8000,"height":34,"width":34}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}}],"outline":[{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}},"radius":{"expr":{"Literal":{"Value":"4D"}}}}}],"lockAspect":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"c614661e9e338d8aa46b","howCreated":"InsertVisualButton"}
```

#### 0a36164a4ae61211b8af — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/0a36164a4ae61211b8af/visual.json). Position: `{"x":14.285714285714286,"y":234.2857142857143,"z":10000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":8000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CHARTOFACCOUNTS"}},"Property":"CHARTOFACCOUNTS"}},"queryRef":"CHARTOFACCOUNTS.CHARTOFACCOUNTS","nativeQueryRef":"CHARTOFACCOUNTS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Chart of Accounts'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"CHARTOFACCOUNTS","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"CHARTOFACCOUNTS"}}],"Values":[[{"Literal":{"Value":"'YCOA'"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"CHARTOFACCOUNTS","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 4a6498daebc550a471ab — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/4a6498daebc550a471ab/visual.json). Position: `{"x":689.9005756148614,"y":33.49031920460492,"z":15000,"height":20.07861852433281,"width":100.47095761381476,"tabOrder":13000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Currency'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 58c27e1fcbadbbe5b2fb — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/58c27e1fcbadbbe5b2fb/visual.json). Position: `{"x":982.9408686551544,"y":33.49031920460492,"z":13000,"height":20.07861852433281,"width":98.78488749345892,"tabOrder":11000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Language'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 639dfb56abab0f588a4a — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/639dfb56abab0f588a4a/visual.json). Position: `{"x":1066.25,"y":16.25,"z":12000,"height":50,"width":196.25,"tabOrder":10000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}},"queryRef":"SAPLANGUAGE.LANGUAGENAME","nativeQueryRef":"LANGUAGENAME","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"_ISOLanguage"}},"queryRef":"SAPLANGUAGE._ISOLanguage","nativeQueryRef":"_ISOLanguage","active":false}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"s","Entity":"SAPLANGUAGE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"s"}},"Property":"LANGUAGENAME"}}],"Values":[[{"Literal":{"Value":"'English'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'English'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}}]},"valueMap":[{"0":"English"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"LANGUAGENAME","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 675b671de54ec46caa31 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/675b671de54ec46caa31/visual.json). Position: `{"x":14.285714285714286,"y":382.8571428571429,"z":3000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":2000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALYEAR","nativeQueryRef":"FISCALYEAR","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Year'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}}],"Values":[[{"Literal":{"Value":"2016L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALYEAR","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"06fffa506c1060bc2042","field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":1,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}},"Right":{"Literal":{"Value":"2015L"}}}}}]}}]}}
```

#### 78bc3bd6fdb14f792ab1 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/78bc3bd6fdb14f792ab1/visual.json). Position: `{"x":14.285714285714286,"y":452.8571428571429,"z":4000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":3000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALPERIOD"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALPERIOD","nativeQueryRef":"FISCALPERIOD1","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Period'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALPERIOD"}}],"Values":[[{"Literal":{"Value":"2L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALPERIOD","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 7cbe2da8c2d5dde0ae0a — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/7cbe2da8c2d5dde0ae0a/visual.json). Position: `{"x":65.71428571428572,"y":24.28571428571429,"z":6000,"height":35.714285714285715,"width":260,"tabOrder":5000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"YTD Financial Statement","textStyle":{"fontFamily":"Segoe (Bold)","fontSize":"14pt"}}]}]}}]},"drillFilterOtherVisuals":true}}
```

#### 822616374fa48aafab8f — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/822616374fa48aafab8f/visual.json). Position: `{"x":14.285714285714286,"y":165.71428571428572,"z":5000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":4000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Company Code'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"COMPANYCODE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"COMPANYCODE"}}],"Values":[[{"Literal":{"Value":"'1710'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"COMPANYCODE","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 85916a0a672b27aae9c4 — image

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/85916a0a672b27aae9c4/visual.json). Position: `{"x":0,"y":3.25,"z":42001,"height":27.25,"width":34.25,"tabOrder":1000}`.

```json
{"visual":{"visualType":"image","objects":{"general":[{"properties":{"imageUrl":{"expr":{"ResourcePackageItem":{"PackageName":"RegisteredResources","PackageType":1,"ItemName":"Data_Bar_Vertical_Highlight26202892008048195.png"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"c614661e9e338d8aa46b","howCreated":"InsertVisualButton"}
```

#### 9836b6b6f8ba5dbee5b0 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/9836b6b6f8ba5dbee5b0/visual.json). Position: `{"x":14.444444444444445,"y":522.2222222222222,"z":17000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":16000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"EN"}},"queryRef":"SEGMENTTEXT.EN","nativeQueryRef":"SegmentText","active":true,"displayName":"SegmentText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_SEGMENTTEXT"}},"Property":"FIELD_PARAM_SEGMENTTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Segment'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"pendingChangesIcon":[{"properties":{"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"syncGroup":{"groupName":"Segment","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"c7fe47135e53c5674ccb","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### 998a50853a91425a7b26 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/998a50853a91425a7b26/visual.json). Position: `{"x":15.070643642072215,"y":105.4945054945055,"z":11000,"height":60.27487179487179,"width":197.58953427524858,"tabOrder":9000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"EN"}},"queryRef":"LEDGERTEXT.EN","nativeQueryRef":"LedgerText","active":false,"displayName":"LedgerText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_LEDGERTEXT"}},"Property":"FIELD_PARAM_LEDGERTEXT"}},"index":0,"length":4}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}},"filter":{"filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}}],"Values":[[{"Literal":{"Value":"'Ledger 0L'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'Ledger 0L'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}}]},"valueMap":[{"0":"Ledger 0L"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Ledger'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}}}}],"title":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Slicer'"}}}}}]},"syncGroup":{"groupName":"Ledger","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"64c905b4ee713ca7136c","field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]}}]}}
```

#### b295dc684c36334c2cac — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/b295dc684c36334c2cac/visual.json). Position: `{"x":0,"y":0,"z":0,"height":82,"width":1280}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### b3238f301ea38b3f425f — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/b3238f301ea38b3f425f/visual.json). Position: `{"x":771.9518576661434,"y":16.74515960230246,"z":14000,"height":50.23547880690738,"width":195.9183673469388,"tabOrder":12000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}},"queryRef":"_FIELD_PARAM_AGGR_CURRENCY._FIELD_PARAM_AGGR_CURRENCY","nativeQueryRef":"_FIELD_PARAM_AGGR_CURRENCY","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"_","Entity":"_FIELD_PARAM_AGGR_CURRENCY","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"_"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY Fields"}}],"Values":[[{"Literal":{"Value":"'''AGGR_H''[COMPANYCODECURRENCY]'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'''AGGR_H''[COMPANYCODECURRENCY]'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY Fields"}}}]},"valueMap":[{"0":"Company Code Currency"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### be48ebae767cadca9857 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/be48ebae767cadca9857/visual.json). Position: `{"x":14.444444444444445,"y":590,"z":16000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":15000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"EN"}},"queryRef":"PROFITCENTERTEXT.EN","nativeQueryRef":"ProfitCenterText","active":true,"displayName":"ProfitCenterText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_PROFITCENTERTEXT"}},"Property":"FIELD_PARAM_PROFITCENTERTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Profit Center'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"ProfitCenter","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"9c14e88edc360d095246","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"p","Entity":"PROFITCENTERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"p"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]},"howCreated":"User"}]}}
```

#### c10a06d89384aad6b615 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/c10a06d89384aad6b615/visual.json). Position: `{"x":15,"y":97.5,"z":1000,"height":787.5,"width":195,"tabOrder":1000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### c614661e9e338d8aa46b — visualGroup

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/c614661e9e338d8aa46b/visual.json). Position: `{"x":15.5,"y":24,"z":7000,"height":34,"width":34.5,"tabOrder":17000}`.

```json
{"visualGroup":{"displayName":"Group 1","groupMode":"ScaleMode"}}
```

#### cec7836f9dbcae9f25a7 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/cec7836f9dbcae9f25a7/visual.json). Position: `{"x":16,"y":302,"z":2000,"height":68,"width":198,"tabOrder":14000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY","nativeQueryRef":"GLACCOUNTHIERARCHY","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"HIERARCHYVERSION"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION","nativeQueryRef":"HIERARCHYVERSION","active":false}]}}},"expansionStates":[{"roles":["Values"],"levels":[{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION"],"isCollapsed":true,"isPinned":true}],"root":{}}],"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"g","Entity":"GLACCOUNTHIERARCHYWTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"g"}},"Property":"GLACCOUNTHIERARCHY"}}],"Values":[[{"Literal":{"Value":"'YPA1'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'YPA1'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}}}]},"valueMap":[{"0":"YPA1"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'GL Hierarchy'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"GLACCOUNTHIERARCHY","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"26847c6270db59f56692","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### e53fc44ec2db63eb3626 — pivotTable

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/e53fc44ec2db63eb3626/visual.json). Position: `{"x":238,"y":112,"z":9000,"height":756,"width":1014,"tabOrder":7000}`.

```json
{"visual":{"visualType":"pivotTable","query":{"queryState":{"Columns":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"AGGR_H.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","active":true,"displayName":"Company Code Currency"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"queryRef":"DEBITCREDITCODETEXT.EN","nativeQueryRef":"Debit/Credit","active":false,"displayName":"Debit/Credit"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_DEBITCREDITCODETEXT"}},"Property":"FIELD_PARAM_DEBITCREDITCODETEXT"}},"index":1,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_CURRENCY"}},"Property":"_FIELD_PARAM_AGGR_CURRENCY"}},"index":0,"length":1}]},"Rows":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL1_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL1_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL1_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL2_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL2_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL2_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL3_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL3_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL3_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL4_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL4_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL4_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL5_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL5_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL5_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL6_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL6_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL6_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL7_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL7_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL7_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL8_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL8_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL8_TEXT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL9_TEXT"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL9_TEXT","nativeQueryRef":"GLACCOUNT_HIER_LEVEL9_TEXT","active":false}]},"Values":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_AGGR_HRCHY"}},"Property":"AGGR_HRCHY_COMPANYCODE_OPENING_BALANCE"}},"queryRef":"__MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_OPENING_BALANCE","nativeQueryRef":"Opening Balance","displayName":"Opening Balance"},{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_AGGR_HRCHY"}},"Property":"AGGR_HRCHY_COMPANYCODE_CURRENT_PERIOD"}},"queryRef":"__MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_CURRENT_PERIOD","nativeQueryRef":"Current Period","displayName":"Current Period"},{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_AGGR_HRCHY"}},"Property":"AGGR_HRCHY_COMPANYCODE_CLOSING_BALANCE"}},"queryRef":"__MEASURES_AGGR_HRCHY.AGGR_HRCHY_COMPANYCODE_CLOSING_BALANCE","nativeQueryRef":"Closing Balance","displayName":"Closing Balance"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE"}},"Property":"FIELD_PARAM_AGGR_HRCHY_CLOSING_BALANCE"}},"index":2,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD"}},"Property":"FIELD_PARAM_AGGR_HRCHY_CURRENT_PERIOD"}},"index":1,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE"}},"Property":"FIELD_PARAM_AGGR_HRCHY_OPENING_BALANCE"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL1_TEXT"}},"direction":"Ascending"}]}},"expansionStates":[{"roles":["Rows"],"levels":[{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL1_TEXT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL1_TEXT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL2_TEXT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL2_TEXT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL3_TEXT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL3_TEXT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL4_TEXT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL4_TEXT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL5_TEXT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL5_TEXT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL6_TEXT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL6_TEXT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL7_TEXT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL7_TEXT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL8_TEXT"],"isCollapsed":true,"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNT_HIER_LEVEL9_TEXT"],"isCollapsed":true}],"root":{"children":[{"identityValues":[{"Literal":{"Value":"'0YPS1 Project Profitability FSV: Net Margin'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'020 Net Margin'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'08 Net Revenue'"}}],"isToggled":true},{"identityValues":[{"Literal":{"Value":"'09 Costs'"}}],"isToggled":true}]},{"identityValues":[{"Literal":{"Value":"'00NOTASSGND'"}}],"isToggled":true}]},{"identityValues":[{"Literal":{"Value":"'0YPA1 SAP Best Practices Contribution Margin Report'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'00NOTASSGND'"}}],"children":[{"identityValues":[{"Literal":{"Value":"'10016000000 Land & Ld Improvemts'"}}],"isToggled":true},{"identityValues":[{"Literal":{"Value":"'10010010000 Petty Cash'"}}],"isToggled":true}]},{"identityValues":[{"Literal":{"Value":"'08 Contribution Margin Report'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'09 P&L before Tax'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'010 CM III'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'012 CM II'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'015 CM I'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'020 Net Sales'"}}],"isToggled":true}]},{"identityValues":[{"Literal":{"Value":"'022 Variances'"}}],"isToggled":true}]}]},{"identityValues":[{"Literal":{"Value":"'014 Non Operationg Expenses'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'10094226000 COPA assessments-Non'"}}],"isToggled":true}]}]}]}]}]}}],"objects":{"columnHeaders":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"grid":[{"properties":{"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}},"gridHorizontal":{"expr":{"Literal":{"Value":"true"}}},"gridHorizontalWeight":{"expr":{"Literal":{"Value":"5D"}}},"gridHorizontalColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"rowPadding":{"expr":{"Literal":{"Value":"6D"}}},"gridVertical":{"expr":{"Literal":{"Value":"false"}}}}}],"subTotals":[{"properties":{"perColumnLevel":{"expr":{"Literal":{"Value":"true"}}},"columnSubtotals":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Accounting Documents'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}]},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"03d7f8200b5a06a26553","field":{"Column":{"Expression":{"SourceRef":{"Entity":"AGGR_H"}},"Property":"COMPANYCODECURRENCY"}},"type":"Categorical"},{"name":"918cb3ff8e9ca2432302","field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"type":"Categorical"},{"name":"65e57dc365723ea3c1a2","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL1_TEXT"}},"type":"Categorical"},{"name":"20904e825c625734a525","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL2_TEXT"}},"type":"Categorical"},{"name":"c075e2ed00c743193cac","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL3_TEXT"}},"type":"Categorical"},{"name":"32cb28069479ec0dcc12","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL4_TEXT"}},"type":"Categorical"},{"name":"58ec6c3b3a81542d3be0","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL5_TEXT"}},"type":"Categorical"},{"name":"801a3d0fd1571ce6116e","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL6_TEXT"}},"type":"Categorical"},{"name":"cfc7cb1660b7e8eb6147","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL7_TEXT"}},"type":"Categorical"},{"name":"8711e960ea54bee01701","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL8_TEXT"}},"type":"Categorical"},{"name":"c1bd193f9a1121168c34","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNT_HIER_LEVEL9_TEXT"}},"type":"Categorical"},{"name":"b93b8ea63c0e65558a34","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_AGGR_HRCHY"}},"Property":"AGGR_HRCHY_COMPANYCODE_OPENING_BALANCE"}},"type":"Advanced"},{"name":"a83a6e174967d5190399","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_AGGR_HRCHY"}},"Property":"AGGR_HRCHY_COMPANYCODE_CURRENT_PERIOD"}},"type":"Advanced"},{"name":"3c01de88dc6da4e9238d","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_AGGR_HRCHY"}},"Property":"AGGR_HRCHY_COMPANYCODE_CLOSING_BALANCE"}},"type":"Advanced"}]}}
```

#### f88b044ec9f7a920f4fd — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/bf28c024fb01861a71b5/visuals/f88b044ec9f7a920f4fd/visual.json). Position: `{"x":225.71428571428572,"y":97.14285714285715,"z":8000,"height":787.1428571428572,"width":1040,"tabOrder":6000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

### Accounting Documents — e6299790245906d72cee

[Page definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/page.json). 1280 × 900; FitToWidth; 20 visual containers. Active authoring page: False.

Page configuration (including all page-level filtering, drillthrough and interaction metadata if authored):

```json
{"$schema":"https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json","name":"e6299790245906d72cee","displayName":"Accounting Documents","displayOption":"FitToWidth","height":900,"width":1280,"filterConfig":{"filters":[{"name":"5a2bde042c5925403e68","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"type":"Categorical","howCreated":"Drillthrough"}]},"pageBinding":{"name":"57e1b01d716c884ba598","type":"Drillthrough","parameters":[{"name":"80696ae606d6969ee348","boundFilter":"5a2bde042c5925403e68","asAggregation":false,"qnaSingleSelectRequired":false,"fieldExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}}}]}}
```

| Container | Type | Authored labels | Bound fields / measures |
|---|---|---|---|
| [14a74c0833d4b6ae09a0](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/14a74c0833d4b6ae09a0/visual.json) | slicer | .visual.objects.header[0].properties.text='Chart of Accounts' | queryRef: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: c.CHARTOFACCOUNTS |
| [222517b6abe4551fb997](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/222517b6abe4551fb997/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: SAPLANGUAGE.LANGUAGENAME; Column: SAPLANGUAGE.LANGUAGENAME; queryRef: SAPLANGUAGE._ISOLanguage; Column: SAPLANGUAGE._ISOLanguage; Column: s.LANGUAGENAME |
| [250d30d02d70e4b9178d](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/250d30d02d70e4b9178d/visual.json) | image |  |  |
| [39c583ecd4ce939c16d6](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/39c583ecd4ce939c16d6/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Account Documents Report |  |
| [3b8ecac0217ab004162b](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/3b8ecac0217ab004162b/visual.json) | slicer | .visual.objects.header[0].properties.text='Company Code' | queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; Column: c.COMPANYCODE |
| [440048e028b4d86029be](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/440048e028b4d86029be/visual.json) | shape |  |  |
| [5114060e1cb642640b2e](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/5114060e1cb642640b2e/visual.json) | shape |  |  |
| [5e8b021e0a8ba6b6835e](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/5e8b021e0a8ba6b6835e/visual.json) | shape |  |  |
| [7145bcb4e592aeb51615](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/7145bcb4e592aeb51615/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=ProfitCenterText; .visual.objects.header[0].properties.text='Profit Center' | queryRef: PROFITCENTERTEXT.EN; Column: PROFITCENTERTEXT.EN; Column: _PROFITCENTERTEXT.FIELD_PARAM_PROFITCENTERTEXT; Column: PROFITCENTERTEXT.DE; Column: p.DE |
| [7a63c7ee9e12e7940b43](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/7a63c7ee9e12e7940b43/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY; Column: _.FIELD_PARAM_CURRENCY Fields; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY Fields |
| [8c58dd955027e07bcea2](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/8c58dd955027e07bcea2/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Currency' |  |
| [8fef46ca513875a290d4](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/8fef46ca513875a290d4/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=LedgerText; .visual.objects.header[0].properties.text='Ledger'; .visual.visualContainerObjects.title[0].properties.text='Slicer' | queryRef: LEDGERTEXT.EN; Column: LEDGERTEXT.EN; Column: _LEDGERTEXT.FIELD_PARAM_LEDGERTEXT; Column: l.DE; Column: LEDGERTEXT.DE |
| [9fee9327dd090d2828d0](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/9fee9327dd090d2828d0/visual.json) | pivotTable | .visual.query.queryState.Columns.projections[0].displayName=Company Code Currency; .visual.query.queryState.Columns.projections[1].displayName=Debit/Credit; .visual.query.queryState.Rows.projections[1].displayName=GL Account Name; .visual.query.queryState.Values.projections[0].displayName=Current Period; .visual.visualContainerObjects.title[0].properties.text='Accounting Documents' | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; queryRef: DEBITCREDITCODETEXT.EN; Column: DEBITCREDITCODETEXT.EN; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY; Column: _DEBITCREDITCODETEXT.FIELD_PARAM_DEBITCREDITCODETEXT; queryRef: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; Column: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; queryRef: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; Column: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; queryRef: GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT; Column: GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT; Column: _GLACCOUNTINCHARTOFACCOUNTSTEXT.FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT; queryRef: __MEASURES_OTHER.COMPANYCODE_CURRENT_PERIOD; Measure: __MEASURES_OTHER.COMPANYCODE_CURRENT_PERIOD; Column: _FIELD_PARAM_CURRENT_PERIOD.FIELD_PARAM_CURRENT_PERIOD |
| [a5d3434d662f6807987f](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/a5d3434d662f6807987f/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=SegmentText; .visual.objects.header[0].properties.text='Segment' | queryRef: SEGMENTTEXT.EN; Column: SEGMENTTEXT.EN; Column: _SEGMENTTEXT.FIELD_PARAM_SEGMENTTEXT; Column: ISOLANGUAGE.LANGUAGECODE |
| [a6a8fe5d04616e2bdb78](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/a6a8fe5d04616e2bdb78/visual.json) | shape |  |  |
| [ab5659a759dac3704b40](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/ab5659a759dac3704b40/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Language' |  |
| [bb31a9b7082a09c6ea17](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/bb31a9b7082a09c6ea17/visual.json) | visualGroup | .visualGroup.displayName=Group 1 |  |
| [d117bc05fdeb97785435](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/d117bc05fdeb97785435/visual.json) | actionButton |  |  |
| [d4c55b82a48ca0d26231](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/d4c55b82a48ca0d26231/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Year' | queryRef: FISCALPERIODFORVARIANT.FISCALYEAR; Column: FISCALPERIODFORVARIANT.FISCALYEAR; Column: f.FISCALYEAR |
| [d9ef9a34a2eb8909edec](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/d9ef9a34a2eb8909edec/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Period' | queryRef: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: f.FISCALPERIOD |

#### 14a74c0833d4b6ae09a0 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/14a74c0833d4b6ae09a0/visual.json). Position: `{"x":16.74515960230246,"y":234.43223443223445,"z":9000,"height":68.65515436944008,"width":195.9183673469388,"tabOrder":8000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CHARTOFACCOUNTS"}},"Property":"CHARTOFACCOUNTS"}},"queryRef":"CHARTOFACCOUNTS.CHARTOFACCOUNTS","nativeQueryRef":"CHARTOFACCOUNTS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Chart of Accounts'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"CHARTOFACCOUNTS","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"CHARTOFACCOUNTS"}}],"Values":[[{"Literal":{"Value":"'YCOA'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"CHARTOFACCOUNTS","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 222517b6abe4551fb997 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/222517b6abe4551fb997/visual.json). Position: `{"x":1066.25,"y":16.25,"z":11000,"height":50,"width":196.25,"tabOrder":10000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}},"queryRef":"SAPLANGUAGE.LANGUAGENAME","nativeQueryRef":"LANGUAGENAME","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"_ISOLanguage"}},"queryRef":"SAPLANGUAGE._ISOLanguage","nativeQueryRef":"_ISOLanguage","active":false}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"s","Entity":"SAPLANGUAGE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"s"}},"Property":"LANGUAGENAME"}}],"Values":[[{"Literal":{"Value":"'English'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'English'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}}]},"valueMap":[{"0":"English"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"LANGUAGENAME","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 250d30d02d70e4b9178d — image

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/250d30d02d70e4b9178d/visual.json). Position: `{"x":0,"y":3.25,"z":42001,"height":27.25,"width":34.25,"tabOrder":1000}`.

```json
{"visual":{"visualType":"image","objects":{"general":[{"properties":{"imageUrl":{"expr":{"ResourcePackageItem":{"PackageName":"RegisteredResources","PackageType":1,"ItemName":"Data_Bar_Vertical_Highlight26202892008048195.png"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"bb31a9b7082a09c6ea17","howCreated":"InsertVisualButton"}
```

#### 39c583ecd4ce939c16d6 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/39c583ecd4ce939c16d6/visual.json). Position: `{"x":65.71428571428572,"y":24.28571428571429,"z":5000,"height":35.714285714285715,"width":260,"tabOrder":5000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Account Documents Report","textStyle":{"fontFamily":"Segoe (Bold)","fontSize":"14pt"}}]}]}}]},"drillFilterOtherVisuals":true}}
```

#### 3b8ecac0217ab004162b — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/3b8ecac0217ab004162b/visual.json). Position: `{"x":16.74515960230246,"y":165.77708006279434,"z":4000,"height":68.65515436944008,"width":195.9183673469388,"tabOrder":4000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Company Code'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"COMPANYCODE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"COMPANYCODE"}}],"Values":[[{"Literal":{"Value":"'1710'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"COMPANYCODE","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 440048e028b4d86029be — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/440048e028b4d86029be/visual.json). Position: `{"x":16,"y":98,"z":1000,"height":704,"width":196,"tabOrder":1000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 5114060e1cb642640b2e — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/5114060e1cb642640b2e/visual.json). Position: `{"x":0,"y":0,"z":0,"height":82,"width":1280}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 5e8b021e0a8ba6b6835e — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/5e8b021e0a8ba6b6835e/visual.json). Position: `{"x":229.4086865515437,"y":97.12192569335427,"z":7000,"height":785.3479853479854,"width":1033.1763474620618,"tabOrder":6000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 7145bcb4e592aeb51615 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/7145bcb4e592aeb51615/visual.json). Position: `{"x":16.666666666666668,"y":510,"z":15000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":14000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"EN"}},"queryRef":"PROFITCENTERTEXT.EN","nativeQueryRef":"ProfitCenterText","active":true,"displayName":"ProfitCenterText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_PROFITCENTERTEXT"}},"Property":"FIELD_PARAM_PROFITCENTERTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Profit Center'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"ProfitCenter","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"1b91365f838d238696ea","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"p","Entity":"PROFITCENTERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"p"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]},"howCreated":"User"}]}}
```

#### 7a63c7ee9e12e7940b43 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/7a63c7ee9e12e7940b43/visual.json). Position: `{"x":771.9518576661434,"y":16.74515960230246,"z":13000,"height":50.23547880690738,"width":195.9183673469388,"tabOrder":12000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"queryRef":"_FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY","nativeQueryRef":"FIELD_PARAM_CURRENCY","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"_","Entity":"_FIELD_PARAM_CURRENCY","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"_"}},"Property":"FIELD_PARAM_CURRENCY Fields"}}],"Values":[[{"Literal":{"Value":"'''GLACCOUNTLINEITEMRAWDATA''[COMPANYCODECURRENCY]'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'''GLACCOUNTLINEITEMRAWDATA''[COMPANYCODECURRENCY]'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY Fields"}}}]},"valueMap":[{"0":"Company Code Currency"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FIELD_PARAM_CURRENCY","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 8c58dd955027e07bcea2 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/8c58dd955027e07bcea2/visual.json). Position: `{"x":689.9005756148614,"y":33.49031920460492,"z":14000,"height":20.07861852433281,"width":100.47095761381476,"tabOrder":13000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Currency'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 8fef46ca513875a290d4 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/8fef46ca513875a290d4/visual.json). Position: `{"x":16.74515960230246,"y":105.4945054945055,"z":10000,"height":60.27487179487179,"width":197.58953427524858,"tabOrder":9000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"EN"}},"queryRef":"LEDGERTEXT.EN","nativeQueryRef":"LedgerText","active":false,"displayName":"LedgerText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_LEDGERTEXT"}},"Property":"FIELD_PARAM_LEDGERTEXT"}},"index":0,"length":4}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}},"filter":{"filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}}],"Values":[[{"Literal":{"Value":"'Ledger 0L'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'Ledger 0L'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}}]},"valueMap":[{"0":"Ledger 0L"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Ledger'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}}}}],"title":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Slicer'"}}}}}]},"syncGroup":{"groupName":"Ledger","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"f0346e54169edcfce806","field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]}}]}}
```

#### 9fee9327dd090d2828d0 — pivotTable

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/9fee9327dd090d2828d0/visual.json). Position: `{"x":242.80481423338566,"y":110.51805337519623,"z":8000,"height":756.8812140240711,"width":1008.0586080586081,"tabOrder":7000}`.

```json
{"visual":{"visualType":"pivotTable","query":{"queryState":{"Columns":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","active":true,"displayName":"Company Code Currency"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"queryRef":"DEBITCREDITCODETEXT.EN","nativeQueryRef":"Debit/Credit","active":false,"displayName":"Debit/Credit"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_DEBITCREDITCODETEXT"}},"Property":"FIELD_PARAM_DEBITCREDITCODETEXT"}},"index":1,"length":1}]},"Rows":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT","nativeQueryRef":"GLACCOUNT","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTSTEXT.EN","nativeQueryRef":"GL Account Name","active":true,"displayName":"GL Account Name"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"ACCOUNTINGDOCUMENT"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT","nativeQueryRef":"ACCOUNTINGDOCUMENT","active":true}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"index":1,"length":1}]},"Values":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_OTHER"}},"Property":"COMPANYCODE_CURRENT_PERIOD"}},"queryRef":"__MEASURES_OTHER.COMPANYCODE_CURRENT_PERIOD","nativeQueryRef":"Current Period","displayName":"Current Period"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENT_PERIOD"}},"Property":"FIELD_PARAM_CURRENT_PERIOD"}},"index":0,"length":1}]}}},"expansionStates":[{"roles":["Rows"],"levels":[{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}}],"isPinned":true},{"queryRefs":["GLACCOUNTINCHARTOFACCOUNTSTEXT.EN"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}}],"isPinned":true},{"queryRefs":["GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT"],"isCollapsed":true,"isPinned":true}],"root":{"children":[{"identityValues":[{"Literal":{"Value":"'0021120000'"}}],"isToggled":true},{"identityValues":[{"Literal":{"Value":"'0011001000'"}}],"isToggled":true},{"identityValues":[{"Literal":{"Value":"'0012100000'"}}],"isToggled":true,"children":[{"identityValues":[{"Literal":{"Value":"'Rcvbls Domestic'"}}],"isToggled":true}]},{"identityValues":[{"Literal":{"Value":"'0013400000'"}}],"isToggled":true},{"identityValues":[{"Literal":{"Value":"'0013600000'"}}],"isToggled":true},{"identityValues":[{"Literal":{"Value":"'0021100000'"}}],"isToggled":true}]}}],"objects":{"columnHeaders":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"grid":[{"properties":{"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}},"gridHorizontal":{"expr":{"Literal":{"Value":"true"}}},"gridHorizontalWeight":{"expr":{"Literal":{"Value":"5D"}}},"gridHorizontalColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"rowPadding":{"expr":{"Literal":{"Value":"6D"}}}}}],"subTotals":[{"properties":{"columnSubtotals":{"expr":{"Literal":{"Value":"false"}}},"perRowLevel":{"expr":{"Literal":{"Value":"true"}}},"rowSubtotals":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"layout":{"expr":{"Literal":{"Value":"'Tabular'"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Accounting Documents'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### a5d3434d662f6807987f — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/a5d3434d662f6807987f/visual.json). Position: `{"x":15.555555555555555,"y":442.22222222222223,"z":16000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":15000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"EN"}},"queryRef":"SEGMENTTEXT.EN","nativeQueryRef":"SegmentText","active":true,"displayName":"SegmentText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_SEGMENTTEXT"}},"Property":"FIELD_PARAM_SEGMENTTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Segment'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"pendingChangesIcon":[{"properties":{"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"syncGroup":{"groupName":"Segment","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"3adb9052e305595607d4","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### a6a8fe5d04616e2bdb78 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/a6a8fe5d04616e2bdb78/visual.json). Position: `{"x":0.5,"y":0,"z":8000,"height":34,"width":34}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}}],"outline":[{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}},"radius":{"expr":{"Literal":{"Value":"4D"}}}}}],"lockAspect":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"bb31a9b7082a09c6ea17","howCreated":"InsertVisualButton"}
```

#### ab5659a759dac3704b40 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/ab5659a759dac3704b40/visual.json). Position: `{"x":982.9408686551544,"y":33.49031920460492,"z":12000,"height":20.07861852433281,"width":98.78488749345892,"tabOrder":11000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Language'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### bb31a9b7082a09c6ea17 — visualGroup

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/bb31a9b7082a09c6ea17/visual.json). Position: `{"x":15.5,"y":24,"z":6000,"height":34,"width":34.5,"tabOrder":16000}`.

```json
{"visualGroup":{"displayName":"Group 1","groupMode":"ScaleMode"}}
```

#### d117bc05fdeb97785435 — actionButton

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/d117bc05fdeb97785435/visual.json). Position: `{"x":0,"y":0,"z":16001,"height":40,"width":100}`.

```json
{"visual":{"visualType":"actionButton","objects":{"icon":[{"properties":{"shapeType":{"expr":{"Literal":{"Value":"'back'"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"visualLink":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"type":{"expr":{"Literal":{"Value":"'Back'"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### d4c55b82a48ca0d26231 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/d4c55b82a48ca0d26231/visual.json). Position: `{"x":16.74515960230246,"y":303.08738880167454,"z":2000,"height":68.65515436944008,"width":195.9183673469388,"tabOrder":2000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALYEAR","nativeQueryRef":"FISCALYEAR","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Year'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}}],"Values":[[{"Literal":{"Value":"2016L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALYEAR","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"70de0e5ebb4d25a7d95c","field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":1,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}},"Right":{"Literal":{"Value":"2015L"}}}}}]}}]}}
```

#### d9ef9a34a2eb8909edec — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/e6299790245906d72cee/visuals/d9ef9a34a2eb8909edec/visual.json). Position: `{"x":15.070643642072215,"y":373.41705913134484,"z":3000,"height":68.65515436944008,"width":195.9183673469388,"tabOrder":3000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALPERIOD"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALPERIOD","nativeQueryRef":"FISCALPERIOD1","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Period'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALPERIOD"}}],"Values":[[{"Literal":{"Value":"2L"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALPERIOD","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

### Line Item Details — 8b1b618b6ff001ff0e26

[Page definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/page.json). 1280 × 900; FitToWidth; 22 visual containers. Active authoring page: False.

Page configuration (including all page-level filtering, drillthrough and interaction metadata if authored):

```json
{"$schema":"https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json","name":"8b1b618b6ff001ff0e26","displayName":"Line Item Details","displayOption":"FitToWidth","height":900,"width":1280,"filterConfig":{"filters":[{"name":"74be4368f7b7ac7d4b64","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"ACCOUNTINGDOCUMENT"}},"type":"Categorical","howCreated":"Drillthrough"}]},"pageBinding":{"name":"ce37519a6c1d1ff51ce4","type":"Drillthrough","parameters":[{"name":"59f664c22586757b152b","boundFilter":"74be4368f7b7ac7d4b64","asAggregation":false,"qnaSingleSelectRequired":false,"fieldExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"ACCOUNTINGDOCUMENT"}}}]}}
```

| Container | Type | Authored labels | Bound fields / measures |
|---|---|---|---|
| [0ced80506953f3c68c7f](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/0ced80506953f3c68c7f/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=ProfitCenterText; .visual.objects.header[0].properties.text='Profit Center' | queryRef: PROFITCENTERTEXT.EN; Column: PROFITCENTERTEXT.EN; Column: _PROFITCENTERTEXT.FIELD_PARAM_PROFITCENTERTEXT; Column: PROFITCENTERTEXT.DE; Column: p.DE |
| [0e575137473aa7623157](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/0e575137473aa7623157/visual.json) | shape |  |  |
| [1b7862689aeb98774859](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/1b7862689aeb98774859/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Language' |  |
| [27bf1035c00beb43e452](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/27bf1035c00beb43e452/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_TRIALBALANCE_FIELDS.FIELD_PARAM_TRIALBALANCE_FIELDS; Column: _FIELD_PARAM_TRIALBALANCE_FIELDS.FIELD_PARAM_TRIALBALANCE_FIELDS |
| [3cdcdcee2d2824317418](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/3cdcdcee2d2824317418/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=LedgerText; .visual.objects.header[0].properties.text='Ledger'; .visual.visualContainerObjects.title[0].properties.text='Slicer' | queryRef: LEDGERTEXT.EN; Column: LEDGERTEXT.EN; Column: _LEDGERTEXT.FIELD_PARAM_LEDGERTEXT; Column: l.DE; Column: LEDGERTEXT.DE |
| [3ce787753854bbc32dd9](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/3ce787753854bbc32dd9/visual.json) | tableEx | .visual.visualContainerObjects.title[0].properties.text='Accounting Documents' | queryRef: GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT; Column: GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT; queryRef: GLACCOUNTLINEITEMRAWDATA.DOCUMENTDATE; Column: GLACCOUNTLINEITEMRAWDATA.DOCUMENTDATE; queryRef: GLACCOUNTLINEITEMRAWDATA.POSTINGDATE; Column: GLACCOUNTLINEITEMRAWDATA.POSTINGDATE; queryRef: GLACCOUNTLINEITEMRAWDATA.CREATIONDATE; Column: GLACCOUNTLINEITEMRAWDATA.CREATIONDATE; queryRef: GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENTTYPE; Column: GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENTTYPE |
| [5c5b7cec9f3ce9cda9b0](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/5c5b7cec9f3ce9cda9b0/visual.json) | shape |  |  |
| [65482e820d92ecaedc31](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/65482e820d92ecaedc31/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Period' | queryRef: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: f.FISCALPERIOD |
| [66a76032acca5b00cc94](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/66a76032acca5b00cc94/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: SAPLANGUAGE.LANGUAGENAME; Column: SAPLANGUAGE.LANGUAGENAME; queryRef: SAPLANGUAGE._ISOLanguage; Column: SAPLANGUAGE._ISOLanguage; Column: s.LANGUAGENAME |
| [67a69b1425c9d9510dd3](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/67a69b1425c9d9510dd3/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Line Item Details |  |
| [78d5296331a393a49ffa](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/78d5296331a393a49ffa/visual.json) | slicer | .visual.objects.header[0].properties.text='Company Code' | queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; Column: c.COMPANYCODE |
| [82b308d53826bd43822e](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/82b308d53826bd43822e/visual.json) | shape |  |  |
| [89630faab3ff40b159d6](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/89630faab3ff40b159d6/visual.json) | actionButton |  |  |
| [ab956a4e8db4522f47c8](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/ab956a4e8db4522f47c8/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Field' |  |
| [b25f36452c7368c43e83](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/b25f36452c7368c43e83/visual.json) | shape |  |  |
| [c31dfab6b3e43390ce20](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/c31dfab6b3e43390ce20/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Year' | queryRef: FISCALPERIODFORVARIANT.FISCALYEAR; Column: FISCALPERIODFORVARIANT.FISCALYEAR; Column: f.FISCALYEAR |
| [cbddb9d84a7933e1c1f2](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/cbddb9d84a7933e1c1f2/visual.json) | tableEx | .visual.query.queryState.Values.projections[2].displayName=Debit/Credit; .visual.query.queryState.Values.projections[4].displayName=GL Account Name; .visual.query.queryState.Values.projections[16].displayName=Profit Center; .visual.query.queryState.Values.projections[17].displayName=Segment; .visual.query.queryState.Values.projections[18].displayName=Cost Center; .visual.query.queryState.Values.projections[19].displayName=Tax Code; .visual.query.queryState.Values.projections[20].displayName=Tax Country; .visual.visualContainerObjects.title[0].properties.text='Accounting Documents' | queryRef: GLACCOUNTLINEITEMRAWDATA.LEDGERGLLINEITEM; Column: GLACCOUNTLINEITEMRAWDATA.LEDGERGLLINEITEM; queryRef: GLACCOUNTLINEITEMRAWDATA.POSTINGKEY; Column: GLACCOUNTLINEITEMRAWDATA.POSTINGKEY; queryRef: DEBITCREDITCODETEXT.EN; Column: DEBITCREDITCODETEXT.EN; queryRef: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; Column: GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT; queryRef: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; Column: GLACCOUNTINCHARTOFACCOUNTSTEXT.EN; queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; queryRef: Sum(GLACCOUNTLINEITEMRAWDATA.AMOUNTINCOMPANYCODECURRENCY); Column: GLACCOUNTLINEITEMRAWDATA.AMOUNTINCOMPANYCODECURRENCY; queryRef: GLACCOUNTLINEITEMRAWDATA.TRANSACTIONCURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.TRANSACTIONCURRENCY; queryRef: Sum(GLACCOUNTLINEITEMRAWDATA.AMOUNTINTRANSACTIONCURRENCY); Column: GLACCOUNTLINEITEMRAWDATA.AMOUNTINTRANSACTIONCURRENCY; queryRef: GLACCOUNTLINEITEMRAWDATA.GLOBALCURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.GLOBALCURRENCY; queryRef: Sum(GLACCOUNTLINEITEMRAWDATA.AMOUNTINGLOBALCURRENCY); Column: GLACCOUNTLINEITEMRAWDATA.AMOUNTINGLOBALCURRENCY; queryRef: Sum(GLACCOUNTLINEITEMRAWDATA.QUANTITY); Column: GLACCOUNTLINEITEMRAWDATA.QUANTITY; queryRef: GLACCOUNTINCHARTOFACCOUNTS.PARTNERCOMPANY; Column: GLACCOUNTINCHARTOFACCOUNTS.PARTNERCOMPANY; queryRef: GLACCOUNTLINEITEMRAWDATA.PRODUCT; Column: GLACCOUNTLINEITEMRAWDATA.PRODUCT; queryRef: GLACCOUNTLINEITEMRAWDATA.DOCUMENTITEMTEXT; Column: GLACCOUNTLINEITEMRAWDATA.DOCUMENTITEMTEXT; queryRef: COSTCENTER.PLANT; Column: COSTCENTER.PLANT; queryRef: PROFITCENTER.PROFITCENTER; Column: PROFITCENTER.PROFITCENTER; queryRef: SEGMENTTEXT.SEGMENT; Column: SEGMENTTEXT.SEGMENT; queryRef: COSTCENTER.COSTCENTER; Column: COSTCENTER.COSTCENTER; queryRef: GLACCOUNTLINEITEMRAWDATA.TAXCODE; Column: GLACCOUNTLINEITEMRAWDATA.TAXCODE; queryRef: GLACCOUNTLINEITEMRAWDATA.TAXCOUNTRY; Column: GLACCOUNTLINEITEMRAWDATA.TAXCOUNTRY; Column: _DEBITCREDITCODETEXT.FIELD_PARAM_DEBITCREDITCODETEXT; Column: _GLACCOUNTINCHARTOFACCOUNTSTEXT.FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT; Column: _FIELD_PARAM_LINE_ITEM_FIELDS.FIELD_PARAM_LINE_ITEM_FIELDS |
| [cdaf1c3f069c8cd2b848](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/cdaf1c3f069c8cd2b848/visual.json) | image |  |  |
| [da3f00e40878564ff88f](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/da3f00e40878564ff88f/visual.json) | visualGroup | .visualGroup.displayName=Group 1 |  |
| [e729f582459a75c98abe](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/e729f582459a75c98abe/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=SegmentText; .visual.objects.header[0].properties.text='Segment' | queryRef: SEGMENTTEXT.EN; Column: SEGMENTTEXT.EN; Column: _SEGMENTTEXT.FIELD_PARAM_SEGMENTTEXT; Column: ISOLANGUAGE.LANGUAGECODE |
| [e88308640fb0a5b1d150](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/e88308640fb0a5b1d150/visual.json) | slicer | .visual.objects.header[0].properties.text='Chart of Accounts' | queryRef: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: c.CHARTOFACCOUNTS |
| [f96baca1a52d7d4c017f](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/f96baca1a52d7d4c017f/visual.json) | shape |  |  |

#### 0ced80506953f3c68c7f — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/0ced80506953f3c68c7f/visual.json). Position: `{"x":13.333333333333332,"y":510,"z":4000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":16000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"EN"}},"queryRef":"PROFITCENTERTEXT.EN","nativeQueryRef":"ProfitCenterText","active":true,"displayName":"ProfitCenterText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_PROFITCENTERTEXT"}},"Property":"FIELD_PARAM_PROFITCENTERTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Profit Center'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"ProfitCenter","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"f0e1dad0d794c8b90437","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"p","Entity":"PROFITCENTERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"p"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]},"howCreated":"User"}]}}
```

#### 0e575137473aa7623157 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/0e575137473aa7623157/visual.json). Position: `{"x":0,"y":0,"z":1000,"height":82,"width":1280}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 1b7862689aeb98774859 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/1b7862689aeb98774859/visual.json). Position: `{"x":982.9408686551544,"y":33.49031920460492,"z":18000,"height":20.07861852433281,"width":98.78488749345892,"tabOrder":15000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Language'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 27bf1035c00beb43e452 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/27bf1035c00beb43e452/visual.json). Position: `{"x":1063.3364801415978,"y":456.4778809512733,"z":14000,"height":50,"width":195.9954,"tabOrder":10000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_TRIALBALANCE_FIELDS"}},"Property":"FIELD_PARAM_TRIALBALANCE_FIELDS"}},"queryRef":"_FIELD_PARAM_TRIALBALANCE_FIELDS.FIELD_PARAM_TRIALBALANCE_FIELDS","nativeQueryRef":"FIELD_PARAM_TRIALBALANCE_FIELDS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"false"}}},"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FIELD_PARAM_TRIALBALANCE_FIELDS","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 3cdcdcee2d2824317418 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/3cdcdcee2d2824317418/visual.json). Position: `{"x":15.070643642072215,"y":105.4945054945055,"z":16000,"height":60.27487179487179,"width":197.58953427524858,"tabOrder":13000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"EN"}},"queryRef":"LEDGERTEXT.EN","nativeQueryRef":"LedgerText","active":false,"displayName":"LedgerText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_LEDGERTEXT"}},"Property":"FIELD_PARAM_LEDGERTEXT"}},"index":0,"length":4}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}},"filter":{"filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}}],"Values":[[{"Literal":{"Value":"'Ledger 0L'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'Ledger 0L'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}}]},"valueMap":[{"0":"Ledger 0L"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Ledger'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}}}}],"title":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Slicer'"}}}}}]},"syncGroup":{"groupName":"Ledger","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"4197b1280d542ac1e987","field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]}}]}}
```

#### 3ce787753854bbc32dd9 — tableEx

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/3ce787753854bbc32dd9/visual.json). Position: `{"x":239.45578231292518,"y":113.86708529565672,"z":11000,"height":309.7854526425955,"width":1011.4076399790686,"tabOrder":7000}`.

```json
{"visual":{"visualType":"tableEx","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"ACCOUNTINGDOCUMENT"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENT","nativeQueryRef":"ACCOUNTINGDOCUMENT"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"DOCUMENTDATE"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.DOCUMENTDATE","nativeQueryRef":"DOCUMENTDATE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"POSTINGDATE"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.POSTINGDATE","nativeQueryRef":"POSTINGDATE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"CREATIONDATE"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.CREATIONDATE","nativeQueryRef":"CREATIONDATE"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"ACCOUNTINGDOCUMENTTYPE"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.ACCOUNTINGDOCUMENTTYPE","nativeQueryRef":"ACCOUNTINGDOCUMENTTYPE"}]}}},"objects":{"columnHeaders":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"grid":[{"properties":{"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}},"gridHorizontal":{"expr":{"Literal":{"Value":"true"}}},"gridHorizontalWeight":{"expr":{"Literal":{"Value":"5D"}}},"gridHorizontalColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"rowPadding":{"expr":{"Literal":{"Value":"6D"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Accounting Documents'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}]},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"d0baeb776560ccb009b3","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"ACCOUNTINGDOCUMENT"}},"type":"Categorical"},{"name":"2fd21d1b91961be7b7a7","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"DOCUMENTDATE"}},"type":"Categorical"},{"name":"144b6384a0a3323aaeeb","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"POSTINGDATE"}},"type":"Categorical"},{"name":"d85ccfc0bec91d5d0a69","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"CREATIONDATE"}},"type":"Categorical"},{"name":"b0e26097e5e42b0366d0","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"ACCOUNTINGDOCUMENTTYPE"}},"type":"Categorical"}]}}
```

#### 5c5b7cec9f3ce9cda9b0 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/5c5b7cec9f3ce9cda9b0/visual.json). Position: `{"x":15,"y":97.5,"z":2000,"height":787.5,"width":195,"tabOrder":1000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 65482e820d92ecaedc31 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/65482e820d92ecaedc31/visual.json). Position: `{"x":14.285714285714286,"y":372.8571428571429,"z":5000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":3000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALPERIOD"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALPERIOD","nativeQueryRef":"FISCALPERIOD1","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Period'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALPERIOD"}}],"Values":[[{"Literal":{"Value":"2L"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALPERIOD","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 66a76032acca5b00cc94 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/66a76032acca5b00cc94/visual.json). Position: `{"x":1066.25,"y":16.25,"z":17000,"height":50,"width":196.25,"tabOrder":14000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}},"queryRef":"SAPLANGUAGE.LANGUAGENAME","nativeQueryRef":"LANGUAGENAME","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"_ISOLanguage"}},"queryRef":"SAPLANGUAGE._ISOLanguage","nativeQueryRef":"_ISOLanguage","active":false}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"s","Entity":"SAPLANGUAGE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"s"}},"Property":"LANGUAGENAME"}}],"Values":[[{"Literal":{"Value":"'English'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'English'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}}]},"valueMap":[{"0":"English"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"LANGUAGENAME","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 67a69b1425c9d9510dd3 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/67a69b1425c9d9510dd3/visual.json). Position: `{"x":65.71428571428572,"y":24.28571428571429,"z":7000,"height":35.714285714285715,"width":260,"tabOrder":5000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Line Item Details","textStyle":{"fontFamily":"Segoe (Bold)","fontSize":"14pt"}}]}]}}]},"drillFilterOtherVisuals":true}}
```

#### 78d5296331a393a49ffa — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/78d5296331a393a49ffa/visual.json). Position: `{"x":14.285714285714286,"y":165.71428571428572,"z":6000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":4000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Company Code'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"COMPANYCODE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"COMPANYCODE"}}],"Values":[[{"Literal":{"Value":"'1710'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"COMPANYCODE","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 82b308d53826bd43822e — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/82b308d53826bd43822e/visual.json). Position: `{"x":0.5,"y":0,"z":8000,"height":34,"width":34}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}}],"outline":[{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}},"radius":{"expr":{"Literal":{"Value":"4D"}}}}}],"lockAspect":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"da3f00e40878564ff88f","howCreated":"InsertVisualButton"}
```

#### 89630faab3ff40b159d6 — actionButton

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/89630faab3ff40b159d6/visual.json). Position: `{"x":0,"y":0,"z":18001,"height":40,"width":100}`.

```json
{"visual":{"visualType":"actionButton","objects":{"icon":[{"properties":{"shapeType":{"expr":{"Literal":{"Value":"'back'"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"visualLink":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"type":{"expr":{"Literal":{"Value":"'Back'"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### ab956a4e8db4522f47c8 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/ab956a4e8db4522f47c8/visual.json). Position: `{"x":999.5462218170795,"y":472.864224025877,"z":15000,"height":15.059022501308215,"width":73.66714809000523,"tabOrder":11000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Field'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### b25f36452c7368c43e83 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/b25f36452c7368c43e83/visual.json). Position: `{"x":226.05965463108322,"y":450.44479330193616,"z":10000,"height":433.6996336996337,"width":1039.8744113029827,"tabOrder":6000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### c31dfab6b3e43390ce20 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/c31dfab6b3e43390ce20/visual.json). Position: `{"x":14.285714285714286,"y":302.8571428571429,"z":3000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":2000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALYEAR","nativeQueryRef":"FISCALYEAR","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Year'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}}],"Values":[[{"Literal":{"Value":"2016L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALYEAR","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"212a9cc7d8557d9560bc","field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":1,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}},"Right":{"Literal":{"Value":"2015L"}}}}}]}}]}}
```

#### cbddb9d84a7933e1c1f2 — tableEx

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/cbddb9d84a7933e1c1f2/visual.json). Position: `{"x":239.45578231292518,"y":512.4018838304553,"z":13000,"height":356.6718995290424,"width":1011.4076399790686,"tabOrder":9000}`.

```json
{"visual":{"visualType":"tableEx","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"LEDGERGLLINEITEM"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.LEDGERGLLINEITEM","nativeQueryRef":"LEDGERGLLINEITEM"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"POSTINGKEY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.POSTINGKEY","nativeQueryRef":"POSTINGKEY"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"queryRef":"DEBITCREDITCODETEXT.EN","nativeQueryRef":"Debit/Credit","displayName":"Debit/Credit"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTS.GLACCOUNT","nativeQueryRef":"GLACCOUNT"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTSTEXT.EN","nativeQueryRef":"GL Account Name","displayName":"GL Account Name"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"COMPANYCODECURRENCY"},{"field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"AMOUNTINCOMPANYCODECURRENCY"}},"Function":0}},"queryRef":"Sum(GLACCOUNTLINEITEMRAWDATA.AMOUNTINCOMPANYCODECURRENCY)","nativeQueryRef":"Sum of AMOUNTINCOMPANYCODECURRENCY"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"TRANSACTIONCURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.TRANSACTIONCURRENCY","nativeQueryRef":"TRANSACTIONCURRENCY"},{"field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"AMOUNTINTRANSACTIONCURRENCY"}},"Function":0}},"queryRef":"Sum(GLACCOUNTLINEITEMRAWDATA.AMOUNTINTRANSACTIONCURRENCY)","nativeQueryRef":"Sum of AMOUNTINTRANSACTIONCURRENCY"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"GLOBALCURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.GLOBALCURRENCY","nativeQueryRef":"GLOBALCURRENCY"},{"field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"AMOUNTINGLOBALCURRENCY"}},"Function":0}},"queryRef":"Sum(GLACCOUNTLINEITEMRAWDATA.AMOUNTINGLOBALCURRENCY)","nativeQueryRef":"Sum of AMOUNTINGLOBALCURRENCY"},{"field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"QUANTITY"}},"Function":0}},"queryRef":"Sum(GLACCOUNTLINEITEMRAWDATA.QUANTITY)","nativeQueryRef":"Sum of QUANTITY"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"PARTNERCOMPANY"}},"queryRef":"GLACCOUNTINCHARTOFACCOUNTS.PARTNERCOMPANY","nativeQueryRef":"PARTNERCOMPANY"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"PRODUCT"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.PRODUCT","nativeQueryRef":"PRODUCT"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"DOCUMENTITEMTEXT"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.DOCUMENTITEMTEXT","nativeQueryRef":"DOCUMENTITEMTEXT"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"PLANT"}},"queryRef":"COSTCENTER.PLANT","nativeQueryRef":"PLANT"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}},"queryRef":"PROFITCENTER.PROFITCENTER","nativeQueryRef":"Profit Center","displayName":"Profit Center"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"SEGMENT"}},"queryRef":"SEGMENTTEXT.SEGMENT","nativeQueryRef":"Segment","displayName":"Segment"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}},"queryRef":"COSTCENTER.COSTCENTER","nativeQueryRef":"Cost Center","displayName":"Cost Center"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"TAXCODE"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.TAXCODE","nativeQueryRef":"Tax Code","displayName":"Tax Code"},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"TAXCOUNTRY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.TAXCOUNTRY","nativeQueryRef":"Tax Country","displayName":"Tax Country"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_DEBITCREDITCODETEXT"}},"Property":"FIELD_PARAM_DEBITCREDITCODETEXT"}},"index":2,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"FIELD_PARAM_GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"index":4,"length":1},{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_LINE_ITEM_FIELDS"}},"Property":"FIELD_PARAM_LINE_ITEM_FIELDS"}},"index":16,"length":5}]}}},"objects":{"columnHeaders":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"grid":[{"properties":{"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}},"gridHorizontal":{"expr":{"Literal":{"Value":"true"}}},"gridHorizontalWeight":{"expr":{"Literal":{"Value":"5D"}}},"gridHorizontalColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"rowPadding":{"expr":{"Literal":{"Value":"6D"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Accounting Documents'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}]},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"b4d77679e0d8cc0ee059","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"LEDGERGLLINEITEM"}},"type":"Categorical"},{"name":"9af005f790cc44305674","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"POSTINGKEY"}},"type":"Categorical"},{"name":"c62781203d33786ecc10","field":{"Column":{"Expression":{"SourceRef":{"Entity":"DEBITCREDITCODETEXT"}},"Property":"EN"}},"type":"Categorical"},{"name":"155975ed61be3c773da2","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"GLACCOUNT"}},"type":"Categorical"},{"name":"1686544a943d6074b426","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTSTEXT"}},"Property":"EN"}},"type":"Categorical"},{"name":"56f87ec7d3e0d1049403","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"type":"Categorical"},{"name":"6ccae537ca57dabca7be","field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"AMOUNTINCOMPANYCODECURRENCY"}},"Function":0}},"type":"Advanced"},{"name":"6310d61207bea079471d","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"TRANSACTIONCURRENCY"}},"type":"Categorical"},{"name":"0588e62979d4aa2eeb2e","field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"AMOUNTINTRANSACTIONCURRENCY"}},"Function":0}},"type":"Advanced"},{"name":"698d680581b4aa400618","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"GLOBALCURRENCY"}},"type":"Categorical"},{"name":"6a32f2bb403a6d3a5c03","field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"AMOUNTINGLOBALCURRENCY"}},"Function":0}},"type":"Advanced"},{"name":"484032c8ca9473206ea6","field":{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"QUANTITY"}},"Function":0}},"type":"Advanced"},{"name":"6923e44deb3acc4e8ec5","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTINCHARTOFACCOUNTS"}},"Property":"PARTNERCOMPANY"}},"type":"Categorical"},{"name":"e0c919b86e875c21349a","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"PRODUCT"}},"type":"Categorical"},{"name":"aec9333e80ea74860070","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"DOCUMENTITEMTEXT"}},"type":"Categorical"},{"name":"920f12a1347a65d48dd1","field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"PLANT"}},"type":"Categorical"},{"name":"5d7b0acb0eb2ed4e2514","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTER"}},"Property":"PROFITCENTER"}},"type":"Categorical"},{"name":"2f2ea3b0b48874012d41","field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"SEGMENT"}},"type":"Categorical"},{"name":"d3cabb407316b057e865","field":{"Column":{"Expression":{"SourceRef":{"Entity":"COSTCENTER"}},"Property":"COSTCENTER"}},"type":"Categorical"},{"name":"a822ae504087dc8b9052","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"TAXCODE"}},"type":"Categorical"},{"name":"e768037a391a01646c67","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"TAXCOUNTRY"}},"type":"Categorical"}]}}
```

#### cdaf1c3f069c8cd2b848 — image

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/cdaf1c3f069c8cd2b848/visual.json). Position: `{"x":0,"y":3.25,"z":42001,"height":27.25,"width":34.25,"tabOrder":1000}`.

```json
{"visual":{"visualType":"image","objects":{"general":[{"properties":{"imageUrl":{"expr":{"ResourcePackageItem":{"PackageName":"RegisteredResources","PackageType":1,"ItemName":"Data_Bar_Vertical_Highlight26202892008048195.png"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"da3f00e40878564ff88f","howCreated":"InsertVisualButton"}
```

#### da3f00e40878564ff88f — visualGroup

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/da3f00e40878564ff88f/visual.json). Position: `{"x":15.5,"y":24,"z":9000,"height":34,"width":34.5,"tabOrder":18000}`.

```json
{"visualGroup":{"displayName":"Group 1","groupMode":"ScaleMode"}}
```

#### e729f582459a75c98abe — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/e729f582459a75c98abe/visual.json). Position: `{"x":15.555555555555555,"y":442.22222222222223,"z":8000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":17000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"EN"}},"queryRef":"SEGMENTTEXT.EN","nativeQueryRef":"SegmentText","active":true,"displayName":"SegmentText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_SEGMENTTEXT"}},"Property":"FIELD_PARAM_SEGMENTTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Segment'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"pendingChangesIcon":[{"properties":{"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"syncGroup":{"groupName":"Segment","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"5f07d8f977ca69271216","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### e88308640fb0a5b1d150 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/e88308640fb0a5b1d150/visual.json). Position: `{"x":14.285714285714286,"y":234.2857142857143,"z":12000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":8000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CHARTOFACCOUNTS"}},"Property":"CHARTOFACCOUNTS"}},"queryRef":"CHARTOFACCOUNTS.CHARTOFACCOUNTS","nativeQueryRef":"CHARTOFACCOUNTS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Chart of Accounts'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"CHARTOFACCOUNTS","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"CHARTOFACCOUNTS"}}],"Values":[[{"Literal":{"Value":"'YCOA'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"CHARTOFACCOUNTS","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### f96baca1a52d7d4c017f — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/8b1b618b6ff001ff0e26/visuals/f96baca1a52d7d4c017f/visual.json). Position: `{"x":226.05965463108322,"y":95.44740973312402,"z":0,"height":346.6248037676609,"width":1039.8744113029827,"tabOrder":12000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

### Profitability — 9d8153603d7adaea330a

[Page definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/page.json). 1280 × 900; ActualSize; 69 visual containers. Active authoring page: False.

Page configuration (including all page-level filtering, drillthrough and interaction metadata if authored):

```json
{"$schema":"https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json","name":"9d8153603d7adaea330a","displayName":"Profitability","displayOption":"ActualSize","height":900,"width":1280}
```

| Container | Type | Authored labels | Bound fields / measures |
|---|---|---|---|
| [022a7e9c46b0d68d3022](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/022a7e9c46b0d68d3022/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [04623e7ca05eea00d863](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/04623e7ca05eea00d863/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Net Profit |  |
| [09b33a634ec51d353018](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/09b33a634ec51d353018/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: SAPLANGUAGE.LANGUAGENAME; Column: SAPLANGUAGE.LANGUAGENAME; queryRef: SAPLANGUAGE._ISOLanguage; Column: SAPLANGUAGE._ISOLanguage; Column: s.LANGUAGENAME |
| [0a21ef8ad686d5e4b929](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/0a21ef8ad686d5e4b929/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Profitability |  |
| [0c7fc44c0b01a3616547](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/0c7fc44c0b01a3616547/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Operating Profit Margin |  |
| [0f380954ddd08239c338](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/0f380954ddd08239c338/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Period' | queryRef: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: FISCALPERIODFORVARIANT.FISCALPERIOD; Column: f.FISCALPERIOD |
| [1074ece32c830c1966ec](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/1074ece32c830c1966ec/visual.json) | shape |  |  |
| [11ada8b8336c85311a3b](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/11ada8b8336c85311a3b/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Currency' |  |
| [1315e08073bc8f984534](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/1315e08073bc8f984534/visual.json) | gauge |  | queryRef: _AMOUNTS.OPERATING_PROFIT_MARGIN; Measure: __MEASURES_PROFITABILITY.OPERATING_PROFIT_MARGIN |
| [14d6bcb60ee87a5cd018](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/14d6bcb60ee87a5cd018/visual.json) | slicer | .visual.objects.header[0].properties.text='Company Code' | queryRef: COMPANYCODE.COMPANYCODE; Column: COMPANYCODE.COMPANYCODE; Column: c.COMPANYCODE |
| [151ea07762c8d967eb4e](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/151ea07762c8d967eb4e/visual.json) | visualGroup | .visualGroup.displayName=Group 1 |  |
| [158c31a673be93de0082](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/158c31a673be93de0082/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Revenue |  |
| [1ac3a94a571df8458099](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/1ac3a94a571df8458099/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [23bf942a0ca5124ba71a](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/23bf942a0ca5124ba71a/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Total Revenue By Fiscal Period |  |
| [285c54fc0abc8c98a981](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/285c54fc0abc8c98a981/visual.json) | shape |  |  |
| [2b0f011724edab3fef72](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/2b0f011724edab3fef72/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=ProfitCenterText; .visual.objects.header[0].properties.text='Profit Center' | queryRef: PROFITCENTERTEXT.EN; Column: PROFITCENTERTEXT.EN; Column: _PROFITCENTERTEXT.FIELD_PARAM_PROFITCENTERTEXT; Column: PROFITCENTERTEXT.DE; Column: p.DE |
| [2d5ffd4803385dd4609b](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/2d5ffd4803385dd4609b/visual.json) | shape |  |  |
| [35955bbf87215a08c92c](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/35955bbf87215a08c92c/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Product Group |  |
| [38ba28337072550a1c02](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/38ba28337072550a1c02/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Gross Profit |  |
| [3afdfd7103e703db0509](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3afdfd7103e703db0509/visual.json) | image |  |  |
| [3b14ddfa0de09d7499cc](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3b14ddfa0de09d7499cc/visual.json) | shape |  |  |
| [3bae70177e636e675e00](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3bae70177e636e675e00/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Opex Ratio |  |
| [3ddf5cea3860ab505497](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3ddf5cea3860ab505497/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Other Op. Expenses |  |
| [3e849ceeeea481c9f8c4](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3e849ceeeea481c9f8c4/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=SegmentText; .visual.objects.header[0].properties.text='Segment' | queryRef: SEGMENTTEXT.EN; Column: SEGMENTTEXT.EN; Column: _SEGMENTTEXT.FIELD_PARAM_SEGMENTTEXT; Column: ISOLANGUAGE.LANGUAGECODE |
| [4155f330c17ce0b4b7b6](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/4155f330c17ce0b4b7b6/visual.json) | slicer | .visual.objects.header[0].properties.text='Language' | queryRef: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY; Column: _.FIELD_PARAM_CURRENCY Fields; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY Fields |
| [415bf1693044bd13d828](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/415bf1693044bd13d828/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Income Statement |  |
| [519f715eb7a64122058c](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/519f715eb7a64122058c/visual.json) | slicer | .visual.objects.header[0].properties.text='GL Hierarchy' | queryRef: GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY; Column: GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY; queryRef: GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION; Column: GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION; Column: g.GLACCOUNTHIERARCHY; Column: ISOLANGUAGE.LANGUAGECODE |
| [53b2df6c0480a9dc2782](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/53b2df6c0480a9dc2782/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=Gross Profit | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_GROSSPROFIT; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_GROSSPROFIT; Column: _FIELD_PARAM_GROSSPROFIT.FIELD_PARAM_GROSSPROFIT |
| [57bcf2d8812aa7b07050](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/57bcf2d8812aa7b07050/visual.json) | slicer | .visual.objects.header[0].properties.text='Fiscal Year' | queryRef: FISCALPERIODFORVARIANT.FISCALYEAR; Column: FISCALPERIODFORVARIANT.FISCALYEAR; Column: f.FISCALYEAR |
| [59b051541b1d543aa51d](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/59b051541b1d543aa51d/visual.json) | shape |  |  |
| [5a2d3700c504558b172d](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/5a2d3700c504558b172d/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Gross Profit Margin |  |
| [5efe6c50d35ce324cb0a](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/5efe6c50d35ce324cb0a/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Customer |  |
| [61eae0b8ceada142c317](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/61eae0b8ceada142c317/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=; .visual.visualContainerObjects.title[0].properties.text='Language' |  |
| [64b317bc39396e70d326](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/64b317bc39396e70d326/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=Revenue | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_REVENUE; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_REVENUE; Column: _FIELD_PARAM_REVENUE.FIELD_PARAM_INCOMESTATEMENT |
| [655af0410d90c7749d45](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/655af0410d90c7749d45/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [6fa8688cb4b70e97bb3e](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/6fa8688cb4b70e97bb3e/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [6fcef90eacd36bd88940](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/6fcef90eacd36bd88940/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=Inventory Change | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_INVENTORYCHANGE; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_INVENTORYCHANGE; Column: _FIELD_PARAM_INVENTORYCHANGE.FIELD_PARAM_INVENTORYCHANGE |
| [70709086d98d4dcd4cbe](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/70709086d98d4dcd4cbe/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=COGS | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_COGS; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_COGS; Column: _FIELD_PARAM_COGS.FIELD_PARAM_COGS |
| [75886cb4b31c09c2e902](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/75886cb4b31c09c2e902/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=Taxes | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_TAXES; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_TAXES; Column: _FIELD_PARAM_TAXES.FIELD_PARAM_TAXES |
| [7632ae1ced5016a7d981](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/7632ae1ced5016a7d981/visual.json) | shape |  |  |
| [76e89baf32ed37ec2f17](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/76e89baf32ed37ec2f17/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [78d65aa986ec40802884](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/78d65aa986ec40802884/visual.json) | gauge |  | queryRef: _AMOUNTS.COMPANYCODE_GROSSPROFITMARGIN; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_GROSSPROFITMARGIN |
| [8a9a5fbd8952886eb0ee](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/8a9a5fbd8952886eb0ee/visual.json) | slicer |  | queryRef: CUSTOMER.CUSTOMERNAME; Column: CUSTOMER.CUSTOMERNAME |
| [8fb599db59cdbe98bcd2](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/8fb599db59cdbe98bcd2/visual.json) | gauge |  | queryRef: _AMOUNTS.OPEX_RATIO; Measure: __MEASURES_PROFITABILITY.OPEX_RATIO |
| [96823269b0ba7401e740](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/96823269b0ba7401e740/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [a0c0b9ff7900e842b898](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/a0c0b9ff7900e842b898/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=Other Expenses | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_OTHEREXPENSES; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_OTHEREXPENSES; Column: _FIELD_PARAM_OTHEREXPENSES.FIELD_PARAM_OTHEREXPENSES |
| [a925beda709586be3266](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/a925beda709586be3266/visual.json) | shape |  |  |
| [ab9488dca4c8b4cef225](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/ab9488dca4c8b4cef225/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [ad530b585647d2b55877](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/ad530b585647d2b55877/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=Product Group 2 | queryRef: PRODUCTGROUP2TEXT.EN; Column: PRODUCTGROUP2TEXT.EN; Column: _PRODUCTGROUP2TEXT.FIELD_PARAM_PRODUCTGROUP2TEXT |
| [b1b7966ca02e3569c543](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b1b7966ca02e3569c543/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=OPEX | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_OPEX; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_OPEX; Column: _FIELD_PARAM_OPEX.FIELD_PARAM_OPEX |
| [b7a6a87e09a4940e9109](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b7a6a87e09a4940e9109/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Operating Income (EBIT) |  |
| [b7f4565c37aa078c1106](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b7f4565c37aa078c1106/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [b94535e71c8e65003062](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b94535e71c8e65003062/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=Net Profit | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_NETPROFIT; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_NETPROFIT; Column: _FIELD_PARAM_NETPROFIT.FIELD_PARAM_NETPROFIT |
| [c1d2de3ae6cd0807b3ce](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c1d2de3ae6cd0807b3ce/visual.json) | slicer | .visual.objects.header[0].properties.text='Chart of Accounts' | queryRef: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: CHARTOFACCOUNTS.CHARTOFACCOUNTS; Column: c.CHARTOFACCOUNTS |
| [c1d8994dd7b802b60ba7](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c1d8994dd7b802b60ba7/visual.json) | shape |  |  |
| [c278eb8a97d10501cb15](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c278eb8a97d10501cb15/visual.json) | shape |  |  |
| [c7187f211a405064e4c9](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c7187f211a405064e4c9/visual.json) | slicer |  | queryRef: CUSTOMER.CUSTOMERNAME; Column: CUSTOMER.CUSTOMERNAME |
| [cd816d48edf2ddbde4c7](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/cd816d48edf2ddbde4c7/visual.json) | columnChart | .visual.query.queryState.Y.projections[0].displayName=Revenue | queryRef: GLACCOUNTLINEITEMRAWDATA.FISCALPERIOD; Column: GLACCOUNTLINEITEMRAWDATA.FISCALPERIOD; queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_REVENUE; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_REVENUE; Column: _FIELD_PARAM_REVENUE.FIELD_PARAM_INCOMESTATEMENT |
| [d2d2e10a1b33a063c700](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/d2d2e10a1b33a063c700/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Taxes |  |
| [d647a0b100002a3b4540](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/d647a0b100002a3b4540/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Product |  |
| [dbfe0631d909c8e19800](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/dbfe0631d909c8e19800/visual.json) | shape |  |  |
| [df6f230a62965ca36001](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/df6f230a62965ca36001/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=COGS |  |
| [e32cb6d088001702206b](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/e32cb6d088001702206b/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=OPEX |  |
| [e46c98b5df766161f081](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/e46c98b5df766161f081/visual.json) | slicer | .visual.query.queryState.Values.projections[0].displayName=LedgerText; .visual.objects.header[0].properties.text='Ledger'; .visual.visualContainerObjects.title[0].properties.text='Slicer' | queryRef: LEDGERTEXT.EN; Column: LEDGERTEXT.EN; Column: _LEDGERTEXT.FIELD_PARAM_LEDGERTEXT; Column: l.DE; Column: LEDGERTEXT.DE |
| [e6bb0a4a0c4a40221c9a](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/e6bb0a4a0c4a40221c9a/visual.json) | cardVisual | .visual.query.queryState.Data.projections[0].displayName=Operating Profit | queryRef: __MEASURES_PROFITABILITY.COMPANYCODE_OPERATINGPROFIT; Measure: __MEASURES_PROFITABILITY.COMPANYCODE_OPERATINGPROFIT; Column: _FIELD_PARAM_OPERATINGPROFIT.FIELD_PARAM_OPERATINGPROFIT |
| [eaee74256e69018e1978](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/eaee74256e69018e1978/visual.json) | multiRowCard | .visual.query.queryState.Values.projections[0].displayName=Company Code Currency | queryRef: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY; Column: _FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY |
| [edabcba475aaa324156b](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/edabcba475aaa324156b/visual.json) | shape |  |  |
| [f2080c4ec32101bb2dc3](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/f2080c4ec32101bb2dc3/visual.json) | textbox | .visual.objects.general[0].properties.paragraphs[0].textRuns[0].value=Inventory Change |  |
| [fac176d08a7507778d66](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/fac176d08a7507778d66/visual.json) | shape |  |  |

#### 022a7e9c46b0d68d3022 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/022a7e9c46b0d68d3022/visual.json). Position: `{"x":1187.5,"y":728.75,"z":52000,"height":32.5,"width":80,"tabOrder":51000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"dataLabels":[{"properties":{"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 04623e7ca05eea00d863 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/04623e7ca05eea00d863/visual.json). Position: `{"x":770,"y":770,"z":44000,"height":53.75,"width":200,"tabOrder":43000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Net Profit","textStyle":{"fontWeight":"bold"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 09b33a634ec51d353018 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/09b33a634ec51d353018/visual.json). Position: `{"x":1066.25,"y":16.25,"z":1000,"height":50,"width":196.25,"tabOrder":1000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}},"queryRef":"SAPLANGUAGE.LANGUAGENAME","nativeQueryRef":"LANGUAGENAME","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"_ISOLanguage"}},"queryRef":"SAPLANGUAGE._ISOLanguage","nativeQueryRef":"_ISOLanguage","active":false}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"s","Entity":"SAPLANGUAGE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"s"}},"Property":"LANGUAGENAME"}}],"Values":[[{"Literal":{"Value":"'English'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'English'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"SAPLANGUAGE"}},"Property":"LANGUAGENAME"}}}]},"valueMap":[{"0":"English"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"LANGUAGENAME","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 0a21ef8ad686d5e4b929 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/0a21ef8ad686d5e4b929/visual.json). Position: `{"x":65.71428571428572,"y":24.28571428571429,"z":5000,"height":35.714285714285715,"width":260,"tabOrder":5000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Profitability","textStyle":{"fontFamily":"Segoe (Bold)","fontSize":"14pt"}}]}]}}]},"drillFilterOtherVisuals":true}}
```

#### 0c7fc44c0b01a3616547 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/0c7fc44c0b01a3616547/visual.json). Position: `{"x":917.5,"y":180,"z":30000,"height":40,"width":215,"tabOrder":29000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Operating Profit Margin","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}],"horizontalTextAlignment":"center"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 0f380954ddd08239c338 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/0f380954ddd08239c338/visual.json). Position: `{"x":14.285714285714286,"y":452.8571428571429,"z":9000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":8000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALPERIOD"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALPERIOD","nativeQueryRef":"FISCALPERIOD1","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Period'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALPERIOD"}}],"Values":[[{"Literal":{"Value":"2L"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALPERIOD","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 1074ece32c830c1966ec — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/1074ece32c830c1966ec/visual.json). Position: `{"x":15,"y":97.5,"z":7000,"height":787.5,"width":195,"tabOrder":6000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 11ada8b8336c85311a3b — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/11ada8b8336c85311a3b/visual.json). Position: `{"x":689.9005756148614,"y":33.49031920460492,"z":4000,"height":20.07861852433281,"width":100.47095761381476,"tabOrder":4000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Currency'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 1315e08073bc8f984534 — gauge

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/1315e08073bc8f984534/visual.json). Position: `{"x":1038.75,"y":260,"z":32000,"height":100,"width":141.25,"tabOrder":31000}`.

```json
{"visual":{"visualType":"gauge","query":{"queryState":{"Y":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"OPERATING_PROFIT_MARGIN"}},"queryRef":"_AMOUNTS.OPERATING_PROFIT_MARGIN","nativeQueryRef":"OPERATING_PROFIT_MARGIN"}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"OPERATING_PROFIT_MARGIN"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"target":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"labels":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"calloutValue":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"dataPoint":[{"properties":{"fill":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 14d6bcb60ee87a5cd018 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/14d6bcb60ee87a5cd018/visual.json). Position: `{"x":14.285714285714286,"y":165.71428571428572,"z":10000,"height":68.57142857142857,"width":197.14285714285717,"tabOrder":9000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"COMPANYCODE"}},"Property":"COMPANYCODE"}},"queryRef":"COMPANYCODE.COMPANYCODE","nativeQueryRef":"COMPANYCODE","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Company Code'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"COMPANYCODE","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"COMPANYCODE"}}],"Values":[[{"Literal":{"Value":"'1710'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"COMPANYCODE","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 151ea07762c8d967eb4e — visualGroup

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/151ea07762c8d967eb4e/visual.json). Position: `{"x":15.5,"y":24,"z":6000,"height":34,"width":34.5,"tabOrder":66000}`.

```json
{"visualGroup":{"displayName":"Group 1","groupMode":"ScaleMode"}}
```

#### 158c31a673be93de0082 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/158c31a673be93de0082/visual.json). Position: `{"x":768.75,"y":432.5,"z":36000,"height":40,"width":138.75,"tabOrder":35000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Revenue","textStyle":{"fontSize":"10.5pt"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 1ac3a94a571df8458099 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/1ac3a94a571df8458099/visual.json). Position: `{"x":1187.5,"y":600,"z":65000,"height":32.5,"width":80,"tabOrder":64000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 23bf942a0ca5124ba71a — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/23bf942a0ca5124ba71a/visual.json). Position: `{"x":198.75,"y":383.75,"z":34000,"height":42.5,"width":286.25,"tabOrder":33000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Total Revenue By Fiscal Period","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}],"horizontalTextAlignment":"center"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 285c54fc0abc8c98a981 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/285c54fc0abc8c98a981/visual.json). Position: `{"x":767.5,"y":483.75,"z":56000,"height":48.75,"width":495,"tabOrder":55000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'line'"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.1}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}},"transparency":{"expr":{"Literal":{"Value":"70D"}}}},"selector":{"id":"default"}}]},"drillFilterOtherVisuals":true}}
```

#### 2b0f011724edab3fef72 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/2b0f011724edab3fef72/visual.json). Position: `{"x":13.333333333333332,"y":583.4444442353692,"z":14000,"height":67.77777777777777,"width":197.77777777777777,"tabOrder":13000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"EN"}},"queryRef":"PROFITCENTERTEXT.EN","nativeQueryRef":"ProfitCenterText","active":true,"displayName":"ProfitCenterText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_PROFITCENTERTEXT"}},"Property":"FIELD_PARAM_PROFITCENTERTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Profit Center'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"ProfitCenter","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"c06a17b5282b6c581348","field":{"Column":{"Expression":{"SourceRef":{"Entity":"PROFITCENTERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"p","Entity":"PROFITCENTERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"p"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]},"howCreated":"User"}]}}
```

#### 2d5ffd4803385dd4609b — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/2d5ffd4803385dd4609b/visual.json). Position: `{"x":227.5,"y":171.25,"z":22000,"height":187.5,"width":332.5,"tabOrder":21000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 35955bbf87215a08c92c — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/35955bbf87215a08c92c/visual.json). Position: `{"x":518.75,"y":102.5,"z":17000,"height":41.25,"width":140,"tabOrder":16000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Product Group","textStyle":{"fontWeight":"bold","fontFamily":"DIN"}}],"horizontalTextAlignment":"right"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 38ba28337072550a1c02 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/38ba28337072550a1c02/visual.json). Position: `{"x":769.4379798041256,"y":518.0845908373934,"z":38000,"height":41.10944444444444,"width":176.66333333333336,"tabOrder":37000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Gross Profit","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 3afdfd7103e703db0509 — image

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3afdfd7103e703db0509/visual.json). Position: `{"x":0,"y":3.25,"z":42001,"height":27.25,"width":34.25,"tabOrder":1000}`.

```json
{"visual":{"visualType":"image","objects":{"general":[{"properties":{"imageUrl":{"expr":{"ResourcePackageItem":{"PackageName":"RegisteredResources","PackageType":1,"ItemName":"Data_Bar_Vertical_Highlight26202892008048195.png"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"151ea07762c8d967eb4e","howCreated":"InsertVisualButton"}
```

#### 3b14ddfa0de09d7499cc — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3b14ddfa0de09d7499cc/visual.json). Position: `{"x":752.5,"y":375,"z":26000,"height":493.75,"width":510,"tabOrder":25000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### 3bae70177e636e675e00 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3bae70177e636e675e00/visual.json). Position: `{"x":542.5,"y":180,"z":29000,"height":40,"width":175,"tabOrder":28000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Opex Ratio","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}],"horizontalTextAlignment":"center"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 3ddf5cea3860ab505497 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3ddf5cea3860ab505497/visual.json). Position: `{"x":770,"y":630,"z":41000,"height":40,"width":142.5,"tabOrder":40000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Other Op. Expenses","textStyle":{"fontSize":"10.5pt"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 3e849ceeeea481c9f8c4 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/3e849ceeeea481c9f8c4/visual.json). Position: `{"x":13.333333333333332,"y":515.5555555555555,"z":15000,"height":67.77266666666667,"width":197.7711111111111,"tabOrder":14000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"SEGMENTTEXT"}},"Property":"EN"}},"queryRef":"SEGMENTTEXT.EN","nativeQueryRef":"SegmentText","active":true,"displayName":"SegmentText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_SEGMENTTEXT"}},"Property":"FIELD_PARAM_SEGMENTTEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Segment'"}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"pendingChangesIcon":[{"properties":{"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}]},"syncGroup":{"groupName":"Segment","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"7a18860028e7f17d35e3","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### 4155f330c17ce0b4b7b6 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/4155f330c17ce0b4b7b6/visual.json). Position: `{"x":771.9518576661434,"y":16.74515960230246,"z":3000,"height":50.23547880690738,"width":195.9183673469388,"tabOrder":3000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"queryRef":"_FIELD_PARAM_CURRENCY.FIELD_PARAM_CURRENCY","nativeQueryRef":"FIELD_PARAM_CURRENCY","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Language'"}}},"textSize":{"expr":{"Literal":{"Value":"12D"}}},"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"_","Entity":"_FIELD_PARAM_CURRENCY","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"_"}},"Property":"FIELD_PARAM_CURRENCY Fields"}}],"Values":[[{"Literal":{"Value":"'''GLACCOUNTLINEITEMRAWDATA''[COMPANYCODECURRENCY]'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'''GLACCOUNTLINEITEMRAWDATA''[COMPANYCODECURRENCY]'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY Fields"}}}]},"valueMap":[{"0":"Company Code Currency"}]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FIELD_PARAM_CURRENCY","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 415bf1693044bd13d828 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/415bf1693044bd13d828/visual.json). Position: `{"x":686.25,"y":383.75,"z":35000,"height":42.5,"width":286.25,"tabOrder":34000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Income Statement","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}],"horizontalTextAlignment":"center"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 519f715eb7a64122058c — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/519f715eb7a64122058c/visual.json). Position: `{"x":14,"y":306,"z":13000,"height":68,"width":198,"tabOrder":12000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY","nativeQueryRef":"GLACCOUNTHIERARCHY","active":true},{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"HIERARCHYVERSION"}},"queryRef":"GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION","nativeQueryRef":"HIERARCHYVERSION","active":false}]}}},"expansionStates":[{"roles":["Values"],"levels":[{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.GLACCOUNTHIERARCHY"],"isCollapsed":true,"identityKeys":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}}],"isPinned":true},{"queryRefs":["GLACCOUNTHIERARCHYWTEXT.HIERARCHYVERSION"],"isCollapsed":true,"isPinned":true}],"root":{}}],"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"g","Entity":"GLACCOUNTHIERARCHYWTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"g"}},"Property":"GLACCOUNTHIERARCHY"}}],"Values":[[{"Literal":{"Value":"'YPA1'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'YPA1'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTHIERARCHYWTEXT"}},"Property":"GLACCOUNTHIERARCHY"}}}]},"valueMap":[{"0":"YPA1"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'GL Hierarchy'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"GLACCOUNTHIERARCHY","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"05e167dfa92d97dd13b6","field":{"Column":{"Expression":{"SourceRef":{"Entity":"ISOLANGUAGE"}},"Property":"LANGUAGECODE"}},"howCreated":"User","objects":{"general":[{"properties":{"requireSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]}}]}}
```

#### 53b2df6c0480a9dc2782 — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/53b2df6c0480a9dc2782/visual.json). Position: `{"x":992.5,"y":503.75,"z":46000,"height":41.25,"width":191.25,"tabOrder":45000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_GROSSPROFIT"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_GROSSPROFIT","nativeQueryRef":"Gross Profit","displayName":"Gross Profit"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_GROSSPROFIT"}},"Property":"FIELD_PARAM_GROSSPROFIT"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_GROSSPROFIT"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"cellPadding":{"expr":{"Literal":{"Value":"1L"}}},"backgroundShow":{"expr":{"Literal":{"Value":"true"}}},"backgroundTransparency":{"expr":{"Literal":{"Value":"100D"}}}}}],"value":[{"properties":{"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Bold'', wf_segoe-ui_bold, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"true"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_GROSSPROFIT"}},{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}}},"selector":{"id":"default"}},{"properties":{"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"bold":{"expr":{"Literal":{"Value":"true"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Bold'', wf_segoe-ui_bold, helvetica, arial, sans-serif'"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_GROSSPROFIT"}}],"label":[{"properties":{"textWrap":{"expr":{"Literal":{"Value":"true"}}},"position":{"expr":{"Literal":{"Value":"'belowValue'"}}},"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_GROSSPROFIT"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_GROSSPROFIT"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"0D"}}},"right":{"expr":{"Literal":{"Value":"0D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 57bcf2d8812aa7b07050 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/57bcf2d8812aa7b07050/visual.json). Position: `{"x":14.285714285714286,"y":382.8571428571429,"z":8000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":7000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"queryRef":"FISCALPERIODFORVARIANT.FISCALYEAR","nativeQueryRef":"FISCALYEAR","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Fiscal Year'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}}],"Values":[[{"Literal":{"Value":"2016L"}}]]}}}]}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"FISCALYEAR","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"fdd1c58e0bce0a8098bb","field":{"Column":{"Expression":{"SourceRef":{"Entity":"FISCALPERIODFORVARIANT"}},"Property":"FISCALYEAR"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"f","Entity":"FISCALPERIODFORVARIANT","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":1,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"FISCALYEAR"}},"Right":{"Literal":{"Value":"2015L"}}}}}]}}]}}
```

#### 59b051541b1d543aa51d — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/59b051541b1d543aa51d/visual.json). Position: `{"x":0.5,"y":0,"z":8000,"height":34,"width":34}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"4L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}}],"outline":[{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}},"radius":{"expr":{"Literal":{"Value":"4D"}}}}}],"lockAspect":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true},"parentGroupName":"151ea07762c8d967eb4e","howCreated":"InsertVisualButton"}
```

#### 5a2d3700c504558b172d — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/5a2d3700c504558b172d/visual.json). Position: `{"x":218.75,"y":180,"z":28000,"height":42.5,"width":177.5,"tabOrder":27000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Gross Profit Margin","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}],"horizontalTextAlignment":"center"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 5efe6c50d35ce324cb0a — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/5efe6c50d35ce324cb0a/visual.json). Position: `{"x":146.25,"y":102.5,"z":16000,"height":41.25,"width":137.5,"tabOrder":15000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Customer","textStyle":{"fontWeight":"bold","fontFamily":"DIN"}}],"horizontalTextAlignment":"right"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 61eae0b8ceada142c317 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/61eae0b8ceada142c317/visual.json). Position: `{"x":982.9408686551544,"y":33.49031920460492,"z":2000,"height":20.07861852433281,"width":98.78488749345892,"tabOrder":2000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":""}]}]}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"text":{"expr":{"Literal":{"Value":"'Language'"}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}},"alignment":{"expr":{"Literal":{"Value":"'center'"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 64b317bc39396e70d326 — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/64b317bc39396e70d326/visual.json). Position: `{"x":1037.5,"y":407.5,"z":45000,"height":71.25,"width":151.25,"tabOrder":44000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_REVENUE"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_REVENUE","nativeQueryRef":"Revenue","displayName":"Revenue"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_REVENUE"}},"Property":"FIELD_PARAM_INCOMESTATEMENT"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_REVENUE"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"orientation":{"expr":{"Literal":{"Value":"1D"}}},"cellPadding":{"expr":{"Literal":{"Value":"1L"}}},"style":{"expr":{"Literal":{"Value":"'Cards'"}}},"alignment":{"expr":{"Literal":{"Value":"'middle'"}}},"backgroundShow":{"expr":{"Literal":{"Value":"false"}}}}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"value":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"showFilterRestatementButton":{"expr":{"Literal":{"Value":"true"}}},"showOptionsMenu":{"expr":{"Literal":{"Value":"true"}}},"showSeeDataLayoutToggleButton":{"expr":{"Literal":{"Value":"true"}}},"showFocusModeButton":{"expr":{"Literal":{"Value":"true"}}},"showPinButton":{"expr":{"Literal":{"Value":"true"}}},"showDrillDownExpandButton":{"expr":{"Literal":{"Value":"true"}}},"showDrillDownLevelButton":{"expr":{"Literal":{"Value":"true"}}},"showDrillToggleButton":{"expr":{"Literal":{"Value":"true"}}},"showDrillUpButton":{"expr":{"Literal":{"Value":"true"}}},"showDrillRoleSelector":{"expr":{"Literal":{"Value":"true"}}},"showVisualErrorButton":{"expr":{"Literal":{"Value":"true"}}},"showVisualWarningButton":{"expr":{"Literal":{"Value":"true"}}},"showVisualInformationButton":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 655af0410d90c7749d45 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/655af0410d90c7749d45/visual.json). Position: `{"x":1186.25,"y":480,"z":62000,"height":32.5,"width":80,"tabOrder":61000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 6fa8688cb4b70e97bb3e — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/6fa8688cb4b70e97bb3e/visual.json). Position: `{"x":1186.25,"y":440,"z":60000,"height":32.5,"width":80,"tabOrder":59000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 6fcef90eacd36bd88940 — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/6fcef90eacd36bd88940/visual.json). Position: `{"x":988.75,"y":573.75,"z":47000,"height":50,"width":200,"tabOrder":46000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_INVENTORYCHANGE"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_INVENTORYCHANGE","nativeQueryRef":"Inventory Change","displayName":"Inventory Change"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_INVENTORYCHANGE"}},"Property":"FIELD_PARAM_INVENTORYCHANGE"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_INVENTORYCHANGE"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"cellPadding":{"expr":{"Literal":{"Value":"1L"}}}}}],"value":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_INVENTORYCHANGE"}},{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}}},"selector":{"id":"default"}},{"properties":{"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_INVENTORYCHANGE"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_INVENTORYCHANGE"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 70709086d98d4dcd4cbe — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/70709086d98d4dcd4cbe/visual.json). Position: `{"x":1017.5,"y":451.25,"z":61000,"height":61.25,"width":168.75,"tabOrder":60000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_COGS"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_COGS","nativeQueryRef":"COGS","displayName":"COGS"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_COGS"}},"Property":"FIELD_PARAM_COGS"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_COGS"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"orientation":{"expr":{"Literal":{"Value":"1D"}}},"cellPadding":{"expr":{"Literal":{"Value":"1L"}}},"style":{"expr":{"Literal":{"Value":"'Cards'"}}},"alignment":{"expr":{"Literal":{"Value":"'middle'"}}},"backgroundShow":{"expr":{"Literal":{"Value":"false"}}}}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"value":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 75886cb4b31c09c2e902 — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/75886cb4b31c09c2e902/visual.json). Position: `{"x":1052.5,"y":702.5,"z":51000,"height":48.75,"width":135,"tabOrder":50000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_TAXES"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_TAXES","nativeQueryRef":"Taxes","displayName":"Taxes"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_TAXES"}},"Property":"FIELD_PARAM_TAXES"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_TAXES"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"cellPadding":{"expr":{"Literal":{"Value":"1L"}}}}}],"value":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_TAXES"}},{"properties":{"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}}},"selector":{"id":"default"}},{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_TAXES"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_TAXES"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 7632ae1ced5016a7d981 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/7632ae1ced5016a7d981/visual.json). Position: `{"x":768.75,"y":398.75,"z":55000,"height":48.75,"width":492.5,"tabOrder":54000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'line'"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.1}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}},"transparency":{"expr":{"Literal":{"Value":"70D"}}},"weight":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"id":"default"}}]},"drillFilterOtherVisuals":true}}
```

#### 76e89baf32ed37ec2f17 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/76e89baf32ed37ec2f17/visual.json). Position: `{"x":1187.5,"y":686.25,"z":58000,"height":33.75,"width":80,"tabOrder":57000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"subTitle":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 78d65aa986ec40802884 — gauge

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/78d65aa986ec40802884/visual.json). Position: `{"x":321.25,"y":260,"z":27000,"height":100,"width":141.25,"tabOrder":26000}`.

```json
{"visual":{"visualType":"gauge","query":{"queryState":{"Y":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_GROSSPROFITMARGIN"}},"queryRef":"_AMOUNTS.COMPANYCODE_GROSSPROFITMARGIN","nativeQueryRef":"COMPANYCODE_GROSSPROFITMARGIN"}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_GROSSPROFITMARGIN"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"target":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"fontSize":{"expr":{"Literal":{"Value":"9D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}}}}],"labels":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"0D"}}},"fontSize":{"expr":{"Literal":{"Value":"9D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"labelPrecision":{"expr":{"Literal":{"Value":"0L"}}}}}],"calloutValue":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"}}}}}],"dataPoint":[{"properties":{"fill":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}},"target":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":2,"Percent":-0.5}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 8a9a5fbd8952886eb0ee — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/8a9a5fbd8952886eb0ee/visual.json). Position: `{"x":918.75,"y":118.75,"z":21000,"height":43.75,"width":353.75,"tabOrder":20000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CUSTOMER"}},"Property":"CUSTOMERNAME"}},"queryRef":"CUSTOMER.CUSTOMERNAME","nativeQueryRef":"CUSTOMERNAME","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"items":[{"properties":{"textSize":{"expr":{"Literal":{"Value":"9D"}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"transparency":{"expr":{"Literal":{"Value":"100D"}}}}}]},"syncGroup":{"groupName":"CUSTOMERNAME1","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### 8fb599db59cdbe98bcd2 — gauge

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/8fb599db59cdbe98bcd2/visual.json). Position: `{"x":675,"y":260,"z":31000,"height":100,"width":140,"tabOrder":30000}`.

```json
{"visual":{"visualType":"gauge","query":{"queryState":{"Y":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"OPEX_RATIO"}},"queryRef":"_AMOUNTS.OPEX_RATIO","nativeQueryRef":"OPEX_RATIO"}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"OPEX_RATIO"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"target":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"labels":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"calloutValue":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"dataPoint":[{"properties":{"fill":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### 96823269b0ba7401e740 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/96823269b0ba7401e740/visual.json). Position: `{"x":1187.5,"y":562.5,"z":64000,"height":32.5,"width":80,"tabOrder":63000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### a0c0b9ff7900e842b898 — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/a0c0b9ff7900e842b898/visual.json). Position: `{"x":1032.5,"y":612.5,"z":49000,"height":60,"width":155,"tabOrder":48000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_OTHEREXPENSES"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_OTHEREXPENSES","nativeQueryRef":"Other Expenses","displayName":"Other Expenses"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_OTHEREXPENSES"}},"Property":"FIELD_PARAM_OTHEREXPENSES"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_OTHEREXPENSES"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"cellPadding":{"expr":{"Literal":{"Value":"1L"}}}}}],"value":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_OTHEREXPENSES"}},{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_OTHEREXPENSES"}},{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}}},"selector":{"id":"default"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_OTHEREXPENSES"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_OTHEREXPENSES"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### a925beda709586be3266 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/a925beda709586be3266/visual.json). Position: `{"x":767.5,"y":645,"z":57000,"height":48.75,"width":493.75,"tabOrder":56000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'line'"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.1}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}},"transparency":{"expr":{"Literal":{"Value":"70D"}}}},"selector":{"id":"default"}}]},"drillFilterOtherVisuals":true}}
```

#### ab9488dca4c8b4cef225 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/ab9488dca4c8b4cef225/visual.json). Position: `{"x":1187.5,"y":638.75,"z":66000,"height":32.5,"width":80,"tabOrder":65000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### ad530b585647d2b55877 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/ad530b585647d2b55877/visual.json). Position: `{"x":567.5,"y":118.75,"z":20000,"height":43.75,"width":352.5,"tabOrder":19000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"PRODUCTGROUP2TEXT"}},"Property":"EN"}},"queryRef":"PRODUCTGROUP2TEXT.EN","nativeQueryRef":"Product Group 2","active":true,"displayName":"Product Group 2"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_PRODUCTGROUP2TEXT"}},"Property":"FIELD_PARAM_PRODUCTGROUP2TEXT"}},"index":0,"length":1}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"items":[{"properties":{"textSize":{"expr":{"Literal":{"Value":"9D"}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"header":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"transparency":{"expr":{"Literal":{"Value":"100D"}}}}}]},"syncGroup":{"groupName":"EN","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### b1b7966ca02e3569c543 — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b1b7966ca02e3569c543/visual.json). Position: `{"x":1017.5,"y":535,"z":48000,"height":61.25,"width":171.25,"tabOrder":47000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_OPEX"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_OPEX","nativeQueryRef":"OPEX","displayName":"OPEX"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_OPEX"}},"Property":"FIELD_PARAM_OPEX"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_OPEX"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"value":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI Bold'', wf_segoe-ui_bold, helvetica, arial, sans-serif'"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}}},"selector":{"id":"default"}},{"properties":{"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_OPEX"}},{"properties":{"bold":{"expr":{"Literal":{"Value":"true"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_OPEX"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"layout":[{"properties":{"cellPadding":{"expr":{"Literal":{"Value":"1L"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### b7a6a87e09a4940e9109 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b7a6a87e09a4940e9109/visual.json). Position: `{"x":770,"y":677.5,"z":42000,"height":53.75,"width":200,"tabOrder":41000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Operating Income (EBIT)","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### b7f4565c37aa078c1106 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b7f4565c37aa078c1106/visual.json). Position: `{"x":1187.5,"y":525,"z":63000,"height":32.5,"width":80,"tabOrder":62000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### b94535e71c8e65003062 — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/b94535e71c8e65003062/visual.json). Position: `{"x":1042.5,"y":748.75,"z":53000,"height":62.5,"width":146.25,"tabOrder":52000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_NETPROFIT"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_NETPROFIT","nativeQueryRef":"Net Profit","displayName":"Net Profit"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_NETPROFIT"}},"Property":"FIELD_PARAM_NETPROFIT"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_NETPROFIT"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"cellPadding":{"expr":{"Literal":{"Value":"1L"}}}}}],"value":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"bold":{"expr":{"Literal":{"Value":"true"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_NETPROFIT"}},{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"true"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_NETPROFIT"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_NETPROFIT"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### c1d2de3ae6cd0807b3ce — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c1d2de3ae6cd0807b3ce/visual.json). Position: `{"x":14.285714285714286,"y":234.2857142857143,"z":11000,"height":68.57142857142857,"width":198.57142857142858,"tabOrder":10000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CHARTOFACCOUNTS"}},"Property":"CHARTOFACCOUNTS"}},"queryRef":"CHARTOFACCOUNTS.CHARTOFACCOUNTS","nativeQueryRef":"CHARTOFACCOUNTS","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"header":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Chart of Accounts'"}}},"textSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}],"general":[{"properties":{"filter":{"filter":{"Version":2,"From":[{"Name":"c","Entity":"CHARTOFACCOUNTS","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"CHARTOFACCOUNTS"}}],"Values":[[{"Literal":{"Value":"'YCOA'"}}]]}}}]}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"syncGroup":{"groupName":"CHARTOFACCOUNTS","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### c1d8994dd7b802b60ba7 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c1d8994dd7b802b60ba7/visual.json). Position: `{"x":928.75,"y":171.25,"z":24000,"height":187.5,"width":333,"tabOrder":23000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### c278eb8a97d10501cb15 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c278eb8a97d10501cb15/visual.json). Position: `{"x":0,"y":0,"z":0,"height":82,"width":1280}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### c7187f211a405064e4c9 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/c7187f211a405064e4c9/visual.json). Position: `{"x":216.25,"y":118.75,"z":19000,"height":43.75,"width":352.5,"tabOrder":18000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"CUSTOMER"}},"Property":"CUSTOMERNAME"}},"queryRef":"CUSTOMER.CUSTOMERNAME","nativeQueryRef":"CUSTOMERNAME","active":true}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}},"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}],"selection":[{"properties":{"selectAllCheckboxEnabled":{"expr":{"Literal":{"Value":"true"}}}}}],"items":[{"properties":{"textSize":{"expr":{"Literal":{"Value":"9D"}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}},"outlineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#605E5C'"}}}}}}}],"header":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"transparency":{"expr":{"Literal":{"Value":"100D"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"visualHeader":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}]},"syncGroup":{"groupName":"CUSTOMERNAME","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true}}
```

#### cd816d48edf2ddbde4c7 — columnChart

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/cd816d48edf2ddbde4c7/visual.json). Position: `{"x":255,"y":423.75,"z":33000,"height":428.75,"width":465,"tabOrder":32000}`.

```json
{"visual":{"visualType":"columnChart","query":{"queryState":{"Category":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"FISCALPERIOD"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.FISCALPERIOD","nativeQueryRef":"FISCALPERIOD1","active":true,"format":"G"}]},"Y":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_REVENUE"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_REVENUE","nativeQueryRef":"Revenue","displayName":"Revenue"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_REVENUE"}},"Property":"FIELD_PARAM_INCOMESTATEMENT"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"FISCALPERIOD"}},"direction":"Ascending"}]}},"objects":{"labels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"enableBackground":{"expr":{"Literal":{"Value":"false"}}},"labelDensity":{"expr":{"Literal":{"Value":"82L"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"0D"}}}}}],"zoom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"valueAxis":[{"properties":{"showAxisTitle":{"expr":{"Literal":{"Value":"false"}}},"labelColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"gridlineColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.2}}}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"0D"}}},"gridlineStyle":{"expr":{"Literal":{"Value":"'solid'"}}},"gridlineTransparency":{"expr":{"Literal":{"Value":"50D"}}}}}],"categoryAxis":[{"properties":{"showAxisTitle":{"expr":{"Literal":{"Value":"true"}}},"axisType":{"expr":{"Literal":{"Value":"'Categorical'"}}},"labelColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"logAxisScale":{"expr":{"Literal":{"Value":"false"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"0D"}}},"invertAxis":{"expr":{"Literal":{"Value":"false"}}},"fontSize":{"expr":{"Literal":{"Value":"9D"}}},"start":{"expr":{"Literal":{"Value":"1D"}}},"end":{"expr":{"Literal":{"Value":"16D"}}},"concatenateLabels":{"expr":{"Literal":{"Value":"false"}}},"titleText":{"expr":{"Literal":{"Value":"'Posting period'"}}},"titleFontSize":{"expr":{"Literal":{"Value":"9D"}}},"titleFontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"titleBold":{"expr":{"Literal":{"Value":"true"}}}}}],"dataPoint":[{"properties":{"fill":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}}},"selector":{"metadata":"_AMOUNTS.COMPANYCODE_REVENUE"}},{"properties":{"fill":{"solid":{"color":{"expr":{"Literal":{"Value":"'#637CEF'"}}}}}}},{"properties":{"fill":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_REVENUE"}},{"properties":{"fill":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0.6}}}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_REVENUE"}}]},"visualContainerObjects":{"title":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"5d20621bbc16903a72c5","field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"FISCALPERIOD"}},"type":"Advanced"},{"name":"35891d32211b745d1d30","field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_REVENUE"}},"type":"Advanced"}]}}
```

#### d2d2e10a1b33a063c700 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/d2d2e10a1b33a063c700/visual.json). Position: `{"x":770,"y":720,"z":43000,"height":40,"width":140,"tabOrder":42000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Taxes"}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### d647a0b100002a3b4540 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/d647a0b100002a3b4540/visual.json). Position: `{"x":838.75,"y":102.5,"z":18000,"height":38.75,"width":138.75,"tabOrder":17000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Product","textStyle":{"fontWeight":"bold","fontFamily":"DIN"}}],"horizontalTextAlignment":"right"}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### dbfe0631d909c8e19800 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/dbfe0631d909c8e19800/visual.json). Position: `{"x":577.5,"y":171.25,"z":23000,"height":187.5,"width":332.5,"tabOrder":22000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### df6f230a62965ca36001 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/df6f230a62965ca36001/visual.json). Position: `{"x":768.75,"y":472.5,"z":37000,"height":41.25,"width":140,"tabOrder":36000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"COGS","textStyle":{"fontSize":"10.5pt"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### e32cb6d088001702206b — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/e32cb6d088001702206b/visual.json). Position: `{"x":770,"y":555,"z":40000,"height":41.25,"width":177.5,"tabOrder":39000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"OPEX","textStyle":{"fontWeight":"bold","fontSize":"10.5pt"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### e46c98b5df766161f081 — slicer

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/e46c98b5df766161f081/visual.json). Position: `{"x":15.070643642072215,"y":105.4945054945055,"z":12000,"height":60.27487179487179,"width":197.58953427524858,"tabOrder":11000}`.

```json
{"visual":{"visualType":"slicer","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"EN"}},"queryRef":"LEDGERTEXT.EN","nativeQueryRef":"LedgerText","active":false,"displayName":"LedgerText"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_LEDGERTEXT"}},"Property":"FIELD_PARAM_LEDGERTEXT"}},"index":0,"length":4}]}}},"objects":{"data":[{"properties":{"mode":{"expr":{"Literal":{"Value":"'Dropdown'"}}}}}],"general":[{"properties":{"selfFilterEnabled":{"expr":{"Literal":{"Value":"true"}}},"filter":{"filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}}],"Values":[[{"Literal":{"Value":"'Ledger 0L'"}}]]}},"Annotations":{"filterExpressionMetadata":{"expressions":[{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}],"decomposedIdentities":{"values":[[{"0":[{"Literal":{"Value":"'Ledger 0L'"}}]}]],"columns":[{"value":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}}}]},"valueMap":[{"0":"Ledger 0L"}]}}}]}}}}],"header":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"textSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}},"text":{"expr":{"Literal":{"Value":"'Ledger'"}}}}}],"items":[{"properties":{"fontColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"background":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"padding":{"expr":{"Literal":{"Value":"3D"}}},"textSize":{"expr":{"Literal":{"Value":"9D"}}},"bold":{"expr":{"Literal":{"Value":"false"}}}}}],"selection":[{"properties":{"strictSingleSelect":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}}}}],"title":[{"properties":{"text":{"expr":{"Literal":{"Value":"'Slicer'"}}}}}]},"syncGroup":{"groupName":"Ledger","fieldChanges":true,"filterChanges":true},"drillFilterOtherVisuals":true},"filterConfig":{"filters":[{"name":"3fa87e6ce647fe1b00c8","field":{"Column":{"Expression":{"SourceRef":{"Entity":"LEDGERTEXT"}},"Property":"DE"}},"type":"Advanced","filter":{"Version":2,"From":[{"Name":"l","Entity":"LEDGERTEXT","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"l"}},"Property":"DE"}},"Right":{"Literal":{"Value":"null"}}}}}}}]}}]}}
```

#### e6bb0a4a0c4a40221c9a — cardVisual

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/e6bb0a4a0c4a40221c9a/visual.json). Position: `{"x":1017.5,"y":658.75,"z":50000,"height":55,"width":171.25,"tabOrder":49000}`.

```json
{"visual":{"visualType":"cardVisual","query":{"queryState":{"Data":{"projections":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_OPERATINGPROFIT"}},"queryRef":"__MEASURES_PROFITABILITY.COMPANYCODE_OPERATINGPROFIT","nativeQueryRef":"Operating Profit","displayName":"Operating Profit"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_OPERATINGPROFIT"}},"Property":"FIELD_PARAM_OPERATINGPROFIT"}},"index":0,"length":1}]}},"sortDefinition":{"sort":[{"field":{"Measure":{"Expression":{"SourceRef":{"Entity":"__MEASURES_PROFITABILITY"}},"Property":"COMPANYCODE_OPERATINGPROFIT"}},"direction":"Descending"}],"isDefaultSort":true}},"objects":{"layout":[{"properties":{"cellPadding":{"expr":{"Literal":{"Value":"1L"}}}}}],"value":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}},"bold":{"expr":{"Literal":{"Value":"true"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_OPERATINGPROFIT"}},{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"bold":{"expr":{"Literal":{"Value":"true"}}},"horizontalAlignment":{"expr":{"Literal":{"Value":"'right'"}}},"labelDisplayUnits":{"expr":{"Literal":{"Value":"1D"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_OPERATINGPROFIT"}}],"label":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.COMPANYCODE_OPERATINGPROFIT"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"metadata":"__MEASURES_PROFITABILITY.GLOBAL_OPERATINGPROFIT"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}],"fillCustom":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### eaee74256e69018e1978 — multiRowCard

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/eaee74256e69018e1978/visual.json). Position: `{"x":1187.5,"y":777.5,"z":54000,"height":32.5,"width":80,"tabOrder":53000}`.

```json
{"visual":{"visualType":"multiRowCard","query":{"queryState":{"Values":{"projections":[{"field":{"Column":{"Expression":{"SourceRef":{"Entity":"GLACCOUNTLINEITEMRAWDATA"}},"Property":"COMPANYCODECURRENCY"}},"queryRef":"GLACCOUNTLINEITEMRAWDATA.COMPANYCODECURRENCY","nativeQueryRef":"Company Code Currency","displayName":"Company Code Currency"}],"fieldParameters":[{"parameterExpr":{"Column":{"Expression":{"SourceRef":{"Entity":"_FIELD_PARAM_CURRENCY"}},"Property":"FIELD_PARAM_CURRENCY"}},"index":0,"length":1}]}},"sortDefinition":{"isDefaultSort":true}},"objects":{"categoryLabels":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"fontSize":{"expr":{"Literal":{"Value":"10.5D"}}}}}],"dataLabels":[{"properties":{"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":1,"Percent":0}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}],"card":[{"properties":{"cardPadding":{"expr":{"Literal":{"Value":"2D"}}},"barShow":{"expr":{"Literal":{"Value":"false"}}},"outlineStyle":{"expr":{"Literal":{"Value":"0D"}}},"outlineWeight":{"expr":{"Literal":{"Value":"1D"}}}}}],"cardTitle":[{"properties":{"fontFamily":{"expr":{"Literal":{"Value":"'wf_standard-font, helvetica, arial, sans-serif'"}}},"fontSize":{"expr":{"Literal":{"Value":"10D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#252423'"}}}}},"bold":{"expr":{"Literal":{"Value":"true"}}}}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"padding":[{"properties":{"bottom":{"expr":{"Literal":{"Value":"14D"}}},"top":{"expr":{"Literal":{"Value":"0D"}}},"left":{"expr":{"Literal":{"Value":"5D"}}}}}],"general":[{"properties":{"keepLayerOrder":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### edabcba475aaa324156b — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/edabcba475aaa324156b/visual.json). Position: `{"x":226.25,"y":375,"z":25000,"height":493.75,"width":510,"tabOrder":24000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'rectangle'"}}},"roundEdge":{"expr":{"Literal":{"Value":"20L"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}},"selector":{"id":"default"}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":0}}}}},"transparency":{"expr":{"Literal":{"Value":"0D"}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"shadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}},{"properties":{"shadowPositionPreset":{"expr":{"Literal":{"Value":"'custom'"}}},"angle":{"expr":{"Literal":{"Value":"44D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}},"selector":{"id":"default"}}]},"visualContainerObjects":{"dropShadow":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"preset":{"expr":{"Literal":{"Value":"'Custom'"}}},"shadowSpread":{"expr":{"Literal":{"Value":"0D"}}},"shadowBlur":{"expr":{"Literal":{"Value":"4D"}}},"angle":{"expr":{"Literal":{"Value":"80D"}}},"shadowDistance":{"expr":{"Literal":{"Value":"2D"}}},"transparency":{"expr":{"Literal":{"Value":"90D"}}}}}],"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}}],"border":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}},"radius":{"expr":{"Literal":{"Value":"4D"}}},"color":{"solid":{"color":{"expr":{"Literal":{"Value":"'#FAFAFA'"}}}}}}}]},"drillFilterOtherVisuals":true},"howCreated":"InsertVisualButton"}
```

#### f2080c4ec32101bb2dc3 — textbox

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/f2080c4ec32101bb2dc3/visual.json). Position: `{"x":770,"y":592.5,"z":39000,"height":36.25,"width":135,"tabOrder":38000}`.

```json
{"visual":{"visualType":"textbox","objects":{"general":[{"properties":{"paragraphs":[{"textRuns":[{"value":"Inventory Change","textStyle":{"fontSize":"10.5pt"}}]}]}}]},"visualContainerObjects":{"background":[{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}]},"drillFilterOtherVisuals":true}}
```

#### fac176d08a7507778d66 — shape

[Visual definition](../Record_to_Report_Financial_Insights.Report/definition/pages/9d8153603d7adaea330a/visuals/fac176d08a7507778d66/visual.json). Position: `{"x":767.5,"y":736.25,"z":59000,"height":48.75,"width":493.75,"tabOrder":58000}`.

```json
{"visual":{"visualType":"shape","objects":{"shape":[{"properties":{"tileShape":{"expr":{"Literal":{"Value":"'line'"}}}}}],"rotation":[{"properties":{"shapeAngle":{"expr":{"Literal":{"Value":"0L"}}}}}],"fill":[{"properties":{"fillColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.1}}}}}},"selector":{"id":"default"}},{"properties":{"show":{"expr":{"Literal":{"Value":"false"}}}}}],"outline":[{"properties":{"show":{"expr":{"Literal":{"Value":"true"}}}}},{"properties":{"lineColor":{"solid":{"color":{"expr":{"ThemeDataColor":{"ColorId":0,"Percent":-0.3}}}}},"transparency":{"expr":{"Literal":{"Value":"70D"}}}},"selector":{"id":"default"}}]},"drillFilterOtherVisuals":true}}
```

## All other synced files in the two items

The table/relationship/page/visual inventories above account for their definition files. The following lists every remaining file; runtime artifacts or data not present in the checkout are not invented.

- [Record_to_Report_Financial_Insights.SemanticModel\.platform](../Record_to_Report_Financial_Insights.SemanticModel/.platform) — 434 bytes.
- [Record_to_Report_Financial_Insights.SemanticModel\definition.pbism](../Record_to_Report_Financial_Insights.SemanticModel/definition.pbism) — 198 bytes.
- [Record_to_Report_Financial_Insights.SemanticModel\definition\database.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/database.tmdl) — 39 bytes.
- [Record_to_Report_Financial_Insights.SemanticModel\definition\expressions.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/expressions.tmdl) — 1526 bytes.
- [Record_to_Report_Financial_Insights.SemanticModel\definition\model.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/model.tmdl) — 3290 bytes.
- [Record_to_Report_Financial_Insights.SemanticModel\definition\cultures\en-US.tmdl](../Record_to_Report_Financial_Insights.SemanticModel/definition/cultures/en-US.tmdl) — 33879 bytes.
- [Record_to_Report_Financial_Insights.Report\.platform](../Record_to_Report_Financial_Insights.Report/.platform) — 428 bytes.
- [Record_to_Report_Financial_Insights.Report\definition.pbir](../Record_to_Report_Financial_Insights.Report/definition.pbir) — 269 bytes.
- [Record_to_Report_Financial_Insights.Report\definition\report.json](../Record_to_Report_Financial_Insights.Report/definition/report.json) — 1931 bytes.
- [Record_to_Report_Financial_Insights.Report\definition\version.json](../Record_to_Report_Financial_Insights.Report/definition/version.json) — 152 bytes.
- [Record_to_Report_Financial_Insights.Report\definition\pages\pages.json](../Record_to_Report_Financial_Insights.Report/definition/pages/pages.json) — 369 bytes.
- [Record_to_Report_Financial_Insights.Report\StaticResources\RegisteredResources\Data_Bar_Vertical_Highlight26202892008048195.png](../Record_to_Report_Financial_Insights.Report/StaticResources/RegisteredResources/Data_Bar_Vertical_Highlight26202892008048195.png) — 1119 bytes.
- [Record_to_Report_Financial_Insights.Report\StaticResources\SharedResources\BaseThemes\CY23SU04.json](../Record_to_Report_Financial_Insights.Report/StaticResources/SharedResources/BaseThemes/CY23SU04.json) — 12774 bytes.

## Coverage totals

- Tables: 67; columns: 1224; hidden columns: 177; calculated columns: 10; measures: 106.
- Partitions: 67 (one per table); relationships: 63; pages: 6; visual containers: 173.
- Other files explicitly listed: 13. Local-date tables: 0.
