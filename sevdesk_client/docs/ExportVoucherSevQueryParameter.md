# ExportVoucherSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name, which is &#39;Voucher&#39; | 
**object_name** | **object** | Model name, which is &#39;SevQuery&#39; | 
**filter** | [**ExportVoucherSevQueryParameterFilter**](ExportVoucherSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_voucher_sev_query_parameter import ExportVoucherSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportVoucherSevQueryParameter from a JSON string
export_voucher_sev_query_parameter_instance = ExportVoucherSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ExportVoucherSevQueryParameter.to_json())

# convert the object into a dict
export_voucher_sev_query_parameter_dict = export_voucher_sev_query_parameter_instance.to_dict()
# create an instance of ExportVoucherSevQueryParameter from a dict
export_voucher_sev_query_parameter_from_dict = ExportVoucherSevQueryParameter.from_dict(export_voucher_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


