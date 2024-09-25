# ModelCreditNoteUpdateContact

The contact used in the creditNote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_update_contact import ModelCreditNoteUpdateContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNoteUpdateContact from a JSON string
model_credit_note_update_contact_instance = ModelCreditNoteUpdateContact.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNoteUpdateContact.to_json())

# convert the object into a dict
model_credit_note_update_contact_dict = model_credit_note_update_contact_instance.to_dict()
# create an instance of ModelCreditNoteUpdateContact from a dict
model_credit_note_update_contact_from_dict = ModelCreditNoteUpdateContact.from_dict(model_credit_note_update_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


