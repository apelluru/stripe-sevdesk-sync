# ModelPartCategory

Category of the part.<br>      For all categories, send a GET to /Category?objectType=Part

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the category | 
**object_name** | **str** | Model name, which is &#39;Category&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_part_category import ModelPartCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPartCategory from a JSON string
model_part_category_instance = ModelPartCategory.from_json(json)
# print the JSON string representation of the object
print(ModelPartCategory.to_json())

# convert the object into a dict
model_part_category_dict = model_part_category_instance.to_dict()
# create an instance of ModelPartCategory from a dict
model_part_category_from_dict = ModelPartCategory.from_dict(model_part_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


