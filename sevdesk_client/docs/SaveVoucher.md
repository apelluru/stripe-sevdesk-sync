# SaveVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher** | [**ModelVoucher**](ModelVoucher.md) |  | 
**voucher_pos_save** | [**List[ModelVoucherPos]**](ModelVoucherPos.md) |  | [optional] 
**voucher_pos_delete** | [**SaveVoucherVoucherPosDelete**](SaveVoucherVoucherPosDelete.md) |  | [optional] 
**filename** | **bytearray** | Filename of a previously upload file which should be attached. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_voucher import SaveVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of SaveVoucher from a JSON string
save_voucher_instance = SaveVoucher.from_json(json)
# print the JSON string representation of the object
print(SaveVoucher.to_json())

# convert the object into a dict
save_voucher_dict = save_voucher_instance.to_dict()
# create an instance of SaveVoucher from a dict
save_voucher_from_dict = SaveVoucher.from_dict(save_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


