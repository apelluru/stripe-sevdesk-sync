# InvoiceGetPdf200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**base64encoded** | **bool** |  | [optional] 
**content** | **bytearray** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.invoice_get_pdf200_response import InvoiceGetPdf200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGetPdf200Response from a JSON string
invoice_get_pdf200_response_instance = InvoiceGetPdf200Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceGetPdf200Response.to_json())

# convert the object into a dict
invoice_get_pdf200_response_dict = invoice_get_pdf200_response_instance.to_dict()
# create an instance of InvoiceGetPdf200Response from a dict
invoice_get_pdf200_response_from_dict = InvoiceGetPdf200Response.from_dict(invoice_get_pdf200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


