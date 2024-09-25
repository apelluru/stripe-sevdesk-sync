# ModelOrderPosResponseOrder

The order to which the position belongs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the order | 
**object_name** | **str** | Model name, which is &#39;Order&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_pos_response_order import ModelOrderPosResponseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderPosResponseOrder from a JSON string
model_order_pos_response_order_instance = ModelOrderPosResponseOrder.from_json(json)
# print the JSON string representation of the object
print(ModelOrderPosResponseOrder.to_json())

# convert the object into a dict
model_order_pos_response_order_dict = model_order_pos_response_order_instance.to_dict()
# create an instance of ModelOrderPosResponseOrder from a dict
model_order_pos_response_order_from_dict = ModelOrderPosResponseOrder.from_dict(model_order_pos_response_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


