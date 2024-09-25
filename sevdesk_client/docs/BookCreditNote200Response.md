# BookCreditNote200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object_name** | **str** |  | [optional] 
**additional_information** | **str** |  | [optional] 
**create** | **datetime** | Date of email creation | [optional] 
**credit_note** | [**BookCreditNote200ResponseCreditNote**](BookCreditNote200ResponseCreditNote.md) |  | [optional] 
**from_status** | **str** |  | [optional] 
**to_status** | **str** |  | [optional] 
**ammount_payed** | **str** |  | [optional] 
**booking_date** | **datetime** |  | [optional] 
**sev_client** | [**BookCreditNote200ResponseSevClient**](BookCreditNote200ResponseSevClient.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.book_credit_note200_response import BookCreditNote200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BookCreditNote200Response from a JSON string
book_credit_note200_response_instance = BookCreditNote200Response.from_json(json)
# print the JSON string representation of the object
print(BookCreditNote200Response.to_json())

# convert the object into a dict
book_credit_note200_response_dict = book_credit_note200_response_instance.to_dict()
# create an instance of BookCreditNote200Response from a dict
book_credit_note200_response_from_dict = BookCreditNote200Response.from_dict(book_credit_note200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


