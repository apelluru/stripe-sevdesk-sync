# CreateCreditNoteFromInvoice201ResponseObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_note** | [**ModelCreditNoteResponse**](ModelCreditNoteResponse.md) |  | [optional] 
**credit_note_pos** | [**List[ModelCreditNotePosResponse]**](ModelCreditNotePosResponse.md) | An array of creditNote positions | [optional] 
**discount** | [**List[ModelDiscountsResponse]**](ModelDiscountsResponse.md) | An array of discounts (can be empty) | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.create_credit_note_from_invoice201_response_objects import CreateCreditNoteFromInvoice201ResponseObjects

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteFromInvoice201ResponseObjects from a JSON string
create_credit_note_from_invoice201_response_objects_instance = CreateCreditNoteFromInvoice201ResponseObjects.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteFromInvoice201ResponseObjects.to_json())

# convert the object into a dict
create_credit_note_from_invoice201_response_objects_dict = create_credit_note_from_invoice201_response_objects_instance.to_dict()
# create an instance of CreateCreditNoteFromInvoice201ResponseObjects from a dict
create_credit_note_from_invoice201_response_objects_from_dict = CreateCreditNoteFromInvoice201ResponseObjects.from_dict(create_credit_note_from_invoice201_response_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


