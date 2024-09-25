# SaveVoucherVoucherPosDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of voucher position | 
**object_name** | **str** | Object name of voucher position | 

## Example

```python
from sevdesk_client.openapi_client.models.save_voucher_voucher_pos_delete import SaveVoucherVoucherPosDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SaveVoucherVoucherPosDelete from a JSON string
save_voucher_voucher_pos_delete_instance = SaveVoucherVoucherPosDelete.from_json(json)
# print the JSON string representation of the object
print(SaveVoucherVoucherPosDelete.to_json())

# convert the object into a dict
save_voucher_voucher_pos_delete_dict = save_voucher_voucher_pos_delete_instance.to_dict()
# create an instance of SaveVoucherVoucherPosDelete from a dict
save_voucher_voucher_pos_delete_from_dict = SaveVoucherVoucherPosDelete.from_dict(save_voucher_voucher_pos_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


