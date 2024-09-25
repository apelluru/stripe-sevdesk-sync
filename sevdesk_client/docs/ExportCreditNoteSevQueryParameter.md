# ExportCreditNoteSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name, which is &#39;CreditNote&#39; | 
**object_name** | **object** | Model name, which is &#39;SevQuery&#39; | 
**filter** | [**ExportCreditNoteSevQueryParameterFilter**](ExportCreditNoteSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_credit_note_sev_query_parameter import ExportCreditNoteSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCreditNoteSevQueryParameter from a JSON string
export_credit_note_sev_query_parameter_instance = ExportCreditNoteSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ExportCreditNoteSevQueryParameter.to_json())

# convert the object into a dict
export_credit_note_sev_query_parameter_dict = export_credit_note_sev_query_parameter_instance.to_dict()
# create an instance of ExportCreditNoteSevQueryParameter from a dict
export_credit_note_sev_query_parameter_from_dict = ExportCreditNoteSevQueryParameter.from_dict(export_credit_note_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


