# Gold SQL presentation views

[Overview](README.md) | [Transformations](03-notebook-transformations.md) | [Semantic model](05-semantic-model-and-report.md)

## 1. Scope and deployment behavior

The [Gold view-creation notebook](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py) contains **80 distinct `CREATE OR ALTER VIEW` definitions: 64 multilingual text views and 16 other presentation views. This catalog accounts for every definition in execution order. These are SQL endpoint views, not additional Git-level Fabric items or Delta writes.

Every cell checks a list of prerequisite objects in `INFORMATION_SCHEMA.TABLES`, then executes dynamic SQL. Missing prerequisites produce an `ERROR:` result. A Python wrapper captures errors, continues subsequent cells, and prints a final summary without raising. A successful notebook activity is therefore not a guarantee that these views exist. The target is the notebook's installed Gold name.

## 2. Shared multilingual text-view algorithm

The `vt*` family takes language choices from `SAPLANGUAGE`, with a case-sensitive language/code equality condition. A master-key CTE selects distinct master keys, source system and relevant code attributes, usually also aliasing a code as a fallback label. The code cross-applies those keys to languages; reads text rows with non-null Key; full-outer-joins key/language combinations and actual texts; coalesces missing/empty values to master defaults; and pivots the configured field with `MAX` into ISO-language columns.

The fixed language output is: `ZH, TH, KO, RO, SL, HR, UK, ET, AR, HE, CA, CS, DE, SH, EN, FR, EL, HU, IT, JA, DA, PL, ZF, NL, NO, PT, SK, RU, ES, TR, FI, SV, BG, LT, LV, HI, KK, VI` (38 columns). The SQL does not dynamically add other languages. Missing translations normally show a business code, not an arbitrary other-language label. Pivot `MAX` can collapse multiple candidate texts.

The field actually pivoted is listed below. Several views pivot a code rather than a descriptive name, so their names alone should not be used to infer human-readable translated output. Dependencies below come from FROM/JOIN references, excluding local CTE names; guards list the separately checked objects.

## 3. Complete text-view catalog

| # | SQL view / source cell | Direct source objects (also depends on SAPLANGUAGE) | Pivoted field |
|---:|---|---|---|
| 1 | [vtACCOUNTINGDOCUMENTTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L134) | `I_ACCOUNTINGDOCUMENTTYPE`, `I_ACCOUNTINGDOCUMENTTYPETEXT` | `ACCOUNTINGDOCUMENTTYPENAME` |
| 2 | [vtACCTASSIGNMENTCATEGORYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L214) | `I_ACCOUNTASSIGNMENTCATEGORY`, `I_ACCTASSIGNMENTCATEGORYTEXT` | `ACCOUNTASSIGNMENTCATEGORY` |
| 3 | [vtASSETCLASSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L294) | `I_ASSETCLASS`, `I_ASSETCLASSTEXT` | `ASSETCLASSNAME` |
| 4 | [vtASSETTRANSACTIONTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L373) | `I_ASSETTRANSACTIONTYPE`, `I_ASSETTRANSACTIONTYPETEXT` | `ASSETTRANSACTIONTYPENAME` |
| 5 | [vtBILLINGDOCUMENTTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L454) | `I_BILLINGDOCUMENTTYPE`, `I_BILLINGDOCUMENTTYPETEXT` | `BILLINGDOCUMENTTYPENAME` |
| 6 | [vtBUSINESSAREATEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L535) | `I_BUSINESSAREA`, `I_BUSINESSAREATEXT` | `BUSINESSAREANAME` |
| 7 | [vtCHARTOFACCOUNTSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L616) | `I_CHARTOFACCOUNTS`, `I_CHARTOFACCOUNTSTEXT` | `CHARTOFACCOUNTSNAME` |
| 8 | [vtCOSTCENTERACTIVITYTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L695) | `I_COSTCENTERACTIVITYTYPE`, `I_COSTCENTERACTIVITYTYPETEXT` | `COSTCENTERACTIVITYTYPENAME` |
| 9 | [vtCOSTCENTERTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L775) | `I_COSTCENTER`, `I_COSTCENTERTEXT` | `COSTCENTERNAME` |
| 10 | [vtCUSTOMERGROUPTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L856) | `I_CUSTOMERGROUP`, `I_CUSTOMERGROUPTEXT` | `CUSTOMERGROUPNAME` |
| 11 | [vtDEBITCREDITCODETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L934) | `I_DEBITCREDITCODE`, `I_DEBITCREDITCODETEXT` | `DEBITCREDITCODENAME` |
| 12 | [vtDELIVERYBLOCKREASONTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1013) | `I_DELIVERYBLOCKREASON`, `I_DELIVERYBLOCKREASONTEXT` | `DELIVERYBLOCKREASONTEXT` |
| 13 | [vtDELIVERYBLOCKSTATUSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1091) | `I_DELIVERYBLOCKSTATUS`, `I_DELIVERYBLOCKSTATUSTEXT` | `DELIVERYBLOCKSTATUSDESC` |
| 14 | [vtDELIVERYDOCUMENTTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1170) | `I_DELIVERYDOCUMENTTYPE`, `I_DELIVERYDOCUMENTTYPETEXT` | `DELIVERYDOCUMENTTYPENAME` |
| 15 | [vtDISTRIBUTIONCHANNELTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1249) | `I_DISTRIBUTIONCHANNEL`, `I_DISTRIBUTIONCHANNELTEXT` | `DISTRIBUTIONCHANNELNAME` |
| 16 | [vtDIVISIONTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1327) | `I_DIVISION`, `I_DIVISIONTEXT` | `DIVISIONNAME` |
| 17 | [vtDUNNINGAREATEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1406) | `I_DUNNINGAREA`, `I_DUNNINGAREATEXT` | `DUNNINGAREANAME` |
| 18 | [vtDUNNINGKEYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1488) | `I_DUNNINGKEY`, `I_DUNNINGKEYTEXT` | `MAXIMUMDUNNINGLEVELDESCRIPTION` |
| 19 | [vtEQUIPMENTTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1567) | `I_EQUIPMENT`, `I_EQUIPMENTTEXT` | `EQUIPMENTNAME` |
| 20 | [vtFUNCTIONALLOCATIONTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1637) | `I_FUNCTIONALLOCATION`, `I_FUNCTIONALLOCATIONTEXT` | `FUNCTIONALLOCATIONNAME` |
| 21 | [vtFUNCTIONALAREATEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1716) | `I_FUNCTIONALAREA`, `I_FUNCTIONALAREATEXT` | `FUNCTIONALAREANAME` |
| 22 | [vtGLACCOUNTINCHARTOFACCOUNTSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1796) | `I_GLACCOUNTINCHARTOFACCOUNTS`, `I_GLACCOUNTTEXT` | `GLACCOUNTNAME` |
| 23 | [vtGLACCOUNTTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1876) | `I_GLACCOUNTINCHARTOFACCOUNTS`, `I_GLACCOUNTTEXT` | `GLACCOUNTNAME` |
| 24 | [vtLEDGERTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L1958) | `I_LEDGER`, `I_LEDGERTEXT` | `LEDGERNAME` |
| 25 | [vtMOVEMENTCATEGORYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2038) | `I_MOVEMENTCATEGORY`, `I_MOVEMENTCATEGORYTEXT` | `ASSETACCTTRANSCLASSFCTNNAME` |
| 26 | [vtOVERALLBILLINGSTATUSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2118) | `I_OVERALLBILLINGSTATUS`, `I_OVERALLBILLINGSTATUSTEXT` | `OVERALLBILLINGSTATUSDESC` |
| 27 | [vtPAYMENTBLOCKINGREASONTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2198) | `I_PAYMENTBLOCKINGREASON`, `I_PAYMENTBLOCKINGREASONTEXT` | `PAYMENTBLOCKINGREASONNAME` |
| 28 | [vtPAYMENTTERMSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2277) | `I_PAYMENTTERMS`, `I_PAYMENTTERMSTEXT` | `PAYMENTTERMSDESCRIPTION` |
| 29 | [vtPOSTINGKEYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2359) | `I_POSTINGKEY`, `I_POSTINGKEYTEXT` | `POSTINGKEYNAME` |
| 30 | [vtPRODUCTGROUP_2TEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2439) | `I_PRODUCTGROUP_2`, `I_PRODUCTGROUPTEXT_2` | `PRODUCTGROUPNAME` |
| 31 | [vtPRODUCTTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2519) | `I_PRODUCT`, `I_PRODUCTDESCRIPTION` | `PRODUCTDESCRIPTION` |
| 32 | [vtPROFITCENTERTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2600) | `I_PROFITCENTER`, `I_PROFITCENTERTEXT` | `PROFITCENTERNAME` |
| 33 | [vtPURCHASINGDOCUMENTORIGINTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2683) | `I_PURCHASINGDOCUMENTORIGIN`, `I_PURCHASINGDOCUMENTORIGINTEXT` | `PURCHASINGDOCUMENTORIGIN` |
| 34 | [vtPURCHASINGDOCUMENTSTATUSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2761) | `I_PURCHASINGDOCUMENTSTATUS`, `I_PURCHASINGDOCUMENTSTATUSTEXT` | `PURCHASINGDOCUMENTSTATUS` |
| 35 | [vtPURCHASINGDOCUMENTTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2839) | `I_PURCHASINGDOCUMENTTYPE`, `I_PURCHASINGDOCUMENTTYPETEXT` | `PURCHASINGDOCUMENTTYPE` |
| 36 | [vtPURCHASINGPROCESSINGSTATUSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2919) | `I_PURCHASINGPROCESSINGSTATUS`, `I_PURGPROCESSINGSTATUSTEXT` | `PURCHASINGPROCESSINGSTATUSNAME` |
| 37 | [vtPURGDOCUMENTCATEGORYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L2998) | `I_PURCHASINGDOCUMENTCATEGORY`, `I_PURGDOCUMENTCATEGORYTEXT` | `PURCHASINGDOCUMENTCATEGORY` |
| 38 | [vtPURGDOCUMENTITEMCATEGORYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3075) | `I_PURGDOCUMENTITEMCATEGORY`, `I_PURGDOCUMENTITEMCATEGORYTEXT` | `PURCHASINGDOCUMENTITEMCATEGORY` |
| 39 | [vtSALESDISTRICTTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3154) | `I_SALESDISTRICT`, `I_SALESDISTRICTTEXT` | `SALESDISTRICTNAME` |
| 40 | [vtSALESGROUPTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3234) | `I_SALESGROUP`, `I_SALESGROUPTEXT` | `SALESGROUPNAME` |
| 41 | [vtSALESOFFICETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3314) | `I_SALESOFFICE`, `I_SALESOFFICETEXT` | `SALESOFFICENAME` |
| 42 | [vtSALESORGANIZATIONTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3394) | `I_SALESORGANIZATION`, `I_SALESORGANIZATIONTEXT` | `SALESORGANIZATIONNAME` |
| 43 | [vtSDDOCUMENTCATEGORYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3474) | `I_SDDOCUMENTCATEGORY`, `I_SDDOCUMENTCATEGORYTEXT` | `SDDOCUMENTCATEGORYNAME` |
| 44 | [vtSEGMENTTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3553) | `I_SEGMENT`, `I_SEGMENTTEXT` | `SEGMENTNAME` |
| 45 | [vtSHIPMENTBLOCKREASONTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3633) | `I_SHIPMENTBLOCKREASON`, `I_SHIPMENTBLOCKREASONTEXT` | `SHIPMENTBLOCKREASONTEXT` |
| 46 | [vtSHIPPINGPOINTTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3701) | `I_SHIPPINGPOINT`, `I_SHIPPINGPOINTTEXT` | `SHIPPINGPOINTNAME` |
| 47 | [vtSUPPLIERINVOICESTATUSTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3781) | `I_SUPPLIERINVOICESTATUSAPI01`, `I_SUPPLIERINVOICESTATUSTEXT` | `SUPPLIERINVOICESTATUS` |
| 48 | [vtTAXCODETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3858) | `I_TAXCODE`, `I_TAXCODETEXT` | `TAXCODE` |
| 49 | [vtFACTORYCALENDARTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5855) | `I_FACTORYCALENDAR`, `I_FACTORYCALENDARTEXT` | `FACTORYCALENDARNAME` |
| 50 | [vtOPERATIONCONTROLPROFILETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5935) | `I_OPERATIONCONTROLPROFILE`, `I_OPERATIONCONTROLPROFILETEXT` | `OPERATIONCONTROLPROFILENAME` |
| 51 | [vtOPERATIONSETUPGROUPTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6015) | `I_OPERATIONSETUPGROUP`, `I_OPERATIONSETUPGROUPTEXT` | `OPERATIONSETUPGROUPNAME` |
| 52 | [vtOPERATIONSETUPGROUPCATTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6097) | `I_OPERATIONSETUPGROUPCATEGORY`, `I_OPERATIONSETUPGROUPCATTEXT` | `OPERATIONSETUPGROUPCATNAME` |
| 53 | [vtOPERATIONSETUPTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6178) | `I_OPERATIONSETUPTYPE`, `I_OPERATIONSETUPTYPETEXT` | `OPERATIONSETUPTYPENAME` |
| 54 | [vtOPERATIONSTANDARDTEXTTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6259) | `I_OPERATIONSTANDARDTEXT`, `I_OPERATIONSTANDARDTEXTTEXT` | `OPERATIONSTANDARDTEXTCODENAME` |
| 55 | [vtWORKCENTERTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6339) | `I_WORKCENTER`, `I_WORKCENTERTEXT` | `WORKCENTERTEXT` |
| 56 | [vtWORKCENTERTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6419) | `I_WORKCENTERTYPE`, `I_WORKCENTERTYPETEXT` | `WORKCENTERTYPENAME` |
| 57 | [vtFINALCONFIRMATIONTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6499) | `I_FINALCONFIRMATIONTYPE`, `I_FINALCONFIRMATIONTYPETEXT` | `FINALCONFIRMATIONTYPENAME` |
| 58 | [vtORDERCONFIRMATIONTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6579) | `I_ORDERCONFIRMATIONTYPE`, `I_ORDERCONFIRMATIONTYPETEXT` | `ORDERCONFIRMATIONTYPENAME` |
| 59 | [vtVARIANCEREASONTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6659) | `I_VARIANCEREASON`, `I_VARIANCEREASONTEXT` | `VARIANCEREASONNAME` |
| 60 | [vtGOODSMOVEMENTTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6740) | `I_GOODSMOVEMENTTYPE`, `I_GOODSMOVEMENTTYPET` | `GOODSMOVEMENTTYPENAME` |
| 61 | [vtMATERIALREQUIREMENTTYPETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6820) | `I_MATERIALREQUIREMENTTYPE`, `I_MATERIALREQUIREMENTTYPETEXT` | `REQUIREMENTTYPENAME` |
| 62 | [vtPRODUCTIONSUPPLYAREATEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6900) | `I_PRODUCTIONSUPPLYAREA`, `I_PRODUCTIONSUPPLYAREATEXT` | `PRODUCTIONSUPPLYAREANAME` |
| 63 | [vtACCOUNTINGDOCUMENTCATEGORYTEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L6981) | `I_ACCOUNTINGDOCUMENTCATEGORY`, `I_ACCOUNTINGDOCUMENTCATEGORYT` | `ACCOUNTINGDOCUMENTCATEGORYNAME` |
| 64 | [vtSPECIALGLCODETEXT](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L7061) | `I_SPECIALGLCODE`, `I_SPECIALGLCODETEXT` | `SPECIALGLCODENAME` |

### Notable text-view variants

- `vtACCTASSIGNMENTCATEGORYTEXT` pivots ACCOUNTASSIGNMENTCATEGORY, not a descriptive name; its master-key CTE also selects consumption/special-stock attributes.
- `vtGLACCOUNTINCHARTOFACCOUNTSTEXT` and `vtGLACCOUNTTEXT` both use I_GLACCOUNTINCHARTOFACCOUNTS and I_GLACCOUNTTEXT, despite different presentation names.
- `vtPRODUCTTEXT` uses I_PRODUCTDESCRIPTION rather than a table named I_PRODUCTTEXT.
- `vtPRODUCTGROUP_2TEXT` uses the _2 SAP object names.
- Purchasing-origin/status/type/category, supplier-invoice-status and tax-code variants pivot the listed code field. They do not automatically select a name field.
- Full-outer key/text joins normally match on Key and _ISOLanguage, relying on surrogate key uniqueness across systems rather than an explicit system predicate.

## 4. All other views

### SAPLANGUAGE

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L89).
- Direct dependencies: `I_LANGUAGE`, `I_LANGUAGETEXT`.
- Prerequisite guard: `I_LANGUAGE`, `I_LANGUAGETEXT`.

Builds the distinct language/ISO-language/name/code mapping from I_LANGUAGE and I_LANGUAGETEXT. The text language must equal its language code; source systems must match. Emits a blank _SystemName, so this mapping is shared at the presentation level.

### COSTCENTERHIERARCHY

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L3937).
- Direct dependencies: `I_COSTCENTERHIERARCHYNODE`.
- Prerequisite guard: `I_COSTCENTERHIERARCHYNODE`.

Flattens the cost center hierarchy with a fixed series of left self-joins L1 through L9, starting at NODETYPE='R'. Source nodes are restricted to VALIDITYENDDATE='99991231'. Projects each level's node and Key, deepest available child/parent and attributes, a pipe-delimited HIERARCHYPATH and MAXHIERARCHYLEVEL. This is fixed-depth, not recursive arbitrary-depth traversal. Self-join predicates do not explicitly include source system.

### COSTCENTERHIERARCHYNODEFINAL

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L4213).
- Direct dependencies: `I_COSTCENTERHIERARCHYNODE`, `I_COSTCENTERHIERARCHYNODET`, `I_COSTCENTERTEXT`.
- Prerequisite guard: `I_COSTCENTERHIERARCHYNODE`, `I_COSTCENTERHIERARCHYNODET`, `I_COSTCENTERTEXT`.

Unions root/intermediate node labels from hierarchy-node text with leaf labels from cost center master text. Retains node attributes plus LANGUAGE, _ISOLanguage and HIERARCHYNODETEXT. Active-end-date conditions appear in join predicates; leaf branches require a non-null language.

### GLACCOUNTHIERARCHY

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L4272).
- Direct dependencies: `I_GLACCOUNTHIERARCHYNODE`.
- Prerequisite guard: `I_GLACCOUNTHIERARCHYNODE`.

Flattens the GL account hierarchy with a fixed series of left self-joins L1 through L9, starting at NODETYPE='R'. Source nodes are restricted to VALIDITYENDDATE='99991231'. Projects each level's node and Key, deepest available child/parent and attributes, a pipe-delimited HIERARCHYPATH and MAXHIERARCHYLEVEL. This is fixed-depth, not recursive arbitrary-depth traversal. Self-join predicates do not explicitly include source system.

### GLACCOUNTHIERARCHYNODEFINAL

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L4598).
- Direct dependencies: `I_GLACCOUNTHIERARCHYNODE`, `I_GLACCOUNTHIERARCHYNODET`, `I_GLACCOUNTTEXT`.
- Prerequisite guard: `I_GLACCOUNTHIERARCHYNODE`, `I_GLACCOUNTHIERARCHYNODET`, `I_GLACCOUNTTEXT`.

Unions root/intermediate node labels from hierarchy-node text with leaf labels from GL account master text. Retains node attributes plus LANGUAGE, _ISOLanguage and HIERARCHYNODETEXT. Active-end-date conditions appear in join predicates; leaf branches require a non-null language.

### PROFITCENTERHIERARCHY

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L4659).
- Direct dependencies: `I_PROFITCENTERHIERARCHYNODE`.
- Prerequisite guard: `I_PROFITCENTERHIERARCHYNODE`.

Flattens the profit center hierarchy with a fixed series of left self-joins L1 through L9, starting at NODETYPE='R'. Source nodes are restricted to VALIDITYENDDATE='99991231'. Projects each level's node and Key, deepest available child/parent and attributes, a pipe-delimited HIERARCHYPATH and MAXHIERARCHYLEVEL. This is fixed-depth, not recursive arbitrary-depth traversal. Self-join predicates do not explicitly include source system.

### PROFITCENTERHIERARCHYNODEFINAL

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L4920).
- Direct dependencies: `I_PROFITCENTERHIERARCHYNODE`, `I_PROFITCENTERHIERARCHYNODET`, `I_PROFITCENTERTEXT`.
- Prerequisite guard: `I_PROFITCENTERHIERARCHYNODE`, `I_PROFITCENTERHIERARCHYNODET`, `I_PROFITCENTERTEXT`.

Unions root/intermediate node labels from hierarchy-node text with leaf labels from profit center master text. Retains node attributes plus LANGUAGE, _ISOLanguage and HIERARCHYNODETEXT. Active-end-date conditions appear in join predicates; leaf branches require a non-null language.

### vCOSTCENTER

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L4980).
- Direct dependencies: `I_COSTCENTER`.
- Prerequisite guard: `I_COSTCENTER`.

Projects an explicit attribute list from I_COSTCENTER, retaining rows whose VALIDITYENDDATE equals the maximum for that Key. Keeps Key, system and timestamp plus business and validity fields. This is latest-version selection, not an as-of-today validity predicate; ties can retain multiple rows.

### vCOSTCENTERACTIVITYTYPE

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5108).
- Direct dependencies: `I_COSTCENTERACTIVITYTYPE`.
- Prerequisite guard: `I_COSTCENTERACTIVITYTYPE`.

Projects an explicit attribute list from I_COSTCENTERACTIVITYTYPE, retaining rows whose VALIDITYENDDATE equals the maximum for that Key. Keeps Key, system and timestamp plus business and validity fields. This is latest-version selection, not an as-of-today validity predicate; ties can retain multiple rows.

### vCOSTCENTERHIERARCHYWTEXT

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5178).
- Direct dependencies: `COSTCENTERHIERARCHYNODEFINAL`, `I_LANGUAGE`, `I_LANGUAGETEXT`, `COSTCENTERHIERARCHY`, `I_COSTCENTER`.
- Prerequisite guard: `COSTCENTERHIERARCHY`, `SAPLANGUAGE`, `COSTCENTERHIERARCHYNODEFINAL`, `I_COSTCENTER`.

Enriches the flattened cost center hierarchy with one row per available ISO language. Joins text for each of nine level keys, concatenates node and label into COSTCENTER_HIER_LEVELn_TEXT, and maps the leaf to I_COSTCENTER.Key as COSTCENTER_NODE_KEY. Carries the hierarchy path, depth and validity fields. Some leaf/master joins do not explicitly include _SystemName.

### vGLACCOUNTLINEITEMRAWDATA_AGGR

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5297).
- Direct dependencies: `I_GLACCOUNTLINEITEMRAWDATA`.
- Prerequisite guard: `I_GLACCOUNTLINEITEMRAWDATA`.

Groups Gold GL line items by debit/credit, company, three currency codes, fiscal-period/ledger/profit/cost/chart/segment/GL/product-group/product/customer keys, fiscal year/period, partner company and tax attributes. Sums company-code, global and transaction currency amounts. It does not expose _SystemName as a separate grouping column; dimension foreign keys carry much of the source distinction.

### vGLACCOUNTHIERARCHYWTEXT

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5379).
- Direct dependencies: `GLACCOUNTHIERARCHYNODEFINAL`, `I_LANGUAGE`, `I_LANGUAGETEXT`, `GLACCOUNTHIERARCHY`, `I_GLACCOUNTINCHARTOFACCOUNTS`.
- Prerequisite guard: `SAPLANGUAGE`, `GLACCOUNTHIERARCHY`, `GLACCOUNTHIERARCHYNODEFINAL`.

Enriches the flattened GL account hierarchy with one row per available ISO language. Joins text for each of nine level keys, concatenates node and label into GLACCOUNT_HIER_LEVELn_TEXT, and maps the leaf to I_GLACCOUNTINCHARTOFACCOUNTS.Key as GLACCOUNT_NODE_KEY. Carries the hierarchy path, depth and validity fields. Some leaf/master joins do not explicitly include _SystemName.

### vPROFITCENTER

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5497).
- Direct dependencies: `I_PROFITCENTER`.
- Prerequisite guard: `I_PROFITCENTER`.

Projects an explicit attribute list from I_PROFITCENTER, retaining rows whose VALIDITYENDDATE equals the maximum for that Key. Keeps Key, system and timestamp plus business and validity fields. This is latest-version selection, not an as-of-today validity predicate; ties can retain multiple rows.

### vPROFITCENTERHIERARCHYWTEXT

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5580).
- Direct dependencies: `PROFITCENTERHIERARCHYNODEFINAL`, `I_LANGUAGE`, `I_LANGUAGETEXT`, `PROFITCENTERHIERARCHY`, `I_PROFITCENTER`.
- Prerequisite guard: `PROFITCENTERHIERARCHYNODEFINAL`, `PROFITCENTERHIERARCHY`, `SAPLANGUAGE`, `I_PROFITCENTER`.

Enriches the flattened profit center hierarchy with one row per available ISO language. Joins text for each of nine level keys, concatenates node and label into PROFITCENTER_HIER_LEVELn_TEXT, and maps the leaf to I_PROFITCENTER.Key as PROFITCENTER_NODE_KEY. Carries the hierarchy path, depth and validity fields. Some leaf/master joins do not explicitly include _SystemName.

### vSUPPLIERINVOICEITEM

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5699).
- Direct dependencies: `C_SUPPLIERINVOICEDEX`, `C_SUPPLIERINVOICEITEMDEX`.
- Prerequisite guard: `C_SUPPLIERINVOICEDEX`, `C_SUPPLIERINVOICEITEMDEX`.

Left-joins supplier invoice header to invoice items on invoice number and fiscal year. Projects item quantities/amounts/variance flags, header gross amount, document metadata and selected dimension keys. The header amount repeats at item grain; the join has no explicit _SystemName predicate.

### vSUPPLIERINVOICEITEMCOMPLIANT

- Source: [SQL cell](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L5784).
- Direct dependencies: `C_SUPPLIERINVOICEITEMDEX`, `C_PURCHASEORDERITEMDEX`.
- Prerequisite guard: `C_SUPPLIERINVOICEITEMDEX`, `C_PURCHASEORDERITEMDEX`.

Joins invoice items to distinct purchase-order/contract items on purchase order, item and _SystemName. Classifies PO compliance, contract use and reversal, then sums invoice item amount by fiscal year/system and selected organization/product/fiscal/currency keys and flags. The positive compliance literal is spelled 'Complaint' in the source; it is not silently corrected here.

## 5. Financial reporting lineage and limitations

The financial model explicitly references 24 SQL objects: ten `I_*` base tables, nine `vt*` text views, four `v*` presentation views, and `SAPLANGUAGE`. Its business-facing logical table names are aliases for those source objects, not a requirement for a second set of identically named SQL objects. For example, logical `PRODUCTGROUP2TEXT` requests physical `vtPRODUCTGROUP_2TEXT`. See the model analysis for the checked-in partition expressions.

The exact-name cross-check confirms that **all 14 view sources requested by the model are defined in this notebook**. The four `v*` sources are `vGLACCOUNTLINEITEMRAWDATA_AGGR`, `vCOSTCENTER`, `vPROFITCENTER`, and `vGLACCOUNTHIERARCHYWTEXT`; the nine `vt*` sources cover chart of accounts, cost center, debit/credit, GL account, ledger, product group, product, profit center, and segment texts. There is no established missing-view-name mismatch in this snapshot.

Only views whose prerequisites exist can be created. The ten `I_*` model sources depend on metadata-driven Delta table creation; no table data or active configuration rows prove their live availability. The broader view catalog includes sales, procurement, equipment and production labels; that does not prove those domains are enabled or used by the installed financial report.

Hierarchy depth is capped at nine. Node joins rely on hierarchy and parent/node identifiers without consistently adding system/version isolation. Latest-version dimensions use maximum end date rather than a report-date interval. Validate these assumptions for multi-system data and nonstandard SAP hierarchies.
