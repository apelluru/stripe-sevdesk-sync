# ModelContactAddressUpdateCountry

Country of the contact address.<br>      For all countries, send a GET to /StaticCountry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the country | 
**object_name** | **str** | Model name, which is &#39;StaticCountry&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_address_update_country import ModelContactAddressUpdateCountry

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactAddressUpdateCountry from a JSON string
model_contact_address_update_country_instance = ModelContactAddressUpdateCountry.from_json(json)
# print the JSON string representation of the object
print(ModelContactAddressUpdateCountry.to_json())

# convert the object into a dict
model_contact_address_update_country_dict = model_contact_address_update_country_instance.to_dict()
# create an instance of ModelContactAddressUpdateCountry from a dict
model_contact_address_update_country_from_dict = ModelContactAddressUpdateCountry.from_dict(model_contact_address_update_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


