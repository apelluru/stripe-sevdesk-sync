# ModelCreditNotePos

creditNote position model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The creditNote position id. | [optional] [readonly] 
**object_name** | **str** | The creditNote position object name | 
**map_all** | **bool** |  | 
**create** | **str** | Date of creditNote position creation | [optional] [readonly] 
**update** | **str** | Date of last creditNote position update | [optional] [readonly] 
**credit_note** | [**ModelCreditNotePosCreditNote**](ModelCreditNotePosCreditNote.md) |  | [optional] 
**part** | [**ModelCreditNotePosPart**](ModelCreditNotePosPart.md) |  | [optional] 
**quantity** | **float** | Quantity of the article/part | 
**price** | **float** | Price of the article/part. Is either gross or net, depending on the sevdesk account setting. | [optional] 
**price_net** | **float** | Net price of the part | [optional] [readonly] 
**price_tax** | **float** | Tax on the price of the part | [optional] 
**price_gross** | **float** | Gross price of the part | [optional] 
**name** | **str** | Name of the article/part. | [optional] 
**unity** | [**ModelCreditNotePosUnity**](ModelCreditNotePosUnity.md) |  | 
**sev_client** | [**ModelCreditNotePosSevClient**](ModelCreditNotePosSevClient.md) |  | [optional] 
**position_number** | **int** | Position number of your position. Can be used to creditNote multiple positions. | [optional] 
**text** | **str** | A text describing your position. | [optional] 
**discount** | **float** | An optional discount of the position. | [optional] 
**optional** | **bool** | Defines if the position is optional. | [optional] 
**tax_rate** | **float** | Tax rate of the position. | 
**sum_discount** | **float** | Discount sum of the position | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_pos import ModelCreditNotePos

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNotePos from a JSON string
model_credit_note_pos_instance = ModelCreditNotePos.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNotePos.to_json())

# convert the object into a dict
model_credit_note_pos_dict = model_credit_note_pos_instance.to_dict()
# create an instance of ModelCreditNotePos from a dict
model_credit_note_pos_from_dict = ModelCreditNotePos.from_dict(model_credit_note_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


