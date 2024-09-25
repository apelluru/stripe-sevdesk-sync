# ModelVoucherTaxSet

** Use this in sevdesk-Update 2.0 (replaces taxType / taxSet).**  Tax set of the voucher. Needs to be added if you chose the taxType=custom.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the object | 
**object_name** | **str** | Model name, which is &#39;TaxSet&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_tax_set import ModelVoucherTaxSet

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherTaxSet from a JSON string
model_voucher_tax_set_instance = ModelVoucherTaxSet.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherTaxSet.to_json())

# convert the object into a dict
model_voucher_tax_set_dict = model_voucher_tax_set_instance.to_dict()
# create an instance of ModelVoucherTaxSet from a dict
model_voucher_tax_set_from_dict = ModelVoucherTaxSet.from_dict(model_voucher_tax_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


