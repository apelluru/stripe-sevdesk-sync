# SaveOrderOrderPosDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of order position | 
**object_name** | **str** | Object name of order position | 

## Example

```python
from sevdesk_client.openapi_client.models.save_order_order_pos_delete import SaveOrderOrderPosDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SaveOrderOrderPosDelete from a JSON string
save_order_order_pos_delete_instance = SaveOrderOrderPosDelete.from_json(json)
# print the JSON string representation of the object
print(SaveOrderOrderPosDelete.to_json())

# convert the object into a dict
save_order_order_pos_delete_dict = save_order_order_pos_delete_instance.to_dict()
# create an instance of SaveOrderOrderPosDelete from a dict
save_order_order_pos_delete_from_dict = SaveOrderOrderPosDelete.from_dict(save_order_order_pos_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


