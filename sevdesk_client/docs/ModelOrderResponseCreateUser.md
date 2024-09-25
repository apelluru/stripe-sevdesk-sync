# ModelOrderResponseCreateUser

Will be filled automatically by our system and can't be changed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the user | 
**object_name** | **str** | Model name, which is &#39;SevUser&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_response_create_user import ModelOrderResponseCreateUser

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderResponseCreateUser from a JSON string
model_order_response_create_user_instance = ModelOrderResponseCreateUser.from_json(json)
# print the JSON string representation of the object
print(ModelOrderResponseCreateUser.to_json())

# convert the object into a dict
model_order_response_create_user_dict = model_order_response_create_user_instance.to_dict()
# create an instance of ModelOrderResponseCreateUser from a dict
model_order_response_create_user_from_dict = ModelOrderResponseCreateUser.from_dict(model_order_response_create_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


