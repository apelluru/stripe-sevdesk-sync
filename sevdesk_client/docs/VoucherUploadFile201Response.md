# VoucherUploadFile201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**VoucherUploadFile201ResponseObjects**](VoucherUploadFile201ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.voucher_upload_file201_response import VoucherUploadFile201Response

# TODO update the JSON string below
json = "{}"
# create an instance of VoucherUploadFile201Response from a JSON string
voucher_upload_file201_response_instance = VoucherUploadFile201Response.from_json(json)
# print the JSON string representation of the object
print(VoucherUploadFile201Response.to_json())

# convert the object into a dict
voucher_upload_file201_response_dict = voucher_upload_file201_response_instance.to_dict()
# create an instance of VoucherUploadFile201Response from a dict
voucher_upload_file201_response_from_dict = VoucherUploadFile201Response.from_dict(voucher_upload_file201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


