# CreateClearingAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the check account | [optional] 
**accounting_number** | **int** | The booking account used for this clearing account, e.g. 3320 in SKR04 and 1723 in SKR03. Must be unique among all your CheckAccounts. Ask your tax consultant what to choose. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.create_clearing_account import CreateClearingAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClearingAccount from a JSON string
create_clearing_account_instance = CreateClearingAccount.from_json(json)
# print the JSON string representation of the object
print(CreateClearingAccount.to_json())

# convert the object into a dict
create_clearing_account_dict = create_clearing_account_instance.to_dict()
# create an instance of CreateClearingAccount from a dict
create_clearing_account_from_dict = CreateClearingAccount.from_dict(create_clearing_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


