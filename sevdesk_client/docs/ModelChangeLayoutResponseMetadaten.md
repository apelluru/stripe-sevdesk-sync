# ModelChangeLayoutResponseMetadaten


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | **int** | the number of pages in the document | [optional] 
**doc_id** | **str** | the id of the document | [optional] [readonly] 
**thumbs** | [**List[ModelChangeLayoutResponseMetadatenThumbsInner]**](ModelChangeLayoutResponseMetadatenThumbsInner.md) | the pdf file | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_change_layout_response_metadaten import ModelChangeLayoutResponseMetadaten

# TODO update the JSON string below
json = "{}"
# create an instance of ModelChangeLayoutResponseMetadaten from a JSON string
model_change_layout_response_metadaten_instance = ModelChangeLayoutResponseMetadaten.from_json(json)
# print the JSON string representation of the object
print(ModelChangeLayoutResponseMetadaten.to_json())

# convert the object into a dict
model_change_layout_response_metadaten_dict = model_change_layout_response_metadaten_instance.to_dict()
# create an instance of ModelChangeLayoutResponseMetadaten from a dict
model_change_layout_response_metadaten_from_dict = ModelChangeLayoutResponseMetadaten.from_dict(model_change_layout_response_metadaten_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


