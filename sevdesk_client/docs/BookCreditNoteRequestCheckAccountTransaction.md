# BookCreditNoteRequestCheckAccountTransaction

The check account transaction on which should be booked.<br>      The transaction will be linked to the credit note.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the check account transaction on which should be booked. | 
**object_name** | **str** | Internal object name which is &#39;CheckAccountTransaction&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.book_credit_note_request_check_account_transaction import BookCreditNoteRequestCheckAccountTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BookCreditNoteRequestCheckAccountTransaction from a JSON string
book_credit_note_request_check_account_transaction_instance = BookCreditNoteRequestCheckAccountTransaction.from_json(json)
# print the JSON string representation of the object
print(BookCreditNoteRequestCheckAccountTransaction.to_json())

# convert the object into a dict
book_credit_note_request_check_account_transaction_dict = book_credit_note_request_check_account_transaction_instance.to_dict()
# create an instance of BookCreditNoteRequestCheckAccountTransaction from a dict
book_credit_note_request_check_account_transaction_from_dict = BookCreditNoteRequestCheckAccountTransaction.from_dict(book_credit_note_request_check_account_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


