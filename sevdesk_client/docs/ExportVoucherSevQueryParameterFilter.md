# ExportVoucherSevQueryParameterFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date of the voucher | [optional] 
**end_date** | **datetime** | End date of the voucher | [optional] 
**start_pay_date** | **datetime** | Start pay date of the voucher | [optional] 
**end_pay_date** | **datetime** | End pay date of the voucher | [optional] 
**contact** | [**ExportVoucherSevQueryParameterFilterContact**](ExportVoucherSevQueryParameterFilterContact.md) |  | [optional] 
**start_amount** | **int** | filters the vouchers by amount | [optional] 
**end_amount** | **int** | filters the vouchers by amount | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_voucher_sev_query_parameter_filter import ExportVoucherSevQueryParameterFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportVoucherSevQueryParameterFilter from a JSON string
export_voucher_sev_query_parameter_filter_instance = ExportVoucherSevQueryParameterFilter.from_json(json)
# print the JSON string representation of the object
print(ExportVoucherSevQueryParameterFilter.to_json())

# convert the object into a dict
export_voucher_sev_query_parameter_filter_dict = export_voucher_sev_query_parameter_filter_instance.to_dict()
# create an instance of ExportVoucherSevQueryParameterFilter from a dict
export_voucher_sev_query_parameter_filter_from_dict = ExportVoucherSevQueryParameterFilter.from_dict(export_voucher_sev_query_parameter_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


