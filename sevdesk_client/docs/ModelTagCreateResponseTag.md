# ModelTagCreateResponseTag

The tag information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the tag | 
**object_name** | **str** | Model name, which is &#39;Tag&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_tag_create_response_tag import ModelTagCreateResponseTag

# TODO update the JSON string below
json = "{}"
# create an instance of ModelTagCreateResponseTag from a JSON string
model_tag_create_response_tag_instance = ModelTagCreateResponseTag.from_json(json)
# print the JSON string representation of the object
print(ModelTagCreateResponseTag.to_json())

# convert the object into a dict
model_tag_create_response_tag_dict = model_tag_create_response_tag_instance.to_dict()
# create an instance of ModelTagCreateResponseTag from a dict
model_tag_create_response_tag_from_dict = ModelTagCreateResponseTag.from_dict(model_tag_create_response_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


