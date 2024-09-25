# ExportVoucher200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**mimetype** | **str** |  | [optional] 
**base64_encoded** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_voucher200_response import ExportVoucher200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExportVoucher200Response from a JSON string
export_voucher200_response_instance = ExportVoucher200Response.from_json(json)
# print the JSON string representation of the object
print(ExportVoucher200Response.to_json())

# convert the object into a dict
export_voucher200_response_dict = export_voucher200_response_instance.to_dict()
# create an instance of ExportVoucher200Response from a dict
export_voucher200_response_from_dict = ExportVoucher200Response.from_dict(export_voucher200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


