# SaveInvoiceDiscountSaveInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | **bool** | Defines if this is a discount or a surcharge | [optional] 
**text** | **str** | A text for your discount | [optional] 
**percentage** | **bool** | Defines if this is a percentage or an absolute discount | [optional] 
**value** | **float** | Value of the discount | [optional] 
**object_name** | **str** | Object name of the discount | [optional] 
**map_all** | **bool** | Internal param | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_invoice_discount_save_inner import SaveInvoiceDiscountSaveInner

# TODO update the JSON string below
json = "{}"
# create an instance of SaveInvoiceDiscountSaveInner from a JSON string
save_invoice_discount_save_inner_instance = SaveInvoiceDiscountSaveInner.from_json(json)
# print the JSON string representation of the object
print(SaveInvoiceDiscountSaveInner.to_json())

# convert the object into a dict
save_invoice_discount_save_inner_dict = save_invoice_discount_save_inner_instance.to_dict()
# create an instance of SaveInvoiceDiscountSaveInner from a dict
save_invoice_discount_save_inner_from_dict = SaveInvoiceDiscountSaveInner.from_dict(save_invoice_discount_save_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


