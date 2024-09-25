# ModelVoucherPosAccountDatev

<b>Use this in sevdesk-Update 2.0 (replaces accountingType).</b>       The account datev to which the position belongs.<br>       An account datev is the booking account to which the position belongs.<br>       For more information, please refer to   <a href='#tag/Voucher/Account-Datev'>this</a> section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the account datev | 
**object_name** | **str** | Model name, which is &#39;AccountDatev&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_pos_account_datev import ModelVoucherPosAccountDatev

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherPosAccountDatev from a JSON string
model_voucher_pos_account_datev_instance = ModelVoucherPosAccountDatev.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherPosAccountDatev.to_json())

# convert the object into a dict
model_voucher_pos_account_datev_dict = model_voucher_pos_account_datev_instance.to_dict()
# create an instance of ModelVoucherPosAccountDatev from a dict
model_voucher_pos_account_datev_from_dict = ModelVoucherPosAccountDatev.from_dict(model_voucher_pos_account_datev_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


