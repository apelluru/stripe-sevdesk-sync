# ModelChangeLayoutResponse

Layout model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**metadaten** | [**ModelChangeLayoutResponseMetadaten**](ModelChangeLayoutResponseMetadaten.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_change_layout_response import ModelChangeLayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelChangeLayoutResponse from a JSON string
model_change_layout_response_instance = ModelChangeLayoutResponse.from_json(json)
# print the JSON string representation of the object
print(ModelChangeLayoutResponse.to_json())

# convert the object into a dict
model_change_layout_response_dict = model_change_layout_response_instance.to_dict()
# create an instance of ModelChangeLayoutResponse from a dict
model_change_layout_response_from_dict = ModelChangeLayoutResponse.from_dict(model_change_layout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


