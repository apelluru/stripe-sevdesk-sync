# ExportInvoiceZipSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name, which is &#39;Invoice&#39; | 
**object_name** | **object** | Model name, which is &#39;SevQuery&#39; | 
**filter** | [**ExportInvoiceSevQueryParameterFilter**](ExportInvoiceSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_invoice_zip_sev_query_parameter import ExportInvoiceZipSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportInvoiceZipSevQueryParameter from a JSON string
export_invoice_zip_sev_query_parameter_instance = ExportInvoiceZipSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ExportInvoiceZipSevQueryParameter.to_json())

# convert the object into a dict
export_invoice_zip_sev_query_parameter_dict = export_invoice_zip_sev_query_parameter_instance.to_dict()
# create an instance of ExportInvoiceZipSevQueryParameter from a dict
export_invoice_zip_sev_query_parameter_from_dict = ExportInvoiceZipSevQueryParameter.from_dict(export_invoice_zip_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


