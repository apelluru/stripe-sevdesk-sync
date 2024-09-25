# CreditNoteGetPdf200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**base64encoded** | **bool** |  | [optional] 
**content** | **bytearray** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.credit_note_get_pdf200_response import CreditNoteGetPdf200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteGetPdf200Response from a JSON string
credit_note_get_pdf200_response_instance = CreditNoteGetPdf200Response.from_json(json)
# print the JSON string representation of the object
print(CreditNoteGetPdf200Response.to_json())

# convert the object into a dict
credit_note_get_pdf200_response_dict = credit_note_get_pdf200_response_instance.to_dict()
# create an instance of CreditNoteGetPdf200Response from a dict
credit_note_get_pdf200_response_from_dict = CreditNoteGetPdf200Response.from_dict(credit_note_get_pdf200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


