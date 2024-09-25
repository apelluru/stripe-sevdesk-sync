# ModelCreditNotePosCreditNote

The creditNote to which the position belongs.  <span style='color:red'>Required</span> if you want to create/update an credit note position for an existing credit note\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the creditNote | 
**object_name** | **str** | Model name, which is &#39;creditNote&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_pos_credit_note import ModelCreditNotePosCreditNote

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNotePosCreditNote from a JSON string
model_credit_note_pos_credit_note_instance = ModelCreditNotePosCreditNote.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNotePosCreditNote.to_json())

# convert the object into a dict
model_credit_note_pos_credit_note_dict = model_credit_note_pos_credit_note_instance.to_dict()
# create an instance of ModelCreditNotePosCreditNote from a dict
model_credit_note_pos_credit_note_from_dict = ModelCreditNotePosCreditNote.from_dict(model_credit_note_pos_credit_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


