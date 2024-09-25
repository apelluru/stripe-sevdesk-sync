# SaveInvoiceInvoicePosDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of invoice position | 
**object_name** | **str** | Object name of invoice position | 

## Example

```python
from sevdesk_client.openapi_client.models.save_invoice_invoice_pos_delete import SaveInvoiceInvoicePosDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SaveInvoiceInvoicePosDelete from a JSON string
save_invoice_invoice_pos_delete_instance = SaveInvoiceInvoicePosDelete.from_json(json)
# print the JSON string representation of the object
print(SaveInvoiceInvoicePosDelete.to_json())

# convert the object into a dict
save_invoice_invoice_pos_delete_dict = save_invoice_invoice_pos_delete_instance.to_dict()
# create an instance of SaveInvoiceInvoicePosDelete from a dict
save_invoice_invoice_pos_delete_from_dict = SaveInvoiceInvoicePosDelete.from_dict(save_invoice_invoice_pos_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


