# CreateCreditNoteFromInvoiceRequestInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the existing invoice | 
**object_name** | **str** | The objectName must be &#39;Invoice&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.create_credit_note_from_invoice_request_invoice import CreateCreditNoteFromInvoiceRequestInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteFromInvoiceRequestInvoice from a JSON string
create_credit_note_from_invoice_request_invoice_instance = CreateCreditNoteFromInvoiceRequestInvoice.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteFromInvoiceRequestInvoice.to_json())

# convert the object into a dict
create_credit_note_from_invoice_request_invoice_dict = create_credit_note_from_invoice_request_invoice_instance.to_dict()
# create an instance of CreateCreditNoteFromInvoiceRequestInvoice from a dict
create_credit_note_from_invoice_request_invoice_from_dict = CreateCreditNoteFromInvoiceRequestInvoice.from_dict(create_credit_note_from_invoice_request_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


