# ReportOrderSevQueryParameterFilterContact

filters the orders by contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.report_order_sev_query_parameter_filter_contact import ReportOrderSevQueryParameterFilterContact

# TODO update the JSON string below
json = "{}"
# create an instance of ReportOrderSevQueryParameterFilterContact from a JSON string
report_order_sev_query_parameter_filter_contact_instance = ReportOrderSevQueryParameterFilterContact.from_json(json)
# print the JSON string representation of the object
print(ReportOrderSevQueryParameterFilterContact.to_json())

# convert the object into a dict
report_order_sev_query_parameter_filter_contact_dict = report_order_sev_query_parameter_filter_contact_instance.to_dict()
# create an instance of ReportOrderSevQueryParameterFilterContact from a dict
report_order_sev_query_parameter_filter_contact_from_dict = ReportOrderSevQueryParameterFilterContact.from_dict(report_order_sev_query_parameter_filter_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


