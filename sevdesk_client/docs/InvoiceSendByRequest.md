# InvoiceSendByRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_type** | **str** | Specifies the way in which the invoice was sent to the customer.&lt;br&gt;       Accepts &#39;VPR&#39; (print), &#39;VP&#39; (postal), &#39;VM&#39; (mail) and &#39;VPDF&#39; (downloaded pfd). | 
**send_draft** | **bool** | To create a draft of an invoice for internal use. This operation will not alter the status of the invoice or create bookings for reports. | 

## Example

```python
from sevdesk_client.openapi_client.models.invoice_send_by_request import InvoiceSendByRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSendByRequest from a JSON string
invoice_send_by_request_instance = InvoiceSendByRequest.from_json(json)
# print the JSON string representation of the object
print(InvoiceSendByRequest.to_json())

# convert the object into a dict
invoice_send_by_request_dict = invoice_send_by_request_instance.to_dict()
# create an instance of InvoiceSendByRequest from a dict
invoice_send_by_request_from_dict = InvoiceSendByRequest.from_dict(invoice_send_by_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


