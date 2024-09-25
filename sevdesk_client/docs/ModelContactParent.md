# ModelContactParent

The parent contact to which this contact belongs. Must be an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the parent contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_parent import ModelContactParent

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactParent from a JSON string
model_contact_parent_instance = ModelContactParent.from_json(json)
# print the JSON string representation of the object
print(ModelContactParent.to_json())

# convert the object into a dict
model_contact_parent_dict = model_contact_parent_instance.to_dict()
# create an instance of ModelContactParent from a dict
model_contact_parent_from_dict = ModelContactParent.from_dict(model_contact_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


