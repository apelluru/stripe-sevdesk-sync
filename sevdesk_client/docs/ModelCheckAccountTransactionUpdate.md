# ModelCheckAccountTransactionUpdate

CheckAccountTransaction model. Responsible for the transactions on payment accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_date** | **datetime** | Date the check account transaction was booked | [optional] 
**entry_date** | **datetime** | Date the check account transaction was imported | [optional] 
**paymt_purpose** | **str** | the purpose of the transaction | [optional] 
**amount** | **float** | Amount of the transaction | [optional] 
**payee_payer_name** | **str** | Name of the payee/payer | [optional] 
**check_account** | [**ModelCheckAccountTransactionUpdateCheckAccount**](ModelCheckAccountTransactionUpdateCheckAccount.md) |  | [optional] 
**status** | **int** | Status of the check account transaction.&lt;br&gt;       100 &lt;-&gt; Created&lt;br&gt;       200 &lt;-&gt; Linked&lt;br&gt;       300 &lt;-&gt; Private&lt;br&gt;       400 &lt;-&gt; Booked | [optional] 
**source_transaction** | [**ModelCheckAccountTransactionSourceTransaction**](ModelCheckAccountTransactionSourceTransaction.md) |  | [optional] 
**target_transaction** | [**ModelCheckAccountTransactionTargetTransaction**](ModelCheckAccountTransactionTargetTransaction.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_check_account_transaction_update import ModelCheckAccountTransactionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCheckAccountTransactionUpdate from a JSON string
model_check_account_transaction_update_instance = ModelCheckAccountTransactionUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelCheckAccountTransactionUpdate.to_json())

# convert the object into a dict
model_check_account_transaction_update_dict = model_check_account_transaction_update_instance.to_dict()
# create an instance of ModelCheckAccountTransactionUpdate from a dict
model_check_account_transaction_update_from_dict = ModelCheckAccountTransactionUpdate.from_dict(model_check_account_transaction_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


