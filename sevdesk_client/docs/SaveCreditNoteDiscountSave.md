# SaveCreditNoteDiscountSave


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | **bool** | Defines if this is a discount or a surcharge | 
**text** | **str** | A text for your discount | 
**percentage** | **bool** | Defines if this is a percentage or an absolute discount | 
**value** | **float** | Value of the discount | 
**object_name** | **str** | Object name of the discount | 
**map_all** | **bool** | Internal param | 

## Example

```python
from sevdesk_client.openapi_client.models.save_credit_note_discount_save import SaveCreditNoteDiscountSave

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCreditNoteDiscountSave from a JSON string
save_credit_note_discount_save_instance = SaveCreditNoteDiscountSave.from_json(json)
# print the JSON string representation of the object
print(SaveCreditNoteDiscountSave.to_json())

# convert the object into a dict
save_credit_note_discount_save_dict = save_credit_note_discount_save_instance.to_dict()
# create an instance of SaveCreditNoteDiscountSave from a dict
save_credit_note_discount_save_from_dict = SaveCreditNoteDiscountSave.from_dict(save_credit_note_discount_save_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


