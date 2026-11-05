# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.11"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "18275add-7d43-4a42-815a-b1c738d97308",
# META       "default_lakehouse_name": "bps_gold_c792846f",
# META       "default_lakehouse_workspace_id": "649676ea-3e7c-457d-a728-7e8e8cdafee9",
# META       "known_lakehouses": [
# META         {
# META           "id": "18275add-7d43-4a42-815a-b1c738d97308"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# > ⚠️ **Do Not Edit** — This notebook is maintained and deployed by **Business Process Solutions**. Any manual changes will be overwritten during the next update. Want to make changes? Duplicate this notebook and work from the copy.

# CELL ********************

p_gold_lakehouse_name = "bps_gold_c792846f"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

# Configure %%tsql magic to continue execution on cell failure and track results
import re
from IPython import get_ipython
from IPython.utils.capture import capture_output

_cell_results = []

ip = get_ipython()
if ip is not None:
    _original_tsql = ip.magics_manager.magics.get('cell', {}).get('tsql')
    if _original_tsql:
        def _safe_tsql(line, cell):
            match = re.search(r'CREATE OR ALTER VIEW (?:\[dbo\]\.)?\[?(\w+)\]?', cell, re.IGNORECASE)
            view_name = match.group(1) if match else 'Unknown'
            try:
                # Capture displayed output so we can detect the "missing table" SELECT result, which does not raise an exception
                with capture_output() as captured:
                    _original_tsql(line, cell)
                captured.show()

                output_text = captured.stdout + captured.stderr
                for out in captured.outputs:
                    output_text += str(out.data.get('text/plain', '')) if hasattr(out, 'data') else str(out)

                error_match = re.search(r'ERROR:[^\n\r\'"]*', output_text)
                if error_match:
                    _cell_results.append((view_name, 'FAILED', error_match.group(0).strip()))
                else:
                    _cell_results.append((view_name, 'SUCCESS', None))
            except Exception as e:
                _cell_results.append((view_name, 'FAILED', str(e)))
                print(f"[CELL ERROR] {type(e).__name__}: {e}")
        ip.register_magic_function(_safe_tsql, magic_kind='cell', magic_name='tsql')


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### SAPLANGUAGE

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_LANGUAGE', 'I_LANGUAGETEXT') AND TABLE_SCHEMA = 'dbo') <> 2
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_LANGUAGE OR I_LANGUAGETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[SAPLANGUAGE]
# MAGIC         AS
# MAGIC         SELECT DISTINCT [I_LANGUAGE].[LANGUAGE],
# MAGIC             [I_LANGUAGETEXT].[_ISOLanguage],
# MAGIC             [I_LANGUAGETEXT].[LANGUAGENAME],
# MAGIC             [I_LANGUAGETEXT].[LANGUAGECODE],
# MAGIC             '''' AS [_SystemName]
# MAGIC         FROM [I_LANGUAGE]
# MAGIC         LEFT OUTER JOIN [I_LANGUAGETEXT] ON [I_LANGUAGE].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC         WHERE [I_LANGUAGETEXT].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC             AND [I_LANGUAGE].[_SystemName] = [I_LANGUAGETEXT].[_SystemName];
# MAGIC     ')
# MAGIC     SELECT 'View [dbo].[SAPLANGUAGE] created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtACCOUNTINGDOCUMENTTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_ACCOUNTINGDOCUMENTTYPE', 'I_ACCOUNTINGDOCUMENTTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_ACCOUNTINGDOCUMENTTYPE OR I_ACCOUNTINGDOCUMENTTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtACCOUNTINGDOCUMENTTYPETEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,ACCOUNTINGDOCUMENTTYPEKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[ACCOUNTINGDOCUMENTTYPE]
# MAGIC 				,[ACCOUNTINGDOCUMENTTYPE] AS ACCOUNTINGDOCUMENTTYPENAME
# MAGIC 			FROM [I_ACCOUNTINGDOCUMENTTYPE]
# MAGIC 			)
# MAGIC 			,ACCOUNTINGDOCUMENTTYPEKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM ACCOUNTINGDOCUMENTTYPEKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,ACCOUNTINGDOCUMENTTYPETextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_ACCOUNTINGDOCUMENTTYPETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,ACCOUNTINGDOCUMENTTYPETextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.ACCOUNTINGDOCUMENTTYPE, ''''), kl.ACCOUNTINGDOCUMENTTYPE) AS ACCOUNTINGDOCUMENTTYPE
# MAGIC 				,COALESCE(NULLIF(txt.ACCOUNTINGDOCUMENTTYPENAME, ''''), kl.ACCOUNTINGDOCUMENTTYPENAME) AS ACCOUNTINGDOCUMENTTYPENAME
# MAGIC 			FROM ACCOUNTINGDOCUMENTTYPEKeysLanguages kl
# MAGIC 			FULL OUTER JOIN ACCOUNTINGDOCUMENTTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM ACCOUNTINGDOCUMENTTYPETextprefill AS SourceTable
# MAGIC 		PIVOT(max([ACCOUNTINGDOCUMENTTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtACCOUNTINGDOCUMENTTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtACCTASSIGNMENTCATEGORYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_ACCOUNTASSIGNMENTCATEGORY', 'I_ACCTASSIGNMENTCATEGORYTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_ACCOUNTASSIGNMENTCATEGORY OR I_ACCTASSIGNMENTCATEGORYTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [vtACCTASSIGNMENTCATEGORYTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,AcctAssignmentCategoryKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,ACCOUNTASSIGNMENTCATEGORY
# MAGIC 				,CONSUMPTIONPOSTING
# MAGIC 				,INVENTORYSPECIALSTOCKTYPE
# MAGIC 			FROM [I_ACCOUNTASSIGNMENTCATEGORY]
# MAGIC 			)
# MAGIC 			,AcctAssignmentCategoryKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM AcctAssignmentCategoryKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,AcctAssignmentCategoryTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_ACCTASSIGNMENTCATEGORYTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,AcctAssignmentCategoryTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.ACCOUNTASSIGNMENTCATEGORY, ''''), kl.ACCOUNTASSIGNMENTCATEGORY) AS ACCOUNTASSIGNMENTCATEGORY
# MAGIC 			FROM AcctAssignmentCategoryKeysLanguages kl
# MAGIC 			FULL OUTER JOIN AcctAssignmentCategoryTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM AcctAssignmentCategoryTextprefill AS SourceTable
# MAGIC 		PIVOT(max([ACCOUNTASSIGNMENTCATEGORY]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 
# MAGIC 	SELECT 'View [vtACCTASSIGNMENTCATEGORYTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtASSETCLASSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_ASSETCLASS', 'I_ASSETCLASSTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_ASSETCLASS OR I_ASSETCLASSTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtASSETCLASSTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,ASSETCLASSKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[ASSETCLASS]
# MAGIC 				,[ASSETCLASS] AS ASSETCLASSNAME
# MAGIC 			FROM [I_ASSETCLASS]
# MAGIC 			)
# MAGIC 			,ASSETCLASSKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM ASSETCLASSKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,ASSETCLASSTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_ASSETCLASSTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,ASSETCLASSTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.ASSETCLASS, ''''), kl.ASSETCLASS) AS ASSETCLASS
# MAGIC 				,COALESCE(NULLIF(txt.ASSETCLASSNAME, ''''), kl.ASSETCLASSNAME) AS ASSETCLASSNAME
# MAGIC 			FROM ASSETCLASSKeysLanguages kl
# MAGIC 			FULL OUTER JOIN ASSETCLASSTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM ASSETCLASSTextprefill AS SourceTable
# MAGIC 		PIVOT(max([ASSETCLASSNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 
# MAGIC 	SELECT 'View [dbo].[vtASSETCLASSTEXT] created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtASSETTRANSACTIONTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_ASSETTRANSACTIONTYPE', 'I_ASSETTRANSACTIONTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_ASSETTRANSACTIONTYPE OR I_ASSETTRANSACTIONTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtASSETTRANSACTIONTYPETEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,ASSETTRANSACTIONTYPEKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[ASSETTRANSACTIONTYPE]
# MAGIC 				,[ASSETTRANSACTIONTYPE] AS ASSETTRANSACTIONTYPENAME
# MAGIC 			FROM [I_ASSETTRANSACTIONTYPE]
# MAGIC 			)
# MAGIC 			,ASSETTRANSACTIONTYPEKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM ASSETTRANSACTIONTYPEKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,ASSETTRANSACTIONTYPETextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_ASSETTRANSACTIONTYPETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,ASSETTRANSACTIONTYPETextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.ASSETTRANSACTIONTYPE, ''''), kl.ASSETTRANSACTIONTYPE) AS ASSETTRANSACTIONTYPE
# MAGIC 				,COALESCE(NULLIF(txt.ASSETTRANSACTIONTYPENAME, ''''), kl.ASSETTRANSACTIONTYPENAME) AS ASSETTRANSACTIONTYPENAME
# MAGIC 			FROM ASSETTRANSACTIONTYPEKeysLanguages kl
# MAGIC 			FULL OUTER JOIN ASSETTRANSACTIONTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM ASSETTRANSACTIONTYPETextprefill AS SourceTable
# MAGIC 		PIVOT(max([ASSETTRANSACTIONTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 
# MAGIC 	SELECT 'View [dbo].[vtASSETTRANSACTIONTYPETEXT] created successfully!'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtBILLINGDOCUMENTTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_BILLINGDOCUMENTTYPE', 'I_BILLINGDOCUMENTTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_BILLINGDOCUMENTTYPE OR I_BILLINGDOCUMENTTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtBILLINGDOCUMENTTYPETEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,BILLINGDOCUMENTTYPEKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[BILLINGDOCUMENTTYPE]
# MAGIC 				,[BILLINGDOCUMENTTYPE] AS BILLINGDOCUMENTTYPENAME
# MAGIC 			FROM [I_BILLINGDOCUMENTTYPE]
# MAGIC 			)
# MAGIC 			,BILLINGDOCUMENTTYPEKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM BILLINGDOCUMENTTYPEKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,BILLINGDOCUMENTTYPETextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_BILLINGDOCUMENTTYPETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,BILLINGDOCUMENTTYPETextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.BILLINGDOCUMENTTYPE, ''''), kl.BILLINGDOCUMENTTYPE) AS BILLINGDOCUMENTTYPE
# MAGIC 				,COALESCE(NULLIF(txt.BILLINGDOCUMENTTYPENAME, ''''), kl.BILLINGDOCUMENTTYPENAME) AS BILLINGDOCUMENTTYPENAME
# MAGIC 			FROM BILLINGDOCUMENTTYPEKeysLanguages kl
# MAGIC 			FULL OUTER JOIN BILLINGDOCUMENTTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM BILLINGDOCUMENTTYPETextprefill AS SourceTable
# MAGIC 		PIVOT(max([BILLINGDOCUMENTTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 
# MAGIC 	SELECT 'View [dbo].[vtBILLINGDOCUMENTTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtBUSINESSAREATEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_BUSINESSAREA', 'I_BUSINESSAREATEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_BUSINESSAREA OR I_BUSINESSAREATEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtBUSINESSAREATEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,BusinessAreaKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[BUSINESSAREA]
# MAGIC 				,[BUSINESSAREA] AS BUSINESSAREANAME
# MAGIC 			FROM [I_BUSINESSAREA]
# MAGIC 			)
# MAGIC 			,BusinessAreaKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM BusinessAreaKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,BusinessAreaTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_BUSINESSAREATEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,BusinessAreaTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.BUSINESSAREA, ''''), kl.BUSINESSAREA) AS BUSINESSAREA
# MAGIC 				,COALESCE(NULLIF(txt.BUSINESSAREANAME, ''''), kl.BUSINESSAREANAME) AS BUSINESSAREANAME
# MAGIC 			FROM BusinessAreaKeysLanguages kl
# MAGIC 			FULL OUTER JOIN BusinessAreaTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM BusinessAreaTextprefill AS SourceTable
# MAGIC 		PIVOT(max([BUSINESSAREANAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtBUSINESSAREATEXT] created successfully!'
# MAGIC END
# MAGIC 
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtCHARTOFACCOUNTSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_CHARTOFACCOUNTS', 'I_CHARTOFACCOUNTSTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_CHARTOFACCOUNTS OR I_CHARTOFACCOUNTSTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtCHARTOFACCOUNTSTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,CHARTOFACCOUNTSKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[CHARTOFACCOUNTS]
# MAGIC 				,[CHARTOFACCOUNTS] AS CHARTOFACCOUNTSNAME
# MAGIC 			FROM [I_CHARTOFACCOUNTS]
# MAGIC 			)
# MAGIC 			,CHARTOFACCOUNTSKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM CHARTOFACCOUNTSKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,CHARTOFACCOUNTSTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_CHARTOFACCOUNTSTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,CHARTOFACCOUNTSTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.CHARTOFACCOUNTS, ''''), kl.CHARTOFACCOUNTS) AS CHARTOFACCOUNTS
# MAGIC 				,COALESCE(NULLIF(txt.CHARTOFACCOUNTSNAME, ''''), kl.CHARTOFACCOUNTSNAME) AS CHARTOFACCOUNTSNAME
# MAGIC 			FROM CHARTOFACCOUNTSKeysLanguages kl
# MAGIC 			FULL OUTER JOIN CHARTOFACCOUNTSTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM CHARTOFACCOUNTSTextprefill AS SourceTable
# MAGIC 		PIVOT(max([CHARTOFACCOUNTSNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtCHARTOFACCOUNTSTEXT] created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtCOSTCENTERACTIVITYTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_COSTCENTERACTIVITYTYPE', 'I_COSTCENTERACTIVITYTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_COSTCENTERACTIVITYTYPE OR I_COSTCENTERACTIVITYTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [vtCOSTCENTERACTIVITYTYPETEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,COSTCENTERACTIVITYTYPEKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,CONTROLLINGAREA
# MAGIC 				,COSTCTRACTIVITYTYPE
# MAGIC 				,COSTCTRACTIVITYTYPE AS COSTCTRACTIVITYTYPEDESC
# MAGIC 			FROM [I_COSTCENTERACTIVITYTYPE]
# MAGIC 			)
# MAGIC 			,COSTCENTERACTIVITYTYPEKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM COSTCENTERACTIVITYTYPEKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,COSTCENTERACTIVITYTYPETextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_COSTCENTERACTIVITYTYPETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,COSTCENTERACTIVITYTYPETextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.CONTROLLINGAREA, ''''), kl.CONTROLLINGAREA) AS CONTROLLINGAREA
# MAGIC 				,COALESCE(NULLIF(txt.COSTCTRACTIVITYTYPE, ''''), kl.COSTCTRACTIVITYTYPE) AS COSTCENTERACTIVITYTYPE
# MAGIC 				,COALESCE(NULLIF(txt.COSTCTRACTIVITYTYPEDESC, ''''), kl.COSTCTRACTIVITYTYPEDESC) AS COSTCENTERACTIVITYTYPENAME
# MAGIC 			FROM COSTCENTERACTIVITYTYPEKeysLanguages kl
# MAGIC 			FULL OUTER JOIN COSTCENTERACTIVITYTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM COSTCENTERACTIVITYTYPETextprefill AS SourceTable
# MAGIC 		PIVOT(max([COSTCENTERACTIVITYTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [vtCOSTCENTERACTIVITYTYPETEXT] created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtCOSTCENTERTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_COSTCENTER', 'I_COSTCENTERTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_COSTCENTER OR I_COSTCENTERTEXT does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtCOSTCENTERTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,COSTCENTERKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,CONTROLLINGAREA
# MAGIC 				,COSTCENTER
# MAGIC 				,COSTCENTER AS COSTCENTERLONGNAME
# MAGIC 				,COSTCENTER AS COSTCENTERNAME
# MAGIC 			FROM [I_COSTCENTER]
# MAGIC 			)
# MAGIC 			,COSTCENTERKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM COSTCENTERKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,COSTCENTERTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_COSTCENTERTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,COSTCENTERTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.CONTROLLINGAREA, ''''), kl.CONTROLLINGAREA) AS CONTROLLINGAREA
# MAGIC 				,COALESCE(NULLIF(txt.COSTCENTER, ''''), kl.COSTCENTER) AS COSTCENTER
# MAGIC 				,COALESCE(NULLIF(txt.COSTCENTERNAME, ''''), kl.COSTCENTERNAME) AS COSTCENTERNAME
# MAGIC 			FROM COSTCENTERKeysLanguages kl
# MAGIC 			FULL OUTER JOIN COSTCENTERTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM COSTCENTERTextprefill AS SourceTable
# MAGIC 		PIVOT(max([COSTCENTERNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtCOSTCENTERTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtCUSTOMERGROUPTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_CUSTOMERGROUP', 'I_CUSTOMERGROUPTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_CUSTOMERGROUP OR I_CUSTOMERGROUPTEXT does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtCUSTOMERGROUPTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,CUSTOMERGROUPKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[CUSTOMERGROUP]
# MAGIC 				,[CUSTOMERGROUP] AS CUSTOMERGROUPNAME
# MAGIC 			FROM [I_CUSTOMERGROUP]
# MAGIC 			)
# MAGIC 			,CUSTOMERGROUPKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM CUSTOMERGROUPKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,CUSTOMERGROUPTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_CUSTOMERGROUPTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,CUSTOMERGROUPTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.CUSTOMERGROUP, ''''), kl.CUSTOMERGROUP) AS CUSTOMERGROUP
# MAGIC 				,COALESCE(NULLIF(txt.CUSTOMERGROUPNAME, ''''), kl.CUSTOMERGROUPNAME) AS CUSTOMERGROUPNAME
# MAGIC 			FROM CUSTOMERGROUPKeysLanguages kl
# MAGIC 			FULL OUTER JOIN CUSTOMERGROUPTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM CUSTOMERGROUPTextprefill AS SourceTable
# MAGIC 		PIVOT(max([CUSTOMERGROUPNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtCUSTOMERGROUPTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDEBITCREDITCODETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DEBITCREDITCODE', 'I_DEBITCREDITCODETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DEBITCREDITCODE OR I_DEBITCREDITCODETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDEBITCREDITCODETEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,DEBITCREDITCODEKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,DEBITCREDITCODE
# MAGIC 				,DEBITCREDITCODE AS DEBITCREDITCODENAME
# MAGIC 			FROM [I_DEBITCREDITCODE]
# MAGIC 			)
# MAGIC 			,DEBITCREDITCODEKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DEBITCREDITCODEKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,DEBITCREDITCODETextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DEBITCREDITCODETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,debitcredittextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.DEBITCREDITCODE, ''''), kl.DEBITCREDITCODE) AS DEBITCREDITCODE
# MAGIC 				,COALESCE(NULLIF(txt.DEBITCREDITCODENAME, ''''), kl.DEBITCREDITCODENAME) AS DEBITCREDITCODENAME
# MAGIC 			FROM DEBITCREDITCODEKeysLanguages kl
# MAGIC 			FULL OUTER JOIN DEBITCREDITCODETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM debitcredittextprefill AS SourceTable
# MAGIC 		PIVOT(max([DEBITCREDITCODENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtDEBITCREDITCODETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDELIVERYBLOCKREASONTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DELIVERYBLOCKREASON', 'I_DELIVERYBLOCKREASONTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DELIVERYBLOCKREASON OR I_DELIVERYBLOCKREASONTEXT does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDELIVERYBLOCKREASONTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKREASONKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[DELIVERYBLOCKREASON]
# MAGIC 				,[DELIVERYBLOCKREASON] AS DELIVERYBLOCKREASONTEXT
# MAGIC 			FROM [I_DELIVERYBLOCKREASON]
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKREASONKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DELIVERYBLOCKREASONKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKREASONTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DELIVERYBLOCKREASONTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKREASONTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[DELIVERYBLOCKREASON], ''''), kl.[DELIVERYBLOCKREASON]) AS DELIVERYBLOCKREASON
# MAGIC 				,COALESCE(NULLIF(txt.DELIVERYBLOCKREASONTEXT, ''''), kl.DELIVERYBLOCKREASONTEXT) AS DELIVERYBLOCKREASONTEXT
# MAGIC 			FROM DELIVERYBLOCKREASONKeysLanguages kl
# MAGIC 			FULL OUTER JOIN DELIVERYBLOCKREASONTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM DELIVERYBLOCKREASONTextprefill AS SourceTable
# MAGIC 		PIVOT(max([DELIVERYBLOCKREASONTEXT]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtDELIVERYBLOCKREASONTEXT] created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDELIVERYBLOCKSTATUSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DELIVERYBLOCKSTATUS', 'I_DELIVERYBLOCKSTATUSTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DELIVERYBLOCKSTATUS OR I_DELIVERYBLOCKSTATUSTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDELIVERYBLOCKSTATUSTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKSTATUSKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[DELIVERYBLOCKSTATUS]
# MAGIC 				,[DELIVERYBLOCKSTATUS] AS DELIVERYBLOCKSTATUSDESC
# MAGIC 			FROM [I_DELIVERYBLOCKSTATUS]
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKSTATUSKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DELIVERYBLOCKSTATUSKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKSTATUSTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DELIVERYBLOCKSTATUSTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,DELIVERYBLOCKSTATUSTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[DELIVERYBLOCKSTATUS], ''''), kl.[DELIVERYBLOCKSTATUS]) AS DELIVERYBLOCKSTATUS
# MAGIC 				,COALESCE(NULLIF(txt.DELIVERYBLOCKSTATUSDESC, ''''), kl.DELIVERYBLOCKSTATUSDESC) AS DELIVERYBLOCKSTATUSDESC
# MAGIC 			FROM DELIVERYBLOCKSTATUSKeysLanguages kl
# MAGIC 			FULL OUTER JOIN DELIVERYBLOCKSTATUSTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM DELIVERYBLOCKSTATUSTextprefill AS SourceTable
# MAGIC 		PIVOT(max([DELIVERYBLOCKSTATUSDESC]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtDELIVERYBLOCKSTATUSTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDELIVERYDOCUMENTTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DELIVERYDOCUMENTTYPE', 'I_DELIVERYDOCUMENTTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DELIVERYDOCUMENTTYPE OR I_DELIVERYDOCUMENTTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDELIVERYDOCUMENTTYPETEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,DELIVERYDOCUMENTTYPEKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[DELIVERYDOCUMENTTYPE]
# MAGIC 				,[DELIVERYDOCUMENTTYPE] AS DELIVERYDOCUMENTTYPENAME
# MAGIC 			FROM [I_DELIVERYDOCUMENTTYPE]
# MAGIC 			)
# MAGIC 			,DELIVERYDOCUMENTTYPEKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DELIVERYDOCUMENTTYPEKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,DELIVERYDOCUMENTTYPETextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DELIVERYDOCUMENTTYPETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,DELIVERYDOCUMENTTYPETextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.DELIVERYDOCUMENTTYPE, ''''), kl.DELIVERYDOCUMENTTYPE) AS DELIVERYDOCUMENTTYPE
# MAGIC 				,COALESCE(NULLIF(txt.DELIVERYDOCUMENTTYPENAME, ''''), kl.DELIVERYDOCUMENTTYPENAME) AS DELIVERYDOCUMENTTYPENAME
# MAGIC 			FROM DELIVERYDOCUMENTTYPEKeysLanguages kl
# MAGIC 			FULL OUTER JOIN DELIVERYDOCUMENTTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM DELIVERYDOCUMENTTYPETextprefill AS SourceTable
# MAGIC 		PIVOT(max([DELIVERYDOCUMENTTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtDELIVERYDOCUMENTTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDISTRIBUTIONCHANNELTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DISTRIBUTIONCHANNEL', 'I_DISTRIBUTIONCHANNELTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DISTRIBUTIONCHANNEL OR I_DISTRIBUTIONCHANNELTEXT does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDISTRIBUTIONCHANNELTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,DISTRIBUTIONCHANNELKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_UpdateTimeStamp]
# MAGIC 				,[_SystemName]
# MAGIC 				,[DISTRIBUTIONCHANNEL]
# MAGIC 				,[DISTRIBUTIONCHANNEL] AS DISTRIBUTIONCHANNELNAME
# MAGIC 			FROM [I_DISTRIBUTIONCHANNEL]
# MAGIC 			)
# MAGIC 			,DISTRIBUTIONCHANNELKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DISTRIBUTIONCHANNELKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,DISTRIBUTIONCHANNELTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DISTRIBUTIONCHANNELTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,DISTRIBUTIONCHANNELTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[DISTRIBUTIONCHANNEL], ''''), kl.[DISTRIBUTIONCHANNEL]) AS DISTRIBUTIONCHANNEL
# MAGIC 				,COALESCE(NULLIF(txt.DISTRIBUTIONCHANNELNAME, ''''), kl.DISTRIBUTIONCHANNELNAME) AS DISTRIBUTIONCHANNELNAME
# MAGIC 			FROM DISTRIBUTIONCHANNELKeysLanguages kl
# MAGIC 			FULL OUTER JOIN DISTRIBUTIONCHANNELTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM DISTRIBUTIONCHANNELTextprefill AS SourceTable
# MAGIC 		PIVOT(max([DISTRIBUTIONCHANNELNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtDISTRIBUTIONCHANNELTEXT] created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDIVISIONTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DIVISION', 'I_DIVISIONTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DIVISION OR I_DIVISIONTEXT does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDIVISIONTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,DIVISIONKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_UpdateTimeStamp]
# MAGIC 				,[_SystemName]
# MAGIC 				,[DIVISION]
# MAGIC 				,[DIVISION] AS DIVISIONNAME
# MAGIC 			FROM [I_DIVISION]
# MAGIC 			)
# MAGIC 			,DIVISIONKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DIVISIONKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,DIVISIONTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DIVISIONTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,DIVISIONTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[DIVISION], ''''), kl.[DIVISION]) AS DIVISION
# MAGIC 				,COALESCE(NULLIF(txt.DIVISIONNAME, ''''), kl.DIVISIONNAME) AS DIVISIONNAME
# MAGIC 			FROM DIVISIONKeysLanguages kl
# MAGIC 			FULL OUTER JOIN DIVISIONTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM DIVISIONTextprefill AS SourceTable
# MAGIC 		PIVOT(max([DIVISIONNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC 	SELECT 'View [dbo].[vtDIVISIONTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDUNNINGAREATEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DUNNINGAREA', 'I_DUNNINGAREATEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DUNNINGAREA OR I_DUNNINGAREATEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDUNNINGAREATEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages AS (
# MAGIC 			SELECT
# MAGIC 				_ISOLanguage,
# MAGIC 				[LANGUAGE],
# MAGIC 				[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 		)
# MAGIC 		,DUNNINGAREAKeys AS (
# MAGIC 			SELECT distinct [Key]
# MAGIC 			,[_SystemName]
# MAGIC 			,[DUNNINGAREA]
# MAGIC 			,[DUNNINGAREA] AS DUNNINGAREANAME
# MAGIC 			FROM [I_DUNNINGAREA]
# MAGIC 		)
# MAGIC 		,DUNNINGAREAKeysLanguages AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DUNNINGAREAKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 		)
# MAGIC 		,DUNNINGAREATextWithoutNull AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DUNNINGAREATEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 		)
# MAGIC 		,DUNNINGAREATextprefill AS (
# MAGIC 		SELECT
# MAGIC 			COALESCE(txt.[Key], kl.[Key]) AS [Key],
# MAGIC 			COALESCE(txt._SystemName, kl._SystemName) AS _SystemName,
# MAGIC 			COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage,
# MAGIC 			COALESCE(NULLIF(txt.DUNNINGAREA, ''''), kl.DUNNINGAREA) AS DUNNINGAREA,
# MAGIC 			COALESCE(NULLIF(txt.DUNNINGAREANAME, ''''), kl.DUNNINGAREANAME) AS DUNNINGAREANAME
# MAGIC 		FROM DUNNINGAREAKeysLanguages kl
# MAGIC 		FULL OUTER JOIN DUNNINGAREATextWithoutNull AS txt
# MAGIC 			ON kl.[Key] = txt.[Key]
# MAGIC 			AND kl.[_ISOLanguage] = txt.[_ISOLanguage])
# MAGIC 		SELECT *
# MAGIC 		FROM DUNNINGAREATextprefill
# MAGIC 		AS SourceTable PIVOT(
# MAGIC 			max([DUNNINGAREANAME]) FOR [_ISOLanguage] IN
# MAGIC 			(
# MAGIC 			[ZH],[TH],[KO],[RO],[SL],[HR],[UK],[ET],[AR],[HE],[CA],[CS],[DE],[SH],[EN],[FR],[EL],[HU],[IT],[JA],[DA],[PL],[ZF],[NL],[NO],[PT],[SK],[RU],[ES],[TR],[FI],[SV],[BG],[LT],[LV],[HI],[KK],[VI])
# MAGIC 			) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtDUNNINGAREATEXT created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtDUNNINGKEYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_DUNNINGKEY', 'I_DUNNINGKEYTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_DUNNINGKEY OR I_DUNNINGKEYTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtDUNNINGKEYTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,DUNNINGKEYKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[DUNNINGKEY]
# MAGIC 				,[DUNNINGKEY] AS MAXIMUMDUNNINGLEVELDESCRIPTION
# MAGIC 			FROM [I_DUNNINGKEY]
# MAGIC 			)
# MAGIC 			,DUNNINGKEYKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM DUNNINGKEYKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,DUNNINGKEYTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_DUNNINGKEYTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,DUNNINGKEYTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.DUNNINGKEY, ''''), kl.DUNNINGKEY) AS DUNNINGKEY
# MAGIC 				,COALESCE(NULLIF(txt.MAXIMUMDUNNINGLEVELDESCRIPTION, ''''), kl.MAXIMUMDUNNINGLEVELDESCRIPTION) AS MAXIMUMDUNNINGLEVELDESCRIPTION
# MAGIC 			FROM DUNNINGKEYKeysLanguages kl
# MAGIC 			FULL OUTER JOIN DUNNINGKEYTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM DUNNINGKEYTextprefill AS SourceTable
# MAGIC 		PIVOT(max([MAXIMUMDUNNINGLEVELDESCRIPTION]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtDUNNINGKEYTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtEQUIPMENTTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_EQUIPMENT', 'I_EQUIPMENTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_EQUIPMENT OR I_EQUIPMENTTEXT does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtEQUIPMENTTEXT]
# MAGIC         AS WITH Languages AS (
# MAGIC         SELECT
# MAGIC             _ISOLanguage,
# MAGIC             [LANGUAGE],
# MAGIC             [LANGUAGENAME]
# MAGIC         FROM SAPLANGUAGE
# MAGIC         WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC         )
# MAGIC         ,EQUIPMENTKeys AS (
# MAGIC         SELECT distinct [Key]
# MAGIC         ,[_SystemName]
# MAGIC         ,[EQUIPMENT]
# MAGIC         ,[EQUIPMENT] AS EQUIPMENTNAME
# MAGIC         FROM [I_EQUIPMENT]
# MAGIC         )
# MAGIC         ,EQUIPMENTKeysLanguages AS (
# MAGIC         SELECT * FROM EQUIPMENTKeys AS keys
# MAGIC         CROSS APPLY Languages AS lang
# MAGIC         )
# MAGIC         ,EQUIPMENTTextWithoutNull AS (
# MAGIC         SELECT * FROM [I_EQUIPMENTTEXT]
# MAGIC         WHERE [Key] IS NOT NULL
# MAGIC         )
# MAGIC         ,EQUIPMENTTextprefill AS (
# MAGIC         SELECT
# MAGIC             COALESCE(txt.[Key], kl.[Key]) AS [Key],
# MAGIC             COALESCE(txt._SystemName, kl._SystemName) AS _SystemName,
# MAGIC             COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage,
# MAGIC             COALESCE(NULLIF(txt.EQUIPMENT, ''''), kl.EQUIPMENT) AS EQUIPMENT, 
# MAGIC             COALESCE(NULLIF(txt.EQUIPMENTNAME, ''''), kl.EQUIPMENTNAME) AS EQUIPMENTNAME
# MAGIC         FROM EQUIPMENTKeysLanguages kl
# MAGIC         FULL OUTER JOIN EQUIPMENTTextWithoutNull AS txt
# MAGIC             ON kl.[Key] = txt.[Key]
# MAGIC             AND kl.[_ISOLanguage] = txt.[_ISOLanguage])
# MAGIC         SELECT * FROM EQUIPMENTTextprefill
# MAGIC         AS SourceTable PIVOT(max([EQUIPMENTNAME]) FOR [_ISOLanguage] IN
# MAGIC         ([ZH],[TH],[KO],[RO],[SL],[HR],[UK],[ET],[AR],[HE],[CA],[CS],[DE],[SH],[EN],[FR],[EL],[HU],[IT],[JA],[DA],[PL],[ZF],[NL],[NO],[PT],[SK],[RU],[ES],[TR],[FI],[SV],[BG],[LT],[LV],[HI],[KK],[VI])
# MAGIC         ) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtEQUIPMENTTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_FUNCTIONALLOCATION', 'I_FUNCTIONALLOCATIONTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_FUNCTIONALLOCATION OR I_FUNCTIONALLOCATIONTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtFUNCTIONALLOCATIONTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,FUNCTIONALLOCATIONKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[FUNCTIONALLOCATION]
# MAGIC 				,[FUNCTIONALLOCATION] AS FUNCTIONALLOCATIONNAME
# MAGIC 			FROM [I_FUNCTIONALLOCATION]
# MAGIC 			)
# MAGIC 			,FUNCTIONALLOCATIONKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM FUNCTIONALLOCATIONKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,FUNCTIONALLOCATIONTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_FUNCTIONALLOCATIONTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,FUNCTIONALLOCATIONTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.FUNCTIONALLOCATION, ''''), kl.FUNCTIONALLOCATION) AS FUNCTIONALLOCATION
# MAGIC 				,COALESCE(NULLIF(txt.FUNCTIONALLOCATIONNAME, ''''), kl.FUNCTIONALLOCATIONNAME) AS FUNCTIONALLOCATIONNAME
# MAGIC 			FROM FUNCTIONALLOCATIONKeysLanguages kl
# MAGIC 			FULL OUTER JOIN FUNCTIONALLOCATIONTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM FUNCTIONALLOCATIONTextprefill AS SourceTable
# MAGIC 		PIVOT(max([FUNCTIONALLOCATIONNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtFUNCTIONALLOCATIONTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtFUNCTIONALAREATEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_FUNCTIONALAREA', 'I_FUNCTIONALAREATEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_FUNCTIONALAREA OR I_FUNCTIONALAREATEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtFUNCTIONALAREATEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,FUNCTIONALAREAKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[FUNCTIONALAREA]
# MAGIC 				,[FUNCTIONALAREA] AS FUNCTIONALAREANAME
# MAGIC 			FROM [I_FUNCTIONALAREA]
# MAGIC 			)
# MAGIC 			,FUNCTIONALAREAKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM FUNCTIONALAREAKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,FUNCTIONALAREATextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_FUNCTIONALAREATEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,FUNCTIONALAREATextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.FUNCTIONALAREA, ''''), kl.FUNCTIONALAREA) AS FUNCTIONALAREA
# MAGIC 				,COALESCE(NULLIF(txt.FUNCTIONALAREANAME, ''''), kl.FUNCTIONALAREANAME) AS FUNCTIONALAREANAME
# MAGIC 			FROM FUNCTIONALAREAKeysLanguages kl
# MAGIC 			FULL OUTER JOIN FUNCTIONALAREATextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM FUNCTIONALAREATextprefill AS SourceTable
# MAGIC 		PIVOT(max([FUNCTIONALAREANAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtFUNCTIONALAREATEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtGLACCOUNTINCHARTOFACCOUNTSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_GLACCOUNTINCHARTOFACCOUNTS', 'I_GLACCOUNTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_GLACCOUNTINCHARTOFACCOUNTS OR I_GLACCOUNTTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtGLACCOUNTINCHARTOFACCOUNTSTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,GLACCOUNTINCHARTOFACCOUNTSKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[GLACCOUNT]
# MAGIC 				,[GLACCOUNT] AS GLACCOUNTNAME
# MAGIC 			FROM [I_GLACCOUNTINCHARTOFACCOUNTS]
# MAGIC 			)
# MAGIC 			,GLACCOUNTINCHARTOFACCOUNTSKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM GLACCOUNTINCHARTOFACCOUNTSKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,GLACCOUNTINCHARTOFACCOUNTSTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_GLACCOUNTTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,GLACCOUNTINCHARTOFACCOUNTSTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.GLACCOUNT, ''''), kl.GLACCOUNT) AS GLACCOUNT
# MAGIC 				,COALESCE(NULLIF(txt.GLACCOUNTNAME, ''''), kl.GLACCOUNTNAME) AS GLACCOUNTNAME
# MAGIC 			FROM GLACCOUNTINCHARTOFACCOUNTSKeysLanguages kl
# MAGIC 			FULL OUTER JOIN GLACCOUNTINCHARTOFACCOUNTSTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM GLACCOUNTINCHARTOFACCOUNTSTextprefill AS SourceTable
# MAGIC 		PIVOT(max([GLACCOUNTNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtGLACCOUNTINCHARTOFACCOUNTSTEXT created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtGLACCOUNTTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_GLACCOUNTINCHARTOFACCOUNTS', 'I_GLACCOUNTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_GLACCOUNTINCHARTOFACCOUNTS OR I_GLACCOUNTTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtGLACCOUNTTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,GLAccountKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,CHARTOFACCOUNTS
# MAGIC 				,GLACCOUNT
# MAGIC 				,GLACCOUNT AS GLACCOUNTLONGNAME
# MAGIC 				,GLACCOUNT AS GLACCOUNTNAME
# MAGIC 			FROM [I_GLACCOUNTINCHARTOFACCOUNTS]
# MAGIC 			)
# MAGIC 			,GLAccountKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM GLAccountKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,GLAccountTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_GLACCOUNTTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,GLAccountTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.CHARTOFACCOUNTS, ''''), kl.CHARTOFACCOUNTS) AS CHARTOFACCOUNTS
# MAGIC 				,COALESCE(NULLIF(txt.GLACCOUNT, ''''), kl.GLACCOUNT) AS GLACCOUNT
# MAGIC 				,COALESCE(NULLIF(txt.GLACCOUNTNAME, ''''), kl.GLACCOUNTNAME) AS GLACCOUNTNAME
# MAGIC 			FROM GLAccountKeysLanguages kl
# MAGIC 			FULL OUTER JOIN GLAccountTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM GLAccountTextprefill AS SourceTable
# MAGIC 		PIVOT(max([GLACCOUNTNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtGLACCOUNTTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtLEDGERTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_LEDGER', 'I_LEDGERTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_LEDGER OR I_LEDGERTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtLEDGERTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,LEDGERKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[LEDGER]
# MAGIC 				,[LEDGER] AS LEDGERNAME
# MAGIC 			FROM [I_LEDGER]
# MAGIC 			)
# MAGIC 			,LEDGERKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM LEDGERKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,LEDGERTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_LEDGERTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,LEDGERTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.LEDGER, ''''), kl.LEDGER) AS LEDGER
# MAGIC 				,COALESCE(NULLIF(txt.LEDGERNAME, ''''), kl.LEDGERNAME) AS LEDGERNAME
# MAGIC 			FROM LEDGERKeysLanguages kl
# MAGIC 			FULL OUTER JOIN LEDGERTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM LEDGERTextprefill AS SourceTable
# MAGIC 		PIVOT(max([LEDGERNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtLEDGERTEXT created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtMOVEMENTCATEGORYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_MOVEMENTCATEGORY', 'I_MOVEMENTCATEGORYTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_MOVEMENTCATEGORY OR I_MOVEMENTCATEGORYTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtMOVEMENTCATEGORYTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,MOVEMENTCATEGORYKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[ASSETACCTTRANSCLASSFCTN]
# MAGIC 				,[ASSETACCTTRANSCLASSFCTN] AS ASSETACCTTRANSCLASSFCTNNAME
# MAGIC 			FROM [I_MOVEMENTCATEGORY]
# MAGIC 			)
# MAGIC 			,MOVEMENTCATEGORYKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM MOVEMENTCATEGORYKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,MOVEMENTCATEGORYTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_MOVEMENTCATEGORYTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,MOVEMENTCATEGORYTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.ASSETACCTTRANSCLASSFCTN, ''''), kl.ASSETACCTTRANSCLASSFCTN) AS ASSETACCTTRANSCLASSFCTN
# MAGIC 				,COALESCE(NULLIF(txt.ASSETACCTTRANSCLASSFCTNNAME, ''''), kl.ASSETACCTTRANSCLASSFCTNNAME) AS ASSETACCTTRANSCLASSFCTNNAME
# MAGIC 			FROM MOVEMENTCATEGORYKeysLanguages kl
# MAGIC 			FULL OUTER JOIN MOVEMENTCATEGORYTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM MOVEMENTCATEGORYTextprefill AS SourceTable
# MAGIC 		PIVOT(max([ASSETACCTTRANSCLASSFCTNNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtMOVEMENTCATEGORYTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtOVERALLBILLINGSTATUSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_OVERALLBILLINGSTATUS', 'I_OVERALLBILLINGSTATUSTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_OVERALLBILLINGSTATUS OR I_OVERALLBILLINGSTATUSTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtOVERALLBILLINGSTATUSTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,OVERALLBILLINGSTATUSKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[OVERALLBILLINGSTATUS]
# MAGIC 				,[OVERALLBILLINGSTATUS] AS OVERALLBILLINGSTATUSDESC
# MAGIC 			FROM [I_OVERALLBILLINGSTATUS]
# MAGIC 			)
# MAGIC 			,OVERALLBILLINGSTATUSKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM OVERALLBILLINGSTATUSKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,OVERALLBILLINGSTATUSTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_OVERALLBILLINGSTATUSTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,OVERALLBILLINGSTATUSTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[OVERALLBILLINGSTATUS], ''''), kl.[OVERALLBILLINGSTATUS]) AS OVERALLBILLINGSTATUS
# MAGIC 				,COALESCE(NULLIF(txt.OVERALLBILLINGSTATUSDESC, ''''), kl.OVERALLBILLINGSTATUSDESC) AS OVERALLBILLINGSTATUSDESC
# MAGIC 			FROM OVERALLBILLINGSTATUSKeysLanguages kl
# MAGIC 			FULL OUTER JOIN OVERALLBILLINGSTATUSTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM OVERALLBILLINGSTATUSTextprefill AS SourceTable
# MAGIC 		PIVOT(max([OVERALLBILLINGSTATUSDESC]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtOVERALLBILLINGSTATUSTEXT created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPAYMENTBLOCKINGREASONTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PAYMENTBLOCKINGREASON', 'I_PAYMENTBLOCKINGREASONTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PAYMENTBLOCKINGREASON OR I_PAYMENTBLOCKINGREASONTEXT does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtPAYMENTBLOCKINGREASONTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PaymentBlockingReasonKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[PAYMENTBLOCKINGREASON]
# MAGIC 			FROM [I_PAYMENTBLOCKINGREASON]
# MAGIC 			)
# MAGIC 			,PaymentBlockingReasonLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PaymentBlockingReasonKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PaymentBlockingReasonTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PAYMENTBLOCKINGREASONTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PaymentBlockingReasonTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.PAYMENTBLOCKINGREASON, ''''), kl.PAYMENTBLOCKINGREASON) AS PAYMENTBLOCKINGREASON
# MAGIC 				,txt.PAYMENTBLOCKINGREASONNAME AS PAYMENTBLOCKINGREASONNAME
# MAGIC 			FROM PaymentBlockingReasonLanguages kl
# MAGIC 			FULL OUTER JOIN PaymentBlockingReasonTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PaymentBlockingReasonTextprefill AS SourceTable
# MAGIC 		PIVOT(max([PAYMENTBLOCKINGREASONNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtPAYMENTBLOCKINGREASONTEXT created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPAYMENTTERMSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE','I_PAYMENTTERMS','I_PAYMENTTERMSTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE, I_PAYMENTTERMS OR I_PAYMENTTERMSTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtPAYMENTTERMSTEXT]
# MAGIC         AS
# MAGIC         WITH
# MAGIC             Languages AS (
# MAGIC                 SELECT
# MAGIC                     _ISOLanguage,
# MAGIC                     [LANGUAGE],
# MAGIC                     LANGUAGENAME
# MAGIC                 FROM SAPLANGUAGE
# MAGIC                 WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,PAYMENTTERMSKeys AS (
# MAGIC                 SELECT distinct
# MAGIC                     [Key]
# MAGIC                     ,[_SystemName]
# MAGIC                     ,PAYMENTTERMS
# MAGIC                     ,PAYMENTTERMS AS PAYMENTTERMSDESCRIPTION
# MAGIC                 FROM I_PAYMENTTERMS
# MAGIC             )
# MAGIC             ,PAYMENTTERMSKeysLanguages AS (
# MAGIC                 SELECT *
# MAGIC                 FROM PAYMENTTERMSKeys AS keys
# MAGIC                 CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,PAYMENTTERMSTextWithoutNull AS (
# MAGIC                 SELECT *
# MAGIC                 FROM I_PAYMENTTERMSTEXT
# MAGIC                 WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,PAYMENTTERMSTextprefill AS (
# MAGIC                 SELECT
# MAGIC                     COALESCE(txt.[Key], kl.[Key]) AS [Key],
# MAGIC                     COALESCE(txt._SystemName, kl._SystemName) AS _SystemName,
# MAGIC                     COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage,
# MAGIC                     COALESCE(NULLIF(txt.PAYMENTTERMS, ''''), kl.PAYMENTTERMS) AS PAYMENTTERMS,
# MAGIC                     COALESCE(NULLIF(txt.PAYMENTTERMSDESCRIPTION, ''''), kl.PAYMENTTERMSDESCRIPTION) AS PAYMENTTERMSDESCRIPTION
# MAGIC                 FROM PAYMENTTERMSKeysLanguages kl
# MAGIC                 FULL OUTER JOIN PAYMENTTERMSTextWithoutNull AS txt
# MAGIC                     ON kl.[Key] = txt.[Key]
# MAGIC                     AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         select * FROM PAYMENTTERMSTextprefill
# MAGIC         AS SourceTable PIVOT(
# MAGIC             max([PAYMENTTERMSDESCRIPTION]) FOR [_ISOLanguage] IN
# MAGIC             (
# MAGIC                 [ZH],[TH],[KO],[RO],[SL],[HR],[UK],[ET],[AR],[HE],[CA],[CS],[DE],[SH],[EN],[FR],[EL],[HU],[IT],[JA],[DA],[PL],[ZF],[NL],[NO],[PT],[SK],[RU],[ES],[TR],[FI],[SV],[BG],[LT],[LV],[HI],[KK],[VI])
# MAGIC             ) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     PRINT 'View vtPAYMENTTERMSTEXT created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPOSTINGKEYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_POSTINGKEY', 'I_POSTINGKEYTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_POSTINGKEY OR I_POSTINGKEYTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtPOSTINGKEYTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,POSTINGKEYKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[POSTINGKEY]
# MAGIC 				,[POSTINGKEY] AS POSTINGKEYNAME
# MAGIC 			FROM [I_POSTINGKEY]
# MAGIC 			)
# MAGIC 			,POSTINGKEYKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM POSTINGKEYKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,POSTINGKEYTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_POSTINGKEYTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,POSTINGKEYTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.POSTINGKEY, ''''), kl.POSTINGKEY) AS POSTINGKEY
# MAGIC 				,COALESCE(NULLIF(txt.POSTINGKEYNAME, ''''), kl.POSTINGKEYNAME) AS POSTINGKEYNAME
# MAGIC 			FROM POSTINGKEYKeysLanguages kl
# MAGIC 			FULL OUTER JOIN POSTINGKEYTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM POSTINGKEYTextprefill AS SourceTable
# MAGIC 		PIVOT(max([POSTINGKEYNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtPOSTINGKEYTEXT created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPRODUCTGROUP_2TEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PRODUCTGROUP_2', 'I_PRODUCTGROUPTEXT_2') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PRODUCTGROUP_2 OR I_PRODUCTGROUPTEXT_2 does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtPRODUCTGROUP_2TEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PRODUCTGROUP_2Keys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[PRODUCTGROUP]
# MAGIC 				,[PRODUCTGROUP] AS PRODUCTGROUPNAME
# MAGIC 			FROM [I_PRODUCTGROUP_2]
# MAGIC 			)
# MAGIC 			,PRODUCTGROUP_2KeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PRODUCTGROUP_2Keys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PRODUCTGROUP_2TextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PRODUCTGROUPTEXT_2]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PRODUCTGROUP_2Textprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.PRODUCTGROUP, ''''), kl.PRODUCTGROUP) AS PRODUCTGROUP
# MAGIC 				,COALESCE(NULLIF(txt.PRODUCTGROUPNAME, ''''), kl.PRODUCTGROUPNAME) AS PRODUCTGROUPNAME
# MAGIC 			FROM PRODUCTGROUP_2KeysLanguages kl
# MAGIC 			FULL OUTER JOIN PRODUCTGROUP_2TextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PRODUCTGROUP_2Textprefill AS SourceTable
# MAGIC 		PIVOT(max([PRODUCTGROUPNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtPRODUCTGROUP_2TEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPRODUCTTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PRODUCT', 'I_PRODUCTDESCRIPTION') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PRODUCT OR I_PRODUCTDESCRIPTION does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtPRODUCTTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PRODUCTKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[PRODUCT]
# MAGIC 				,[PRODUCT] AS PRODUCTDESCRIPTION
# MAGIC 			FROM [I_PRODUCT]
# MAGIC 			)
# MAGIC 			,PRODUCTKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PRODUCTKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PRODUCTTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PRODUCTDESCRIPTION]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PRODUCTTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[PRODUCT], ''''), kl.[PRODUCT]) AS PRODUCT
# MAGIC 				,COALESCE(NULLIF(txt.PRODUCTDESCRIPTION, ''''), kl.PRODUCTDESCRIPTION) AS PRODUCTDESCRIPTION
# MAGIC 			FROM PRODUCTKeysLanguages kl
# MAGIC 			FULL OUTER JOIN PRODUCTTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PRODUCTTextprefill AS SourceTable
# MAGIC 		PIVOT(max([PRODUCTDESCRIPTION]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtPRODUCTTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPROFITCENTERTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PROFITCENTER', 'I_PROFITCENTERTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PROFITCENTER OR I_PROFITCENTERTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtPROFITCENTERTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,ProfitCenterKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,CONTROLLINGAREA
# MAGIC 				,PROFITCENTER
# MAGIC 				,PROFITCENTER AS PROFITCENTERLONGNAME
# MAGIC 				,PROFITCENTER AS PROFITCENTERNAME
# MAGIC 			FROM [I_PROFITCENTER]
# MAGIC 			)
# MAGIC 			,ProfitCenterKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM ProfitCenterKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,ProfitCenterTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PROFITCENTERTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,ProfitCenterTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.CONTROLLINGAREA, ''''), kl.CONTROLLINGAREA) AS CONTROLLINGAREA
# MAGIC 				,COALESCE(NULLIF(txt.PROFITCENTER, ''''), kl.PROFITCENTER) AS PROFITCENTER
# MAGIC 				,COALESCE(NULLIF(txt.PROFITCENTERNAME, ''''), kl.PROFITCENTERNAME) AS PROFITCENTERNAME
# MAGIC 			FROM ProfitCenterKeysLanguages kl
# MAGIC 			FULL OUTER JOIN ProfitCenterTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM ProfitCenterTextprefill AS SourceTable
# MAGIC 		PIVOT(max([PROFITCENTERNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtPROFITCENTERTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPURCHASINGDOCUMENTORIGINTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PURCHASINGDOCUMENTORIGIN', 'I_PURCHASINGDOCUMENTORIGINTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PURCHASINGDOCUMENTORIGIN OR I_PURCHASINGDOCUMENTORIGINTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW vtPURCHASINGDOCUMENTORIGINTEXT
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PurchasingDocumentOriginKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,PURCHASINGDOCUMENTORIGIN
# MAGIC 			FROM [I_PURCHASINGDOCUMENTORIGIN]
# MAGIC 			)
# MAGIC 			,PurchasingDocumentOriginKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PurchasingDocumentOriginKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PurchasingDocumentOriginTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PURCHASINGDOCUMENTORIGINTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PurchasingDocumentOriginTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.PURCHASINGDOCUMENTORIGIN, ''''), kl.PURCHASINGDOCUMENTORIGIN) AS PURCHASINGDOCUMENTORIGIN
# MAGIC 			FROM PurchasingDocumentOriginKeysLanguages kl
# MAGIC 			FULL OUTER JOIN PurchasingDocumentOriginTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PurchasingDocumentOriginTextprefill AS SourceTable
# MAGIC 		PIVOT(max(PURCHASINGDOCUMENTORIGIN) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtPURCHASINGDOCUMENTORIGINTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPURCHASINGDOCUMENTSTATUSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PURCHASINGDOCUMENTSTATUS', 'I_PURCHASINGDOCUMENTSTATUSTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PURCHASINGDOCUMENTSTATUS OR I_PURCHASINGDOCUMENTSTATUSTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW vtPURCHASINGDOCUMENTSTATUSTEXT
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PurchasingDocumentStatusKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,PURCHASINGDOCUMENTSTATUS
# MAGIC 			FROM [I_PURCHASINGDOCUMENTSTATUS]
# MAGIC 			)
# MAGIC 			,PurchasingDocumentStatusKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PurchasingDocumentStatusKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PurchasingDocumentStatusTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PURCHASINGDOCUMENTSTATUSTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PurchasingDocumentStatusTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.PURCHASINGDOCUMENTSTATUS, ''''), kl.PURCHASINGDOCUMENTSTATUS) AS PURCHASINGDOCUMENTSTATUS
# MAGIC 			FROM PurchasingDocumentStatusKeysLanguages kl
# MAGIC 			FULL OUTER JOIN PurchasingDocumentStatusTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PurchasingDocumentStatusTextprefill AS SourceTable
# MAGIC 		PIVOT(max(PURCHASINGDOCUMENTSTATUS) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtPURCHASINGDOCUMENTSTATUSTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPURCHASINGDOCUMENTTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PURCHASINGDOCUMENTTYPE', 'I_PURCHASINGDOCUMENTTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PURCHASINGDOCUMENTTYPE OR I_PURCHASINGDOCUMENTTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW vtPURCHASINGDOCUMENTTYPETEXT
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PurchasingDocumentTypeKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,PURCHASINGDOCUMENTCATEGORY
# MAGIC 				,PURCHASINGDOCUMENTTYPE
# MAGIC 			FROM [I_PURCHASINGDOCUMENTTYPE]
# MAGIC 			)
# MAGIC 			,PurchasingDocumentTypeKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PurchasingDocumentTypeKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PurchasingDocumentTypeTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PURCHASINGDOCUMENTTYPETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PurchasingDocumentTypeTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.PURCHASINGDOCUMENTCATEGORY, ''''), kl.PURCHASINGDOCUMENTCATEGORY) AS PURCHASINGDOCUMENTCATEGORY
# MAGIC 				,COALESCE(NULLIF(txt.PURCHASINGDOCUMENTTYPE, ''''), kl.PURCHASINGDOCUMENTTYPE) AS PURCHASINGDOCUMENTTYPE
# MAGIC 			FROM PurchasingDocumentTypeKeysLanguages kl
# MAGIC 			FULL OUTER JOIN PurchasingDocumentTypeTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PurchasingDocumentTypeTextprefill AS SourceTable
# MAGIC 		PIVOT(max(PURCHASINGDOCUMENTTYPE) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtPURCHASINGDOCUMENTTYPETEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPURCHASINGPROCESSINGSTATUSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PURCHASINGPROCESSINGSTATUS', 'I_PURGPROCESSINGSTATUSTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PURCHASINGPROCESSINGSTATUS OR I_PURGPROCESSINGSTATUSTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtPURCHASINGPROCESSINGSTATUSTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PURCHASINGPROCESSINGSTATUSKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[PURCHASINGPROCESSINGSTATUS]
# MAGIC 				,[PURCHASINGPROCESSINGSTATUS] AS PURCHASINGPROCESSINGSTATUSNAME
# MAGIC 			FROM [I_PURCHASINGPROCESSINGSTATUS]
# MAGIC 			)
# MAGIC 			,PURCHASINGPROCESSINGSTATUSKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PURCHASINGPROCESSINGSTATUSKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PURCHASINGPROCESSINGSTATUSTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PURGPROCESSINGSTATUSTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PURCHASINGPROCESSINGSTATUSTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[PURCHASINGPROCESSINGSTATUS], ''''), kl.[PURCHASINGPROCESSINGSTATUS]) AS PURCHASINGPROCESSINGSTATUS
# MAGIC 				,COALESCE(NULLIF(txt.PURCHASINGPROCESSINGSTATUSNAME, ''''), kl.PURCHASINGPROCESSINGSTATUSNAME) AS PURCHASINGPROCESSINGSTATUSNAME
# MAGIC 			FROM PURCHASINGPROCESSINGSTATUSKeysLanguages kl
# MAGIC 			FULL OUTER JOIN PURCHASINGPROCESSINGSTATUSTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PURCHASINGPROCESSINGSTATUSTextprefill AS SourceTable
# MAGIC 		PIVOT(max([PURCHASINGPROCESSINGSTATUSNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtPURCHASINGPROCESSINGSTATUSTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPURGDOCUMENTCATEGORYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PURCHASINGDOCUMENTCATEGORY', 'I_PURGDOCUMENTCATEGORYTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PURCHASINGDOCUMENTCATEGORY OR I_PURGDOCUMENTCATEGORYTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW vtPURGDOCUMENTCATEGORYTEXT
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PurgDocumentCategoryKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,PURCHASINGDOCUMENTCATEGORY
# MAGIC 			FROM [I_PURCHASINGDOCUMENTCATEGORY]
# MAGIC 			)
# MAGIC 			,PurgDocumentCategoryKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PurgDocumentCategoryKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PurgDocumentCategoryTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PURGDOCUMENTCATEGORYTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PurgDocumentCategoryTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.PURCHASINGDOCUMENTCATEGORY, ''''), kl.PURCHASINGDOCUMENTCATEGORY) AS PURCHASINGDOCUMENTCATEGORY
# MAGIC 			FROM PurgDocumentCategoryKeysLanguages kl
# MAGIC 			FULL OUTER JOIN PurgDocumentCategoryTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PurgDocumentCategoryTextprefill AS SourceTable
# MAGIC 		PIVOT(max(PURCHASINGDOCUMENTCATEGORY) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtPURGDOCUMENTCATEGORYTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPURGDOCUMENTITEMCATEGORYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PURGDOCUMENTITEMCATEGORY', 'I_PURGDOCUMENTITEMCATEGORYTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PURGDOCUMENTITEMCATEGORY OR I_PURGDOCUMENTITEMCATEGORYTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW vtPURGDOCUMENTITEMCATEGORYTEXT
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,PurgDocumentItemCategoryKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,[PURCHASINGDOCUMENTITEMCATEGORY]
# MAGIC 			FROM [I_PURGDOCUMENTITEMCATEGORY]
# MAGIC 			)
# MAGIC 			,PurgDocumentItemCategoryKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM PurgDocumentItemCategoryKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,PurgDocumentItemCategoryTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_PURGDOCUMENTITEMCATEGORYTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,PurgDocumentItemCategoryTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.PURCHASINGDOCUMENTITEMCATEGORY, ''''), kl.PURCHASINGDOCUMENTITEMCATEGORY) AS PURCHASINGDOCUMENTITEMCATEGORY
# MAGIC 			FROM PurgDocumentItemCategoryKeysLanguages kl
# MAGIC 			FULL OUTER JOIN PurgDocumentItemCategoryTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM PurgDocumentItemCategoryTextprefill AS SourceTable
# MAGIC 		PIVOT(max(PURCHASINGDOCUMENTITEMCATEGORY) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtPURGDOCUMENTITEMCATEGORYTEXT created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSALESDISTRICTTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SALESDISTRICT', 'I_SALESDISTRICTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SALESDISTRICT OR I_SALESDISTRICTTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtSALESDISTRICTTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SALESDISTRICTKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[SALESDISTRICT]
# MAGIC 				,[SALESDISTRICT] AS SALESDISTRICTNAME
# MAGIC 			FROM [I_SALESDISTRICT]
# MAGIC 			)
# MAGIC 			,SALESDISTRICTKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SALESDISTRICTKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SALESDISTRICTTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SALESDISTRICTTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SALESDISTRICTTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[SALESDISTRICT], ''''), kl.[SALESDISTRICT]) AS SALESDISTRICT
# MAGIC 				,COALESCE(NULLIF(txt.SALESDISTRICTNAME, ''''), kl.SALESDISTRICTNAME) AS SALESDISTRICTNAME
# MAGIC 			FROM SALESDISTRICTKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SALESDISTRICTTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SALESDISTRICTTextprefill AS SourceTable
# MAGIC 		PIVOT(max([SALESDISTRICTNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtSALESDISTRICTTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSALESGROUPTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SALESGROUP', 'I_SALESGROUPTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SALESGROUP OR I_SALESGROUPTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtSALESGROUPTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SALESGROUPKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[SALESGROUP]
# MAGIC 				,[SALESGROUP] AS SALESGROUPNAME
# MAGIC 			FROM [I_SALESGROUP]
# MAGIC 			)
# MAGIC 			,SALESGROUPKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SALESGROUPKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SALESGROUPTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SALESGROUPTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SALESGROUPTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[SALESGROUP], ''''), kl.[SALESGROUP]) AS SALESGROUP
# MAGIC 				,COALESCE(NULLIF(txt.SALESGROUPNAME, ''''), kl.SALESGROUPNAME) AS SALESGROUPNAME
# MAGIC 			FROM SALESGROUPKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SALESGROUPTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SALESGROUPTextprefill AS SourceTable
# MAGIC 		PIVOT(max([SALESGROUPNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtSALESGROUPTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSALESOFFICETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SALESOFFICE', 'I_SALESOFFICETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SALESOFFICE OR I_SALESOFFICETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtSALESOFFICETEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SALESOFFICEKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[SALESOFFICE]
# MAGIC 				,[SALESOFFICE] AS SALESOFFICENAME
# MAGIC 			FROM [I_SALESOFFICE]
# MAGIC 			)
# MAGIC 			,SALESOFFICEKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SALESOFFICEKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SALESOFFICETextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SALESOFFICETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SALESOFFICETextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[SALESOFFICE], ''''), kl.[SALESOFFICE]) AS SALESOFFICE
# MAGIC 				,COALESCE(NULLIF(txt.SALESOFFICENAME, ''''), kl.SALESOFFICENAME) AS SALESOFFICENAME
# MAGIC 			FROM SALESOFFICEKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SALESOFFICETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SALESOFFICETextprefill AS SourceTable
# MAGIC 		PIVOT(max([SALESOFFICENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtSALESOFFICETEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSALESORGANIZATIONTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SALESORGANIZATION', 'I_SALESORGANIZATIONTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_LANGUAGE OR I_LANGUAGETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtSALESORGANIZATIONTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SALESORGANIZATIONKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[SALESORGANIZATION]
# MAGIC 				,[SALESORGANIZATION] AS SALESORGANIZATIONNAME
# MAGIC 			FROM [I_SALESORGANIZATION]
# MAGIC 			)
# MAGIC 			,SALESORGANIZATIONKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SALESORGANIZATIONKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SALESORGANIZATIONTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SALESORGANIZATIONTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SALESORGANIZATIONTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[SALESORGANIZATION], ''''), kl.[SALESORGANIZATION]) AS SALESORGANIZATION
# MAGIC 				,COALESCE(NULLIF(txt.SALESORGANIZATIONNAME, ''''), kl.SALESORGANIZATIONNAME) AS SALESORGANIZATIONNAME
# MAGIC 			FROM SALESORGANIZATIONKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SALESORGANIZATIONTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SALESORGANIZATIONTextprefill AS SourceTable
# MAGIC 		PIVOT(max([SALESORGANIZATIONNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtSALESORGANIZATIONTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSDDOCUMENTCATEGORYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE','I_SDDOCUMENTCATEGORY', 'I_SDDOCUMENTCATEGORYTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SDDOCUMENTCATEGORY OR I_SDDOCUMENTCATEGORYTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtSDDOCUMENTCATEGORYTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SDDOCUMENTCATEGORYKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[SDDOCUMENTCATEGORY]
# MAGIC 				,[SDDOCUMENTCATEGORY] AS SDDOCUMENTCATEGORYNAME
# MAGIC 			FROM [I_SDDOCUMENTCATEGORY]
# MAGIC 			)
# MAGIC 			,SDDOCUMENTCATEGORYKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SDDOCUMENTCATEGORYKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SDDOCUMENTCATEGORYTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SDDOCUMENTCATEGORYTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SDDOCUMENTCATEGORYTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.SDDOCUMENTCATEGORY, ''''), kl.SDDOCUMENTCATEGORY) AS SDDOCUMENTCATEGORY
# MAGIC 				,COALESCE(NULLIF(txt.SDDOCUMENTCATEGORYNAME, ''''), kl.SDDOCUMENTCATEGORYNAME) AS SDDOCUMENTCATEGORYNAME
# MAGIC 			FROM SDDOCUMENTCATEGORYKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SDDOCUMENTCATEGORYTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SDDOCUMENTCATEGORYTextprefill AS SourceTable
# MAGIC 		PIVOT(max([SDDOCUMENTCATEGORYNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtSDDOCUMENTCATEGORYTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSEGMENTTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SEGMENT', 'I_SEGMENTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SEGMENT OR I_SEGMENTTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtSEGMENTTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SEGMENTKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[SEGMENT]
# MAGIC 				,[SEGMENT] AS SEGMENTNAME
# MAGIC 			FROM [I_SEGMENT]
# MAGIC 			)
# MAGIC 			,SEGMENTKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SEGMENTKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SEGMENTTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SEGMENTTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SEGMENTTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.SEGMENT, ''''), kl.SEGMENT) AS SEGMENT
# MAGIC 				,COALESCE(NULLIF(txt.SEGMENTNAME, ''''), kl.SEGMENTNAME) AS SEGMENTNAME
# MAGIC 			FROM SEGMENTKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SEGMENTTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SEGMENTTextprefill AS SourceTable
# MAGIC 		PIVOT(max([SEGMENTNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtSEGMENTTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSHIPMENTBLOCKREASONTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SHIPMENTBLOCKREASONTEXT', 'I_SHIPMENTBLOCKREASON') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SHIPMENTBLOCKREASONTEXT OR I_SHIPMENTBLOCKREASON does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtSHIPMENTBLOCKREASONTEXT] AS
# MAGIC         WITH Languages AS 
# MAGIC             (SELECT _ISOLanguage,
# MAGIC                 [LANGUAGE],
# MAGIC                 [LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS ) ,SHIPMENTBLOCKREASONKeys AS 
# MAGIC             (SELECT DISTINCT [Key] ,
# MAGIC                 [_SystemName] ,
# MAGIC                 [SHIPMENTBLOCKREASON] ,
# MAGIC                 [SHIPMENTBLOCKREASON] AS SHIPMENTBLOCKREASONTEXT
# MAGIC             FROM [I_SHIPMENTBLOCKREASON] ) ,SHIPMENTBLOCKREASONKeysLanguages AS 
# MAGIC             (SELECT *
# MAGIC             FROM SHIPMENTBLOCKREASONKeys AS keys CROSS APPLY Languages AS lang ) ,SHIPMENTBLOCKREASONTextWithoutNull AS 
# MAGIC             (SELECT *
# MAGIC             FROM [I_SHIPMENTBLOCKREASONTEXT]
# MAGIC             WHERE [Key] IS NOT NULL ) ,SHIPMENTBLOCKREASONTextprefill AS 
# MAGIC             (SELECT COALESCE(txt.[Key],
# MAGIC                 kl.[Key]) AS [Key],
# MAGIC                 COALESCE(txt._SystemName,
# MAGIC                 kl._SystemName) AS _SystemName,
# MAGIC                 COALESCE(txt._ISOLanguage,
# MAGIC                 kl._ISOLanguage) AS _ISOLanguage,
# MAGIC                 COALESCE(txt.[SHIPMENTBLOCKREASON],
# MAGIC                 kl.[SHIPMENTBLOCKREASON]) AS SHIPMENTBLOCKREASON,
# MAGIC                 COALESCE(txt.SHIPMENTBLOCKREASONTEXT,
# MAGIC                 kl.SHIPMENTBLOCKREASONTEXT) AS SHIPMENTBLOCKREASONTEXT
# MAGIC             FROM SHIPMENTBLOCKREASONKeysLanguages kl FULL OUTER
# MAGIC             JOIN SHIPMENTBLOCKREASONTextWithoutNull AS txt
# MAGIC                 ON kl.[Key] = txt.[Key]
# MAGIC                     AND kl.[_ISOLanguage] = txt.[_ISOLanguage])
# MAGIC         SELECT *
# MAGIC         FROM SHIPMENTBLOCKREASONTextprefill AS SourceTable PIVOT(max([SHIPMENTBLOCKREASONTEXT]) FOR [_ISOLanguage] IN ([ZH],[TH],[KO],[RO],[SL],[HR],[UK],[ET],[AR],[HE],[CA],[CS],[DE],[SH],[EN],[FR],[EL],[HU],[IT],[JA],[DA],[PL],[ZF],[NL],[NO],[PT],[SK],[RU],[ES],[TR],[FI],[SV],[BG],[LT],[LV],[HI],[KK],[VI]) ) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtSHIPMENTBLOCKREASONTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSHIPPINGPOINTTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SHIPPINGPOINT', 'I_SHIPPINGPOINTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SHIPPINGPOINT OR I_SHIPPINGPOINTTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vtSHIPPINGPOINTTEXT]
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SHIPPINGPOINTKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT [Key]
# MAGIC 				,[_SystemName]
# MAGIC 				,[SHIPPINGPOINT]
# MAGIC 				,[SHIPPINGPOINT] AS SHIPPINGPOINTNAME
# MAGIC 			FROM [I_SHIPPINGPOINT]
# MAGIC 			)
# MAGIC 			,SHIPPINGPOINTKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SHIPPINGPOINTKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SHIPPINGPOINTTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SHIPPINGPOINTTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SHIPPINGPOINTTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.[SHIPPINGPOINT], ''''), kl.[SHIPPINGPOINT]) AS SHIPPINGPOINT
# MAGIC 				,COALESCE(NULLIF(txt.SHIPPINGPOINTNAME, ''''), kl.SHIPPINGPOINTNAME) AS SHIPPINGPOINTNAME
# MAGIC 			FROM SHIPPINGPOINTKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SHIPPINGPOINTTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SHIPPINGPOINTTextprefill AS SourceTable
# MAGIC 		PIVOT(max([SHIPPINGPOINTNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 
# MAGIC 	')
# MAGIC     SELECT 'View vtSHIPPINGPOINTTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSUPPLIERINVOICESTATUSTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE','I_SUPPLIERINVOICESTATUSTEXT', 'I_SUPPLIERINVOICESTATUSAPI01') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SUPPLIERINVOICESTATUSTEXT OR I_SUPPLIERINVOICESTATUSAPI01 does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW vtSUPPLIERINVOICESTATUSTEXT
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,SupplierInvoiceStatusKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,SUPPLIERINVOICESTATUS
# MAGIC 			FROM [I_SUPPLIERINVOICESTATUSAPI01]
# MAGIC 			)
# MAGIC 			,SupplierInvoiceStatusKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM SupplierInvoiceStatusKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,SupplierInvoiceStatusTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_SUPPLIERINVOICESTATUSTEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,SupplierInvoiceStatusTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.SUPPLIERINVOICESTATUS, ''''), kl.SUPPLIERINVOICESTATUS) AS SUPPLIERINVOICESTATUS
# MAGIC 			FROM SupplierInvoiceStatusKeysLanguages kl
# MAGIC 			FULL OUTER JOIN SupplierInvoiceStatusTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM SupplierInvoiceStatusTextprefill AS SourceTable
# MAGIC 		PIVOT(max(SUPPLIERINVOICESTATUS) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtSUPPLIERINVOICESTATUSTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtTAXCODETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_TAXCODE', 'I_TAXCODETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_TAXCODE OR I_TAXCODETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW vtTAXCODETEXT
# MAGIC 		AS
# MAGIC 		WITH Languages
# MAGIC 		AS (
# MAGIC 			SELECT _ISOLanguage
# MAGIC 				,[LANGUAGE]
# MAGIC 				,[LANGUAGENAME]
# MAGIC 			FROM SAPLANGUAGE
# MAGIC 			WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC 			)
# MAGIC 			,TaxCodeKeys
# MAGIC 		AS (
# MAGIC 			SELECT DISTINCT _SystemName
# MAGIC 				,[Key]
# MAGIC 				,TAXCALCULATIONPROCEDURE
# MAGIC 				,TAXCODE
# MAGIC 			FROM [I_TAXCODE]
# MAGIC 			)
# MAGIC 			,TaxCodeKeysLanguages
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM TaxCodeKeys AS keys
# MAGIC 			CROSS APPLY Languages AS lang
# MAGIC 			)
# MAGIC 			,TaxCodeTextWithoutNull
# MAGIC 		AS (
# MAGIC 			SELECT *
# MAGIC 			FROM [I_TAXCODETEXT]
# MAGIC 			WHERE [Key] IS NOT NULL
# MAGIC 			)
# MAGIC 			,TaxCodeTextprefill
# MAGIC 		AS (
# MAGIC 			SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC 				,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC 				,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC 				,COALESCE(NULLIF(txt.TAXCALCULATIONPROCEDURE, ''''), kl.TAXCALCULATIONPROCEDURE) AS TAXCALCULATIONPROCEDURE
# MAGIC 				,COALESCE(NULLIF(txt.TAXCODE, ''''), kl.TAXCODE) AS TAXCODE
# MAGIC 			FROM TaxCodeKeysLanguages kl
# MAGIC 			FULL OUTER JOIN TaxCodeTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC 				AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC 			)
# MAGIC 		SELECT *
# MAGIC 		FROM TaxCodeTextprefill AS SourceTable
# MAGIC 		PIVOT(max(TAXCODE) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC 	')
# MAGIC     SELECT 'View vtTAXCODETEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### COSTCENTERHIERARCHY

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_COSTCENTERHIERARCHYNODE') AND TABLE_SCHEMA = 'dbo') <> 1
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_COSTCENTERHIERARCHYNODE does not exist'
# MAGIC END
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[COSTCENTERHIERARCHY]
# MAGIC 		AS
# MAGIC 		WITH FHN (
# MAGIC 			[COSTCENTERHIERARCHY],
# MAGIC 			[PARENTNODE],
# MAGIC 			[HIERARCHYNODE],
# MAGIC 			[CONTROLLINGAREA],
# MAGIC 			[NODETYPE],
# MAGIC 			[COSTCENTER],
# MAGIC 			VALIDITYENDDATE,
# MAGIC 			VALIDITYSTARTDATE,
# MAGIC 			[_SystemName],
# MAGIC 			[Key]
# MAGIC 			)
# MAGIC 		AS (
# MAGIC 			SELECT H.[COSTCENTERHIERARCHY],
# MAGIC 				H.[PARENTNODE],
# MAGIC 				H.[HIERARCHYNODE],
# MAGIC 				H.[CONTROLLINGAREA],
# MAGIC 				H.[NODETYPE],
# MAGIC 				H.[COSTCENTER],
# MAGIC 				H.VALIDITYENDDATE,
# MAGIC 				H.VALIDITYSTARTDATE,
# MAGIC 				[_SystemName],
# MAGIC 				H.[Key]
# MAGIC 			FROM [I_COSTCENTERHIERARCHYNODE] H
# MAGIC 			WHERE H.[VALIDITYENDDATE] = ''99991231''
# MAGIC 			GROUP BY H.[COSTCENTERHIERARCHY],
# MAGIC 				H.[PARENTNODE],
# MAGIC 				H.[HIERARCHYNODE],
# MAGIC 				H.[CONTROLLINGAREA],
# MAGIC 				H.[NODETYPE],
# MAGIC 				H.[COSTCENTER],
# MAGIC 				H.VALIDITYENDDATE,
# MAGIC 				H.VALIDITYSTARTDATE,
# MAGIC 				[_SystemName],
# MAGIC 				H.[Key]
# MAGIC 			) (
# MAGIC 				SELECT L1.[COSTCENTERHIERARCHY],
# MAGIC 					L1.[CONTROLLINGAREA],
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						) AS CHILD,
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[PARENTNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[PARENTNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[PARENTNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[PARENTNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[PARENTNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[PARENTNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[PARENTNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[PARENTNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[PARENTNODE]
# MAGIC 							END
# MAGIC 						) AS PARENT		
# MAGIC 					,
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[VALIDITYENDDATE] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[VALIDITYENDDATE] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[VALIDITYENDDATE] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[VALIDITYENDDATE] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[VALIDITYENDDATE] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[VALIDITYENDDATE] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[VALIDITYENDDATE] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[VALIDITYENDDATE] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[VALIDITYENDDATE] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [VALIDITYENDDATE],
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[VALIDITYSTARTDATE] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[VALIDITYSTARTDATE] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[VALIDITYSTARTDATE] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[VALIDITYSTARTDATE] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[VALIDITYSTARTDATE] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[VALIDITYSTARTDATE] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[VALIDITYSTARTDATE] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[VALIDITYSTARTDATE] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[VALIDITYSTARTDATE] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [VALIDITYSTARTDATE],
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[COSTCENTER] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[COSTCENTER] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[COSTCENTER] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[COSTCENTER] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[COSTCENTER] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[COSTCENTER] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[COSTCENTER] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[COSTCENTER] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[COSTCENTER] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [COSTCENTER]
# MAGIC 					/*				,(
# MAGIC 							CASE 
# MAGIC 								WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L9.[Key] -- L9.[HIERARCHYNODE]
# MAGIC 								WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L8.[Key] -- L8.[HIERARCHYNODE]
# MAGIC 								WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L7.[Key] -- L7.[HIERARCHYNODE]
# MAGIC 								WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L6.[Key] -- L6.[HIERARCHYNODE]
# MAGIC 								WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L5.[Key] -- L5.[HIERARCHYNODE]
# MAGIC 								WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L4.[Key] -- L4.[HIERARCHYNODE]
# MAGIC 								WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L3.[Key] -- L3.[HIERARCHYNODE]
# MAGIC 								WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L2.[Key] -- L2.[HIERARCHYNODE]
# MAGIC 								WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L1.[Key] -- L1.[HIERARCHYNODE]
# MAGIC 								END
# MAGIC 							)
# MAGIC 						--) 
# MAGIC 						AS [COST_CENTER_NODE_KEY] */
# MAGIC 					,
# MAGIC 					nullif(L1.[HIERARCHYNODE], NULL) AS LEVEL1,
# MAGIC 					nullif(L1.[Key], NULL) AS LEVEL1_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L1.[CONTROLLINGAREA], NULL), coalesce(L1.[HIERARCHYNODE], NULL)), '''') AS LEVEL1_KEY
# MAGIC 					,
# MAGIC 					nullif(L2.[HIERARCHYNODE], NULL) AS LEVEL2,
# MAGIC 					nullif(L2.[Key], NULL) AS LEVEL2_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L2.[CONTROLLINGAREA], NULL), coalesce(L2.[HIERARCHYNODE], NULL)), '''') AS LEVEL2_KEY
# MAGIC 					,
# MAGIC 					nullif(L3.[HIERARCHYNODE], NULL) AS LEVEL3,
# MAGIC 					nullif(L3.[Key], NULL) AS LEVEL3_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L3.[CONTROLLINGAREA], NULL), coalesce(L3.[HIERARCHYNODE], NULL)), '''') AS LEVEL3_KEY
# MAGIC 					,
# MAGIC 					nullif(L4.[HIERARCHYNODE], NULL) AS LEVEL4,
# MAGIC 					nullif(L4.[Key], NULL) AS LEVEL4_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L4.[CONTROLLINGAREA], NULL), coalesce(L4.[HIERARCHYNODE], NULL)), '''') AS LEVEL4_KEY
# MAGIC 					,
# MAGIC 					nullif(L5.[HIERARCHYNODE], NULL) AS LEVEL5,
# MAGIC 					nullif(L5.[Key], NULL) AS LEVEL5_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L5.[CONTROLLINGAREA], NULL), coalesce(L5.[HIERARCHYNODE], NULL)), '''') AS LEVEL5_KEY
# MAGIC 					,
# MAGIC 					nullif(L6.[HIERARCHYNODE], NULL) AS LEVEL6,
# MAGIC 					nullif(L6.[Key], NULL) AS LEVEL6_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L6.[CONTROLLINGAREA], NULL), coalesce(L6.[HIERARCHYNODE], NULL)), '''') AS LEVEL6_KEY
# MAGIC 					,
# MAGIC 					nullif(L7.[HIERARCHYNODE], NULL) AS LEVEL7,
# MAGIC 					nullif(L7.[Key], NULL) AS LEVEL7_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L7.[CONTROLLINGAREA], NULL), coalesce(L7.[HIERARCHYNODE], NULL)), '''') AS LEVEL7_KEY
# MAGIC 					,
# MAGIC 					nullif(L8.[HIERARCHYNODE], NULL) AS LEVEL8,
# MAGIC 					nullif(L8.[Key], NULL) AS LEVEL8_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L8.[CONTROLLINGAREA], NULL), coalesce(L8.[HIERARCHYNODE], NULL)), '''') AS LEVEL8_KEY
# MAGIC 					,
# MAGIC 					nullif(L9.[HIERARCHYNODE], NULL) AS LEVEL9,
# MAGIC 					nullif(L9.[Key], NULL) AS LEVEL9_KEY
# MAGIC 					--			,NULLIF(CONCAT_WS(''|'', COALESCE(L9.[CONTROLLINGAREA], NULL), COALESCE(L9.[HIERARCHYNODE], NULL)), '''') AS LEVEL9_KEY
# MAGIC 					,
# MAGIC 					CONCAT_WS(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE]) AS HIERARCHYPATH
# MAGIC 					-- [TL]: Added to determine MAX Hierarchy Level 
# MAGIC 					,
# MAGIC 					LEN(CONCAT_WS(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE])) - LEN(REPLACE(CONCAT_WS(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE]), ''|'', '''')) + 1 AS MAXHIERARCHYLEVEL,
# MAGIC 					L1.[_SystemName]
# MAGIC 				FROM FHN L1
# MAGIC 				LEFT OUTER JOIN FHN L2 ON L1.[COSTCENTERHIERARCHY] = L2.[COSTCENTERHIERARCHY]
# MAGIC 					AND L1.[HIERARCHYNODE] = L2.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L3 ON L2.[COSTCENTERHIERARCHY] = L3.[COSTCENTERHIERARCHY]
# MAGIC 					AND L2.[HIERARCHYNODE] = L3.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L4 ON L3.[COSTCENTERHIERARCHY] = L4.[COSTCENTERHIERARCHY]
# MAGIC 					AND L3.[HIERARCHYNODE] = L4.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L5 ON L4.[COSTCENTERHIERARCHY] = L5.[COSTCENTERHIERARCHY]
# MAGIC 					AND L4.[HIERARCHYNODE] = L5.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L6 ON L5.[COSTCENTERHIERARCHY] = L6.[COSTCENTERHIERARCHY]
# MAGIC 					AND L5.[HIERARCHYNODE] = L6.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L7 ON L6.[COSTCENTERHIERARCHY] = L7.[COSTCENTERHIERARCHY]
# MAGIC 					AND L6.[HIERARCHYNODE] = L7.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L8 ON L7.[COSTCENTERHIERARCHY] = L8.[COSTCENTERHIERARCHY]
# MAGIC 					AND L7.[HIERARCHYNODE] = L8.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L9 ON L8.[COSTCENTERHIERARCHY] = L9.[COSTCENTERHIERARCHY]
# MAGIC 					AND L8.[HIERARCHYNODE] = L9.[PARENTNODE]
# MAGIC 				WHERE L1.NODETYPE = ''R''
# MAGIC 				);
# MAGIC 	')
# MAGIC     SELECT 'View COSTCENTERHIERARCHY created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### COSTCENTERHIERARCHYNODEFINAL

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_COSTCENTERHIERARCHYNODE', 'I_COSTCENTERHIERARCHYNODET', 'I_COSTCENTERTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_COSTCENTERHIERARCHYNODE OR I_COSTCENTERHIERARCHYNODET OR I_COSTCENTERTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[COSTCENTERHIERARCHYNODEFINAL]
# MAGIC 		AS
# MAGIC 		SELECT h.*,
# MAGIC 			ht.LANGUAGE,
# MAGIC 			ht.[_ISOLanguage],
# MAGIC 			ht.HIERARCHYNODETEXT AS HIERARCHYNODETEXT
# MAGIC 		FROM [I_COSTCENTERHIERARCHYNODE] h
# MAGIC 		LEFT OUTER JOIN [I_COSTCENTERHIERARCHYNODET] ht ON h.[Key] = ht.[Key]
# MAGIC 			AND h.[_SystemName] = ht.[_SystemName]
# MAGIC 			AND h.VALIDITYENDDATE = ''99991231''
# MAGIC 		WHERE h.NODETYPE IN (''R'', ''N'')
# MAGIC 
# MAGIC 		UNION
# MAGIC 
# MAGIC 		SELECT h.*,
# MAGIC 			ht.LANGUAGE,
# MAGIC 			ht.[_ISOLanguage],
# MAGIC 			ht.[COSTCENTERNAME] AS HIERARCHYNODETEXT
# MAGIC 		FROM [I_COSTCENTERHIERARCHYNODE] h
# MAGIC 		LEFT OUTER JOIN [I_COSTCENTERTEXT] ht ON h.[COSTCENTER] = ht.[COSTCENTER]
# MAGIC 			AND h.[CONTROLLINGAREA] = ht.[CONTROLLINGAREA]
# MAGIC 			AND h.[VALIDITYENDDATE] = ''99991231''
# MAGIC 			AND h.[_SystemName] = ht.[_SystemName]
# MAGIC 		WHERE h.NODETYPE = ''L'';
# MAGIC 	')
# MAGIC     SELECT 'View COSTCENTERHIERARCHYNODEFINAL created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### GLACCOUNTHIERARCHY

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_GLACCOUNTHIERARCHYNODE') AND TABLE_SCHEMA = 'dbo') <> 1
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_GLACCOUNTHIERARCHYNODE does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 
# MAGIC 		CREATE OR ALTER VIEW [dbo].[GLACCOUNTHIERARCHY]
# MAGIC 		AS
# MAGIC 		WITH FHN (
# MAGIC 			[GLACCOUNTHIERARCHY],
# MAGIC 			[PARENTNODE],
# MAGIC 			[HIERARCHYNODE],
# MAGIC 			[CHARTOFACCOUNTS],
# MAGIC 			[GLACCOUNT],
# MAGIC 			[NODETYPE],
# MAGIC 			[Key],
# MAGIC 			[HIERARCHYVERSION],
# MAGIC 			[VALIDITYENDDATE],
# MAGIC 			[VALIDITYSTARTDATE],
# MAGIC 			[_SystemName]
# MAGIC 			)
# MAGIC 		AS (
# MAGIC 			SELECT h.[GLACCOUNTHIERARCHY],
# MAGIC 				h.[PARENTNODE],
# MAGIC 				h.[HIERARCHYNODE],
# MAGIC 				h.[CHARTOFACCOUNTS],
# MAGIC 				h.[GLACCOUNT],
# MAGIC 				h.[NODETYPE],
# MAGIC 				h.[Key],
# MAGIC 				h.[HIERARCHYVERSION],
# MAGIC 				h.[VALIDITYENDDATE],
# MAGIC 				h.[VALIDITYSTARTDATE],
# MAGIC 				h.[_SystemName]
# MAGIC 			FROM [I_GLACCOUNTHIERARCHYNODE] h
# MAGIC 			WHERE h.[VALIDITYENDDATE] = ''99991231''
# MAGIC 			GROUP BY h.[GLACCOUNTHIERARCHY],
# MAGIC 				h.[PARENTNODE],
# MAGIC 				h.[HIERARCHYNODE],
# MAGIC 				h.[CHARTOFACCOUNTS],
# MAGIC 				h.[GLACCOUNT],
# MAGIC 				h.[NODETYPE],
# MAGIC 				h.[Key],
# MAGIC 				h.[HIERARCHYVERSION],
# MAGIC 				h.[VALIDITYENDDATE],
# MAGIC 				h.[VALIDITYSTARTDATE],
# MAGIC 				h.[_SystemName]
# MAGIC 			) (
# MAGIC 				SELECT L1.[GLACCOUNTHIERARCHY],
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[CHARTOFACCOUNTS]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[CHARTOFACCOUNTS]
# MAGIC 							END
# MAGIC 						) AS CHARTOFACCOUNTS,
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						) AS CHILD,
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[PARENTNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[PARENTNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[PARENTNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[PARENTNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[PARENTNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[PARENTNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[PARENTNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[PARENTNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[PARENTNODE]
# MAGIC 							END
# MAGIC 						) AS PARENT,
# MAGIC 					/*(
# MAGIC 							CASE 
# MAGIC 								WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L9.[Key] -- L9.[HIERARCHYNODE]
# MAGIC 								WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L8.[Key] -- L8.[HIERARCHYNODE]
# MAGIC 								WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L7.[Key] -- L7.[HIERARCHYNODE]
# MAGIC 								WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L6.[Key] -- L6.[HIERARCHYNODE]
# MAGIC 								WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L5.[Key] -- L5.[HIERARCHYNODE]
# MAGIC 								WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L4.[Key] -- L4.[HIERARCHYNODE]
# MAGIC 								WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L3.[Key] -- L3.[HIERARCHYNODE]
# MAGIC 								WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L2.[Key] -- L2.[HIERARCHYNODE]
# MAGIC 								WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L1.[Key] -- L1.[HIERARCHYNODE]
# MAGIC 								END
# MAGIC 							)
# MAGIC 						--)
# MAGIC 						AS [glaccount_node_key]*/
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[HIERARCHYVERSION] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[HIERARCHYVERSION] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[HIERARCHYVERSION] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[HIERARCHYVERSION] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[HIERARCHYVERSION] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[HIERARCHYVERSION] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[HIERARCHYVERSION] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[HIERARCHYVERSION] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[HIERARCHYVERSION] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [HIERARCHYVERSION],
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[VALIDITYENDDATE] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[VALIDITYENDDATE] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[VALIDITYENDDATE] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[VALIDITYENDDATE] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[VALIDITYENDDATE] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[VALIDITYENDDATE] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[VALIDITYENDDATE] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[VALIDITYENDDATE] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[VALIDITYENDDATE] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [VALIDITYENDDATE],
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[VALIDITYSTARTDATE] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[VALIDITYSTARTDATE] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[VALIDITYSTARTDATE] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[VALIDITYSTARTDATE] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[VALIDITYSTARTDATE] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[VALIDITYSTARTDATE] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[VALIDITYSTARTDATE] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[VALIDITYSTARTDATE] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[VALIDITYSTARTDATE] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [VALIDITYSTARTDATE],
# MAGIC 					(
# MAGIC 						CASE 
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[GLACCOUNT] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[GLACCOUNT] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[GLACCOUNT] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[GLACCOUNT] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[GLACCOUNT] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[GLACCOUNT] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[GLACCOUNT] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[GLACCOUNT] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[GLACCOUNT] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [GLACCOUNT],
# MAGIC 					nullif(L1.[HIERARCHYNODE], NULL) AS LEVEL1,
# MAGIC 					nullif(L1.[Key], NULL) AS LEVEL1_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L1.[controllingarea], NULL), coalesce(L1.[HIERARCHYNODE], NULL)), '''') AS LEVEL1_KEY
# MAGIC 					,
# MAGIC 					nullif(L2.[HIERARCHYNODE], NULL) AS LEVEL2,
# MAGIC 					nullif(L2.[Key], NULL) AS LEVEL2_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L2.[controllingarea], NULL), coalesce(L2.[HIERARCHYNODE], NULL)), '''') AS LEVEL2_KEY
# MAGIC 					,
# MAGIC 					nullif(L3.[HIERARCHYNODE], NULL) AS LEVEL3,
# MAGIC 					nullif(L3.[Key], NULL) AS LEVEL3_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L3.[controllingarea], NULL), coalesce(L3.[HIERARCHYNODE], NULL)), '''') AS LEVEL3_KEY
# MAGIC 					,
# MAGIC 					nullif(L4.[HIERARCHYNODE], NULL) AS LEVEL4,
# MAGIC 					nullif(L4.[Key], NULL) AS LEVEL4_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L4.[controllingarea], NULL), coalesce(L4.[HIERARCHYNODE], NULL)), '''') AS LEVEL4_KEY
# MAGIC 					,
# MAGIC 					nullif(L5.[HIERARCHYNODE], NULL) AS LEVEL5,
# MAGIC 					nullif(L5.[Key], NULL) AS LEVEL5_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L5.[controllingarea], NULL), coalesce(L5.[HIERARCHYNODE], NULL)), '''') AS LEVEL5_KEY
# MAGIC 					,
# MAGIC 					nullif(L6.[HIERARCHYNODE], NULL) AS LEVEL6,
# MAGIC 					nullif(L6.[Key], NULL) AS LEVEL6_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L6.[controllingarea], NULL), coalesce(L6.[HIERARCHYNODE], NULL)), '''') AS LEVEL6_KEY
# MAGIC 					,
# MAGIC 					nullif(L7.[HIERARCHYNODE], NULL) AS LEVEL7,
# MAGIC 					nullif(L7.[Key], NULL) AS LEVEL7_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L7.[controllingarea], NULL), coalesce(L7.[HIERARCHYNODE], NULL)), '''') AS LEVEL7_KEY
# MAGIC 					,
# MAGIC 					nullif(L8.[HIERARCHYNODE], NULL) AS LEVEL8,
# MAGIC 					nullif(L8.[Key], NULL) AS LEVEL8_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L8.[controllingarea], NULL), coalesce(L8.[HIERARCHYNODE], NULL)), '''') AS LEVEL8_KEY
# MAGIC 					,
# MAGIC 					nullif(L9.[HIERARCHYNODE], NULL) AS LEVEL9,
# MAGIC 					nullif(L9.[Key], NULL) AS LEVEL9_KEY
# MAGIC 					--,nullif(concat_ws(''|'', coalesce(L9.[controllingarea], NULL), coalesce(L9.[HIERARCHYNODE], NULL)), '''') AS LEVEL9_KEY
# MAGIC 					,
# MAGIC 					concat_ws(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE]) AS HIERARCHYPATH
# MAGIC 					-- [TL]: Added to determine MAX Hierarchy Level 
# MAGIC 					,
# MAGIC 					LEN(CONCAT_WS(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE])) - LEN(REPLACE(CONCAT_WS(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE]), ''|'', '''')) + 1 AS MAXHIERARCHYLEVEL,
# MAGIC 					L1.[_SystemName]
# MAGIC 				FROM FHN L1
# MAGIC 				LEFT OUTER JOIN FHN L2 ON L1.[GLACCOUNTHIERARCHY] = L2.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L1.[HIERARCHYNODE] = L2.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L3 ON L2.[GLACCOUNTHIERARCHY] = L3.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L2.[HIERARCHYNODE] = L3.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L4 ON L3.[GLACCOUNTHIERARCHY] = L4.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L3.[HIERARCHYNODE] = L4.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L5 ON L4.[GLACCOUNTHIERARCHY] = L5.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L4.[HIERARCHYNODE] = L5.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L6 ON L5.[GLACCOUNTHIERARCHY] = L6.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L5.[HIERARCHYNODE] = L6.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L7 ON L6.[GLACCOUNTHIERARCHY] = L7.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L6.[HIERARCHYNODE] = L7.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L8 ON L7.[GLACCOUNTHIERARCHY] = L8.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L7.[HIERARCHYNODE] = L8.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L9 ON L8.[GLACCOUNTHIERARCHY] = L9.[GLACCOUNTHIERARCHY]
# MAGIC 					AND L8.[HIERARCHYNODE] = L9.[PARENTNODE]
# MAGIC 				WHERE L1.NODETYPE = ''R''
# MAGIC 					--L1.[PROFITCENTERHIERARCHY] = ''0106/A000/YBPH''
# MAGIC 					-- --''ZUS10_P_CL'' )
# MAGIC 				);
# MAGIC 	')
# MAGIC     SELECT 'View GLACCOUNTHIERARCHY created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### GLACCOUNTHIERARCHYNODEFINAL

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_GLACCOUNTHIERARCHYNODE', 'I_GLACCOUNTHIERARCHYNODET', 'I_GLACCOUNTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_GLACCOUNTHIERARCHYNODE OR I_GLACCOUNTHIERARCHYNODET OR I_GLACCOUNTTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[GLACCOUNTHIERARCHYNODEFINAL]
# MAGIC 		AS
# MAGIC 		SELECT h.*,
# MAGIC 			ht.LANGUAGE,
# MAGIC 			ht.[_ISOLanguage],
# MAGIC 			ht.HIERARCHYNODETEXT AS HIERARCHYNODETEXT
# MAGIC 		FROM [I_GLACCOUNTHIERARCHYNODE] h
# MAGIC 		LEFT OUTER JOIN [I_GLACCOUNTHIERARCHYNODET] ht ON h.[Key] = ht.[Key]
# MAGIC 			AND h.VALIDITYENDDATE = ''99991231''
# MAGIC 			AND h.[_SystemName] = ht.[_SystemName]
# MAGIC 		WHERE h.NODETYPE IN (''R'', ''N'')
# MAGIC 
# MAGIC 		UNION
# MAGIC 
# MAGIC 		SELECT h.*,
# MAGIC 			ht.LANGUAGE,
# MAGIC 			ht.[_ISOLanguage],
# MAGIC 			ht.[GLACCOUNTNAME] AS HIERARCHYNODETEXT
# MAGIC 		FROM [I_GLACCOUNTHIERARCHYNODE] h
# MAGIC 		LEFT OUTER JOIN [I_GLACCOUNTTEXT] ht ON h.[CHARTOFACCOUNTS] = ht.[CHARTOFACCOUNTS]
# MAGIC 			AND h.[GLACCOUNT] = ht.[GLACCOUNT]
# MAGIC 			AND h.[_SystemName] = ht.[_SystemName]
# MAGIC 			AND h.VALIDITYENDDATE = ''99991231''
# MAGIC 		WHERE h.NODETYPE = ''L''
# MAGIC 			AND LANGUAGE IS NOT NULL;
# MAGIC 	')
# MAGIC     SELECT 'View GLACCOUNTHIERARCHYNODEFINAL created or altered successfully.'
# MAGIC END
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### PROFITCENTERHIERARCHY

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_PROFITCENTERHIERARCHYNODE') AND TABLE_SCHEMA = 'dbo') <> 1
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_PROFITCENTERHIERARCHYNODE does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[PROFITCENTERHIERARCHY]
# MAGIC 		AS
# MAGIC 		WITH FHN (
# MAGIC 			[PROFITCENTERHIERARCHY],
# MAGIC 			[PARENTNODE],
# MAGIC 			[HIERARCHYNODE],
# MAGIC 			[CONTROLLINGAREA],
# MAGIC 			[NODETYPE],
# MAGIC 			[PROFITCENTER],
# MAGIC 			VALIDITYENDDATE,
# MAGIC 			VALIDITYSTARTDATE,
# MAGIC 			[_SystemName],
# MAGIC 			[Key]
# MAGIC 			)
# MAGIC 		AS (
# MAGIC 			SELECT h.[PROFITCENTERHIERARCHY],
# MAGIC 				h.[PARENTNODE],
# MAGIC 				h.[HIERARCHYNODE],
# MAGIC 				h.[CONTROLLINGAREA],
# MAGIC 				h.[NODETYPE],
# MAGIC 				[PROFITCENTER],
# MAGIC 				VALIDITYENDDATE,
# MAGIC 				VALIDITYSTARTDATE,
# MAGIC 				[_SystemName],
# MAGIC 				h.[Key]
# MAGIC 			FROM I_PROFITCENTERHIERARCHYNODE h
# MAGIC 			WHERE h.[VALIDITYENDDATE] = ''99991231''
# MAGIC 			GROUP BY h.[PROFITCENTERHIERARCHY],
# MAGIC 				h.[PARENTNODE],
# MAGIC 				h.[HIERARCHYNODE],
# MAGIC 				h.[CONTROLLINGAREA],
# MAGIC 				h.[NODETYPE],
# MAGIC 				[PROFITCENTER],
# MAGIC 				h.VALIDITYENDDATE,
# MAGIC 				h.VALIDITYSTARTDATE,
# MAGIC 				[_SystemName],
# MAGIC 				h.[Key]
# MAGIC 			) (
# MAGIC 				SELECT L1.[PROFITCENTERHIERARCHY],
# MAGIC 					L1.[CONTROLLINGAREA],
# MAGIC 					(
# MAGIC 						CASE
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						) AS CHILD,
# MAGIC 					(
# MAGIC 						CASE
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[PARENTNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[PARENTNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[PARENTNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[PARENTNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[PARENTNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[PARENTNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[PARENTNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[PARENTNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[PARENTNODE]
# MAGIC 							END
# MAGIC 						) AS PARENT,
# MAGIC 					(
# MAGIC 						CASE
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[VALIDITYENDDATE] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[VALIDITYENDDATE] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[VALIDITYENDDATE] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[VALIDITYENDDATE] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[VALIDITYENDDATE] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[VALIDITYENDDATE] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[VALIDITYENDDATE] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[VALIDITYENDDATE] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[VALIDITYENDDATE] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [VALIDITYENDDATE],
# MAGIC 					(
# MAGIC 						CASE
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[VALIDITYSTARTDATE] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[VALIDITYSTARTDATE] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[VALIDITYSTARTDATE] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[VALIDITYSTARTDATE] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[VALIDITYSTARTDATE] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[VALIDITYSTARTDATE] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[VALIDITYSTARTDATE] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[VALIDITYSTARTDATE] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[VALIDITYSTARTDATE] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [VALIDITYSTARTDATE],
# MAGIC 					(
# MAGIC 						CASE
# MAGIC 							WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L9.[PROFITCENTER] -- L9.[HIERARCHYNODE]
# MAGIC 							WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L8.[PROFITCENTER] -- L8.[HIERARCHYNODE]
# MAGIC 							WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L7.[PROFITCENTER] -- L7.[HIERARCHYNODE]
# MAGIC 							WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L6.[PROFITCENTER] -- L6.[HIERARCHYNODE]
# MAGIC 							WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L5.[PROFITCENTER] -- L5.[HIERARCHYNODE]
# MAGIC 							WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L4.[PROFITCENTER] -- L4.[HIERARCHYNODE]
# MAGIC 							WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L3.[PROFITCENTER] -- L3.[HIERARCHYNODE]
# MAGIC 							WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L2.[PROFITCENTER] -- L2.[HIERARCHYNODE]
# MAGIC 							WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 								THEN L1.[PROFITCENTER] -- L1.[HIERARCHYNODE]
# MAGIC 							END
# MAGIC 						)
# MAGIC 					--)
# MAGIC 					AS [PROFITCENTER]
# MAGIC 					/*			,(
# MAGIC 							CASE
# MAGIC 								WHEN L9.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L9.[Key] -- L9.[HIERARCHYNODE]
# MAGIC 								WHEN L8.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L8.[Key] -- L8.[HIERARCHYNODE]
# MAGIC 								WHEN L7.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L7.[Key] -- L7.[HIERARCHYNODE]
# MAGIC 								WHEN L6.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L6.[Key] -- L6.[HIERARCHYNODE]
# MAGIC 								WHEN L5.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L5.[Key] -- L5.[HIERARCHYNODE]
# MAGIC 								WHEN L4.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L4.[Key] -- L4.[HIERARCHYNODE]
# MAGIC 								WHEN L3.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L3.[Key] -- L3.[HIERARCHYNODE]
# MAGIC 								WHEN L2.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L2.[Key] -- L2.[HIERARCHYNODE]
# MAGIC 								WHEN L1.[HIERARCHYNODE] IS NOT NULL
# MAGIC 									THEN L1.[Key] -- L1.[HIERARCHYNODE]
# MAGIC 								END
# MAGIC 							)
# MAGIC 
# MAGIC 						AS [profit_center_node_key]   */
# MAGIC 					,
# MAGIC 					nullif(L1.[HIERARCHYNODE], NULL) AS LEVEL1,
# MAGIC 					nullif(L1.[Key], NULL) AS LEVEL1_KEY,
# MAGIC 					nullif(L2.[HIERARCHYNODE], NULL) AS LEVEL2,
# MAGIC 					nullif(L2.[Key], NULL) AS LEVEL2_KEY,
# MAGIC 					nullif(L3.[HIERARCHYNODE], NULL) AS LEVEL3,
# MAGIC 					nullif(L3.[Key], NULL) AS LEVEL3_KEY,
# MAGIC 					nullif(L4.[HIERARCHYNODE], NULL) AS LEVEL4,
# MAGIC 					nullif(L4.[Key], NULL) AS LEVEL4_KEY,
# MAGIC 					nullif(L5.[HIERARCHYNODE], NULL) AS LEVEL5,
# MAGIC 					nullif(L5.[Key], NULL) AS LEVEL5_KEY,
# MAGIC 					nullif(L6.[HIERARCHYNODE], NULL) AS LEVEL6,
# MAGIC 					nullif(L6.[Key], NULL) AS LEVEL6_KEY,
# MAGIC 					nullif(L7.[HIERARCHYNODE], NULL) AS LEVEL7,
# MAGIC 					nullif(L7.[Key], NULL) AS LEVEL7_KEY,
# MAGIC 					nullif(L8.[HIERARCHYNODE], NULL) AS LEVEL8,
# MAGIC 					nullif(L8.[Key], NULL) AS LEVEL8_KEY,
# MAGIC 					nullif(L9.[HIERARCHYNODE], NULL) AS LEVEL9,
# MAGIC 					nullif(L9.[Key], NULL) AS LEVEL9_KEY,
# MAGIC 					concat_ws(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE]) AS HIERARCHYPATH
# MAGIC 					-- [TL]: Added to determine MAX Hierarchy Level
# MAGIC 					,
# MAGIC 					LEN(CONCAT_WS(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE])) - LEN(REPLACE(CONCAT_WS(''|'', L1.[HIERARCHYNODE], L2.[HIERARCHYNODE], L3.[HIERARCHYNODE], L4.[HIERARCHYNODE], L5.[HIERARCHYNODE], L6.[HIERARCHYNODE], L7.[HIERARCHYNODE], L8.[HIERARCHYNODE], L9.[HIERARCHYNODE]), ''|'', '''')) + 1 AS MAXHIERARCHYLEVEL,
# MAGIC 					L1.[_SystemName]
# MAGIC 				FROM FHN L1
# MAGIC 				LEFT OUTER JOIN FHN L2 ON L1.[PROFITCENTERHIERARCHY] = L2.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L1.[HIERARCHYNODE] = L2.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L3 ON L2.[PROFITCENTERHIERARCHY] = L3.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L2.[HIERARCHYNODE] = L3.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L4 ON L3.[PROFITCENTERHIERARCHY] = L4.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L3.[HIERARCHYNODE] = L4.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L5 ON L4.[PROFITCENTERHIERARCHY] = L5.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L4.[HIERARCHYNODE] = L5.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L6 ON L5.[PROFITCENTERHIERARCHY] = L6.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L5.[HIERARCHYNODE] = L6.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L7 ON L6.[PROFITCENTERHIERARCHY] = L7.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L6.[HIERARCHYNODE] = L7.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L8 ON L7.[PROFITCENTERHIERARCHY] = L8.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L7.[HIERARCHYNODE] = L8.[PARENTNODE]
# MAGIC 				LEFT OUTER JOIN FHN L9 ON L8.[PROFITCENTERHIERARCHY] = L9.[PROFITCENTERHIERARCHY]
# MAGIC 					AND L8.[HIERARCHYNODE] = L9.[PARENTNODE]
# MAGIC 				WHERE L1.NODETYPE = ''R''
# MAGIC 					--L1.[PROFITCENTERHIERARCHY] = ''0106/A000/YBPH''
# MAGIC 					-- --''ZUS10_P_CL'' )
# MAGIC 				);
# MAGIC   	')
# MAGIC     SELECT 'View PROFITCENTERHIERARCHY created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### PROFITCENTERHIERARCHYNODEFINAL

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_PROFITCENTERHIERARCHYNODE', 'I_PROFITCENTERHIERARCHYNODET', 'I_PROFITCENTERTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_PROFITCENTERHIERARCHYNODE OR I_PROFITCENTERHIERARCHYNODET OR I_PROFITCENTERTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[PROFITCENTERHIERARCHYNODEFINAL]
# MAGIC 		AS
# MAGIC 		SELECT h.*,
# MAGIC 			ht.LANGUAGE,
# MAGIC 			ht.[_ISOLanguage],
# MAGIC 			ht.HIERARCHYNODETEXT AS HIERARCHYNODETEXT
# MAGIC 		FROM [I_PROFITCENTERHIERARCHYNODE] h
# MAGIC 		LEFT OUTER JOIN [I_PROFITCENTERHIERARCHYNODET] ht ON h.[Key] = ht.[Key]
# MAGIC 			AND h.[_SystemName] = ht.[_SystemName]
# MAGIC 			AND h.VALIDITYENDDATE = ''99991231''
# MAGIC 		WHERE h.NODETYPE IN (''R'', ''N'')
# MAGIC 
# MAGIC 		UNION
# MAGIC 
# MAGIC 		SELECT h.*,
# MAGIC 			ht.LANGUAGE,
# MAGIC 			ht.[_ISOLanguage],
# MAGIC 			ht.[PROFITCENTERNAME] AS HIERARCHYNODETEXT
# MAGIC 		FROM [I_PROFITCENTERHIERARCHYNODE] h
# MAGIC 		LEFT OUTER JOIN [I_PROFITCENTERTEXT] ht ON h.[CONTROLLINGAREA] = ht.[CONTROLLINGAREA]
# MAGIC 			AND h.[PROFITCENTER] = ht.[PROFITCENTER]
# MAGIC 			AND h.VALIDITYENDDATE = ''99991231''
# MAGIC 			AND h.[_SystemName] = ht.[_SystemName]
# MAGIC 		WHERE h.NODETYPE = ''L'';
# MAGIC 	')
# MAGIC     SELECT 'View PROFITCENTERHIERARCHYNODEFINAL created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vCOSTCENTER

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if I_COSTCENTER table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_COSTCENTER') AND TABLE_SCHEMA = 'dbo') <> 1
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_COSTCENTER does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vCOSTCENTER]
# MAGIC 		AS
# MAGIC 		SELECT [Key],
# MAGIC 			[_UpdateTimeStamp],
# MAGIC 			[_SystemName],
# MAGIC 			[ACTLDEPSTATISTICALKEYFIGURES],
# MAGIC 			[ACTLINDEPSTATISTICALKEYFIGURES],
# MAGIC 			[ACTYDEPDNTFORMULAPLANNINGTMPL],
# MAGIC 			[ACTYDEPENDENTALLOCATIONTMPL],
# MAGIC 			[ACTYINDEPENDENTALLOCATIONTMPL],
# MAGIC 			[ACTYINDEPFORMULAPLANNINGTMPL],
# MAGIC 			[ADDRESSADDITIONALNAME],
# MAGIC 			[ADDRESSNAME],
# MAGIC 			[AVAILABILITYCONTROLISACTIVE],
# MAGIC 			[AVAILABILITYCONTROLPROFILE],
# MAGIC 			[BUDGETCARRYINGCOSTCENTER],
# MAGIC 			[BUSINESSAREA],
# MAGIC 			[CITYNAME],
# MAGIC 			[COMPANYCODE],
# MAGIC 			[CONDITIONAPPLICATION],
# MAGIC 			[CONDITIONUSAGE],
# MAGIC 			[CONSUMPTIONQTYISRECORDED],
# MAGIC 			[CONTROLLINGAREA],
# MAGIC 			[COSTCENTER],
# MAGIC 			[COSTCENTERACCOUNTINGOVERHEAD],
# MAGIC 			[COSTCENTERADDRNAME3],
# MAGIC 			[COSTCENTERADDRNAME4],
# MAGIC 			[COSTCENTERALLOCATIONMETHOD],
# MAGIC 			[COSTCENTERALTERNATIVEFUNCTION],
# MAGIC 			[COSTCENTERCATEGORY],
# MAGIC 			[COSTCENTERCREATEDBYUSER],
# MAGIC 			[COSTCENTERCREATIONDATE],
# MAGIC 			[COSTCENTERCURRENCY],
# MAGIC 			[COSTCENTERFUNCTION],
# MAGIC 			[COSTCENTERISCOMPLETE],
# MAGIC 			[COSTCENTERPRINTERDESTINATION],
# MAGIC 			[COSTCENTERSTANDARDHIERAREA],
# MAGIC 			[COSTCOLLECTOR],
# MAGIC 			[COSTCTRRESPONSIBLEPERSONNAME],
# MAGIC 			[COSTCTRRESPONSIBLEUSER],
# MAGIC 			[COSTINGSHEET],
# MAGIC 			[COUNTRY],
# MAGIC 			[DATACOMMUNICATIONPHONENUMBER],
# MAGIC 			[DEPARTMENT],
# MAGIC 			[DISTRICT],
# MAGIC 			[FAXNUMBER],
# MAGIC 			[FORMOFADDRESS],
# MAGIC 			[FUNCTIONALAREA],
# MAGIC 			[FUNCTIONALAREAISFIXASSIGNED],
# MAGIC 			[FUND],
# MAGIC 			[FUNDISFIXASSIGNED],
# MAGIC 			[GRANTID],
# MAGIC 			[GRANTIDISFIXASSIGNED],
# MAGIC 			[ISBLKDFORPRIMARYCOSTSPOSTING],
# MAGIC 			[ISBLKDFORSECONDARYCOSTSPOSTING],
# MAGIC 			[ISBLOCKEDFORCOMMITMENTPOSTING],
# MAGIC 			[ISBLOCKEDFORPLANPRIMARYCOSTS],
# MAGIC 			[ISBLOCKEDFORPLANREVENUES],
# MAGIC 			[ISBLOCKEDFORPLANSECONDARYCOSTS],
# MAGIC 			[ISBLOCKEDFORREVENUEPOSTING],
# MAGIC 			[ISSTATISTICALCOSTCENTER],
# MAGIC 			[JOINTVENTURE],
# MAGIC 			[JOINTVENTURECLASS],
# MAGIC 			[JOINTVENTUREEQUITYTYPE],
# MAGIC 			[JOINTVENTUREOBJECTTYPE],
# MAGIC 			[JOINTVENTURERECOVERYCODE],
# MAGIC 			[JOINTVENTURESUBCLASS],
# MAGIC 			[LANGUAGE],
# MAGIC 			[LOGICALSYSTEM],
# MAGIC 			[OBJECTINTERNALID],
# MAGIC 			[PHONENUMBER1],
# MAGIC 			[PHONENUMBER2],
# MAGIC 			[PLANT],
# MAGIC 			[POBOX],
# MAGIC 			[POBOXPOSTALCODE],
# MAGIC 			[POSTALCODE],
# MAGIC 			[PROFITCENTER],
# MAGIC 			[REGION],
# MAGIC 			[STREETADDRESSNAME],
# MAGIC 			[SUBSEQUENTCOSTCENTER],
# MAGIC 			[TAXJURISDICTION],
# MAGIC 			[TELEBOXNUMBER],
# MAGIC 			[TELETEXNUMBER],
# MAGIC 			[TELEXNUMBER],
# MAGIC 			[VALIDITYENDDATE],
# MAGIC 			[VALIDITYSTARTDATE]
# MAGIC 		FROM [I_COSTCENTER] CC1
# MAGIC 		WHERE [VALIDITYENDDATE] = (
# MAGIC 				SELECT MAX(VALIDITYENDDATE)
# MAGIC 				FROM [I_COSTCENTER] CC2
# MAGIC 				WHERE CC1.[Key] = CC2.[Key]
# MAGIC 				);
# MAGIC 	')
# MAGIC     SELECT 'View vCOSTCENTER created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vCOSTCENTERACTIVITYTYPE

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_COSTCENTERACTIVITYTYPE') AND TABLE_SCHEMA = 'dbo') <> 1
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_COSTCENTERACTIVITYTYPE does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vCOSTCENTERACTIVITYTYPE]
# MAGIC 		AS
# MAGIC 		SELECT [Key],
# MAGIC 			[_UpdateTimeStamp],
# MAGIC 			[_SystemName],
# MAGIC 			[ACTIVITYTYPEISBLOCKED],
# MAGIC 			[ACTLPOSTGCOSTCENTERACTYTYPECAT],
# MAGIC 			[ACTUALPRICEALLOCATIONMETHOD],
# MAGIC 			[ACTUALQUANTITYISSETMANUALLY],
# MAGIC 			[ALLOCATIONCOSTELEMENT],
# MAGIC 			[CONTROLLINGAREA],
# MAGIC 			[COSTCTRACTIVITYTYPE],
# MAGIC 			[COSTCTRACTIVITYTYPECATEGORY],
# MAGIC 			[COSTCTRACTIVITYTYPEOUTPQTYUNIT],
# MAGIC 			[COSTCTRACTIVITYTYPEQTYUNIT],
# MAGIC 			[COSTCTRACTIVITYTYPEVALIDCAT],
# MAGIC 			[COSTCTRACTYTYPEISCTRLGRLVTCOMP],
# MAGIC 			[COSTCTRACTYTYPEISHUMRSCERLVT],
# MAGIC 			[COSTORIGINGROUP],
# MAGIC 			[CREATIONDATE],
# MAGIC 			[ENTEREDBYUSER],
# MAGIC 			[FIXEDCOSTISPREDISTRIBUTED],
# MAGIC 			[OUTPUTQUANTITYFACTOR],
# MAGIC 			[PERIODPRICEISAVERAGE],
# MAGIC 			[PLANQUANTITYISSETMANUALLY],
# MAGIC 			[PRICEALLOCATIONMETHOD],
# MAGIC 			[VALIDITYENDDATE],
# MAGIC 			[VALIDITYSTARTDATE]
# MAGIC 		FROM [I_COSTCENTERACTIVITYTYPE] CCA1
# MAGIC 		WHERE [VALIDITYENDDATE] = (
# MAGIC 				SELECT MAX(VALIDITYENDDATE)
# MAGIC 				FROM [I_COSTCENTERACTIVITYTYPE] CCA2
# MAGIC 				WHERE CCA1.[Key] = CCA2.[Key]
# MAGIC 				);
# MAGIC 	')
# MAGIC     SELECT 'View vCOSTCENTERACTIVITYTYPE created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vCOSTCENTERHIERARCHYWTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('COSTCENTERHIERARCHY', 'SAPLANGUAGE', 'COSTCENTERHIERARCHYNODEFINAL', 'I_COSTCENTER') AND TABLE_SCHEMA = 'dbo') <> 4
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table COSTCENTERHIERARCHY OR SAPLANGUAGE OR COSTCENTERHIERARCHYNODEFINAL OR I_COSTCENTER does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vCOSTCENTERHIERARCHYWTEXT]
# MAGIC 		AS
# MAGIC 		WITH COSTCENTERHIERARCHYNODEFINAL
# MAGIC 		AS (
# MAGIC 			SELECT ht.[Key],
# MAGIC 				[HIERARCHYNODETEXT],
# MAGIC 				[VALIDITYENDDATE],
# MAGIC 				[_ISOLanguage]
# MAGIC 			FROM [dbo].[COSTCENTERHIERARCHYNODEFINAL] ht
# MAGIC 			),
# MAGIC         SAPLANG
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [I_LANGUAGE].[LANGUAGE],
# MAGIC                 [I_LANGUAGETEXT].[_ISOLanguage],
# MAGIC                 [I_LANGUAGETEXT].[LANGUAGENAME],
# MAGIC                 [I_LANGUAGETEXT].[LANGUAGECODE],
# MAGIC 				[I_LANGUAGETEXT].[_SystemName]
# MAGIC             FROM [I_LANGUAGE]
# MAGIC             LEFT OUTER JOIN [I_LANGUAGETEXT] ON [I_LANGUAGE].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC             WHERE [I_LANGUAGETEXT].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC                 AND [I_LANGUAGE].[_SystemName] = [I_LANGUAGETEXT].[_SystemName]
# MAGIC         )
# MAGIC 		SELECT h.[COSTCENTERHIERARCHY],
# MAGIC 			h.[CONTROLLINGAREA],
# MAGIC 			h.[CHILD],
# MAGIC 			h.[PARENT],
# MAGIC 			ht.[Key] AS [COSTCENTER_NODE_KEY],
# MAGIC 			sp.[_ISOLanguage] AS [_ISOLanguage],
# MAGIC 			h.[LEVEL1],
# MAGIC 			h.[LEVEL1_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL1], l1.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL1_TEXT,
# MAGIC 			h.[LEVEL2],
# MAGIC 			h.[LEVEL2_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL2], l2.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL2_TEXT,
# MAGIC 			h.[LEVEL3],
# MAGIC 			h.[LEVEL3_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL3], l3.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL3_TEXT,
# MAGIC 			h.[LEVEL4],
# MAGIC 			h.[LEVEL4_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL4], l4.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL4_TEXT,
# MAGIC 			h.[LEVEL5],
# MAGIC 			h.[LEVEL5_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL5], l5.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL5_TEXT,
# MAGIC 			h.[LEVEL6],
# MAGIC 			h.[LEVEL6_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL6], l6.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL6_TEXT,
# MAGIC 			h.[LEVEL7],
# MAGIC 			h.[LEVEL7_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL7], l7.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL7_TEXT,
# MAGIC 			h.[LEVEL8],
# MAGIC 			h.[LEVEL8_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL8], l8.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL8_TEXT,
# MAGIC 			h.[LEVEL9],
# MAGIC 			h.[LEVEL9_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL9], l9.HIERARCHYNODETEXT, NULL) AS COSTCENTER_HIER_LEVEL9_TEXT,
# MAGIC 			h.[HIERARCHYPATH],
# MAGIC 			[MAXHIERARCHYLEVEL],
# MAGIC 			h.[_SystemName],
# MAGIC 			h.VALIDITYENDDATE,
# MAGIC 			h.VALIDITYSTARTDATE
# MAGIC 		FROM [dbo].[COSTCENTERHIERARCHY] h
# MAGIC 		LEFT JOIN [SAPLANG] sp ON h.[_SystemName] = sp.[_SystemName]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l1 ON h.LEVEL1_KEY = l1.[Key]
# MAGIC 			AND l1.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l2 ON h.LEVEL2_KEY = l2.[Key]
# MAGIC 			AND l2.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l3 ON h.LEVEL3_KEY = l3.[Key]
# MAGIC 			AND l3.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l4 ON h.LEVEL4_KEY = l4.[Key]
# MAGIC 			AND l4.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l5 ON h.LEVEL5_KEY = l5.[Key]
# MAGIC 			AND l5.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l6 ON h.LEVEL6_KEY = l6.[Key]
# MAGIC 			AND l6.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l7 ON h.LEVEL7_KEY = l7.[Key]
# MAGIC 			AND l7.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l8 ON h.LEVEL8_KEY = l8.[Key]
# MAGIC 			AND l8.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN COSTCENTERHIERARCHYNODEFINAL AS l9 ON h.LEVEL9_KEY = l9.[Key]
# MAGIC 			AND l9.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN [dbo].[I_COSTCENTER] AS ht ON h.CONTROLLINGAREA = ht.CONTROLLINGAREA
# MAGIC 			AND h.COSTCENTER = ht.COSTCENTER
# MAGIC 			AND h.VALIDITYENDDATE = ht.VALIDITYENDDATE
# MAGIC 	')
# MAGIC     SELECT 'View vCOSTCENTERHIERARCHYWTEXT created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vGLACCOUNTLINEITEMRAWDATA_AGGR

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_GLACCOUNTLINEITEMRAWDATA') AND TABLE_SCHEMA = 'dbo') <> 1
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_GLACCOUNTLINEITEMRAWDATA does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vGLACCOUNTLINEITEMRAWDATA_AGGR]
# MAGIC 		AS
# MAGIC 		SELECT f.[_key_IDEBITCREDITCODE],
# MAGIC 			f.[_key_ICOMPANYCODE],
# MAGIC 			f.[COMPANYCODECURRENCY],
# MAGIC 			f.[GLOBALCURRENCY],
# MAGIC 			f.[TRANSACTIONCURRENCY],
# MAGIC 			f.[_key_IFISCALPERIODFORVARIANT],
# MAGIC 			f.[_key_ILEDGER],
# MAGIC 			f.[_key_IPROFITCENTER],
# MAGIC             f.[_key_ICOSTCENTER],
# MAGIC 			f.[_key_ICHARTOFACCOUNTS],
# MAGIC 			f.[_key_ISEGMENT],
# MAGIC 			f.[_key_IGLACCOUNTINCHARTOFACCOUNTS],
# MAGIC 			f.[_key_IPRODUCTGROUP2],
# MAGIC 			f.[_key_IPRODUCT],
# MAGIC 			f.[_key_ICUSTOMER],
# MAGIC 			f.[FISCALYEAR],
# MAGIC 			f.[FISCALPERIOD],
# MAGIC 			f.[PARTNERCOMPANYCODE],
# MAGIC 			f.[TAXCODE],
# MAGIC 			f.[TAXCOUNTRY],
# MAGIC 			SUM([AMOUNTINCOMPANYCODECURRENCY]) AS [AMOUNTINCOMPANYCODECURRENCY],
# MAGIC 			SUM([AMOUNTINGLOBALCURRENCY]) AS [AMOUNTINGLOBALCURRENCY],
# MAGIC 			SUM([AMOUNTINTRANSACTIONCURRENCY]) AS [AMOUNTINTRANSACTIONCURRENCY]
# MAGIC 		FROM [I_GLACCOUNTLINEITEMRAWDATA] AS f
# MAGIC 		GROUP BY f.[_key_IDEBITCREDITCODE],
# MAGIC 			f.[_key_ICOMPANYCODE],
# MAGIC 			f.[COMPANYCODECURRENCY],
# MAGIC 			f.[GLOBALCURRENCY],
# MAGIC 			f.[TRANSACTIONCURRENCY],
# MAGIC 			f.[_key_IFISCALPERIODFORVARIANT],
# MAGIC 			f.[_key_ILEDGER],
# MAGIC 			f.[_key_IPROFITCENTER],
# MAGIC             f.[_key_ICOSTCENTER],
# MAGIC 			f.[_key_ICHARTOFACCOUNTS],
# MAGIC 			f.[_key_ISEGMENT],
# MAGIC 			f.[_key_IGLACCOUNTINCHARTOFACCOUNTS],
# MAGIC 			f.[_key_IPRODUCTGROUP2],
# MAGIC 			f.[_key_IPRODUCT],
# MAGIC 			f.[_key_ICUSTOMER],
# MAGIC 			f.[FISCALYEAR],
# MAGIC 			f.[FISCALPERIOD],
# MAGIC 			f.[PARTNERCOMPANYCODE],
# MAGIC 			f.[TAXCODE],
# MAGIC 			f.[TAXCOUNTRY];
# MAGIC 	')
# MAGIC     SELECT 'View vGLACCOUNTLINEITEMRAWDATA_AGGR created or altered successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vGLACCOUNTHIERARCHYWTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'GLACCOUNTHIERARCHY', 'GLACCOUNTHIERARCHYNODEFINAL') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR GLACCOUNTHIERARCHY OR GLACCOUNTHIERARCHYNODEFINAL does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vGLACCOUNTHIERARCHYWTEXT]
# MAGIC 		AS
# MAGIC 		WITH GLACCOUNTHIERARCHYNODEFINALx
# MAGIC 		AS (
# MAGIC 			SELECT ht.[Key],
# MAGIC 				[HIERARCHYNODETEXT],
# MAGIC 				[VALIDITYENDDATE],
# MAGIC 				[_ISOLanguage]
# MAGIC 			FROM [GLACCOUNTHIERARCHYNODEFINAL] ht
# MAGIC 			),
# MAGIC         SAPLANG
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [I_LANGUAGE].[LANGUAGE],
# MAGIC                 [I_LANGUAGETEXT].[_ISOLanguage],
# MAGIC                 [I_LANGUAGETEXT].[LANGUAGENAME],
# MAGIC                 [I_LANGUAGETEXT].[LANGUAGECODE],
# MAGIC 				[I_LANGUAGETEXT].[_SystemName]
# MAGIC             FROM [I_LANGUAGE]
# MAGIC             LEFT OUTER JOIN [I_LANGUAGETEXT] ON [I_LANGUAGE].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC             WHERE [I_LANGUAGETEXT].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC                 AND [I_LANGUAGE].[_SystemName] = [I_LANGUAGETEXT].[_SystemName]
# MAGIC         )
# MAGIC 		SELECT h.[GLACCOUNTHIERARCHY],
# MAGIC 			h.[CHARTOFACCOUNTS],
# MAGIC 			h.[CHILD],
# MAGIC 			h.[PARENT],
# MAGIC 			h.[HIERARCHYVERSION],
# MAGIC 			ht.[Key] AS [GLACCOUNT_NODE_KEY],
# MAGIC 			sp.[_ISOLanguage] AS [_ISOLanguage],
# MAGIC 			h.[LEVEL1],
# MAGIC 			h.[LEVEL1_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL1], L1.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL1_TEXT,
# MAGIC 			h.[LEVEL2],
# MAGIC 			h.[LEVEL2_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL2], L2.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL2_TEXT,
# MAGIC 			h.[LEVEL3],
# MAGIC 			h.[LEVEL3_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL3], L3.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL3_TEXT,
# MAGIC 			h.[LEVEL4],
# MAGIC 			h.[LEVEL4_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL4], L4.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL4_TEXT,
# MAGIC 			h.[LEVEL5],
# MAGIC 			h.[LEVEL5_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL5], L5.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL5_TEXT,
# MAGIC 			h.[LEVEL6],
# MAGIC 			h.[LEVEL6_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL6], L6.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL6_TEXT,
# MAGIC 			h.[LEVEL7],
# MAGIC 			h.[LEVEL7_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL7], L7.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL7_TEXT,
# MAGIC 			h.[LEVEL8],
# MAGIC 			h.[LEVEL8_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL8], L8.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL8_TEXT,
# MAGIC 			h.[LEVEL9],
# MAGIC 			h.[LEVEL9_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL9], L9.HIERARCHYNODETEXT, NULL) AS GLACCOUNT_HIER_LEVEL9_TEXT,
# MAGIC 			h.[HIERARCHYPATH],
# MAGIC 			h.[MAXHIERARCHYLEVEL],
# MAGIC 			h.[_SystemName],
# MAGIC 			h.VALIDITYENDDATE,
# MAGIC 			h.VALIDITYSTARTDATE
# MAGIC 		FROM [GLACCOUNTHIERARCHY] h
# MAGIC 		LEFT JOIN [SAPLANG] sp ON h.[_SystemName] = sp.[_SystemName]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L1 ON h.LEVEL1_KEY = L1.[Key]
# MAGIC 			AND L1.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L2 ON h.LEVEL2_KEY = L2.[Key]
# MAGIC 			AND L2.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L3 ON h.LEVEL3_KEY = L3.[Key]
# MAGIC 			AND L3.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L4 ON h.LEVEL4_KEY = L4.[Key]
# MAGIC 			AND L4.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L5 ON h.LEVEL5_KEY = L5.[Key]
# MAGIC 			AND L5.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L6 ON h.LEVEL6_KEY = L6.[Key]
# MAGIC 			AND L6.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L7 ON h.LEVEL7_KEY = L7.[Key]
# MAGIC 			AND L7.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L8 ON h.LEVEL8_KEY = L8.[Key]
# MAGIC 			AND L8.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN GLACCOUNTHIERARCHYNODEFINAL AS L9 ON h.LEVEL9_KEY = L9.[Key]
# MAGIC 			AND L9.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN [I_GLACCOUNTINCHARTOFACCOUNTS] AS ht ON h.[GLACCOUNT] = ht.[GLACCOUNT]
# MAGIC 			AND h.CHARTOFACCOUNTS = ht.CHARTOFACCOUNTS;
# MAGIC 	')
# MAGIC     SELECT 'View vGLACCOUNTHIERARCHYWTEXT created or altered successfully.'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vPROFITCENTER

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('I_PROFITCENTER') AND TABLE_SCHEMA = 'dbo') <> 1
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table I_PROFITCENTER does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vPROFITCENTER]
# MAGIC 		AS
# MAGIC 		SELECT [Key],
# MAGIC 			[_UpdateTimeStamp],
# MAGIC 			[_SystemName],
# MAGIC 			[ADDITIONALNAME],
# MAGIC 			[ADDRESSNAME],
# MAGIC 			[CITYNAME],
# MAGIC 			[COMPANYCODE],
# MAGIC 			[CONTROLLINGAREA],
# MAGIC 			[COUNTRY],
# MAGIC 			[DATACOMMUNICATIONPHONENUMBER],
# MAGIC 			[DEPARTMENT],
# MAGIC 			[DISTRICT],
# MAGIC 			[FAXNUMBER],
# MAGIC 			[FORMOFADDRESS],
# MAGIC 			[FORMULAPLANNINGTEMPLATE],
# MAGIC 			[LANGUAGE],
# MAGIC 			[PHONENUMBER1],
# MAGIC 			[PHONENUMBER2],
# MAGIC 			[POBOX],
# MAGIC 			[POBOXPOSTALCODE],
# MAGIC 			[POSTALCODE],
# MAGIC 			[PROFITCENTER],
# MAGIC 			[PROFITCENTERADDRNAME3],
# MAGIC 			[PROFITCENTERADDRNAME4],
# MAGIC 			[PROFITCENTERCREATEDBYUSER],
# MAGIC 			[PROFITCENTERCREATIONDATE],
# MAGIC 			[PROFITCENTERISBLOCKED],
# MAGIC 			[PROFITCENTERPRINTERNAME],
# MAGIC 			[PROFITCENTERSTANDARDHIERARCHY],
# MAGIC 			[PROFITCTRRESPONSIBLEPERSONNAME],
# MAGIC 			[PROFITCTRRESPONSIBLEUSER],
# MAGIC 			[REGION],
# MAGIC 			[SEGMENT],
# MAGIC 			[STREETADDRESSNAME],
# MAGIC 			[TAXJURISDICTION],
# MAGIC 			[TELEBOXNUMBER],
# MAGIC 			[TELETEXNUMBER],
# MAGIC 			[TELEXNUMBER],
# MAGIC 			[VALIDITYSTARTDATE],
# MAGIC 			[VALIDITYENDDATE]
# MAGIC 		FROM [I_PROFITCENTER] PC1
# MAGIC 		WHERE [VALIDITYENDDATE] = (
# MAGIC 				SELECT MAX(VALIDITYENDDATE)
# MAGIC 				FROM [I_PROFITCENTER] PC2
# MAGIC 				WHERE PC1.[Key] = PC2.[Key]
# MAGIC 				);
# MAGIC 	')
# MAGIC     SELECT 'View I_PROFITCENTER created or altered successfully.'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vPROFITCENTERHIERARCHYWTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('PROFITCENTERHIERARCHYNODEFINAL', 'PROFITCENTERHIERARCHY', 'SAPLANGUAGE', 'I_PROFITCENTER') AND TABLE_SCHEMA = 'dbo') <> 4
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table PROFITCENTERHIERARCHYNODEFINAL OR PROFITCENTERHIERARCHY OR SAPLANGUAGE OR I_PROFITCENTER does not exist'
# MAGIC END
# MAGIC 
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vPROFITCENTERHIERARCHYWTEXT]
# MAGIC 		AS
# MAGIC 		WITH PROFITCENTERHIERARCHYNODEFINAL
# MAGIC 		AS (
# MAGIC 			SELECT ht.[Key],
# MAGIC 				[HIERARCHYNODETEXT],
# MAGIC 				[VALIDITYENDDATE],
# MAGIC 				[_ISOLanguage]
# MAGIC 			FROM [dbo].[PROFITCENTERHIERARCHYNODEFINAL] ht
# MAGIC 			),
# MAGIC         SAPLANG
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [I_LANGUAGE].[LANGUAGE],
# MAGIC                 [I_LANGUAGETEXT].[_ISOLanguage],
# MAGIC                 [I_LANGUAGETEXT].[LANGUAGENAME],
# MAGIC                 [I_LANGUAGETEXT].[LANGUAGECODE],
# MAGIC 				[I_LANGUAGETEXT].[_SystemName]
# MAGIC             FROM [I_LANGUAGE]
# MAGIC             LEFT OUTER JOIN [I_LANGUAGETEXT] ON [I_LANGUAGE].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC             WHERE [I_LANGUAGETEXT].[LANGUAGE] = [I_LANGUAGETEXT].[LANGUAGECODE]
# MAGIC                 AND [I_LANGUAGE].[_SystemName] = [I_LANGUAGETEXT].[_SystemName]
# MAGIC         )
# MAGIC 		SELECT h.[PROFITCENTERHIERARCHY],
# MAGIC 			h.[CONTROLLINGAREA],
# MAGIC 			h.[CHILD],
# MAGIC 			h.[PARENT],
# MAGIC 			ht.[Key] AS [PROFITCENTER_NODE_KEY],
# MAGIC 			sp.[_ISOLanguage] AS [_ISOLanguage],
# MAGIC 			h.[LEVEL1],
# MAGIC 			h.[LEVEL1_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL1], l1.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL1_TEXT,
# MAGIC 			h.[LEVEL2],
# MAGIC 			h.[LEVEL2_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL2], l2.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL2_TEXT,
# MAGIC 			h.[LEVEL3],
# MAGIC 			h.[LEVEL3_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL3], l3.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL3_TEXT,
# MAGIC 			h.[LEVEL4],
# MAGIC 			h.[LEVEL4_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL4], l4.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL4_TEXT,
# MAGIC 			h.[LEVEL5],
# MAGIC 			h.[LEVEL5_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL5], l5.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL5_TEXT,
# MAGIC 			h.[LEVEL6],
# MAGIC 			h.[LEVEL6_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL6], l6.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL6_TEXT,
# MAGIC 			h.[LEVEL7],
# MAGIC 			h.[LEVEL7_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL7], l7.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL7_TEXT,
# MAGIC 			h.[LEVEL8],
# MAGIC 			h.[LEVEL8_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL8], l8.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL8_TEXT,
# MAGIC 			h.[LEVEL9],
# MAGIC 			h.[LEVEL9_KEY],
# MAGIC 			Concat_ws('' '', h.[LEVEL9], l9.HIERARCHYNODETEXT, NULL) AS PROFITCENTER_HIER_LEVEL9_TEXT,
# MAGIC 			h.[HIERARCHYPATH],
# MAGIC 			[MAXHIERARCHYLEVEL],
# MAGIC 			h.[_SystemName],
# MAGIC 			h.VALIDITYENDDATE,
# MAGIC 			h.VALIDITYSTARTDATE
# MAGIC 		FROM [dbo].[PROFITCENTERHIERARCHY] h
# MAGIC 		LEFT JOIN [SAPLANG] sp ON h.[_SystemName] = sp.[_SystemName]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l1 ON h.LEVEL1_KEY = l1.[Key]
# MAGIC 			AND l1.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l2 ON h.LEVEL2_KEY = l2.[Key]
# MAGIC 			AND l2.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l3 ON h.LEVEL3_KEY = l3.[Key]
# MAGIC 			AND l3.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l4 ON h.LEVEL4_KEY = l4.[Key]
# MAGIC 			AND l4.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l5 ON h.LEVEL5_KEY = l5.[Key]
# MAGIC 			AND l5.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l6 ON h.LEVEL6_KEY = l6.[Key]
# MAGIC 			AND l6.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l7 ON h.LEVEL7_KEY = l7.[Key]
# MAGIC 			AND l7.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l8 ON h.LEVEL8_KEY = l8.[Key]
# MAGIC 			AND l8.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN PROFITCENTERHIERARCHYNODEFINAL AS l9 ON h.LEVEL9_KEY = l9.[Key]
# MAGIC 			AND l9.[_ISOLanguage] = sp.[_ISOLanguage]
# MAGIC 		LEFT JOIN [dbo].[I_PROFITCENTER] AS ht ON h.CONTROLLINGAREA = ht.CONTROLLINGAREA
# MAGIC 			AND h.PROFITCENTER = ht.PROFITCENTER
# MAGIC 			AND h.VALIDITYENDDATE = ht.VALIDITYENDDATE
# MAGIC 
# MAGIC ')
# MAGIC     SELECT 'View vPROFITCENTERHIERARCHYWTEXT created or altered successfully.'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vSUPPLIERINVOICEITEM

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('C_SUPPLIERINVOICEDEX', 'C_SUPPLIERINVOICEITEMDEX') AND TABLE_SCHEMA = 'dbo') <> 2
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table C_SUPPLIERINVOICEDEX OR C_SUPPLIERINVOICEITEMDEX does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vSUPPLIERINVOICEITEM]
# MAGIC         AS
# MAGIC         SELECT
# MAGIC             SID.SUPPLIERINVOICE
# MAGIC             ,SIID.FISCALYEAR
# MAGIC             ,SIID.SUPPLIERINVOICEITEM
# MAGIC             ,SIID.QTYINPURCHASEORDERPRICEUNIT
# MAGIC             ,SIID.PURCHASEORDERPRICEUNIT
# MAGIC             ,SIID.PURCHASEORDERQUANTITYUNIT
# MAGIC             ,SIID.PURCHASEORDER
# MAGIC             ,SIID.PURCHASEORDERITEM
# MAGIC             ,SID.INVOICEGROSSAMOUNT
# MAGIC             ,SIID.DOCUMENTCURRENCY
# MAGIC             ,SIID.PRMTHBREFERENCEDOCUMENT
# MAGIC             ,SIID.PRMTHBREFERENCEDOCUMENTFSCLYR
# MAGIC             ,SIID.PRMTHBREFERENCEDOCUMENTITEM
# MAGIC             ,SIID.PURCHASEORDERITEMMATERIAL
# MAGIC             ,SIID.QUANTITYINPURCHASEORDERUNIT
# MAGIC             ,SIID.SUPLRINVCITMHASQUALITYVARIANCE
# MAGIC             ,SIID.SUPLRINVCITEMHASORDPRCQTYVARC
# MAGIC             ,SIID.SUPLRINVCITEMHASQTYVARIANCE
# MAGIC             ,SIID.SUPLRINVCITEMHASPRICEVARIANCE
# MAGIC             ,SIID.SUPLRINVCITEMHASOTHERVARIANCE
# MAGIC             ,SIID.SUPLRINVCITEMHASAMOUNTOUTSDTOL
# MAGIC             ,SIID.SUPLRINVCITEMHASDATEVARIANCE
# MAGIC             ,SIID.ISSUBSEQUENTDEBITCREDIT
# MAGIC             ,SIID.PLANT
# MAGIC             ,SIID.SUPPLIERINVOICEITEMAMOUNT
# MAGIC             ,SIID.UNPLANNEDDELIVERYCOST
# MAGIC             ,SIID.DOCUMENTHEADERTEXT
# MAGIC             ,SIID.DOCUMENTDATE
# MAGIC             ,SIID.POSTINGDATE
# MAGIC             ,SIID.COMPANYCODE
# MAGIC             ,SIID.SUPPLIERINVOICEORIGIN
# MAGIC             ,SIID.INVOICINGPARTY
# MAGIC             ,SIID.UNPLANNEDDELIVERYCOSTTAXCODE
# MAGIC             ,SIID.REVERSEDOCUMENT
# MAGIC             ,SIID.REVERSEDOCUMENTFISCALYEAR
# MAGIC             ,SIID.SUPPLIERINVOICEIDBYINVCGPARTY
# MAGIC             ,SIID.ISINVOICE
# MAGIC             ,SIID.SUPPLIERINVOICESTATUS
# MAGIC             ,SIID._key_ICOMPANYCODE
# MAGIC             ,SIID._key_IINVOICINGPARTY
# MAGIC             ,SIID._key_IFISCALYEARFORCOMPANYCODE
# MAGIC             ,SIID._key_IPLANT
# MAGIC             ,SIID._key_IPRODUCT
# MAGIC             ,SID._key_ISUPPLIERINVOICESTATUS
# MAGIC         FROM [dbo].[C_SUPPLIERINVOICEDEX] AS SID
# MAGIC         LEFT OUTER JOIN [dbo].[C_SUPPLIERINVOICEITEMDEX] AS SIID
# MAGIC         ON SID.SUPPLIERINVOICE = SIID.SUPPLIERINVOICE
# MAGIC         AND SID.FISCALYEAR = SIID.FISCALYEAR
# MAGIC     ')
# MAGIC     SELECT 'View vSUPPLIERINVOICEITEM created or altered successfully.'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vSUPPLIERINVOICEITEMCOMPLIANT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if SAPLANGUAGE table exists
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('C_SUPPLIERINVOICEITEMDEX', 'C_PURCHASEORDERITEMDEX') AND TABLE_SCHEMA = 'dbo') <> 2
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table C_SUPPLIERINVOICEITEMDEX OR C_PURCHASEORDERITEMDEX does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC 		CREATE OR ALTER VIEW [dbo].[vSUPPLIERINVOICEITEMCOMPLIANT]
# MAGIC 		AS
# MAGIC 		WITH T_SUPPLIER AS (
# MAGIC 			SELECT
# MAGIC 				PURCHASEORDER, PURCHASEORDERITEM, SUPPLIERINVOICE, SUPPLIERINVOICEITEM, FISCALYEAR, _SystemName, SUPPLIERINVOICEITEMAMOUNT,
# MAGIC 				_key_ICOMPANYCODE, _key_IINVOICINGPARTY, _key_IPLANT, _key_IPRODUCT, _key_ISUPPLIERINVOICESTATUS,
# MAGIC 				_key_IFISCALPERIODFORVARIANT, DOCUMENTDATE, _key_ICURRENCY, DOCUMENTCURRENCY, REVERSEDOCUMENT
# MAGIC 			FROM C_SUPPLIERINVOICEITEMDEX
# MAGIC 		), T_PURCHASEORDER AS (
# MAGIC 			SELECT DISTINCT PURCHASECONTRACT, PURCHASEORDER, PURCHASEORDERITEM, _SystemName FROM C_PURCHASEORDERITEMDEX
# MAGIC 		), T_JOINEDFACTS AS (
# MAGIC 			SELECT
# MAGIC 				A.*,
# MAGIC 				IS_COMPLIANT = IIF(A.PURCHASEORDER IS NULL OR TRIM(A.PURCHASEORDER) = '''', ''Non-Compliant'', ''Complaint''),
# MAGIC 				IS_CONTRACT = IIF(B.PURCHASECONTRACT IS NULL OR TRIM(B.PURCHASECONTRACT) = '''', ''Non-Contract'', ''Contract''),
# MAGIC 				IS_REVERSED = IIF(A.REVERSEDOCUMENT IS NULL OR TRIM(A.REVERSEDOCUMENT) = '''', ''Not-Reversed'', ''Reversed'')
# MAGIC 			FROM T_SUPPLIER A
# MAGIC 			LEFT JOIN T_PURCHASEORDER B ON
# MAGIC 				A.PURCHASEORDER = B.PURCHASEORDER AND
# MAGIC 				A.PURCHASEORDERITEM = B.PURCHASEORDERITEM AND
# MAGIC 				A._SystemName = B._SystemName
# MAGIC 		), T_GB as (
# MAGIC 		Select
# MAGIC 			FISCALYEAR, _SystemName, SUM(SUPPLIERINVOICEITEMAMOUNT) AS SUPPLIERINVOICEITEMAMOUNT,
# MAGIC 			_key_ICOMPANYCODE,
# MAGIC 			_key_IINVOICINGPARTY,
# MAGIC 			_key_IPLANT, _key_IPRODUCT,
# MAGIC 			_key_IFISCALPERIODFORVARIANT, _key_ICURRENCY, DOCUMENTCURRENCY, IS_REVERSED, IS_COMPLIANT, IS_CONTRACT
# MAGIC 		FROM T_JOINEDFACTS
# MAGIC 		GROUP BY FISCALYEAR, _SystemName,
# MAGIC 			_key_ICOMPANYCODE,
# MAGIC 			_key_IINVOICINGPARTY,
# MAGIC 			_key_IPLANT, _key_IPRODUCT,
# MAGIC 			_key_IFISCALPERIODFORVARIANT, _key_ICURRENCY, DOCUMENTCURRENCY, IS_REVERSED, IS_COMPLIANT, IS_CONTRACT
# MAGIC 		)
# MAGIC 		Select * from T_GB
# MAGIC 	')
# MAGIC     SELECT 'View vSUPPLIERINVOICEITEMCOMPLIANT created successfully.'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtFACTORYCALENDARTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_FACTORYCALENDAR', 'I_FACTORYCALENDARTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_FACTORYCALENDAR OR I_FACTORYCALENDARTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtFACTORYCALENDARTEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,FactoryCalendarKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key]
# MAGIC                 ,[_SystemName]
# MAGIC                 ,[FACTORYCALENDAR]
# MAGIC                 ,[FACTORYCALENDAR] AS FACTORYCALENDARNAME
# MAGIC             FROM [I_FACTORYCALENDAR]
# MAGIC             )
# MAGIC             ,FactoryCalendarKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM FactoryCalendarKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,FactoryCalendarTextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_FACTORYCALENDARTEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,FactoryCalendarTextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[FACTORYCALENDAR], ''''), kl.[FACTORYCALENDAR]) AS [FACTORYCALENDAR]
# MAGIC                 ,COALESCE(NULLIF(txt.[FACTORYCALENDARNAME], ''''), kl.[FACTORYCALENDAR]) AS [FACTORYCALENDARNAME]
# MAGIC             FROM FactoryCalendarKeysLanguages kl
# MAGIC             FULL OUTER JOIN FactoryCalendarTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM FactoryCalendarTextprefill AS SourceTable
# MAGIC         PIVOT(max([FACTORYCALENDARNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtFACTORYCALENDARTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtOPERATIONCONTROLPROFILETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_OPERATIONCONTROLPROFILE', 'I_OPERATIONCONTROLPROFILETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_OPERATIONCONTROLPROFILE OR I_OPERATIONCONTROLPROFILETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtOPERATIONCONTROLPROFILETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,OPERATIONCONTROLPROFILEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC 				[_SystemName],
# MAGIC 				[OPERATIONCONTROLPROFILE],
# MAGIC                 [OPERATIONCONTROLPROFILE] AS OPERATIONCONTROLPROFILENAME
# MAGIC             FROM [I_OPERATIONCONTROLPROFILE]
# MAGIC             )
# MAGIC             ,OPERATIONCONTROLPROFILEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM OPERATIONCONTROLPROFILEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,OPERATIONCONTROLPROFILETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_OPERATIONCONTROLPROFILETEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,OPERATIONCONTROLPROFILETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONCONTROLPROFILE], ''''), kl.[OPERATIONCONTROLPROFILE]) AS [OPERATIONCONTROLPROFILE]
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONCONTROLPROFILENAME], ''''), kl.[OPERATIONCONTROLPROFILE]) AS [OPERATIONCONTROLPROFILENAME]
# MAGIC             FROM OPERATIONCONTROLPROFILEKeysLanguages kl
# MAGIC             FULL OUTER JOIN OPERATIONCONTROLPROFILETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM OPERATIONCONTROLPROFILETextprefill AS SourceTable
# MAGIC         PIVOT(max([OPERATIONCONTROLPROFILENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtOPERATIONCONTROLPROFILETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtOPERATIONSETUPGROUPTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_OPERATIONSETUPGROUP', 'I_OPERATIONSETUPGROUPTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_OPERATIONSETUPGROUP OR I_OPERATIONSETUPGROUPTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtOPERATIONSETUPGROUPTEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC                 [OPERATIONSETUPGROUP],
# MAGIC 				[_SystemName],
# MAGIC 				[PLANT],
# MAGIC 				[OPERATIONSETUPGROUPCATEGORY],
# MAGIC                 [OPERATIONSETUPGROUP] AS OPERATIONSETUPGROUPNAME
# MAGIC             FROM [I_OPERATIONSETUPGROUP]
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM OPERATIONSETUPGROUPKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPTextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_OPERATIONSETUPGROUPTEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPTextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSETUPGROUP], ''''), kl.[OPERATIONSETUPGROUP]) AS [OPERATIONSETUPGROUP]
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSETUPGROUPNAME], ''''), kl.[OPERATIONSETUPGROUP]) AS [OPERATIONSETUPGROUPNAME]
# MAGIC             FROM OPERATIONSETUPGROUPKeysLanguages kl
# MAGIC             FULL OUTER JOIN OPERATIONSETUPGROUPTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM OPERATIONSETUPGROUPTextprefill AS SourceTable
# MAGIC         PIVOT(max([OPERATIONSETUPGROUPNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtOPERATIONSETUPGROUPTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtOPERATIONSETUPGROUPCATTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_OPERATIONSETUPGROUPCATEGORY', 'I_OPERATIONSETUPGROUPCATTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_OPERATIONSETUPGROUPCATEGORY OR I_OPERATIONSETUPGROUPCATTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtOPERATIONSETUPGROUPCATTEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPCATEGORYKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC                 [OPERATIONSETUPGROUPCATEGORY],
# MAGIC 				[_SystemName],
# MAGIC 				[PLANT],
# MAGIC 				[OPERATIONSETUPGROUPCATEGORY] AS OPERATIONSETUPGROUPCATNAME
# MAGIC             FROM [I_OPERATIONSETUPGROUPCATEGORY]
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPCATEGORYKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM OPERATIONSETUPGROUPCATEGORYKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPCATEGORYTextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_OPERATIONSETUPGROUPCATTEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,OPERATIONSETUPGROUPCATEGORYTextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSETUPGROUPCATEGORY], ''''), kl.[OPERATIONSETUPGROUPCATEGORY]) AS [OPERATIONSETUPGROUPCATEGORY]
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSETUPGROUPCATNAME], ''''), kl.[OPERATIONSETUPGROUPCATEGORY]) AS [OPERATIONSETUPGROUPCATNAME]
# MAGIC             FROM OPERATIONSETUPGROUPCATEGORYKeysLanguages kl
# MAGIC             FULL OUTER JOIN OPERATIONSETUPGROUPCATEGORYTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM OPERATIONSETUPGROUPCATEGORYTextprefill AS SourceTable
# MAGIC         PIVOT(max([OPERATIONSETUPGROUPCATNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtOPERATIONSETUPGROUPCATTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtOPERATIONSETUPTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_OPERATIONSETUPTYPE', 'I_OPERATIONSETUPTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_OPERATIONSETUPTYPE OR I_OPERATIONSETUPTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtOPERATIONSETUPTYPETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,OPERATIONSETUPTYPEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC                 [OPERATIONSETUPTYPE],
# MAGIC 				[_SystemName],
# MAGIC 				[PLANT],
# MAGIC 				[OPERATIONSETUPTYPE] AS OPERATIONSETUPTYPENAME
# MAGIC             FROM [I_OPERATIONSETUPTYPE]
# MAGIC             )
# MAGIC             ,OPERATIONSETUPTYPEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM OPERATIONSETUPTYPEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,OPERATIONSETUPTYPETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_OPERATIONSETUPTYPETEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,OPERATIONSETUPTYPETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSETUPTYPE], ''''), kl.[OPERATIONSETUPTYPE]) AS [OPERATIONSETUPTYPE]
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSETUPTYPENAME], ''''), kl.[OPERATIONSETUPTYPE]) AS [OPERATIONSETUPTYPENAME]
# MAGIC             FROM OPERATIONSETUPTYPEKeysLanguages kl
# MAGIC             FULL OUTER JOIN OPERATIONSETUPTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM OPERATIONSETUPTYPETextprefill AS SourceTable
# MAGIC         PIVOT(max([OPERATIONSETUPTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtOPERATIONSETUPTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtOPERATIONSTANDARDTEXTTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_OPERATIONSTANDARDTEXT', 'I_OPERATIONSTANDARDTEXTTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_OPERATIONSTANDARDTEXT OR I_OPERATIONSTANDARDTEXTTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtOPERATIONSTANDARDTEXTTEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,OPERATIONSTANDARDTEXTCODEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC 				[OPERATIONSTANDARDTEXTCODE],
# MAGIC 				[_SystemName],
# MAGIC                 [OPERATIONSTANDARDTEXTCODE] AS OPERATIONSTANDARDTEXTCODENAME
# MAGIC             FROM [I_OPERATIONSTANDARDTEXT]
# MAGIC             )
# MAGIC             ,OPERATIONSTANDARDTEXTCODEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM OPERATIONSTANDARDTEXTCODEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,OPERATIONSTANDARDTEXTCODETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_OPERATIONSTANDARDTEXTTEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,OPERATIONSTANDARDTEXTCODETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSTANDARDTEXTCODE], ''''), kl.[OPERATIONSTANDARDTEXTCODE]) AS [OPERATIONSTANDARDTEXTCODE]
# MAGIC                 ,COALESCE(NULLIF(txt.[OPERATIONSTANDARDTEXTCODENAME], ''''), kl.[OPERATIONSTANDARDTEXTCODE]) AS [OPERATIONSTANDARDTEXTCODENAME]
# MAGIC             FROM OPERATIONSTANDARDTEXTCODEKeysLanguages kl
# MAGIC             FULL OUTER JOIN OPERATIONSTANDARDTEXTCODETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM OPERATIONSTANDARDTEXTCODETextprefill AS SourceTable
# MAGIC         PIVOT(max([OPERATIONSTANDARDTEXTCODENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtOPERATIONSTANDARDTEXTTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtWORKCENTERTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC  
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_WORKCENTER', 'I_WORKCENTERTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_WORKCENTER OR I_WORKCENTERTEXT does not exist'
# MAGIC END
# MAGIC  
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtWORKCENTERTEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,WORKCENTERINTERNALIDKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC                 [WORKCENTERINTERNALID],
# MAGIC                 [_SystemName],
# MAGIC                 [WORKCENTERTYPECODE],
# MAGIC                 [WORKCENTER] AS WORKCENTERTEXT
# MAGIC             FROM [I_WORKCENTER]
# MAGIC             )
# MAGIC             ,WORKCENTERINTERNALIDKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM WORKCENTERINTERNALIDKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,WORKCENTERINTERNALIDTextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_WORKCENTERTEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,WORKCENTERINTERNALIDTextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[WORKCENTERINTERNALID], ''''), kl.[WORKCENTERINTERNALID]) AS [WORKCENTERINTERNALID]
# MAGIC                 ,COALESCE(NULLIF(txt.[WORKCENTERTEXT], ''''), kl.[WORKCENTERTEXT]) AS [WORKCENTERTEXT]
# MAGIC             FROM WORKCENTERINTERNALIDKeysLanguages kl
# MAGIC             FULL OUTER JOIN WORKCENTERINTERNALIDTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM WORKCENTERINTERNALIDTextprefill AS SourceTable
# MAGIC         PIVOT(max([WORKCENTERTEXT]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC  
# MAGIC     SELECT 'View [dbo].[vtWORKCENTERTEXT] created successfully!'
# MAGIC END

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtWORKCENTERTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_WORKCENTERTYPE', 'I_WORKCENTERTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_WORKCENTERTYPE OR I_WORKCENTERTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtWORKCENTERTYPETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,WORKCENTERTYPECODEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC 				[WORKCENTERTYPECODE],
# MAGIC 				[_SystemName],
# MAGIC                 [WORKCENTERTYPECODE] AS WORKCENTERTYPENAME
# MAGIC             FROM [I_WORKCENTERTYPE]
# MAGIC             )
# MAGIC             ,WORKCENTERTYPECODEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM WORKCENTERTYPECODEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,WORKCENTERTYPECODETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_WORKCENTERTYPETEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,WORKCENTERTYPECODETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[WORKCENTERTYPECODE], ''''), kl.[WORKCENTERTYPECODE]) AS [WORKCENTERTYPECODE]
# MAGIC                 ,COALESCE(NULLIF(txt.[WORKCENTERTYPENAME], ''''), kl.[WORKCENTERTYPECODE]) AS [WORKCENTERTYPENAME]
# MAGIC             FROM WORKCENTERTYPECODEKeysLanguages kl
# MAGIC             FULL OUTER JOIN WORKCENTERTYPECODETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM WORKCENTERTYPECODETextprefill AS SourceTable
# MAGIC         PIVOT(max([WORKCENTERTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtWORKCENTERTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtFINALCONFIRMATIONTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_FINALCONFIRMATIONTYPE', 'I_FINALCONFIRMATIONTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_FINALCONFIRMATIONTYPE OR I_FINALCONFIRMATIONTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtFINALCONFIRMATIONTYPETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,FINALCONFIRMATIONTYPEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC 				[FINALCONFIRMATIONTYPE],
# MAGIC 				[_SystemName],
# MAGIC                 [FINALCONFIRMATIONTYPE] AS FINALCONFIRMATIONTYPENAME
# MAGIC             FROM [I_FINALCONFIRMATIONTYPE]
# MAGIC             )
# MAGIC             ,FINALCONFIRMATIONTYPEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM FINALCONFIRMATIONTYPEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,FINALCONFIRMATIONTYPETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_FINALCONFIRMATIONTYPETEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,FINALCONFIRMATIONTYPETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[FINALCONFIRMATIONTYPE], ''''), kl.[FINALCONFIRMATIONTYPE]) AS [FINALCONFIRMATIONTYPE]
# MAGIC                 ,COALESCE(NULLIF(txt.[FINALCONFIRMATIONTYPENAME], ''''), kl.[FINALCONFIRMATIONTYPE]) AS [FINALCONFIRMATIONTYPENAME]
# MAGIC             FROM FINALCONFIRMATIONTYPEKeysLanguages kl
# MAGIC             FULL OUTER JOIN FINALCONFIRMATIONTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM FINALCONFIRMATIONTYPETextprefill AS SourceTable
# MAGIC         PIVOT(max([FINALCONFIRMATIONTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtFINALCONFIRMATIONTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtORDERCONFIRMATIONTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_ORDERCONFIRMATIONTYPE', 'I_ORDERCONFIRMATIONTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_ORDERCONFIRMATIONTYPE OR I_ORDERCONFIRMATIONTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtORDERCONFIRMATIONTYPETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,ORDERCONFIRMATIONTYPEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC                 [ORDERCONFIRMATIONTYPE],
# MAGIC 				[_SystemName],
# MAGIC                 [ORDERCONFIRMATIONTYPE] AS ORDERCONFIRMATIONTYPENAME
# MAGIC             FROM [I_ORDERCONFIRMATIONTYPE]
# MAGIC             )
# MAGIC             ,ORDERCONFIRMATIONTYPEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM ORDERCONFIRMATIONTYPEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,ORDERCONFIRMATIONTYPETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_ORDERCONFIRMATIONTYPETEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,ORDERCONFIRMATIONTYPETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[ORDERCONFIRMATIONTYPE], ''''), kl.[ORDERCONFIRMATIONTYPE]) AS [ORDERCONFIRMATIONTYPE]
# MAGIC                 ,COALESCE(NULLIF(txt.[ORDERCONFIRMATIONTYPENAME], ''''), kl.[ORDERCONFIRMATIONTYPE]) AS [ORDERCONFIRMATIONTYPENAME]
# MAGIC             FROM ORDERCONFIRMATIONTYPEKeysLanguages kl
# MAGIC             FULL OUTER JOIN ORDERCONFIRMATIONTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM ORDERCONFIRMATIONTYPETextprefill AS SourceTable
# MAGIC         PIVOT(max([ORDERCONFIRMATIONTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtORDERCONFIRMATIONTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtVARIANCEREASONTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_VARIANCEREASON', 'I_VARIANCEREASONTEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_VARIANCEREASON OR I_VARIANCEREASONTEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtVARIANCEREASONTEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,VARIANCEREASONCODEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC 				[VARIANCEREASONCODE],
# MAGIC 				[_SystemName],
# MAGIC 				[PLANT],
# MAGIC                 [VARIANCEREASONCODE] AS VARIANCEREASONNAME
# MAGIC             FROM [I_VARIANCEREASON]
# MAGIC             )
# MAGIC             ,VARIANCEREASONCODEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM VARIANCEREASONCODEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,VARIANCEREASONCODETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_VARIANCEREASONTEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,VARIANCEREASONCODETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[VARIANCEREASONCODE], ''''), kl.[VARIANCEREASONCODE]) AS [VARIANCEREASONCODE]
# MAGIC                 ,COALESCE(NULLIF(txt.[VARIANCEREASONNAME], ''''), kl.[VARIANCEREASONCODE]) AS [VARIANCEREASONNAME]
# MAGIC             FROM VARIANCEREASONCODEKeysLanguages kl
# MAGIC             FULL OUTER JOIN VARIANCEREASONCODETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM VARIANCEREASONCODETextprefill AS SourceTable
# MAGIC         PIVOT(max([VARIANCEREASONNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtVARIANCEREASONTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtGOODSMOVEMENTTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_GOODSMOVEMENTTYPE', 'I_GOODSMOVEMENTTYPET') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_GOODSMOVEMENTTYPE OR I_GOODSMOVEMENTTYPET does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtGOODSMOVEMENTTYPETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,GOODSMOVEMENTTYPEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC                 [GOODSMOVEMENTTYPE],
# MAGIC 				[_SystemName],
# MAGIC                 [GOODSMOVEMENTTYPE] AS GOODSMOVEMENTTYPENAME
# MAGIC             FROM [I_GOODSMOVEMENTTYPE]
# MAGIC             )
# MAGIC             ,GOODSMOVEMENTTYPEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM GOODSMOVEMENTTYPEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,GOODSMOVEMENTTYPETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_GOODSMOVEMENTTYPET]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,GOODSMOVEMENTTYPETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[GOODSMOVEMENTTYPE], ''''), kl.[GOODSMOVEMENTTYPE]) AS [GOODSMOVEMENTTYPE]
# MAGIC                 ,COALESCE(NULLIF(txt.[GOODSMOVEMENTTYPENAME], ''''), kl.[GOODSMOVEMENTTYPE]) AS [GOODSMOVEMENTTYPENAME]
# MAGIC             FROM GOODSMOVEMENTTYPEKeysLanguages kl
# MAGIC             FULL OUTER JOIN GOODSMOVEMENTTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM GOODSMOVEMENTTYPETextprefill AS SourceTable
# MAGIC         PIVOT(max([GOODSMOVEMENTTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtGOODSMOVEMENTTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtMATERIALREQUIREMENTTYPETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_MATERIALREQUIREMENTTYPE', 'I_MATERIALREQUIREMENTTYPETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_MATERIALREQUIREMENTTYPE OR I_MATERIALREQUIREMENTTYPETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtMATERIALREQUIREMENTTYPETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,REQUIREMENTTYPEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC 				[REQUIREMENTTYPE],
# MAGIC 				[_SystemName],
# MAGIC                 [REQUIREMENTTYPE] AS REQUIREMENTTYPENAME
# MAGIC             FROM [I_MATERIALREQUIREMENTTYPE]
# MAGIC             )
# MAGIC             ,REQUIREMENTTYPEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM REQUIREMENTTYPEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,REQUIREMENTTYPETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_MATERIALREQUIREMENTTYPETEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,REQUIREMENTTYPETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[REQUIREMENTTYPE], ''''), kl.[REQUIREMENTTYPE]) AS [REQUIREMENTTYPE]
# MAGIC                 ,COALESCE(NULLIF(txt.[REQUIREMENTTYPENAME], ''''), kl.[REQUIREMENTTYPE]) AS [REQUIREMENTTYPENAME]
# MAGIC             FROM REQUIREMENTTYPEKeysLanguages kl
# MAGIC             FULL OUTER JOIN REQUIREMENTTYPETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM REQUIREMENTTYPETextprefill AS SourceTable
# MAGIC         PIVOT(max([REQUIREMENTTYPENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtMATERIALREQUIREMENTTYPETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtPRODUCTIONSUPPLYAREATEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_PRODUCTIONSUPPLYAREA', 'I_PRODUCTIONSUPPLYAREATEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_PRODUCTIONSUPPLYAREA OR I_PRODUCTIONSUPPLYAREATEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtPRODUCTIONSUPPLYAREATEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,PRODUCTIONSUPPLYAREAKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key],
# MAGIC 				[PRODUCTIONSUPPLYAREA],
# MAGIC 				[_SystemName],
# MAGIC 				[PLANT],
# MAGIC                 [PRODUCTIONSUPPLYAREA] AS PRODUCTIONSUPPLYAREANAME
# MAGIC             FROM [I_PRODUCTIONSUPPLYAREA]
# MAGIC             )
# MAGIC             ,PRODUCTIONSUPPLYAREAKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM PRODUCTIONSUPPLYAREAKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,PRODUCTIONSUPPLYAREATextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_PRODUCTIONSUPPLYAREATEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,PRODUCTIONSUPPLYAREATextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.[PRODUCTIONSUPPLYAREA], ''''), kl.[PRODUCTIONSUPPLYAREA]) AS [PRODUCTIONSUPPLYAREA]
# MAGIC                 ,COALESCE(NULLIF(txt.[PRODUCTIONSUPPLYAREANAME], ''''), kl.[PRODUCTIONSUPPLYAREA]) AS [PRODUCTIONSUPPLYAREANAME]
# MAGIC             FROM PRODUCTIONSUPPLYAREAKeysLanguages kl
# MAGIC             FULL OUTER JOIN PRODUCTIONSUPPLYAREATextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM PRODUCTIONSUPPLYAREATextprefill AS SourceTable
# MAGIC         PIVOT(max([PRODUCTIONSUPPLYAREANAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtPRODUCTIONSUPPLYAREATEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtACCOUNTINGDOCUMENTCATEGORYTEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_ACCOUNTINGDOCUMENTCATEGORY', 'I_ACCOUNTINGDOCUMENTCATEGORYT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_ACCOUNTINGDOCUMENTCATEGORY OR I_ACCOUNTINGDOCUMENTCATEGORYT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtACCOUNTINGDOCUMENTCATEGORYTEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,ACCOUNTINGDOCUMENTCATEGORYKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key]
# MAGIC                 ,[_SystemName]
# MAGIC                 ,[ACCOUNTINGDOCUMENTCATEGORY]
# MAGIC                 ,[ACCOUNTINGDOCUMENTCATEGORY] AS ACCOUNTINGDOCUMENTCATEGORYNAME
# MAGIC             FROM [I_ACCOUNTINGDOCUMENTCATEGORY]
# MAGIC             )
# MAGIC             ,ACCOUNTINGDOCUMENTCATEGORYKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM ACCOUNTINGDOCUMENTCATEGORYKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,ACCOUNTINGDOCUMENTCATEGORYTextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_ACCOUNTINGDOCUMENTCATEGORYT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,ACCOUNTINGDOCUMENTCATEGORYTextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.ACCOUNTINGDOCUMENTCATEGORY, ''''), kl.ACCOUNTINGDOCUMENTCATEGORY) AS ACCOUNTINGDOCUMENTCATEGORY
# MAGIC                 ,COALESCE(NULLIF(txt.ACCOUNTINGDOCUMENTCATEGORYNAME, ''''), kl.ACCOUNTINGDOCUMENTCATEGORYNAME) AS ACCOUNTINGDOCUMENTCATEGORYNAME
# MAGIC             FROM ACCOUNTINGDOCUMENTCATEGORYKeysLanguages kl
# MAGIC             FULL OUTER JOIN ACCOUNTINGDOCUMENTCATEGORYTextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM ACCOUNTINGDOCUMENTCATEGORYTextprefill AS SourceTable
# MAGIC         PIVOT(max([ACCOUNTINGDOCUMENTCATEGORYNAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtACCOUNTINGDOCUMENTCATEGORYTEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# MARKDOWN ********************

# #### vtSPECIALGLCODETEXT

# CELL ********************

# MAGIC %%tsql -artifact {p_gold_lakehouse_name} -type Lakehouse -session
# MAGIC -- Check for underlying tables before creating the view
# MAGIC DECLARE @TableExists BIT
# MAGIC DECLARE @AllTablesExist BIT = 1
# MAGIC 
# MAGIC -- Check if required tables exist
# MAGIC IF (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SAPLANGUAGE', 'I_SPECIALGLCODE', 'I_SPECIALGLCODETEXT') AND TABLE_SCHEMA = 'dbo') <> 3
# MAGIC BEGIN
# MAGIC     SET @AllTablesExist = 0
# MAGIC     SELECT 'ERROR: Table SAPLANGUAGE OR I_SPECIALGLCODE OR I_SPECIALGLCODETEXT does not exist'
# MAGIC END
# MAGIC 
# MAGIC -- Display missing tables if any
# MAGIC IF @AllTablesExist = 1
# MAGIC BEGIN  
# MAGIC     -- Create the view only if all tables exist
# MAGIC     EXEC('
# MAGIC         CREATE OR ALTER VIEW [dbo].[vtSPECIALGLCODETEXT]
# MAGIC         AS
# MAGIC         WITH Languages
# MAGIC         AS (
# MAGIC             SELECT _ISOLanguage
# MAGIC                 ,[LANGUAGE]
# MAGIC                 ,[LANGUAGENAME]
# MAGIC             FROM SAPLANGUAGE
# MAGIC             WHERE [LANGUAGE] = [LANGUAGECODE] COLLATE Latin1_General_CS_AS
# MAGIC             )
# MAGIC             ,SPECIALGLCODEKeys
# MAGIC         AS (
# MAGIC             SELECT DISTINCT [Key]
# MAGIC                 ,[_SystemName]
# MAGIC                 ,[SPECIALGLCODE]
# MAGIC                 ,[SPECIALGLCODE] AS SPECIALGLCODENAME
# MAGIC             FROM [I_SPECIALGLCODE]
# MAGIC             )
# MAGIC             ,SPECIALGLCODEKeysLanguages
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM SPECIALGLCODEKeys AS keys
# MAGIC             CROSS APPLY Languages AS lang
# MAGIC             )
# MAGIC             ,SPECIALGLCODETextWithoutNull
# MAGIC         AS (
# MAGIC             SELECT *
# MAGIC             FROM [I_SPECIALGLCODETEXT]
# MAGIC             WHERE [Key] IS NOT NULL
# MAGIC             )
# MAGIC             ,SPECIALGLCODETextprefill
# MAGIC         AS (
# MAGIC             SELECT COALESCE(txt.[Key], kl.[Key]) AS [Key]
# MAGIC                 ,COALESCE(txt._SystemName, kl._SystemName) AS _SystemName
# MAGIC                 ,COALESCE(txt._ISOLanguage, kl._ISOLanguage) AS _ISOLanguage
# MAGIC                 ,COALESCE(NULLIF(txt.SPECIALGLCODE, ''''), kl.SPECIALGLCODE) AS SPECIALGLCODE
# MAGIC                 ,COALESCE(NULLIF(txt.SPECIALGLCODELONGNAME, ''''), kl.SPECIALGLCODENAME) AS SPECIALGLCODENAME
# MAGIC             FROM SPECIALGLCODEKeysLanguages kl
# MAGIC             FULL OUTER JOIN SPECIALGLCODETextWithoutNull AS txt ON kl.[Key] = txt.[Key]
# MAGIC                 AND kl.[_ISOLanguage] = txt.[_ISOLanguage]
# MAGIC             )
# MAGIC         SELECT *
# MAGIC         FROM SPECIALGLCODETextprefill AS SourceTable
# MAGIC         PIVOT(max([SPECIALGLCODENAME]) FOR [_ISOLanguage] IN ([ZH], [TH], [KO], [RO], [SL], [HR], [UK], [ET], [AR], [HE], [CA], [CS], [DE], [SH], [EN], [FR], [EL], [HU], [IT], [JA], [DA], [PL], [ZF], [NL], [NO], [PT], [SK], [RU], [ES], [TR], [FI], [SV], [BG], [LT], [LV], [HI], [KK], [VI])) AS PivotTable;
# MAGIC     ')
# MAGIC 
# MAGIC     SELECT 'View [dbo].[vtSPECIALGLCODETEXT] created successfully!'
# MAGIC END


# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

# Execution Summary
success = [r for r in _cell_results if r[1] == 'SUCCESS']
failed  = [r for r in _cell_results if r[1] == 'FAILED']
missing_tables = [r for r in failed if r[2] and r[2].startswith('ERROR:')]

print("=" * 60)
print("NOTEBOOK EXECUTION SUMMARY")
print("=" * 60)
for view_name, status, error in _cell_results:
    icon = "✅" if status == 'SUCCESS' else "❌"
    print(f"{icon}  {view_name}: {status}")
    if error:
        print(f"     Error: {error}")
print("=" * 60)
print(f"Total: {len(_cell_results)}  |  Success: {len(success)}  |  Failed: {len(failed)}  |  Missing Tables: {len(missing_tables)}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
