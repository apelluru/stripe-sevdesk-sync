# ModelContactAddressResponse

ContactAddress model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The contact address id | [optional] [readonly] 
**object_name** | **str** | The contact address object name | [optional] [readonly] 
**create** | **datetime** | Date of contact address creation | [optional] [readonly] 
**update** | **datetime** | Date of last contact address update | [optional] [readonly] 
**contact** | [**ModelContactAddressResponseContact**](ModelContactAddressResponseContact.md) |  | 
**street** | **str** | Street name | [optional] 
**zip** | **str** | Zib code | [optional] 
**city** | **str** | City name | [optional] 
**country** | [**ModelContactAddressResponseCountry**](ModelContactAddressResponseCountry.md) |  | 
**category** | [**ModelContactAddressResponseCategory**](ModelContactAddressResponseCategory.md) |  | [optional] 
**name** | **str** | Name in address | [optional] 
**sev_client** | [**ModelContactAddressResponseSevClient**](ModelContactAddressResponseSevClient.md) |  | [optional] 
**name2** | **str** | Second name in address | [optional] 
**name3** | **str** | Third name in address | [optional] 
**name4** | **str** | Fourth name in address | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_address_response import ModelContactAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactAddressResponse from a JSON string
model_contact_address_response_instance = ModelContactAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ModelContactAddressResponse.to_json())

# convert the object into a dict
model_contact_address_response_dict = model_contact_address_response_instance.to_dict()
# create an instance of ModelContactAddressResponse from a dict
model_contact_address_response_from_dict = ModelContactAddressResponse.from_dict(model_contact_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


