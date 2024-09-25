# ExportContactSevQueryParameterFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zip** | **int** | filters the contacts by zip code | [optional] 
**city** | **str** | filters the contacts by city | [optional] 
**country** | [**ExportContactSevQueryParameterFilterCountry**](ExportContactSevQueryParameterFilterCountry.md) |  | [optional] 
**depth** | **bool** | export only organisations | [optional] 
**only_people** | **bool** | export only people | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_contact_sev_query_parameter_filter import ExportContactSevQueryParameterFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportContactSevQueryParameterFilter from a JSON string
export_contact_sev_query_parameter_filter_instance = ExportContactSevQueryParameterFilter.from_json(json)
# print the JSON string representation of the object
print(ExportContactSevQueryParameterFilter.to_json())

# convert the object into a dict
export_contact_sev_query_parameter_filter_dict = export_contact_sev_query_parameter_filter_instance.to_dict()
# create an instance of ExportContactSevQueryParameterFilter from a dict
export_contact_sev_query_parameter_filter_from_dict = ExportContactSevQueryParameterFilter.from_dict(export_contact_sev_query_parameter_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


