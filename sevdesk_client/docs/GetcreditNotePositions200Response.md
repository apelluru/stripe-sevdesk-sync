# GetcreditNotePositions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelCreditNotePosResponse]**](ModelCreditNotePosResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.getcredit_note_positions200_response import GetcreditNotePositions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetcreditNotePositions200Response from a JSON string
getcredit_note_positions200_response_instance = GetcreditNotePositions200Response.from_json(json)
# print the JSON string representation of the object
print(GetcreditNotePositions200Response.to_json())

# convert the object into a dict
getcredit_note_positions200_response_dict = getcredit_note_positions200_response_instance.to_dict()
# create an instance of GetcreditNotePositions200Response from a dict
getcredit_note_positions200_response_from_dict = GetcreditNotePositions200Response.from_dict(getcredit_note_positions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


