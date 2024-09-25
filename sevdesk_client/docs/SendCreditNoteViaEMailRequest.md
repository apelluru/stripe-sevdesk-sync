# SendCreditNoteViaEMailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_email** | **str** | The recipient of the email. | 
**subject** | **str** | The subject of the email. | 
**text** | **str** | The text of the email. Can contain html. | 
**copy** | **bool** | Should a copy of this email be sent to you? | [optional] 
**additional_attachments** | **str** | Additional attachments to the mail. String of IDs of existing documents in your       *                      sevdesk account separated by &#39;,&#39; | [optional] 
**cc_email** | **str** | String of mail addresses to be put as cc separated by &#39;,&#39; | [optional] 
**bcc_email** | **str** | String of mail addresses to be put as bcc separated by &#39;,&#39; | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.send_credit_note_via_e_mail_request import SendCreditNoteViaEMailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendCreditNoteViaEMailRequest from a JSON string
send_credit_note_via_e_mail_request_instance = SendCreditNoteViaEMailRequest.from_json(json)
# print the JSON string representation of the object
print(SendCreditNoteViaEMailRequest.to_json())

# convert the object into a dict
send_credit_note_via_e_mail_request_dict = send_credit_note_via_e_mail_request_instance.to_dict()
# create an instance of SendCreditNoteViaEMailRequest from a dict
send_credit_note_via_e_mail_request_from_dict = SendCreditNoteViaEMailRequest.from_dict(send_credit_note_via_e_mail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


