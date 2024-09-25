# ReportInvoice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**ReportInvoice200ResponseObjects**](ReportInvoice200ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.report_invoice200_response import ReportInvoice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReportInvoice200Response from a JSON string
report_invoice200_response_instance = ReportInvoice200Response.from_json(json)
# print the JSON string representation of the object
print(ReportInvoice200Response.to_json())

# convert the object into a dict
report_invoice200_response_dict = report_invoice200_response_instance.to_dict()
# create an instance of ReportInvoice200Response from a dict
report_invoice200_response_from_dict = ReportInvoice200Response.from_dict(report_invoice200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


