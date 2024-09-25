# ExportContact200ResponseObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**mimetype** | **str** |  | [optional] 
**base64_encoded** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_contact200_response_objects import ExportContact200ResponseObjects

# TODO update the JSON string below
json = "{}"
# create an instance of ExportContact200ResponseObjects from a JSON string
export_contact200_response_objects_instance = ExportContact200ResponseObjects.from_json(json)
# print the JSON string representation of the object
print(ExportContact200ResponseObjects.to_json())

# convert the object into a dict
export_contact200_response_objects_dict = export_contact200_response_objects_instance.to_dict()
# create an instance of ExportContact200ResponseObjects from a dict
export_contact200_response_objects_from_dict = ExportContact200ResponseObjects.from_dict(export_contact200_response_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


