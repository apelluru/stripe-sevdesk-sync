# ModelCheckAccountTransactionResponse

CheckAccountTransaction model. Responsible for the transactions on payment accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The check account transaction id | [optional] [readonly] 
**object_name** | **str** | The check account transaction object name | [optional] [readonly] 
**create** | **datetime** | Date of check account transaction creation | [optional] [readonly] 
**update** | **datetime** | Date of last check account transaction update | [optional] [readonly] 
**sev_client** | [**ModelCheckAccountTransactionResponseSevClient**](ModelCheckAccountTransactionResponseSevClient.md) |  | [optional] 
**value_date** | **datetime** | Date the check account transaction was imported | [optional] 
**entry_date** | **datetime** | Date the check account transaction was booked | [optional] 
**paymt_purpose** | **str** | The purpose of the transaction | [optional] 
**amount** | **str** | Amount of the transaction | [optional] 
**payee_payer_name** | **str** | Name of the other party | [optional] 
**payee_payer_acct_no** | **str** | IBAN or account number of the other party | [optional] 
**payee_payer_bank_code** | **str** | BIC or bank code of the other party | [optional] 
**check_account** | [**ModelCheckAccountTransactionResponseCheckAccount**](ModelCheckAccountTransactionResponseCheckAccount.md) |  | [optional] 
**status** | **str** | Status of the check account transaction.&lt;br&gt;       100 &lt;-&gt; Created&lt;br&gt;       200 &lt;-&gt; Linked&lt;br&gt;       300 &lt;-&gt; Private&lt;br&gt;       400 &lt;-&gt; Booked | [optional] [readonly] 
**source_transaction** | [**ModelCheckAccountTransactionResponseSourceTransaction**](ModelCheckAccountTransactionResponseSourceTransaction.md) |  | [optional] 
**target_transaction** | [**ModelCheckAccountTransactionResponseTargetTransaction**](ModelCheckAccountTransactionResponseTargetTransaction.md) |  | [optional] 
**enshrined** | **datetime** | Can only be set via [CheckAccountTransaction/{checkAccountTransactionId}/enshrine](#tag/CheckAccountTransaction/operation/checkAccountTransactionEnshrine)  | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_check_account_transaction_response import ModelCheckAccountTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCheckAccountTransactionResponse from a JSON string
model_check_account_transaction_response_instance = ModelCheckAccountTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(ModelCheckAccountTransactionResponse.to_json())

# convert the object into a dict
model_check_account_transaction_response_dict = model_check_account_transaction_response_instance.to_dict()
# create an instance of ModelCheckAccountTransactionResponse from a dict
model_check_account_transaction_response_from_dict = ModelCheckAccountTransactionResponse.from_dict(model_check_account_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


