# OrderGetPdf200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**base64encoded** | **bool** |  | [optional] 
**content** | **bytearray** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.order_get_pdf200_response import OrderGetPdf200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGetPdf200Response from a JSON string
order_get_pdf200_response_instance = OrderGetPdf200Response.from_json(json)
# print the JSON string representation of the object
print(OrderGetPdf200Response.to_json())

# convert the object into a dict
order_get_pdf200_response_dict = order_get_pdf200_response_instance.to_dict()
# create an instance of OrderGetPdf200Response from a dict
order_get_pdf200_response_from_dict = OrderGetPdf200Response.from_dict(order_get_pdf200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


