# ModelOrderAddressCountry

Can be omitted as complete address is defined in address attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the country | 
**object_name** | **str** | Model name, which is &#39;StaticCountry&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_address_country import ModelOrderAddressCountry

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderAddressCountry from a JSON string
model_order_address_country_instance = ModelOrderAddressCountry.from_json(json)
# print the JSON string representation of the object
print(ModelOrderAddressCountry.to_json())

# convert the object into a dict
model_order_address_country_dict = model_order_address_country_instance.to_dict()
# create an instance of ModelOrderAddressCountry from a dict
model_order_address_country_from_dict = ModelOrderAddressCountry.from_dict(model_order_address_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


