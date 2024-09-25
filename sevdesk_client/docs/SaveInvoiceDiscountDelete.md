# SaveInvoiceDiscountDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of discount to delete | [optional] 
**object_name** | **str** | Object name of discount | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_invoice_discount_delete import SaveInvoiceDiscountDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SaveInvoiceDiscountDelete from a JSON string
save_invoice_discount_delete_instance = SaveInvoiceDiscountDelete.from_json(json)
# print the JSON string representation of the object
print(SaveInvoiceDiscountDelete.to_json())

# convert the object into a dict
save_invoice_discount_delete_dict = save_invoice_discount_delete_instance.to_dict()
# create an instance of SaveInvoiceDiscountDelete from a dict
save_invoice_discount_delete_from_dict = SaveInvoiceDiscountDelete.from_dict(save_invoice_discount_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


