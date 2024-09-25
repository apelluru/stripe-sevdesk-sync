# ExportInvoice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**ExportInvoice200ResponseObjects**](ExportInvoice200ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_invoice200_response import ExportInvoice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExportInvoice200Response from a JSON string
export_invoice200_response_instance = ExportInvoice200Response.from_json(json)
# print the JSON string representation of the object
print(ExportInvoice200Response.to_json())

# convert the object into a dict
export_invoice200_response_dict = export_invoice200_response_instance.to_dict()
# create an instance of ExportInvoice200Response from a dict
export_invoice200_response_from_dict = ExportInvoice200Response.from_dict(export_invoice200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


