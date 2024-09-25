# BookCreditNote200ResponseSevClient

Client to which creditNote belongs. Will be filled automatically

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the client | 
**object_name** | **str** | Model name, which is &#39;SevClient&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.book_credit_note200_response_sev_client import BookCreditNote200ResponseSevClient

# TODO update the JSON string below
json = "{}"
# create an instance of BookCreditNote200ResponseSevClient from a JSON string
book_credit_note200_response_sev_client_instance = BookCreditNote200ResponseSevClient.from_json(json)
# print the JSON string representation of the object
print(BookCreditNote200ResponseSevClient.to_json())

# convert the object into a dict
book_credit_note200_response_sev_client_dict = book_credit_note200_response_sev_client_instance.to_dict()
# create an instance of BookCreditNote200ResponseSevClient from a dict
book_credit_note200_response_sev_client_from_dict = BookCreditNote200ResponseSevClient.from_dict(book_credit_note200_response_sev_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


