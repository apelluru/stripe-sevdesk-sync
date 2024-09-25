# ExportVoucherZipSevQueryParameterFilterContact

filters the vouchers by contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.export_voucher_zip_sev_query_parameter_filter_contact import ExportVoucherZipSevQueryParameterFilterContact

# TODO update the JSON string below
json = "{}"
# create an instance of ExportVoucherZipSevQueryParameterFilterContact from a JSON string
export_voucher_zip_sev_query_parameter_filter_contact_instance = ExportVoucherZipSevQueryParameterFilterContact.from_json(json)
# print the JSON string representation of the object
print(ExportVoucherZipSevQueryParameterFilterContact.to_json())

# convert the object into a dict
export_voucher_zip_sev_query_parameter_filter_contact_dict = export_voucher_zip_sev_query_parameter_filter_contact_instance.to_dict()
# create an instance of ExportVoucherZipSevQueryParameterFilterContact from a dict
export_voucher_zip_sev_query_parameter_filter_contact_from_dict = ExportVoucherZipSevQueryParameterFilterContact.from_dict(export_voucher_zip_sev_query_parameter_filter_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


