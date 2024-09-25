# ModelContactCustomFieldResponseContact

name of the contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_custom_field_response_contact import ModelContactCustomFieldResponseContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCustomFieldResponseContact from a JSON string
model_contact_custom_field_response_contact_instance = ModelContactCustomFieldResponseContact.from_json(json)
# print the JSON string representation of the object
print(ModelContactCustomFieldResponseContact.to_json())

# convert the object into a dict
model_contact_custom_field_response_contact_dict = model_contact_custom_field_response_contact_instance.to_dict()
# create an instance of ModelContactCustomFieldResponseContact from a dict
model_contact_custom_field_response_contact_from_dict = ModelContactCustomFieldResponseContact.from_dict(model_contact_custom_field_response_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


