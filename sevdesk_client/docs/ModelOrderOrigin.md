# ModelOrderOrigin

Object from which the order was created. For example an offer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the object | 
**object_name** | **str** | Model name of the object. Could be &#39;Order&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_origin import ModelOrderOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderOrigin from a JSON string
model_order_origin_instance = ModelOrderOrigin.from_json(json)
# print the JSON string representation of the object
print(ModelOrderOrigin.to_json())

# convert the object into a dict
model_order_origin_dict = model_order_origin_instance.to_dict()
# create an instance of ModelOrderOrigin from a dict
model_order_origin_from_dict = ModelOrderOrigin.from_dict(model_order_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


