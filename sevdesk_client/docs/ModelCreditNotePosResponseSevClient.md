# ModelCreditNotePosResponseSevClient

Client to which creditNote position belongs. Will be filled automatically

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the client | 
**object_name** | **str** | Model name, which is &#39;SevClient&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_pos_response_sev_client import ModelCreditNotePosResponseSevClient

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNotePosResponseSevClient from a JSON string
model_credit_note_pos_response_sev_client_instance = ModelCreditNotePosResponseSevClient.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNotePosResponseSevClient.to_json())

# convert the object into a dict
model_credit_note_pos_response_sev_client_dict = model_credit_note_pos_response_sev_client_instance.to_dict()
# create an instance of ModelCreditNotePosResponseSevClient from a dict
model_credit_note_pos_response_sev_client_from_dict = ModelCreditNotePosResponseSevClient.from_dict(model_credit_note_pos_response_sev_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


