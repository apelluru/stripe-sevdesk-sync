# ModelContactUpdateParent

The parent contact to which this contact belongs. Must be an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the parent contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_update_parent import ModelContactUpdateParent

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactUpdateParent from a JSON string
model_contact_update_parent_instance = ModelContactUpdateParent.from_json(json)
# print the JSON string representation of the object
print(ModelContactUpdateParent.to_json())

# convert the object into a dict
model_contact_update_parent_dict = model_contact_update_parent_instance.to_dict()
# create an instance of ModelContactUpdateParent from a dict
model_contact_update_parent_from_dict = ModelContactUpdateParent.from_dict(model_contact_update_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


