# InvoiceResetToOpen200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**InvoiceResetToOpen200ResponseObjects**](InvoiceResetToOpen200ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.invoice_reset_to_open200_response import InvoiceResetToOpen200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceResetToOpen200Response from a JSON string
invoice_reset_to_open200_response_instance = InvoiceResetToOpen200Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceResetToOpen200Response.to_json())

# convert the object into a dict
invoice_reset_to_open200_response_dict = invoice_reset_to_open200_response_instance.to_dict()
# create an instance of InvoiceResetToOpen200Response from a dict
invoice_reset_to_open200_response_from_dict = InvoiceResetToOpen200Response.from_dict(invoice_reset_to_open200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


