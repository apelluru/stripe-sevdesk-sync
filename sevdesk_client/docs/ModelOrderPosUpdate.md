# ModelOrderPosUpdate

Order position model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The order position id | [optional] [readonly] 
**object_name** | **str** | The order position object name | [optional] [readonly] 
**create** | **datetime** | Date of order position creation | [optional] [readonly] 
**update** | **datetime** | Date of last order position update | [optional] [readonly] 
**order** | [**ModelOrderPosOrder**](ModelOrderPosOrder.md) |  | [optional] 
**part** | [**ModelCreditNotePosPart**](ModelCreditNotePosPart.md) |  | [optional] 
**quantity** | **float** | Quantity of the article/part | [optional] 
**price** | **float** | Price of the article/part. Is either gross or net, depending on the sevdesk account setting. | [optional] 
**price_net** | **float** | Net price of the part | [optional] [readonly] 
**price_tax** | **float** | Tax on the price of the part | [optional] 
**price_gross** | **float** | Gross price of the part | [optional] 
**name** | **str** | Name of the article/part. | [optional] 
**unity** | [**ModelCreditNotePosUnity**](ModelCreditNotePosUnity.md) |  | [optional] 
**sev_client** | [**ModelOrderPosSevClient**](ModelOrderPosSevClient.md) |  | [optional] 
**position_number** | **int** | Position number of your position. Can be used to order multiple positions. | [optional] 
**text** | **str** | A text describing your position. | [optional] 
**discount** | **float** | An optional discount of the position. | [optional] 
**optional** | **bool** | Defines if the position is optional. | [optional] 
**tax_rate** | **float** | Tax rate of the position. | [optional] 
**sum_discount** | **float** | Discount sum of the position | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_pos_update import ModelOrderPosUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderPosUpdate from a JSON string
model_order_pos_update_instance = ModelOrderPosUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelOrderPosUpdate.to_json())

# convert the object into a dict
model_order_pos_update_dict = model_order_pos_update_instance.to_dict()
# create an instance of ModelOrderPosUpdate from a dict
model_order_pos_update_from_dict = ModelOrderPosUpdate.from_dict(model_order_pos_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


