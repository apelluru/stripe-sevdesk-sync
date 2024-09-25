# ModelDiscount

Discount model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of the discount | [optional] [readonly] 
**object_name** | **str** | Model name, which is &#39;Discounts&#39; | [optional] [readonly] 
**create** | **datetime** | Date of discount creation | [optional] [readonly] 
**update** | **datetime** | Date of last discount update | [optional] [readonly] 
**object** | [**ModelDiscountObject**](ModelDiscountObject.md) |  | [optional] 
**sev_client** | **str** | Client to which invoice belongs. Will be filled automatically | [optional] [readonly] 
**text** | **str** | A text describing your position. | [optional] [readonly] 
**percentage** | **str** | Defines if this is a percentage or an absolute discount | [optional] 
**value** | **str** | Value of the discount | [optional] 
**is_net** | **str** | Defines is the Discount net or gross 0 - gross 1 - net | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_discount import ModelDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDiscount from a JSON string
model_discount_instance = ModelDiscount.from_json(json)
# print the JSON string representation of the object
print(ModelDiscount.to_json())

# convert the object into a dict
model_discount_dict = model_discount_instance.to_dict()
# create an instance of ModelDiscount from a dict
model_discount_from_dict = ModelDiscount.from_dict(model_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


