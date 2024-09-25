# ModelVoucherSupplier

The contact used in the voucher as a supplier.<br> If you don't have a contact as a supplier, you can set this object to null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_supplier import ModelVoucherSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherSupplier from a JSON string
model_voucher_supplier_instance = ModelVoucherSupplier.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherSupplier.to_json())

# convert the object into a dict
model_voucher_supplier_dict = model_voucher_supplier_instance.to_dict()
# create an instance of ModelVoucherSupplier from a dict
model_voucher_supplier_from_dict = ModelVoucherSupplier.from_dict(model_voucher_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


