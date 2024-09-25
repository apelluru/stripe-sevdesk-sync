# ModelContactAddressUpdate

ContactAddress model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ModelContactAddressUpdateContact**](ModelContactAddressUpdateContact.md) |  | [optional] 
**street** | **str** | Street name | [optional] 
**zip** | **str** | Zib code | [optional] 
**city** | **str** | City name | [optional] 
**country** | [**ModelContactAddressUpdateCountry**](ModelContactAddressUpdateCountry.md) |  | [optional] 
**category** | [**ModelContactAddressResponseCategory**](ModelContactAddressResponseCategory.md) |  | [optional] 
**name** | **str** | Name in address | [optional] 
**name2** | **str** | Second name in address | [optional] 
**name3** | **str** | Third name in address | [optional] 
**name4** | **str** | Fourth name in address | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_address_update import ModelContactAddressUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactAddressUpdate from a JSON string
model_contact_address_update_instance = ModelContactAddressUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelContactAddressUpdate.to_json())

# convert the object into a dict
model_contact_address_update_dict = model_contact_address_update_instance.to_dict()
# create an instance of ModelContactAddressUpdate from a dict
model_contact_address_update_from_dict = ModelContactAddressUpdate.from_dict(model_contact_address_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


