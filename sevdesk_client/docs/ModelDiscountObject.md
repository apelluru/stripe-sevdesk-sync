# ModelDiscountObject

The order used for the discount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the order | 
**object_name** | **str** | Model name, which is &#39;Order&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_discount_object import ModelDiscountObject

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDiscountObject from a JSON string
model_discount_object_instance = ModelDiscountObject.from_json(json)
# print the JSON string representation of the object
print(ModelDiscountObject.to_json())

# convert the object into a dict
model_discount_object_dict = model_discount_object_instance.to_dict()
# create an instance of ModelDiscountObject from a dict
model_discount_object_from_dict = ModelDiscountObject.from_dict(model_discount_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


