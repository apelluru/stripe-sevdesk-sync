# ModelVoucherUpdateSupplier

The contact used in the voucher as a supplier.<br> If you don't have a contact as a supplier, you can set this object to null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | [default to 'Contact']

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_update_supplier import ModelVoucherUpdateSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherUpdateSupplier from a JSON string
model_voucher_update_supplier_instance = ModelVoucherUpdateSupplier.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherUpdateSupplier.to_json())

# convert the object into a dict
model_voucher_update_supplier_dict = model_voucher_update_supplier_instance.to_dict()
# create an instance of ModelVoucherUpdateSupplier from a dict
model_voucher_update_supplier_from_dict = ModelVoucherUpdateSupplier.from_dict(model_voucher_update_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


