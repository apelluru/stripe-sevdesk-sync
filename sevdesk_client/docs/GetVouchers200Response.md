# GetVouchers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelVoucherResponse]**](ModelVoucherResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_vouchers200_response import GetVouchers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVouchers200Response from a JSON string
get_vouchers200_response_instance = GetVouchers200Response.from_json(json)
# print the JSON string representation of the object
print(GetVouchers200Response.to_json())

# convert the object into a dict
get_vouchers200_response_dict = get_vouchers200_response_instance.to_dict()
# create an instance of GetVouchers200Response from a dict
get_vouchers200_response_from_dict = GetVouchers200Response.from_dict(get_vouchers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


