# SaveCreditNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_note** | [**ModelCreditNote**](ModelCreditNote.md) |  | 
**credit_note_pos_save** | [**List[ModelCreditNotePos]**](ModelCreditNotePos.md) |  | [optional] 
**credit_note_pos_delete** | [**SaveCreditNoteCreditNotePosDelete**](SaveCreditNoteCreditNotePosDelete.md) |  | [optional] 
**discount_save** | [**SaveCreditNoteDiscountSave**](SaveCreditNoteDiscountSave.md) |  | [optional] 
**discount_delete** | [**SaveCreditNoteDiscountDelete**](SaveCreditNoteDiscountDelete.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_credit_note import SaveCreditNote

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCreditNote from a JSON string
save_credit_note_instance = SaveCreditNote.from_json(json)
# print the JSON string representation of the object
print(SaveCreditNote.to_json())

# convert the object into a dict
save_credit_note_dict = save_credit_note_instance.to_dict()
# create an instance of SaveCreditNote from a dict
save_credit_note_from_dict = SaveCreditNote.from_dict(save_credit_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


