# ModelOrderPosResponse

Order position model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The order position id | [optional] [readonly] 
**object_name** | **str** | The order position object name | [optional] [readonly] 
**create** | **datetime** | Date of order position creation | [optional] [readonly] 
**update** | **datetime** | Date of last order position update | [optional] [readonly] 
**order** | [**ModelOrderPosResponseOrder**](ModelOrderPosResponseOrder.md) |  | [optional] 
**part** | [**ModelOrderPosResponsePart**](ModelOrderPosResponsePart.md) |  | [optional] 
**quantity** | **str** | Quantity of the article/part | [optional] 
**price** | **str** | Price of the article/part. Is either gross or net, depending on the sevdesk account setting. | [optional] 
**price_net** | **str** | Net price of the part | [optional] [readonly] 
**price_tax** | **str** | Tax on the price of the part | [optional] 
**price_gross** | **str** | Gross price of the part | [optional] 
**name** | **str** | Name of the article/part. | [optional] 
**unity** | [**ModelOrderPosResponseUnity**](ModelOrderPosResponseUnity.md) |  | [optional] 
**sev_client** | [**ModelOrderPosResponseSevClient**](ModelOrderPosResponseSevClient.md) |  | [optional] 
**position_number** | **str** | Position number of your position. Can be used to order multiple positions. | [optional] 
**text** | **str** | A text describing your position. | [optional] 
**discount** | **str** | An optional discount of the position. | [optional] 
**optional** | **bool** | Defines if the position is optional. | [optional] 
**tax_rate** | **str** | Tax rate of the position. | [optional] 
**sum_discount** | **str** | Discount sum of the position | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_pos_response import ModelOrderPosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderPosResponse from a JSON string
model_order_pos_response_instance = ModelOrderPosResponse.from_json(json)
# print the JSON string representation of the object
print(ModelOrderPosResponse.to_json())

# convert the object into a dict
model_order_pos_response_dict = model_order_pos_response_instance.to_dict()
# create an instance of ModelOrderPosResponse from a dict
model_order_pos_response_from_dict = ModelOrderPosResponse.from_dict(model_order_pos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


