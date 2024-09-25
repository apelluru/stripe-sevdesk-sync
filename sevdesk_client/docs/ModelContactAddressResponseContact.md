# ModelContactAddressResponseContact

The contact to which this contact address belongs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_address_response_contact import ModelContactAddressResponseContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactAddressResponseContact from a JSON string
model_contact_address_response_contact_instance = ModelContactAddressResponseContact.from_json(json)
# print the JSON string representation of the object
print(ModelContactAddressResponseContact.to_json())

# convert the object into a dict
model_contact_address_response_contact_dict = model_contact_address_response_contact_instance.to_dict()
# create an instance of ModelContactAddressResponseContact from a dict
model_contact_address_response_contact_from_dict = ModelContactAddressResponseContact.from_dict(model_contact_address_response_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


