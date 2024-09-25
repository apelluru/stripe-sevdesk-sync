# ExportInvoiceZip200Response

Response without Download

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**ExportInvoiceZip200ResponseObjects**](ExportInvoiceZip200ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_invoice_zip200_response import ExportInvoiceZip200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExportInvoiceZip200Response from a JSON string
export_invoice_zip200_response_instance = ExportInvoiceZip200Response.from_json(json)
# print the JSON string representation of the object
print(ExportInvoiceZip200Response.to_json())

# convert the object into a dict
export_invoice_zip200_response_dict = export_invoice_zip200_response_instance.to_dict()
# create an instance of ExportInvoiceZip200Response from a dict
export_invoice_zip200_response_from_dict = ExportInvoiceZip200Response.from_dict(export_invoice_zip200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


