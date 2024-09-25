# ExportVoucherZipSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name, which is &#39;Voucher&#39; | 
**object_name** | **object** | Model name, which is &#39;SevQuery&#39; | 
**filter** | [**ExportVoucherZipSevQueryParameterFilter**](ExportVoucherZipSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_voucher_zip_sev_query_parameter import ExportVoucherZipSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportVoucherZipSevQueryParameter from a JSON string
export_voucher_zip_sev_query_parameter_instance = ExportVoucherZipSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ExportVoucherZipSevQueryParameter.to_json())

# convert the object into a dict
export_voucher_zip_sev_query_parameter_dict = export_voucher_zip_sev_query_parameter_instance.to_dict()
# create an instance of ExportVoucherZipSevQueryParameter from a dict
export_voucher_zip_sev_query_parameter_from_dict = ExportVoucherZipSevQueryParameter.from_dict(export_voucher_zip_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


