# ModelAccountingContact

Accounting contact model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ModelAccountingContactContact**](ModelAccountingContactContact.md) |  | 
**debitor_number** | **int** | Debitor number of the accounting contact. | [optional] 
**creditor_number** | **int** | Creditor number of the accounting contact. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_accounting_contact import ModelAccountingContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccountingContact from a JSON string
model_accounting_contact_instance = ModelAccountingContact.from_json(json)
# print the JSON string representation of the object
print(ModelAccountingContact.to_json())

# convert the object into a dict
model_accounting_contact_dict = model_accounting_contact_instance.to_dict()
# create an instance of ModelAccountingContact from a dict
model_accounting_contact_from_dict = ModelAccountingContact.from_dict(model_accounting_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


