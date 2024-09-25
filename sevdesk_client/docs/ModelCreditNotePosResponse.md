# ModelCreditNotePosResponse

creditNote position model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The creditNote position id | [optional] [readonly] 
**object_name** | **str** | The creditNote position object name | [optional] [readonly] 
**create** | **str** | Date of creditNote position creation | [optional] [readonly] 
**update** | **str** | Date of last creditNote position update | [optional] [readonly] 
**credit_note** | [**ModelCreditNotePosResponseCreditNote**](ModelCreditNotePosResponseCreditNote.md) |  | 
**part** | [**ModelCreditNotePosResponsePart**](ModelCreditNotePosResponsePart.md) |  | [optional] 
**quantity** | **str** | Quantity of the article/part | 
**price** | **str** | Price of the article/part. Is either gross or net, depending on the sevdesk account setting. | [optional] 
**price_net** | **str** | Net price of the part | [optional] [readonly] 
**price_tax** | **str** | Tax on the price of the part | [optional] 
**price_gross** | **str** | Gross price of the part | [optional] 
**name** | **str** | Name of the article/part. | [optional] 
**unity** | [**ModelCreditNotePosResponseUnity**](ModelCreditNotePosResponseUnity.md) |  | 
**sev_client** | [**ModelCreditNotePosResponseSevClient**](ModelCreditNotePosResponseSevClient.md) |  | [optional] 
**position_number** | **str** | Position number of your position. Can be used to creditNote multiple positions. | [optional] 
**text** | **str** | A text describing your position. | [optional] 
**discount** | **str** | An optional discount of the position. | [optional] 
**optional** | **bool** | Defines if the position is optional. | [optional] 
**tax_rate** | **str** | Tax rate of the position. | 
**sum_discount** | **str** | Discount sum of the position | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_pos_response import ModelCreditNotePosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNotePosResponse from a JSON string
model_credit_note_pos_response_instance = ModelCreditNotePosResponse.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNotePosResponse.to_json())

# convert the object into a dict
model_credit_note_pos_response_dict = model_credit_note_pos_response_instance.to_dict()
# create an instance of ModelCreditNotePosResponse from a dict
model_credit_note_pos_response_from_dict = ModelCreditNotePosResponse.from_dict(model_credit_note_pos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


