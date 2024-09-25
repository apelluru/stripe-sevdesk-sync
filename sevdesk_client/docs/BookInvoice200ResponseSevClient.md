# BookInvoice200ResponseSevClient

Client to which invoice belongs. Will be filled automatically

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the client | 
**object_name** | **str** | Model name, which is &#39;SevClient&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.book_invoice200_response_sev_client import BookInvoice200ResponseSevClient

# TODO update the JSON string below
json = "{}"
# create an instance of BookInvoice200ResponseSevClient from a JSON string
book_invoice200_response_sev_client_instance = BookInvoice200ResponseSevClient.from_json(json)
# print the JSON string representation of the object
print(BookInvoice200ResponseSevClient.to_json())

# convert the object into a dict
book_invoice200_response_sev_client_dict = book_invoice200_response_sev_client_instance.to_dict()
# create an instance of BookInvoice200ResponseSevClient from a dict
book_invoice200_response_sev_client_from_dict = BookInvoice200ResponseSevClient.from_dict(book_invoice200_response_sev_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


