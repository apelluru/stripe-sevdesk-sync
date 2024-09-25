# ModelContactResponseParent

The parent contact to which this contact belongs. Must be an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the parent contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_response_parent import ModelContactResponseParent

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactResponseParent from a JSON string
model_contact_response_parent_instance = ModelContactResponseParent.from_json(json)
# print the JSON string representation of the object
print(ModelContactResponseParent.to_json())

# convert the object into a dict
model_contact_response_parent_dict = model_contact_response_parent_instance.to_dict()
# create an instance of ModelContactResponseParent from a dict
model_contact_response_parent_from_dict = ModelContactResponseParent.from_dict(model_contact_response_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


