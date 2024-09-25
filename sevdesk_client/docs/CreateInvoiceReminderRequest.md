# CreateInvoiceReminderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**CreateInvoiceReminderRequestInvoice**](CreateInvoiceReminderRequestInvoice.md) |  | 

## Example

```python
from sevdesk_client.openapi_client.models.create_invoice_reminder_request import CreateInvoiceReminderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceReminderRequest from a JSON string
create_invoice_reminder_request_instance = CreateInvoiceReminderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceReminderRequest.to_json())

# convert the object into a dict
create_invoice_reminder_request_dict = create_invoice_reminder_request_instance.to_dict()
# create an instance of CreateInvoiceReminderRequest from a dict
create_invoice_reminder_request_from_dict = CreateInvoiceReminderRequest.from_dict(create_invoice_reminder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


