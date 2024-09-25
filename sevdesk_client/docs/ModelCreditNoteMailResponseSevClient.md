# ModelCreditNoteMailResponseSevClient

Client to which creditNote belongs. Will be filled automatically

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the client | 
**object_name** | **str** | Model name, which is &#39;SevClient&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_mail_response_sev_client import ModelCreditNoteMailResponseSevClient

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNoteMailResponseSevClient from a JSON string
model_credit_note_mail_response_sev_client_instance = ModelCreditNoteMailResponseSevClient.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNoteMailResponseSevClient.to_json())

# convert the object into a dict
model_credit_note_mail_response_sev_client_dict = model_credit_note_mail_response_sev_client_instance.to_dict()
# create an instance of ModelCreditNoteMailResponseSevClient from a dict
model_credit_note_mail_response_sev_client_from_dict = ModelCreditNoteMailResponseSevClient.from_dict(model_credit_note_mail_response_sev_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


