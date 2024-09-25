# ModelInvoiceResponseAddressCountry

Can be omitted as complete address is defined in address attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the country | 
**object_name** | **str** | Model name, which is &#39;StaticCountry&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_response_address_country import ModelInvoiceResponseAddressCountry

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoiceResponseAddressCountry from a JSON string
model_invoice_response_address_country_instance = ModelInvoiceResponseAddressCountry.from_json(json)
# print the JSON string representation of the object
print(ModelInvoiceResponseAddressCountry.to_json())

# convert the object into a dict
model_invoice_response_address_country_dict = model_invoice_response_address_country_instance.to_dict()
# create an instance of ModelInvoiceResponseAddressCountry from a dict
model_invoice_response_address_country_from_dict = ModelInvoiceResponseAddressCountry.from_dict(model_invoice_response_address_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


