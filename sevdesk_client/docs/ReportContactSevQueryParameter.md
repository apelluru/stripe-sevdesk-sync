# ReportContactSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name which is exported | 
**object_name** | **object** | SevQuery object name | 
**filter** | [**ExportContactSevQueryParameterFilter**](ExportContactSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.report_contact_sev_query_parameter import ReportContactSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ReportContactSevQueryParameter from a JSON string
report_contact_sev_query_parameter_instance = ReportContactSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ReportContactSevQueryParameter.to_json())

# convert the object into a dict
report_contact_sev_query_parameter_dict = report_contact_sev_query_parameter_instance.to_dict()
# create an instance of ReportContactSevQueryParameter from a dict
report_contact_sev_query_parameter_from_dict = ReportContactSevQueryParameter.from_dict(report_contact_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


