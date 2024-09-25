# ExportInvoiceSevQueryParameterFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_type** | **List[str]** | Type of invoices you want to export 1. RE - Rechnung 2. SR - Stornorechnung 3. TR - Teilrechnung 4. AR - Abschlagsrechnung 5. ER - Endrechnung 6. WKR - Wiederkehrende Rechnung 7. MA - Mahnung | [optional] 
**start_date** | **datetime** | Start date of the invoice | [optional] 
**end_date** | **datetime** | End date of the invoice | [optional] 
**contact** | [**ExportInvoiceSevQueryParameterFilterContact**](ExportInvoiceSevQueryParameterFilterContact.md) |  | [optional] 
**start_amount** | **int** | filters the invoices by amount | [optional] 
**end_amount** | **int** | filters the invoices by amount | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_invoice_sev_query_parameter_filter import ExportInvoiceSevQueryParameterFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportInvoiceSevQueryParameterFilter from a JSON string
export_invoice_sev_query_parameter_filter_instance = ExportInvoiceSevQueryParameterFilter.from_json(json)
# print the JSON string representation of the object
print(ExportInvoiceSevQueryParameterFilter.to_json())

# convert the object into a dict
export_invoice_sev_query_parameter_filter_dict = export_invoice_sev_query_parameter_filter_instance.to_dict()
# create an instance of ExportInvoiceSevQueryParameterFilter from a dict
export_invoice_sev_query_parameter_filter_from_dict = ExportInvoiceSevQueryParameterFilter.from_dict(export_invoice_sev_query_parameter_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


