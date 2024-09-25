# GetTagRelations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelTagCreateResponse]**](ModelTagCreateResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_tag_relations200_response import GetTagRelations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagRelations200Response from a JSON string
get_tag_relations200_response_instance = GetTagRelations200Response.from_json(json)
# print the JSON string representation of the object
print(GetTagRelations200Response.to_json())

# convert the object into a dict
get_tag_relations200_response_dict = get_tag_relations200_response_instance.to_dict()
# create an instance of GetTagRelations200Response from a dict
get_tag_relations200_response_from_dict = GetTagRelations200Response.from_dict(get_tag_relations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


