# OrderSendByRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_type** | **str** | Specifies the way in which the order was sent to the customer.&lt;br&gt;       Accepts &#39;VPR&#39; (print), &#39;VP&#39; (postal), &#39;VM&#39; (mail) and &#39;VPDF&#39; (downloaded pfd). | 
**send_draft** | **bool** | To create a draft of an order for internal use. This operation will not alter the status of the order. | 

## Example

```python
from sevdesk_client.openapi_client.models.order_send_by_request import OrderSendByRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSendByRequest from a JSON string
order_send_by_request_instance = OrderSendByRequest.from_json(json)
# print the JSON string representation of the object
print(OrderSendByRequest.to_json())

# convert the object into a dict
order_send_by_request_dict = order_send_by_request_instance.to_dict()
# create an instance of OrderSendByRequest from a dict
order_send_by_request_from_dict = OrderSendByRequest.from_dict(order_send_by_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


