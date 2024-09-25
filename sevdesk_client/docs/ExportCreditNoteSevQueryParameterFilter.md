# ExportCreditNoteSevQueryParameterFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date of the credit note | [optional] 
**end_date** | **datetime** | End date of the credit note | [optional] 
**contact** | [**ExportCreditNoteSevQueryParameterFilterContact**](ExportCreditNoteSevQueryParameterFilterContact.md) |  | [optional] 
**start_amount** | **int** | filters the credit notes by amount | [optional] 
**end_amount** | **int** | filters the credit notes by amount | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.export_credit_note_sev_query_parameter_filter import ExportCreditNoteSevQueryParameterFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCreditNoteSevQueryParameterFilter from a JSON string
export_credit_note_sev_query_parameter_filter_instance = ExportCreditNoteSevQueryParameterFilter.from_json(json)
# print the JSON string representation of the object
print(ExportCreditNoteSevQueryParameterFilter.to_json())

# convert the object into a dict
export_credit_note_sev_query_parameter_filter_dict = export_credit_note_sev_query_parameter_filter_instance.to_dict()
# create an instance of ExportCreditNoteSevQueryParameterFilter from a dict
export_credit_note_sev_query_parameter_filter_from_dict = ExportCreditNoteSevQueryParameterFilter.from_dict(export_credit_note_sev_query_parameter_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


