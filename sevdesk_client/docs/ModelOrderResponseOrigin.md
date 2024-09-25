# ModelOrderResponseOrigin

Object from which the order was created. For example an offer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the object | 
**object_name** | **str** | Model name of the object. Could be &#39;Order&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_response_origin import ModelOrderResponseOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderResponseOrigin from a JSON string
model_order_response_origin_instance = ModelOrderResponseOrigin.from_json(json)
# print the JSON string representation of the object
print(ModelOrderResponseOrigin.to_json())

# convert the object into a dict
model_order_response_origin_dict = model_order_response_origin_instance.to_dict()
# create an instance of ModelOrderResponseOrigin from a dict
model_order_response_origin_from_dict = ModelOrderResponseOrigin.from_dict(model_order_response_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


