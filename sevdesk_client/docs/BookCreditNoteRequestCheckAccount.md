# BookCreditNoteRequestCheckAccount

The check account on which should be booked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the check account on which should be booked. | 
**object_name** | **str** | Internal object name which is &#39;CheckAccount&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.book_credit_note_request_check_account import BookCreditNoteRequestCheckAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BookCreditNoteRequestCheckAccount from a JSON string
book_credit_note_request_check_account_instance = BookCreditNoteRequestCheckAccount.from_json(json)
# print the JSON string representation of the object
print(BookCreditNoteRequestCheckAccount.to_json())

# convert the object into a dict
book_credit_note_request_check_account_dict = book_credit_note_request_check_account_instance.to_dict()
# create an instance of BookCreditNoteRequestCheckAccount from a dict
book_credit_note_request_check_account_from_dict = BookCreditNoteRequestCheckAccount.from_dict(book_credit_note_request_check_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


