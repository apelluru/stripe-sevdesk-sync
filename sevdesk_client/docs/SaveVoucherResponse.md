# SaveVoucherResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher** | [**ModelVoucherResponse**](ModelVoucherResponse.md) |  | [optional] 
**voucher_pos** | [**List[ModelVoucherPosResponse]**](ModelVoucherPosResponse.md) |  | [optional] 
**filename** | **bytearray** | Filename of a previously upload file which should be attached. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_voucher_response import SaveVoucherResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveVoucherResponse from a JSON string
save_voucher_response_instance = SaveVoucherResponse.from_json(json)
# print the JSON string representation of the object
print(SaveVoucherResponse.to_json())

# convert the object into a dict
save_voucher_response_dict = save_voucher_response_instance.to_dict()
# create an instance of SaveVoucherResponse from a dict
save_voucher_response_from_dict = SaveVoucherResponse.from_dict(save_voucher_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


