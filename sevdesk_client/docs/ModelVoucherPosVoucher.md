# ModelVoucherPosVoucher

The voucher to which the position belongs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the voucher | 
**object_name** | **str** | Model name, which is &#39;Voucher&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_pos_voucher import ModelVoucherPosVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherPosVoucher from a JSON string
model_voucher_pos_voucher_instance = ModelVoucherPosVoucher.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherPosVoucher.to_json())

# convert the object into a dict
model_voucher_pos_voucher_dict = model_voucher_pos_voucher_instance.to_dict()
# create an instance of ModelVoucherPosVoucher from a dict
model_voucher_pos_voucher_from_dict = ModelVoucherPosVoucher.from_dict(model_voucher_pos_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


