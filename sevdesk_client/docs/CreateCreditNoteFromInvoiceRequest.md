# CreateCreditNoteFromInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**CreateCreditNoteFromInvoiceRequestInvoice**](CreateCreditNoteFromInvoiceRequestInvoice.md) |  | 

## Example

```python
from sevdesk_client.openapi_client.models.create_credit_note_from_invoice_request import CreateCreditNoteFromInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteFromInvoiceRequest from a JSON string
create_credit_note_from_invoice_request_instance = CreateCreditNoteFromInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteFromInvoiceRequest.to_json())

# convert the object into a dict
create_credit_note_from_invoice_request_dict = create_credit_note_from_invoice_request_instance.to_dict()
# create an instance of CreateCreditNoteFromInvoiceRequest from a dict
create_credit_note_from_invoice_request_from_dict = CreateCreditNoteFromInvoiceRequest.from_dict(create_credit_note_from_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


