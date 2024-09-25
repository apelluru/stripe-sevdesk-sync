# SaveOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**ModelOrderResponse**](ModelOrderResponse.md) |  | [optional] 
**order_pos** | [**List[ModelOrderPosResponse]**](ModelOrderPosResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_order_response import SaveOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveOrderResponse from a JSON string
save_order_response_instance = SaveOrderResponse.from_json(json)
# print the JSON string representation of the object
print(SaveOrderResponse.to_json())

# convert the object into a dict
save_order_response_dict = save_order_response_instance.to_dict()
# create an instance of SaveOrderResponse from a dict
save_order_response_from_dict = SaveOrderResponse.from_dict(save_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


