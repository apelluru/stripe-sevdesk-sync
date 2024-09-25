# ReportOrderSevQueryParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit export | [optional] 
**model_name** | **object** | Model name which is exported | 
**object_name** | **object** | SevQuery object name | 
**filter** | [**ReportOrderSevQueryParameterFilter**](ReportOrderSevQueryParameterFilter.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.report_order_sev_query_parameter import ReportOrderSevQueryParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ReportOrderSevQueryParameter from a JSON string
report_order_sev_query_parameter_instance = ReportOrderSevQueryParameter.from_json(json)
# print the JSON string representation of the object
print(ReportOrderSevQueryParameter.to_json())

# convert the object into a dict
report_order_sev_query_parameter_dict = report_order_sev_query_parameter_instance.to_dict()
# create an instance of ReportOrderSevQueryParameter from a dict
report_order_sev_query_parameter_from_dict = ReportOrderSevQueryParameter.from_dict(report_order_sev_query_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


