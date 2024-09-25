# ModelContactCategory

Category of the contact.<br> For more information,       see <a href='https://my.sevdesk.de/apiOverview/index.html#/doc-contacts#types'>here</a>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the category | 
**object_name** | **str** | Model name, which is &#39;Category&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_category import ModelContactCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCategory from a JSON string
model_contact_category_instance = ModelContactCategory.from_json(json)
# print the JSON string representation of the object
print(ModelContactCategory.to_json())

# convert the object into a dict
model_contact_category_dict = model_contact_category_instance.to_dict()
# create an instance of ModelContactCategory from a dict
model_contact_category_from_dict = ModelContactCategory.from_dict(model_contact_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


