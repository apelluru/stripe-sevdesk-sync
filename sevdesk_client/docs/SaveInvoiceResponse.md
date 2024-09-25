# SaveInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**ModelInvoiceResponse**](ModelInvoiceResponse.md) |  | [optional] 
**invoice_pos** | [**List[ModelInvoicePosResponse]**](ModelInvoicePosResponse.md) |  | [optional] 
**filename** | **bytearray** | Filename of a previously upload file which should be attached. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_invoice_response import SaveInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveInvoiceResponse from a JSON string
save_invoice_response_instance = SaveInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(SaveInvoiceResponse.to_json())

# convert the object into a dict
save_invoice_response_dict = save_invoice_response_instance.to_dict()
# create an instance of SaveInvoiceResponse from a dict
save_invoice_response_from_dict = SaveInvoiceResponse.from_dict(save_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


