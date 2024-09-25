# ModelCheckAccount

CheckAccount model. Responsible for the payment accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The check account id | [optional] [readonly] 
**object_name** | **str** | The check account object name | [optional] [readonly] 
**create** | **datetime** | Date of check account creation | [optional] [readonly] 
**update** | **datetime** | Date of last check account update | [optional] [readonly] 
**sev_client** | [**ModelCheckAccountSevClient**](ModelCheckAccountSevClient.md) |  | [optional] 
**name** | **str** | Name of the check account | 
**type** | **str** | The type of the check account. Account with a CSV or MT940 import are regarded as online.&lt;br&gt;       Apart from that, created check accounts over the API need to be offline, as online accounts with an active connection       to a bank application can not be managed over the API. | 
**import_type** | **str** | Import type. Transactions can be imported by this method on the check account. | [optional] 
**currency** | **str** | The currency of the check account. | 
**default_account** | **int** | Defines if this check account is the default account. | [optional] [default to 0]
**status** | **int** | Status of the check account. 0 &lt;-&gt; Archived - 100 &lt;-&gt; Active | [default to 100]
**bank_server** | **str** | Bank server of check account | [optional] [readonly] 
**auto_map_transactions** | **int** | Defines if transactions on this account are automatically mapped to invoice and vouchers when imported if possible. | [optional] [default to 1]
**accounting_number** | **str** | The booking account used for this bank account, e.g. 1800 in SKR04 and 1200 in SKR03. Must be unique among all your CheckAccounts. Ignore to use a sensible default. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_check_account import ModelCheckAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCheckAccount from a JSON string
model_check_account_instance = ModelCheckAccount.from_json(json)
# print the JSON string representation of the object
print(ModelCheckAccount.to_json())

# convert the object into a dict
model_check_account_dict = model_check_account_instance.to_dict()
# create an instance of ModelCheckAccount from a dict
model_check_account_from_dict = ModelCheckAccount.from_dict(model_check_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


