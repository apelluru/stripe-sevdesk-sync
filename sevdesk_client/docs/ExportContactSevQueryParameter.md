# ExportContactSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name, which is &#39;Contact&#39; | 
**object_name** | **object** | Model name, which is &#39;SevQuery&#39; | 
**filter** | [**ExportContactSevQueryParameterFilter**](ExportContactSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_contact_sev_query_parameter import ExportContactSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportContactSevQueryParameter from a JSON string
export_contact_sev_query_parameter_instance = ExportContactSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ExportContactSevQueryParameter.to_json())

# convert the object into a dict
export_contact_sev_query_parameter_dict = export_contact_sev_query_parameter_instance.to_dict()
# create an instance of ExportContactSevQueryParameter from a dict
export_contact_sev_query_parameter_from_dict = ExportContactSevQueryParameter.from_dict(export_contact_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


