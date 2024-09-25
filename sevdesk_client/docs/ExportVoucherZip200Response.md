# ExportVoucherZip200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**ExportVoucherZip200ResponseObjects**](ExportVoucherZip200ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_voucher_zip200_response import ExportVoucherZip200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExportVoucherZip200Response from a JSON string
export_voucher_zip200_response_instance = ExportVoucherZip200Response.from_json(json)
# print the JSON string representation of the object
print(ExportVoucherZip200Response.to_json())

# convert the object into a dict
export_voucher_zip200_response_dict = export_voucher_zip200_response_instance.to_dict()
# create an instance of ExportVoucherZip200Response from a dict
export_voucher_zip200_response_from_dict = ExportVoucherZip200Response.from_dict(export_voucher_zip200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


