# Complete workspace item and execution catalog

[Overview](README.md) | [Architecture](01-architecture-and-orchestration.md) | [Notebook details](03-notebook-transformations.md)

This inventory is derived from all 30 root item `.platform` definitions. Logical IDs identify Git items, not credentials. The detailed semantic/report subobjects are cataloged in the dedicated reporting documents; this document covers every top-level item and all engineering notebook/pipeline interfaces.

## 1. All Fabric items

| # | Item directory / definition | Type | Logical ID | Role |
|---:|---|---|---|---|
| 1 | [bps_env_c792846f.Environment](../bps_env_c792846f.Environment/.platform) | Environment | `0aba069f-9427-ae29-43d5-d8ff05f1a1ba` | Shared Spark compute and common_lib wheel |
| 2 | [bps_gold_c792846f.Lakehouse](../bps_gold_c792846f.Lakehouse/.platform) | Lakehouse | `38d97308-b1c7-815a-4a42-7d4318275add` | Gold dimensional/derived Delta tables and SQL presentation |
| 3 | [bps_log_collector_pipeline_c792846f.DataPipeline](../bps_log_collector_pipeline_c792846f.DataPipeline/.platform) | DataPipeline | `4991f28b-e0c7-a195-4ae6-13fa27cbdd7a` | Scheduled log collection |
| 4 | [bps_metadata_db_c792846f.SQLDatabase](../bps_metadata_db_c792846f.SQLDatabase/.platform) | SQLDatabase | `c9571a1c-c878-be58-4a11-51b4a1b72d02` | Metadata control plane, checkpoints and logs |
| 5 | [bps_mirrored_db_MySAP_c792846f.MirroredDatabase](../bps_mirrored_db_MySAP_c792846f.MirroredDatabase/.platform) | MirroredDatabase | `4c66704f-02d8-b86d-4593-119a2e7fbaed` | Generic Delta source/bronze-equivalent landing |
| 6 | [bps_nb_balance_aggregate_customer_c792846f.Notebook](../bps_nb_balance_aggregate_customer_c792846f.Notebook/.platform) | Notebook | `0808d45c-8688-88b5-421d-ef699e2b99c5` | Party balance/carry-forward fact materialization |
| 7 | [bps_nb_balance_aggregate_supplier_c792846f.Notebook](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/.platform) | Notebook | `aea39ff8-2e38-8676-4ca5-28909054b9c7` | Party balance/carry-forward fact materialization |
| 8 | [bps_nb_gold_view_creation_c792846f.Notebook](../bps_nb_gold_view_creation_c792846f.Notebook/.platform) | Notebook | `76906f68-2544-9fe7-4e1d-c12d3163b79b` | 80 SQL endpoint CREATE OR ALTER VIEW cells |
| 9 | [bps_nb_log_collector_c792846f Copy.Notebook](../bps_nb_log_collector_c792846f%20Copy.Notebook/.platform) | Notebook | `8fae9af7-3623-ba5e-49e1-d2c28c083a77` | Unreferenced identical copy of the scheduled log collector |
| 10 | [bps_nb_log_collector_c792846f.Notebook](../bps_nb_log_collector_c792846f.Notebook/.platform) | Notebook | `12300806-ddc8-aab2-448a-e0dfdcb2d5e9` | Delta log discovery and SQL append |
| 11 | [bps_nb_s2g_currency_conversion_c792846f.Notebook](../bps_nb_s2g_currency_conversion_c792846f.Notebook/.platform) | Notebook | `9e52d892-b0e7-a51e-41d9-a7aec04d3369` | Daily and fiscal-period exchange-rate derivation |
| 12 | [bps_nb_s2g_dim_delta_c792846f.Notebook](../bps_nb_s2g_dim_delta_c792846f.Notebook/.platform) | Notebook | `c97e6b46-170d-b72d-4ebc-a96f6fbf50ed` | Metadata-dispatched Gold dimension/text processing |
| 13 | [bps_nb_s2g_dim_nodelta_c792846f.Notebook](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/.platform) | Notebook | `6a4e27e4-4ee4-bf92-4801-0f8525860d00` | Metadata-dispatched Gold dimension/text processing |
| 14 | [bps_nb_s2g_dimtd_delta_c792846f.Notebook](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/.platform) | Notebook | `2476786e-dabb-9bf8-4f26-7005aeb4c589` | Metadata-dispatched Gold dimension/text processing |
| 15 | [bps_nb_s2g_dimtd_nodelta_c792846f.Notebook](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/.platform) | Notebook | `9cd71b65-748a-a3ad-4a7d-d055366c6771` | Metadata-dispatched Gold dimension/text processing |
| 16 | [bps_nb_s2g_fact_c792846f.Notebook](../bps_nb_s2g_fact_c792846f.Notebook/.platform) | Notebook | `84e420ab-e3a5-9e3e-4de7-707f3c132b0e` | Gold fact foreign-key enrichment and late-key repair |
| 17 | [bps_nb_s2g_text_delta_c792846f.Notebook](../bps_nb_s2g_text_delta_c792846f.Notebook/.platform) | Notebook | `3f69af30-7254-a108-4189-7bfe8e1eb3bd` | Metadata-dispatched Gold dimension/text processing |
| 18 | [bps_nb_s2g_text_nodelta_c792846f.Notebook](../bps_nb_s2g_text_nodelta_c792846f.Notebook/.platform) | Notebook | `ffbecfc9-4e10-9411-42cc-069522a5ff45` | Metadata-dispatched Gold dimension/text processing |
| 19 | [bps_om_b2s_dim_processing_c792846f.DataPipeline](../bps_om_b2s_dim_processing_c792846f.DataPipeline/.platform) | DataPipeline | `b31636ac-f4d2-ac7c-40a9-e97f6bfe82b5` | Mirrored source to Silver orchestration |
| 20 | [bps_om_b2s_fact_processing_c792846f.DataPipeline](../bps_om_b2s_fact_processing_c792846f.DataPipeline/.platform) | DataPipeline | `1d71d1eb-fb7b-a39f-4e69-b0b9a28d5a51` | Mirrored source to Silver orchestration |
| 21 | [bps_om_b2s_orchestration_pipeline_c792846f.DataPipeline](../bps_om_b2s_orchestration_pipeline_c792846f.DataPipeline/.platform) | DataPipeline | `f50c0db5-36a0-b7a6-40a2-16f033a8d085` | Mirrored source to Silver orchestration |
| 22 | [bps_opm_nb_b2s_dim_c792846f.Notebook](../bps_opm_nb_b2s_dim_c792846f.Notebook/.platform) | Notebook | `cafab856-b6d9-84a7-41e6-57b4212ebff4` | Mirrored dimension snapshot to Silver |
| 23 | [bps_opm_nb_b2s_fact_c792846f.Notebook](../bps_opm_nb_b2s_fact_c792846f.Notebook/.platform) | Notebook | `f3356016-56c3-931d-4769-fb2970b8f120` | Mirrored fact snapshot/CDF to Silver |
| 24 | [bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline](../bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline/.platform) | DataPipeline | `c8a02dee-fee7-aea2-46dc-735ee7c30922` | Silver to Gold orchestration |
| 25 | [bps_s2g_fact_processing_pipeline_c792846f.DataPipeline](../bps_s2g_fact_processing_pipeline_c792846f.DataPipeline/.platform) | DataPipeline | `2dc14a76-ba1f-bd9a-4a1c-00478acfc89f` | Silver to Gold orchestration |
| 26 | [bps_s2g_full_processing_pipeline_c792846f.DataPipeline](../bps_s2g_full_processing_pipeline_c792846f.DataPipeline/.platform) | DataPipeline | `f7bf5bad-d0b9-9c28-456f-2b414cffaf43` | Silver to Gold orchestration |
| 27 | [bps_silver_c792846f.Lakehouse](../bps_silver_c792846f.Lakehouse/.platform) | Lakehouse | `d687a18f-d055-ad1b-4f6f-aa687c0efad9` | Silver standardized data/logs |
| 28 | [Lakehouse_Sample.Lakehouse](../Lakehouse_Sample.Lakehouse/.platform) | Lakehouse | `b422c5be-d7c7-9f8f-4c56-44af8cf96736` | Sample item; no engineering reference found |
| 29 | [Record_to_Report_Financial_Insights.Report](../Record_to_Report_Financial_Insights.Report/.platform) | Report | `048f2edd-4ba2-b448-4e99-955e2eba4b4c` | Record-to-Report financial reporting UI |
| 30 | [Record_to_Report_Financial_Insights.SemanticModel](../Record_to_Report_Financial_Insights.SemanticModel/.platform) | SemanticModel | `a1acc0f7-3514-b784-480f-d4a1edb8009f` | Financial analytical tables, relationships and DAX |

## 2. Notebook interfaces

Defaults are literal assignments before imports in the exported source; blank values normally require pipeline injection. Currency/view notebook defaults are ordinary cells rather than the usual declared parameter cell. A notebook's existence does not imply it is referenced by a pipeline.

### bps_nb_balance_aggregate_customer_c792846f

- Source: [notebook-content.py](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_guid](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py#L52) | `''` |
| [p_gold_lakehouse_name](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py#L53) | `''` |
| [p_silver_lakehouse_name](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py#L54) | `''` |
| [p_output_table_name](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py#L55) | `'BPS_CUSTOMERBALANCEAGGR'` |
| [p_system_name](../bps_nb_balance_aggregate_customer_c792846f.Notebook/notebook-content.py#L56) | `''` |

### bps_nb_balance_aggregate_supplier_c792846f

- Source: [notebook-content.py](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_guid](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py#L52) | `''` |
| [p_gold_lakehouse_name](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py#L53) | `''` |
| [p_silver_lakehouse_name](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py#L54) | `''` |
| [p_output_table_name](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py#L55) | `'BPS_SUPPLIERBALANCEAGGR'` |
| [p_system_name](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/notebook-content.py#L56) | `''` |

### bps_nb_gold_view_creation_c792846f

- Source: [notebook-content.py](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py).
- Kernel: `jupyter`.
- Default lakehouse name: `bps_gold_c792846f`.
- Environment: `not bound`.

| Input/default variable | Checked-in default |
|---|---|
| [p_gold_lakehouse_name](../bps_nb_gold_view_creation_c792846f.Notebook/notebook-content.py#L30) | `'bps_gold_c792846f'` |

### bps_nb_log_collector_c792846f Copy

- Source: [notebook-content.py](../bps_nb_log_collector_c792846f%20Copy.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_silver_lakehouse_name](../bps_nb_log_collector_c792846f%20Copy.Notebook/notebook-content.py#L37) | `''` |
| [p_metadata_database_name](../bps_nb_log_collector_c792846f%20Copy.Notebook/notebook-content.py#L38) | `''` |

### bps_nb_log_collector_c792846f

- Source: [notebook-content.py](../bps_nb_log_collector_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_silver_lakehouse_name](../bps_nb_log_collector_c792846f.Notebook/notebook-content.py#L37) | `''` |
| [p_metadata_database_name](../bps_nb_log_collector_c792846f.Notebook/notebook-content.py#L38) | `''` |

### bps_nb_s2g_currency_conversion_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_silver_lakehouse_name](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py#L40) | `'bps_silver_c792846f'` |
| [p_gold_lakehouse_name](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py#L41) | `'bps_gold_c792846f'` |
| [p_metadata_database_name](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py#L42) | `'bps_metadata_db_c792846f'` |
| [p_guid](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py#L45) | `''` |
| [p_CDSViewName](../bps_nb_s2g_currency_conversion_c792846f.Notebook/notebook-content.py#L46) | `'I_EXCHANGERATERAWDATA'` |

### bps_nb_s2g_dim_delta_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_lookup_output](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_guid](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_system_name](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_gold_lakehouse_name](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py#L43) | `''` |
| [p_silver_lakehouse_name](../bps_nb_s2g_dim_delta_c792846f.Notebook/notebook-content.py#L44) | `''` |

### bps_nb_s2g_dim_nodelta_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_lookup_output](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_guid](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_system_name](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_gold_lakehouse_name](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/notebook-content.py#L43) | `''` |
| [p_silver_lakehouse_name](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/notebook-content.py#L44) | `''` |

### bps_nb_s2g_dimtd_delta_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_lookup_output](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_guid](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_system_name](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_gold_lakehouse_name](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/notebook-content.py#L43) | `''` |
| [p_silver_lakehouse_name](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/notebook-content.py#L44) | `''` |

### bps_nb_s2g_dimtd_nodelta_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_lookup_output](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_guid](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_system_name](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_gold_lakehouse_name](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/notebook-content.py#L43) | `''` |
| [p_silver_lakehouse_name](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/notebook-content.py#L44) | `''` |

### bps_nb_s2g_fact_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_guid](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_gold_lakehouse_name](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_silver_lakehouse_name](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_CDSViewName](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py#L43) | `''` |
| [p_keyFields](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py#L44) | `''` |
| [p_cubeConfig](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py#L45) | `''` |
| [p_system_name](../bps_nb_s2g_fact_c792846f.Notebook/notebook-content.py#L46) | `''` |

### bps_nb_s2g_text_delta_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_lookup_output](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_guid](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_system_name](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_gold_lakehouse_name](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py#L43) | `''` |
| [p_silver_lakehouse_name](../bps_nb_s2g_text_delta_c792846f.Notebook/notebook-content.py#L44) | `''` |

### bps_nb_s2g_text_nodelta_c792846f

- Source: [notebook-content.py](../bps_nb_s2g_text_nodelta_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_lookup_output](../bps_nb_s2g_text_nodelta_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_guid](../bps_nb_s2g_text_nodelta_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_system_name](../bps_nb_s2g_text_nodelta_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_gold_lakehouse_name](../bps_nb_s2g_text_nodelta_c792846f.Notebook/notebook-content.py#L43) | `''` |
| [p_silver_lakehouse_name](../bps_nb_s2g_text_nodelta_c792846f.Notebook/notebook-content.py#L44) | `''` |

### bps_opm_nb_b2s_dim_c792846f

- Source: [notebook-content.py](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_guid](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_silver_lakehouse_name](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_mirror_db_name](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_sort_dataframe_by_time](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L43) | `'_UpdateTimeStamp'` |
| [p_schema_name](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L44) | `'dbo'` |
| [p_source_type](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L45) | `'open-mirroring'` |
| [p_CDSViewName](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L46) | `''` |
| [p_keyFields](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L47) | `''` |
| [p_ODPName](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L48) | `''` |
| [p_system_name](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L49) | `''` |
| [p_mirror_db_workspace_id](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L50) | `''` |
| [p_schema_table_name](../bps_opm_nb_b2s_dim_c792846f.Notebook/notebook-content.py#L51) | `''` |

### bps_opm_nb_b2s_fact_c792846f

- Source: [notebook-content.py](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py).
- Kernel: `synapse_pyspark`.
- Default lakehouse name: `bps_silver_c792846f`.
- Environment: `0aba069f-9427-ae29-43d5-d8ff05f1a1ba`.

| Input/default variable | Checked-in default |
|---|---|
| [p_guid](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L40) | `''` |
| [p_silver_lakehouse_name](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L41) | `''` |
| [p_mirror_db_name](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L42) | `''` |
| [p_source_type](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L43) | `'open-mirroring'` |
| [p_schema_name](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L44) | `'dbo'` |
| [p_sort_dataframe_by_time](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L45) | `'_UpdateTimeStamp'` |
| [p_CDSViewName](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L46) | `''` |
| [p_keyFields](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L47) | `''` |
| [p_ODPName](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L48) | `''` |
| [p_system_name](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L49) | `''` |
| [p_mirror_db_workspace_id](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L50) | `''` |
| [p_schema_table_name](../bps_opm_nb_b2s_fact_c792846f.Notebook/notebook-content.py#L51) | `''` |

## 3. All pipeline activities and item references

The dependency column lists explicit same-container `dependsOn` edges; a child of ForEach/If also depends on its parent container being entered. Empty dependencies do not mean the child is a top-level independent activity.

### bps_log_collector_pipeline_c792846f

Source: [pipeline-content.json](../bps_log_collector_pipeline_c792846f.DataPipeline/pipeline-content.json).

Parameters: none.

| Activity path | Type | Explicit dependency | Bound item / control |
|---|---|---|---|
| Log Collector Notebook | TridentNotebook | none | [bps_nb_log_collector_c792846f](../bps_nb_log_collector_c792846f.Notebook/.platform) |

### bps_om_b2s_dim_processing_c792846f

Source: [pipeline-content.json](../bps_om_b2s_dim_processing_c792846f.DataPipeline/pipeline-content.json).

Parameters: `Mirror_Database_Name` (string, required); `Silver_Lakehouse_Name` (string, default `bps_silver_c792846f`); `System_Name` (string, required); `CdsViewNames` (string, default ` `); `Schema_Table_Name` (string, required); `Schema_Name` (string, required).

| Activity path | Type | Explicit dependency | Bound item / control |
|---|---|---|---|
| Get Dimension Tables | Lookup | none | Metadata SQL lookup |
| For Each Dimension Table | ForEach | Get Dimension Tables (Succeeded); GUID (Succeeded) | Parallel, batchCount=6 |
| For Each Dimension Table / Run Dimension B2S Processing | TridentNotebook | none | [bps_opm_nb_b2s_dim_c792846f](../bps_opm_nb_b2s_dim_c792846f.Notebook/.platform) |
| GUID | SetVariable | none | `v_guid` |

### bps_om_b2s_fact_processing_c792846f

Source: [pipeline-content.json](../bps_om_b2s_fact_processing_c792846f.DataPipeline/pipeline-content.json).

Parameters: `Silver_Lakehouse_Name` (string, default `bps_silver_c792846f`); `Mirror_Database_Name` (string, required); `System_Name` (string, required); `CdsViewNames` (string, default ` `); `Schema_Table_Name` (string, required); `Schema_Name` (string, required).

| Activity path | Type | Explicit dependency | Bound item / control |
|---|---|---|---|
| Get Fact Tables | Lookup | none | Metadata SQL lookup |
| For Each Fact Table | ForEach | Get Fact Tables (Succeeded); GUID (Succeeded) | Parallel, batchCount=3 |
| For Each Fact Table / Run Fact B2S Processing | TridentNotebook | none | [bps_opm_nb_b2s_fact_c792846f](../bps_opm_nb_b2s_fact_c792846f.Notebook/.platform) |
| GUID | SetVariable | none | `v_guid` |

### bps_om_b2s_orchestration_pipeline_c792846f

Source: [pipeline-content.json](../bps_om_b2s_orchestration_pipeline_c792846f.DataPipeline/pipeline-content.json).

Parameters: `Silver_Lakehouse_Name` (string, default `bps_silver_c792846f`); `CdsViewNames` (string, default ` `); `Schema_Table_Name` (string, default `DD03ND`).

| Activity path | Type | Explicit dependency | Bound item / control |
|---|---|---|---|
| Get Open Mirror System Details | Lookup | none | Metadata SQL lookup |
| For each system | ForEach | Get Open Mirror System Details (Succeeded) | Sequential |
| For each system / B2S Dimension Processing | ExecutePipeline | none | [bps_om_b2s_dim_processing_c792846f](../bps_om_b2s_dim_processing_c792846f.DataPipeline/.platform) |
| For each system / B2S Fact Processing | ExecutePipeline | B2S Dimension Processing (Succeeded) | [bps_om_b2s_fact_processing_c792846f](../bps_om_b2s_fact_processing_c792846f.DataPipeline/.platform) |

### bps_s2g_dimension_processing_pipeline_c792846f

Source: [pipeline-content.json](../bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

Parameters: `CdsViewNames` (string, default ` `); `p_system_name` (string, required); `p_guid` (string, required); `p_gold_lakehouse_name` (string, default `bps_gold_c792846f`); `p_silver_lakehouse_name` (string, default `bps_silver_c792846f`).

| Activity path | Type | Explicit dependency | Bound item / control |
|---|---|---|---|
| Get Dimension Delta Tables | Lookup | none | Metadata SQL lookup |
| S2G Dim Delta | TridentNotebook | Get Dimension Delta Tables (Succeeded) | [bps_nb_s2g_dim_delta_c792846f](../bps_nb_s2g_dim_delta_c792846f.Notebook/.platform) |
| Get Dimension Non-Delta Tables | Lookup | S2G Dim Delta (Succeeded) | Metadata SQL lookup |
| S2G Dim No Delta | TridentNotebook | Get Dimension Non-Delta Tables (Succeeded) | [bps_nb_s2g_dim_nodelta_c792846f](../bps_nb_s2g_dim_nodelta_c792846f.Notebook/.platform) |
| Get Dimension-TD Delta Tables | Lookup | S2G Dim No Delta (Succeeded) | Metadata SQL lookup |
| S2G Dim TD Delta | TridentNotebook | Get Dimension-TD Delta Tables (Succeeded) | [bps_nb_s2g_dimtd_delta_c792846f](../bps_nb_s2g_dimtd_delta_c792846f.Notebook/.platform) |
| Get Dimension-TD Non-Delta Tables | Lookup | S2G Dim TD Delta (Succeeded) | Metadata SQL lookup |
| S2G Dim TD No Delta | TridentNotebook | Get Dimension-TD Non-Delta Tables (Succeeded) | [bps_nb_s2g_dimtd_nodelta_c792846f](../bps_nb_s2g_dimtd_nodelta_c792846f.Notebook/.platform) |
| Get Text Dimension Delta Tables | Lookup | S2G Dim TD No Delta (Succeeded) | Metadata SQL lookup |
| S2G Text Delta | TridentNotebook | Get Text Dimension Delta Tables (Succeeded) | [bps_nb_s2g_text_delta_c792846f](../bps_nb_s2g_text_delta_c792846f.Notebook/.platform) |
| Get Text Dimension Non-Delta Tables | Lookup | S2G Text Delta (Succeeded) | Metadata SQL lookup |
| S2G Text No Delta | TridentNotebook | Get Text Dimension Non-Delta Tables (Succeeded) | [bps_nb_s2g_text_nodelta_c792846f](../bps_nb_s2g_text_nodelta_c792846f.Notebook/.platform) |
| If Condition1 | IfCondition | Get Exchange Table (Succeeded) | `@equals(activity('Get Exchange Table').output.firstRow.value, 1)` |
| If Condition1 [true] / Currency Conversion | TridentNotebook | none | [bps_nb_s2g_currency_conversion_c792846f](../bps_nb_s2g_currency_conversion_c792846f.Notebook/.platform) |
| Get Exchange Table | Lookup | S2G Text No Delta (Succeeded) | Metadata SQL lookup |

### bps_s2g_fact_processing_pipeline_c792846f

Source: [pipeline-content.json](../bps_s2g_fact_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

Parameters: `CdsViewNames` (string, default ` `); `p_system_name` (string, required); `p_guid` (string, default `Fact-2026-01-01`); `p_gold_lakehouse_name` (string, default `bps_gold_c792846f`); `p_silver_lakehouse_name` (string, default `bps_silver_c792846f`).

| Activity path | Type | Explicit dependency | Bound item / control |
|---|---|---|---|
| Get Fact Tables | Lookup | none | Metadata SQL lookup |
| ForEach Fact | ForEach | Get Fact Tables (Succeeded) | Sequential |
| ForEach Fact / Get key fields | Lookup | none | Metadata SQL lookup |
| ForEach Fact / Get relationships | Lookup | none | Metadata SQL lookup |
| ForEach Fact / Set Keyfields | SetVariable | Get key fields (Succeeded) | `Keyfields` |
| ForEach Fact / Set Cubeconfig | SetVariable | Get relationships (Succeeded) | `Cubeconfig` |
| ForEach Fact / Process Fact table | TridentNotebook | Set Cubeconfig (Succeeded); Set Keyfields (Succeeded) | [bps_nb_s2g_fact_c792846f](../bps_nb_s2g_fact_c792846f.Notebook/.platform) |
| Finance Aggregate notebooks | IfCondition | ForEach Fact (Succeeded) | `@contains(string(activity('Get Fact Tables').output.value), 'I_OPERATIONALACCTGDOCITEM')` |
| Finance Aggregate notebooks [true] / Customer Balance Aggregate | TridentNotebook | none | [bps_nb_balance_aggregate_customer_c792846f](../bps_nb_balance_aggregate_customer_c792846f.Notebook/.platform) |
| Finance Aggregate notebooks [true] / Supplier Balance Aggregate | TridentNotebook | Customer Balance Aggregate (Succeeded) | [bps_nb_balance_aggregate_supplier_c792846f](../bps_nb_balance_aggregate_supplier_c792846f.Notebook/.platform) |

### bps_s2g_full_processing_pipeline_c792846f

Source: [pipeline-content.json](../bps_s2g_full_processing_pipeline_c792846f.DataPipeline/pipeline-content.json).

Parameters: `p_gold_lakehouse_name` (string, default `bps_gold_c792846f`); `p_silver_lakehouse_name` (string, default `bps_silver_c792846f`); `CDSViewNames` (string, default ` `).

| Activity path | Type | Explicit dependency | Bound item / control |
|---|---|---|---|
| Get System Details | Lookup | Set GUID (Succeeded) | Metadata SQL lookup |
| For each source system | ForEach | Get System Details (Succeeded) | Sequential |
| For each source system / Run Dimension Processing | ExecutePipeline | none | [bps_s2g_dimension_processing_pipeline_c792846f](../bps_s2g_dimension_processing_pipeline_c792846f.DataPipeline/.platform) |
| For each source system / Run Fact Processing | ExecutePipeline | Run Dimension Processing (Succeeded) | [bps_s2g_fact_processing_pipeline_c792846f](../bps_s2g_fact_processing_pipeline_c792846f.DataPipeline/.platform) |
| Set GUID | SetVariable | none | `v_guid` |
| Create Views in Gold Lakehouse | TridentNotebook | For each source system (Succeeded) | [bps_nb_gold_view_creation_c792846f](../bps_nb_gold_view_creation_c792846f.Notebook/.platform) |

Total recursively enumerated activities: **44**. All notebook and child-pipeline item IDs resolve to included `.platform` definitions. This does not validate external connection IDs or concrete lakehouse runtime bindings.

## 4. Metadata SQL object coverage

| Object | Kind | Source |
|---|---|---|
| `AdfExtractionCheckpoint` | Table | [AdfExtractionCheckpoint.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/AdfExtractionCheckpoint.sql) |
| `cubeMetadata` | Table | [cubeMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/cubeMetadata.sql) |
| `Ecc_column_mapping` | Table | [Ecc_column_mapping.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/Ecc_column_mapping.sql) |
| `Ecc_Table_Checkpoint` | Table | [Ecc_Table_Checkpoint.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/Ecc_Table_Checkpoint.sql) |
| `ExtractionLogs` | Table | [ExtractionLogs.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/ExtractionLogs.sql) |
| `extractionScope` | Table | [extractionScope.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/extractionScope.sql) |
| `extractionScopeByDataset` | Table | [extractionScopeByDataset.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/extractionScopeByDataset.sql) |
| `fieldMetadata` | Table | [fieldMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/fieldMetadata.sql) |
| `log_events` | Table | [log_events.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/log_events.sql) |
| `OrchestrationLogs` | Table | [OrchestrationLogs.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/OrchestrationLogs.sql) |
| `SalesforceTableCheckpoint` | Table | [SalesforceTableCheckpoint.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/SalesforceTableCheckpoint.sql) |
| `systemDetails` | Table | [systemDetails.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/systemDetails.sql) |
| `VersionDetails` | Table | [VersionDetails.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/VersionDetails.sql) |
| `viewMetadata` | Table | [viewMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Tables/viewMetadata.sql) |
| `extractionMetadata` | View | [extractionMetadata.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/Views/extractionMetadata.sql) |
| `GenerateSelectQueriesBySalesforceSystem` | Procedure | [GenerateSelectQueriesBySalesforceSystem.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/GenerateSelectQueriesBySalesforceSystem.sql) |
| `GetCheckpointId` | Procedure | [GetCheckpointId.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/GetCheckpointId.sql) |
| `GetMaxSystemModStamp` | Procedure | [GetMaxSystemModStamp.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/GetMaxSystemModStamp.sql) |
| `InsertExtractionLogs` | Procedure | [InsertExtractionLogs.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/InsertExtractionLogs.sql) |
| `InsertOrchestrationLogs` | Procedure | [InsertOrchestrationLogs.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/InsertOrchestrationLogs.sql) |
| `UpdateVersionDetails` | Procedure | [UpdateVersionDetails.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/UpdateVersionDetails.sql) |
| `Upsert_Ecc_Table_Checkpoint` | Procedure | [Upsert_Ecc_Table_Checkpoint.sql](../bps_metadata_db_c792846f.SQLDatabase/dbo/StoredProcedures/Upsert_Ecc_Table_Checkpoint.sql) |

## 5. Support-file coverage and interpretation

- Every Fabric item includes a `.platform` identity definition.
- All seven pipelines include activity content; the three top-level scheduled pipelines also include `.schedules`.
- Each lakehouse includes ALM settings, default-schema metadata and an empty shortcut list. Table data and SQL endpoint contents are not exported by those files.
- The mirror includes mirroring.json. It declares GenericMirror/CDF/Delta settings, not an upstream SAP publisher implementation.
- The Environment includes Sparkcompute.yml and the wheel. The wheel contains six common_lib Python modules plus standard package METADATA, WHEEL, top_level.txt and RECORD. No runtime installation was performed for this analysis.
- The SQL database includes its SQL project and a standard development .gitignore in addition to the 22 SQL definitions.
- The semantic model includes PBISM/TMDL configuration, culture, expressions, relationships and table definitions. See the model document.
- The report includes PBIR/report/page/visual definitions, bookmark and resource definitions, a theme and an embedded image. See the report object catalog.
- The original root README contains only the repository title.
