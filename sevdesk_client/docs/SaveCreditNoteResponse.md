# SaveCreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_note** | [**ModelCreditNoteResponse**](ModelCreditNoteResponse.md) |  | [optional] 
**credit_note_pos** | [**List[ModelCreditNotePosResponse]**](ModelCreditNotePosResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.save_credit_note_response import SaveCreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCreditNoteResponse from a JSON string
save_credit_note_response_instance = SaveCreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(SaveCreditNoteResponse.to_json())

# convert the object into a dict
save_credit_note_response_dict = save_credit_note_response_instance.to_dict()
# create an instance of SaveCreditNoteResponse from a dict
save_credit_note_response_from_dict = SaveCreditNoteResponse.from_dict(save_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


