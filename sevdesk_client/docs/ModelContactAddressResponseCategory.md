# ModelContactAddressResponseCategory

Category of the contact address.<br>       For all categories, send a GET to /Category?objectType=ContactAddress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the category | 
**object_name** | **str** | Model name, which is &#39;Category&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_address_response_category import ModelContactAddressResponseCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactAddressResponseCategory from a JSON string
model_contact_address_response_category_instance = ModelContactAddressResponseCategory.from_json(json)
# print the JSON string representation of the object
print(ModelContactAddressResponseCategory.to_json())

# convert the object into a dict
model_contact_address_response_category_dict = model_contact_address_response_category_instance.to_dict()
# create an instance of ModelContactAddressResponseCategory from a dict
model_contact_address_response_category_from_dict = ModelContactAddressResponseCategory.from_dict(model_contact_address_response_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


