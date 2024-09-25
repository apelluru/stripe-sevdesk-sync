# BookInvoice200ResponseCreditNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the invoice | 
**object_name** | **str** | Internal object name which is &#39;Invoice&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.book_invoice200_response_credit_note import BookInvoice200ResponseCreditNote

# TODO update the JSON string below
json = "{}"
# create an instance of BookInvoice200ResponseCreditNote from a JSON string
book_invoice200_response_credit_note_instance = BookInvoice200ResponseCreditNote.from_json(json)
# print the JSON string representation of the object
print(BookInvoice200ResponseCreditNote.to_json())

# convert the object into a dict
book_invoice200_response_credit_note_dict = book_invoice200_response_credit_note_instance.to_dict()
# create an instance of BookInvoice200ResponseCreditNote from a dict
book_invoice200_response_credit_note_from_dict = BookInvoice200ResponseCreditNote.from_dict(book_invoice200_response_credit_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


