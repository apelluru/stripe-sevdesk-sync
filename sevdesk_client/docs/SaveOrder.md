# SaveOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**ModelOrder**](ModelOrder.md) |  | 
**order_pos_save** | [**List[ModelOrderPos]**](ModelOrderPos.md) |  | [optional] 
**order_pos_delete** | [**SaveOrderOrderPosDelete**](SaveOrderOrderPosDelete.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_order import SaveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of SaveOrder from a JSON string
save_order_instance = SaveOrder.from_json(json)
# print the JSON string representation of the object
print(SaveOrder.to_json())

# convert the object into a dict
save_order_dict = save_order_instance.to_dict()
# create an instance of SaveOrder from a dict
save_order_from_dict = SaveOrder.from_dict(save_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


