# ModelCheckAccountTransaction

CheckAccountTransaction model. Responsible for the transactions on payment accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The check account transaction id | [optional] [readonly] 
**object_name** | **str** | The check account transaction object name | [optional] [readonly] 
**create** | **datetime** | Date of check account transaction creation | [optional] [readonly] 
**update** | **datetime** | Date of last check account transaction update | [optional] [readonly] 
**sev_client** | [**ModelCheckAccountTransactionSevClient**](ModelCheckAccountTransactionSevClient.md) |  | [optional] 
**value_date** | **datetime** | Date the check account transaction was booked | 
**entry_date** | **datetime** | Date the check account transaction was imported | [optional] 
**paymt_purpose** | **str** | The purpose of the transaction | [optional] 
**amount** | **float** | Amount of the transaction | 
**payee_payer_name** | **str** | Name of the other party | 
**payee_payer_acct_no** | **str** | IBAN or account number of the other party | [optional] 
**payee_payer_bank_code** | **str** | BIC or bank code of the other party | [optional] 
**check_account** | [**ModelCheckAccountTransactionCheckAccount**](ModelCheckAccountTransactionCheckAccount.md) |  | 
**status** | **int** | Status of the check account transaction.&lt;br&gt;       100 &lt;-&gt; Created&lt;br&gt;       200 &lt;-&gt; Linked&lt;br&gt;       300 &lt;-&gt; Private&lt;br&gt;       400 &lt;-&gt; Booked | 
**source_transaction** | [**ModelCheckAccountTransactionSourceTransaction**](ModelCheckAccountTransactionSourceTransaction.md) |  | [optional] 
**target_transaction** | [**ModelCheckAccountTransactionTargetTransaction**](ModelCheckAccountTransactionTargetTransaction.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_check_account_transaction import ModelCheckAccountTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCheckAccountTransaction from a JSON string
model_check_account_transaction_instance = ModelCheckAccountTransaction.from_json(json)
# print the JSON string representation of the object
print(ModelCheckAccountTransaction.to_json())

# convert the object into a dict
model_check_account_transaction_dict = model_check_account_transaction_instance.to_dict()
# create an instance of ModelCheckAccountTransaction from a dict
model_check_account_transaction_from_dict = ModelCheckAccountTransaction.from_dict(model_check_account_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


