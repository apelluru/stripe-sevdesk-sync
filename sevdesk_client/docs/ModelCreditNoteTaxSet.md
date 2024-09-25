# ModelCreditNoteTaxSet

**Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax set of the creditNote. Needs to be added if you chose the tax type custom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the object | 
**object_name** | **str** | Model name, which is &#39;TaxSet&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_tax_set import ModelCreditNoteTaxSet

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNoteTaxSet from a JSON string
model_credit_note_tax_set_instance = ModelCreditNoteTaxSet.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNoteTaxSet.to_json())

# convert the object into a dict
model_credit_note_tax_set_dict = model_credit_note_tax_set_instance.to_dict()
# create an instance of ModelCreditNoteTaxSet from a dict
model_credit_note_tax_set_from_dict = ModelCreditNoteTaxSet.from_dict(model_credit_note_tax_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


