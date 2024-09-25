# ModelVoucherResponseTaxSet

**Use this in sevdesk-Update 2.0 (replaces taxType / taxSet).**  Tax set of the voucher. Needs to be added if you chose the taxType=custom.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the object | 
**object_name** | **str** | Model name, which is &#39;TaxSet&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_response_tax_set import ModelVoucherResponseTaxSet

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherResponseTaxSet from a JSON string
model_voucher_response_tax_set_instance = ModelVoucherResponseTaxSet.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherResponseTaxSet.to_json())

# convert the object into a dict
model_voucher_response_tax_set_dict = model_voucher_response_tax_set_instance.to_dict()
# create an instance of ModelVoucherResponseTaxSet from a dict
model_voucher_response_tax_set_from_dict = ModelVoucherResponseTaxSet.from_dict(model_voucher_response_tax_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


