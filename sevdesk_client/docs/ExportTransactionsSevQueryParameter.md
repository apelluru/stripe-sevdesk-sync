# ExportTransactionsSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name, which is &#39;CheckAccountTransaction&#39; | 
**object_name** | **object** | Model name, which is &#39;SevQuery&#39; | 
**filter** | [**ExportTransactionsSevQueryParameterFilter**](ExportTransactionsSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_transactions_sev_query_parameter import ExportTransactionsSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportTransactionsSevQueryParameter from a JSON string
export_transactions_sev_query_parameter_instance = ExportTransactionsSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ExportTransactionsSevQueryParameter.to_json())

# convert the object into a dict
export_transactions_sev_query_parameter_dict = export_transactions_sev_query_parameter_instance.to_dict()
# create an instance of ExportTransactionsSevQueryParameter from a dict
export_transactions_sev_query_parameter_from_dict = ExportTransactionsSevQueryParameter.from_dict(export_transactions_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


