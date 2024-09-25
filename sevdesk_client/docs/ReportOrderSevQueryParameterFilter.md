# ReportOrderSevQueryParameterFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_type** | **str** | Type of orders you want to export 1. AN - Angebote 2. AB - Aufträge 3. LI - Lieferscheine | [optional] 
**start_date** | **datetime** | Start date of the order | [optional] 
**end_date** | **datetime** | End date of the order | [optional] 
**contact** | [**ReportOrderSevQueryParameterFilterContact**](ReportOrderSevQueryParameterFilterContact.md) |  | [optional] 
**start_amount** | **int** | filters the orders by amount | [optional] 
**end_amount** | **int** | filters the orders by amount | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.report_order_sev_query_parameter_filter import ReportOrderSevQueryParameterFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ReportOrderSevQueryParameterFilter from a JSON string
report_order_sev_query_parameter_filter_instance = ReportOrderSevQueryParameterFilter.from_json(json)
# print the JSON string representation of the object
print(ReportOrderSevQueryParameterFilter.to_json())

# convert the object into a dict
report_order_sev_query_parameter_filter_dict = report_order_sev_query_parameter_filter_instance.to_dict()
# create an instance of ReportOrderSevQueryParameterFilter from a dict
report_order_sev_query_parameter_filter_from_dict = ReportOrderSevQueryParameterFilter.from_dict(report_order_sev_query_parameter_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


