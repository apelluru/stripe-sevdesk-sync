# SaveCreditNoteDiscountDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of discount to delete | 
**object_name** | **str** | Object name of discount | 

## Example

```python
from sevdesk_client.openapi_client.models.save_credit_note_discount_delete import SaveCreditNoteDiscountDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCreditNoteDiscountDelete from a JSON string
save_credit_note_discount_delete_instance = SaveCreditNoteDiscountDelete.from_json(json)
# print the JSON string representation of the object
print(SaveCreditNoteDiscountDelete.to_json())

# convert the object into a dict
save_credit_note_discount_delete_dict = save_credit_note_discount_delete_instance.to_dict()
# create an instance of SaveCreditNoteDiscountDelete from a dict
save_credit_note_discount_delete_from_dict = SaveCreditNoteDiscountDelete.from_dict(save_credit_note_discount_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


