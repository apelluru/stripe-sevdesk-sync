# ExportContact200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**ExportContact200ResponseObjects**](ExportContact200ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_contact200_response import ExportContact200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExportContact200Response from a JSON string
export_contact200_response_instance = ExportContact200Response.from_json(json)
# print the JSON string representation of the object
print(ExportContact200Response.to_json())

# convert the object into a dict
export_contact200_response_dict = export_contact200_response_instance.to_dict()
# create an instance of ExportContact200Response from a dict
export_contact200_response_from_dict = ExportContact200Response.from_dict(export_contact200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


