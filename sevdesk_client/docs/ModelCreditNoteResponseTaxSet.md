# ModelCreditNoteResponseTaxSet

**Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax set of the creditNote. Needs to be added if you chose the tax type custom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the object | 
**object_name** | **str** | Model name, which is &#39;TaxSet&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_response_tax_set import ModelCreditNoteResponseTaxSet

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNoteResponseTaxSet from a JSON string
model_credit_note_response_tax_set_instance = ModelCreditNoteResponseTaxSet.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNoteResponseTaxSet.to_json())

# convert the object into a dict
model_credit_note_response_tax_set_dict = model_credit_note_response_tax_set_instance.to_dict()
# create an instance of ModelCreditNoteResponseTaxSet from a dict
model_credit_note_response_tax_set_from_dict = ModelCreditNoteResponseTaxSet.from_dict(model_credit_note_response_tax_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


