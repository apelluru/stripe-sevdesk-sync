# ModelContactAddressUpdateContact

The contact to which this contact address belongs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_address_update_contact import ModelContactAddressUpdateContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactAddressUpdateContact from a JSON string
model_contact_address_update_contact_instance = ModelContactAddressUpdateContact.from_json(json)
# print the JSON string representation of the object
print(ModelContactAddressUpdateContact.to_json())

# convert the object into a dict
model_contact_address_update_contact_dict = model_contact_address_update_contact_instance.to_dict()
# create an instance of ModelContactAddressUpdateContact from a dict
model_contact_address_update_contact_from_dict = ModelContactAddressUpdateContact.from_dict(model_contact_address_update_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


