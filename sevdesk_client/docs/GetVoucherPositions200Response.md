# GetVoucherPositions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelVoucherPosResponse]**](ModelVoucherPosResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_voucher_positions200_response import GetVoucherPositions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVoucherPositions200Response from a JSON string
get_voucher_positions200_response_instance = GetVoucherPositions200Response.from_json(json)
# print the JSON string representation of the object
print(GetVoucherPositions200Response.to_json())

# convert the object into a dict
get_voucher_positions200_response_dict = get_voucher_positions200_response_instance.to_dict()
# create an instance of GetVoucherPositions200Response from a dict
get_voucher_positions200_response_from_dict = GetVoucherPositions200Response.from_dict(get_voucher_positions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


