# CreditNoteSendByRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_type** | **str** | Specifies the way in which the credit note was sent to the customer.&lt;br&gt;       Accepts &#39;VPR&#39; (print), &#39;VP&#39; (postal), &#39;VM&#39; (mail) and &#39;VPDF&#39; (downloaded pfd). | 
**send_draft** | **bool** | To create a draft of a credit note for internal use. This operation will not alter the status of the credit note or create bookings for reports. | 

## Example

```python
from sevdesk_client.openapi_client.models.credit_note_send_by_request import CreditNoteSendByRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteSendByRequest from a JSON string
credit_note_send_by_request_instance = CreditNoteSendByRequest.from_json(json)
# print the JSON string representation of the object
print(CreditNoteSendByRequest.to_json())

# convert the object into a dict
credit_note_send_by_request_dict = credit_note_send_by_request_instance.to_dict()
# create an instance of CreditNoteSendByRequest from a dict
credit_note_send_by_request_from_dict = CreditNoteSendByRequest.from_dict(credit_note_send_by_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


