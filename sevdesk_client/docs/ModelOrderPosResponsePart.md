# ModelOrderPosResponsePart

Part from your inventory which is used in the position.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the part | 
**object_name** | **str** | Model name, which is &#39;Part&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_pos_response_part import ModelOrderPosResponsePart

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderPosResponsePart from a JSON string
model_order_pos_response_part_instance = ModelOrderPosResponsePart.from_json(json)
# print the JSON string representation of the object
print(ModelOrderPosResponsePart.to_json())

# convert the object into a dict
model_order_pos_response_part_dict = model_order_pos_response_part_instance.to_dict()
# create an instance of ModelOrderPosResponsePart from a dict
model_order_pos_response_part_from_dict = ModelOrderPosResponsePart.from_dict(model_order_pos_response_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


