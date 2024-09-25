# ReportOrder200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**ReportOrder200ResponseObjects**](ReportOrder200ResponseObjects.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.report_order200_response import ReportOrder200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReportOrder200Response from a JSON string
report_order200_response_instance = ReportOrder200Response.from_json(json)
# print the JSON string representation of the object
print(ReportOrder200Response.to_json())

# convert the object into a dict
report_order200_response_dict = report_order200_response_instance.to_dict()
# create an instance of ReportOrder200Response from a dict
report_order200_response_from_dict = ReportOrder200Response.from_dict(report_order200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


