# ModelTagResponse

tag model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the tag | [optional] [readonly] 
**object_name** | **str** | Internal object name which is &#39;Tag&#39;. | [optional] [readonly] 
**additional_information** | **str** |  | [optional] 
**create** | **datetime** | Date of tag creation | [optional] [readonly] 
**name** | **str** | name of the tag | [optional] [readonly] 
**sev_client** | [**ModelTagResponseSevClient**](ModelTagResponseSevClient.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_tag_response import ModelTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelTagResponse from a JSON string
model_tag_response_instance = ModelTagResponse.from_json(json)
# print the JSON string representation of the object
print(ModelTagResponse.to_json())

# convert the object into a dict
model_tag_response_dict = model_tag_response_instance.to_dict()
# create an instance of ModelTagResponse from a dict
model_tag_response_from_dict = ModelTagResponse.from_dict(model_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


