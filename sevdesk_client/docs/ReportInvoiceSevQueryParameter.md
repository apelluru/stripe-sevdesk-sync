# ReportInvoiceSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name which is exported | 
**object_name** | **object** | SevQuery object name | 
**filter** | [**ExportInvoiceSevQueryParameterFilter**](ExportInvoiceSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.report_invoice_sev_query_parameter import ReportInvoiceSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ReportInvoiceSevQueryParameter from a JSON string
report_invoice_sev_query_parameter_instance = ReportInvoiceSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ReportInvoiceSevQueryParameter.to_json())

# convert the object into a dict
report_invoice_sev_query_parameter_dict = report_invoice_sev_query_parameter_instance.to_dict()
# create an instance of ReportInvoiceSevQueryParameter from a dict
report_invoice_sev_query_parameter_from_dict = ReportInvoiceSevQueryParameter.from_dict(report_invoice_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


