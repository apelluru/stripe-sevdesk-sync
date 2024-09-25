# VoucherUploadFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | The file to upload | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.voucher_upload_file_request import VoucherUploadFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoucherUploadFileRequest from a JSON string
voucher_upload_file_request_instance = VoucherUploadFileRequest.from_json(json)
# print the JSON string representation of the object
print(VoucherUploadFileRequest.to_json())

# convert the object into a dict
voucher_upload_file_request_dict = voucher_upload_file_request_instance.to_dict()
# create an instance of VoucherUploadFileRequest from a dict
voucher_upload_file_request_from_dict = VoucherUploadFileRequest.from_dict(voucher_upload_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


