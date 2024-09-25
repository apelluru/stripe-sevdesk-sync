# CreateFileImportAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the check account | [optional] 
**import_type** | **str** | Import type. Transactions can be imported by this method on the check account. | [optional] 
**accounting_number** | **int** | The booking account used for this bank account, e.g. 1800 in SKR04 and 1200 in SKR03. Must be unique among all your CheckAccounts. Ignore to use a sensible default. | [optional] 
**iban** | **str** | IBAN of the bank account, without spaces | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.create_file_import_account import CreateFileImportAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileImportAccount from a JSON string
create_file_import_account_instance = CreateFileImportAccount.from_json(json)
# print the JSON string representation of the object
print(CreateFileImportAccount.to_json())

# convert the object into a dict
create_file_import_account_dict = create_file_import_account_instance.to_dict()
# create an instance of CreateFileImportAccount from a dict
create_file_import_account_from_dict = CreateFileImportAccount.from_dict(create_file_import_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


