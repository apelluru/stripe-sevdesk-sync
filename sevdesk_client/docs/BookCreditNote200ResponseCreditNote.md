# BookCreditNote200ResponseCreditNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the credit note | 
**object_name** | **str** | Internal object name which is &#39;CreditNote&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.book_credit_note200_response_credit_note import BookCreditNote200ResponseCreditNote

# TODO update the JSON string below
json = "{}"
# create an instance of BookCreditNote200ResponseCreditNote from a JSON string
book_credit_note200_response_credit_note_instance = BookCreditNote200ResponseCreditNote.from_json(json)
# print the JSON string representation of the object
print(BookCreditNote200ResponseCreditNote.to_json())

# convert the object into a dict
book_credit_note200_response_credit_note_dict = book_credit_note200_response_credit_note_instance.to_dict()
# create an instance of BookCreditNote200ResponseCreditNote from a dict
book_credit_note200_response_credit_note_from_dict = BookCreditNote200ResponseCreditNote.from_dict(book_credit_note200_response_credit_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


