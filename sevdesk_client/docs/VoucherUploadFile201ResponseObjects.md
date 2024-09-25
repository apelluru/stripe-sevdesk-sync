# VoucherUploadFile201ResponseObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | **float** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**origin_mime_type** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**content_hash** | **str** |  | [optional] 
**content** | **List[object]** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.voucher_upload_file201_response_objects import VoucherUploadFile201ResponseObjects

# TODO update the JSON string below
json = "{}"
# create an instance of VoucherUploadFile201ResponseObjects from a JSON string
voucher_upload_file201_response_objects_instance = VoucherUploadFile201ResponseObjects.from_json(json)
# print the JSON string representation of the object
print(VoucherUploadFile201ResponseObjects.to_json())

# convert the object into a dict
voucher_upload_file201_response_objects_dict = voucher_upload_file201_response_objects_instance.to_dict()
# create an instance of VoucherUploadFile201ResponseObjects from a dict
voucher_upload_file201_response_objects_from_dict = VoucherUploadFile201ResponseObjects.from_dict(voucher_upload_file201_response_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


