# ModelCreditNoteMailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**object_name** | **str** |  | [optional] 
**additional_information** | **str** |  | [optional] 
**create** | **datetime** | Date of email creation | [optional] [readonly] 
**update** | **datetime** | Date of last email update | [optional] [readonly] 
**object** | [**ModelCreditNoteResponse**](ModelCreditNoteResponse.md) |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**sev_client** | [**ModelCreditNoteMailResponseSevClient**](ModelCreditNoteMailResponseSevClient.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_mail_response import ModelCreditNoteMailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNoteMailResponse from a JSON string
model_credit_note_mail_response_instance = ModelCreditNoteMailResponse.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNoteMailResponse.to_json())

# convert the object into a dict
model_credit_note_mail_response_dict = model_credit_note_mail_response_instance.to_dict()
# create an instance of ModelCreditNoteMailResponse from a dict
model_credit_note_mail_response_from_dict = ModelCreditNoteMailResponse.from_dict(model_credit_note_mail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


