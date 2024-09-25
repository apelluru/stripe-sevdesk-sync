# ModelVoucherPosEstimatedAccountingType

The accounting type to which the position belongs estimated by our voucher recognition.<br>      An accounting type is the booking account to which the position belongs.<br>      For more information, please refer to      <a href='#tag/Voucher/Accounting-type'>this</a> section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the accounting type | 
**object_name** | **str** | Model name, which is &#39;AccountingType&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_pos_estimated_accounting_type import ModelVoucherPosEstimatedAccountingType

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherPosEstimatedAccountingType from a JSON string
model_voucher_pos_estimated_accounting_type_instance = ModelVoucherPosEstimatedAccountingType.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherPosEstimatedAccountingType.to_json())

# convert the object into a dict
model_voucher_pos_estimated_accounting_type_dict = model_voucher_pos_estimated_accounting_type_instance.to_dict()
# create an instance of ModelVoucherPosEstimatedAccountingType from a dict
model_voucher_pos_estimated_accounting_type_from_dict = ModelVoucherPosEstimatedAccountingType.from_dict(model_voucher_pos_estimated_accounting_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


