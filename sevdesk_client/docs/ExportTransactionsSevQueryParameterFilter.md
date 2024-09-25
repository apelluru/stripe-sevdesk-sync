# ExportTransactionsSevQueryParameterFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paymt_purpose** | **str** | the payment purpose | [optional] 
**name** | **str** | the name of the payee/payer | [optional] 
**start_date** | **datetime** | Start date of the transactions | [optional] 
**end_date** | **datetime** | End date of the transactions | [optional] 
**start_amount** | **int** | filters the transactions by amount | [optional] 
**end_amount** | **int** | filters the transactions by amount | [optional] 
**check_account** | [**ExportTransactionsSevQueryParameterFilterCheckAccount**](ExportTransactionsSevQueryParameterFilterCheckAccount.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_transactions_sev_query_parameter_filter import ExportTransactionsSevQueryParameterFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportTransactionsSevQueryParameterFilter from a JSON string
export_transactions_sev_query_parameter_filter_instance = ExportTransactionsSevQueryParameterFilter.from_json(json)
# print the JSON string representation of the object
print(ExportTransactionsSevQueryParameterFilter.to_json())

# convert the object into a dict
export_transactions_sev_query_parameter_filter_dict = export_transactions_sev_query_parameter_filter_instance.to_dict()
# create an instance of ExportTransactionsSevQueryParameterFilter from a dict
export_transactions_sev_query_parameter_filter_from_dict = ExportTransactionsSevQueryParameterFilter.from_dict(export_transactions_sev_query_parameter_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


