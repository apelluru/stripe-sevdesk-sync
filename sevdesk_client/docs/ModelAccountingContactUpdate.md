# ModelAccountingContactUpdate

Accounting contact model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ModelAccountingContactUpdateContact**](ModelAccountingContactUpdateContact.md) |  | [optional] 
**debitor_number** | **int** | Debitor number of the accounting contact. | [optional] 
**creditor_number** | **int** | Creditor number of the accounting contact. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_accounting_contact_update import ModelAccountingContactUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccountingContactUpdate from a JSON string
model_accounting_contact_update_instance = ModelAccountingContactUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelAccountingContactUpdate.to_json())

# convert the object into a dict
model_accounting_contact_update_dict = model_accounting_contact_update_instance.to_dict()
# create an instance of ModelAccountingContactUpdate from a dict
model_accounting_contact_update_from_dict = ModelAccountingContactUpdate.from_dict(model_accounting_contact_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


