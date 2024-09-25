# CreateInvoiceReminderRequestInvoice

Invoice for the reminder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the invoice | 
**object_name** | **str** | Model name, which is &#39;Invoice&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.create_invoice_reminder_request_invoice import CreateInvoiceReminderRequestInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceReminderRequestInvoice from a JSON string
create_invoice_reminder_request_invoice_instance = CreateInvoiceReminderRequestInvoice.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceReminderRequestInvoice.to_json())

# convert the object into a dict
create_invoice_reminder_request_invoice_dict = create_invoice_reminder_request_invoice_instance.to_dict()
# create an instance of CreateInvoiceReminderRequestInvoice from a dict
create_invoice_reminder_request_invoice_from_dict = CreateInvoiceReminderRequestInvoice.from_dict(create_invoice_reminder_request_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


