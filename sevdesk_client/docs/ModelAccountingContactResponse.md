# ModelAccountingContactResponse

Accounting contact model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The accounting contact id | [optional] [readonly] 
**object_name** | **str** | The accounting contact object name | [optional] [readonly] 
**create** | **datetime** | Date of accounting contact creation | [optional] [readonly] 
**update** | **datetime** | Date of last accounting contact update | [optional] [readonly] 
**contact** | [**ModelAccountingContactResponseContact**](ModelAccountingContactResponseContact.md) |  | [optional] 
**sev_client** | [**ModelAccountingContactResponseSevClient**](ModelAccountingContactResponseSevClient.md) |  | [optional] 
**debitor_number** | **str** | Debitor number of the accounting contact. | [optional] [readonly] 
**creditor_number** | **str** | Creditor number of the accounting contact. | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_accounting_contact_response import ModelAccountingContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccountingContactResponse from a JSON string
model_accounting_contact_response_instance = ModelAccountingContactResponse.from_json(json)
# print the JSON string representation of the object
print(ModelAccountingContactResponse.to_json())

# convert the object into a dict
model_accounting_contact_response_dict = model_accounting_contact_response_instance.to_dict()
# create an instance of ModelAccountingContactResponse from a dict
model_accounting_contact_response_from_dict = ModelAccountingContactResponse.from_dict(model_accounting_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


