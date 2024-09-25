# ModelAccountingContactContact

The contact to which this accounting contact belongs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_accounting_contact_contact import ModelAccountingContactContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccountingContactContact from a JSON string
model_accounting_contact_contact_instance = ModelAccountingContactContact.from_json(json)
# print the JSON string representation of the object
print(ModelAccountingContactContact.to_json())

# convert the object into a dict
model_accounting_contact_contact_dict = model_accounting_contact_contact_instance.to_dict()
# create an instance of ModelAccountingContactContact from a dict
model_accounting_contact_contact_from_dict = ModelAccountingContactContact.from_dict(model_accounting_contact_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


