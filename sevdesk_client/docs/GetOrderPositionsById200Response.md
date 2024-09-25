# GetOrderPositionsById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelOrderPosResponse]**](ModelOrderPosResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_order_positions_by_id200_response import GetOrderPositionsById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderPositionsById200Response from a JSON string
get_order_positions_by_id200_response_instance = GetOrderPositionsById200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrderPositionsById200Response.to_json())

# convert the object into a dict
get_order_positions_by_id200_response_dict = get_order_positions_by_id200_response_instance.to_dict()
# create an instance of GetOrderPositionsById200Response from a dict
get_order_positions_by_id200_response_from_dict = GetOrderPositionsById200Response.from_dict(get_order_positions_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


