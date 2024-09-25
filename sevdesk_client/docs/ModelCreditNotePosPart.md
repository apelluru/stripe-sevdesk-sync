# ModelCreditNotePosPart

Part from your inventory which is used in the position.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the part | 
**object_name** | **str** | Model name, which is &#39;Part&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_pos_part import ModelCreditNotePosPart

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNotePosPart from a JSON string
model_credit_note_pos_part_instance = ModelCreditNotePosPart.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNotePosPart.to_json())

# convert the object into a dict
model_credit_note_pos_part_dict = model_credit_note_pos_part_instance.to_dict()
# create an instance of ModelCreditNotePosPart from a dict
model_credit_note_pos_part_from_dict = ModelCreditNotePosPart.from_dict(model_credit_note_pos_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


