# ModelChangeLayoutResponseMetadatenThumbsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**values** | [**List[ModelChangeLayoutResponseMetadatenThumbsInnerValuesInner]**](ModelChangeLayoutResponseMetadatenThumbsInnerValuesInner.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_change_layout_response_metadaten_thumbs_inner import ModelChangeLayoutResponseMetadatenThumbsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelChangeLayoutResponseMetadatenThumbsInner from a JSON string
model_change_layout_response_metadaten_thumbs_inner_instance = ModelChangeLayoutResponseMetadatenThumbsInner.from_json(json)
# print the JSON string representation of the object
print(ModelChangeLayoutResponseMetadatenThumbsInner.to_json())

# convert the object into a dict
model_change_layout_response_metadaten_thumbs_inner_dict = model_change_layout_response_metadaten_thumbs_inner_instance.to_dict()
# create an instance of ModelChangeLayoutResponseMetadatenThumbsInner from a dict
model_change_layout_response_metadaten_thumbs_inner_from_dict = ModelChangeLayoutResponseMetadatenThumbsInner.from_dict(model_change_layout_response_metadaten_thumbs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


