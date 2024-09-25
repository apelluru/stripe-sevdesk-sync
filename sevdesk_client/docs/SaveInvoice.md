# SaveInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**ModelInvoice**](ModelInvoice.md) |  | 
**invoice_pos_save** | [**List[ModelInvoicePos]**](ModelInvoicePos.md) |  | [optional] 
**invoice_pos_delete** | [**SaveInvoiceInvoicePosDelete**](SaveInvoiceInvoicePosDelete.md) |  | [optional] 
**filename** | **bytearray** | Filename of a previously upload file which should be attached. | [optional] 
**discount_save** | [**List[SaveInvoiceDiscountSaveInner]**](SaveInvoiceDiscountSaveInner.md) |  | [optional] 
**discount_delete** | [**SaveInvoiceDiscountDelete**](SaveInvoiceDiscountDelete.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_invoice import SaveInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of SaveInvoice from a JSON string
save_invoice_instance = SaveInvoice.from_json(json)
# print the JSON string representation of the object
print(SaveInvoice.to_json())

# convert the object into a dict
save_invoice_dict = save_invoice_instance.to_dict()
# create an instance of SaveInvoice from a dict
save_invoice_from_dict = SaveInvoice.from_dict(save_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


