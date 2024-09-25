# ModelCheckAccountTransactionCheckAccount

The check account to which the transaction belongs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the check account | 
**object_name** | **str** | Model name, which is &#39;CheckAccount&#39; | [default to 'CheckAccount']

## Example

```python
from sevdesk_client.openapi_client.models.model_check_account_transaction_check_account import ModelCheckAccountTransactionCheckAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCheckAccountTransactionCheckAccount from a JSON string
model_check_account_transaction_check_account_instance = ModelCheckAccountTransactionCheckAccount.from_json(json)
# print the JSON string representation of the object
print(ModelCheckAccountTransactionCheckAccount.to_json())

# convert the object into a dict
model_check_account_transaction_check_account_dict = model_check_account_transaction_check_account_instance.to_dict()
# create an instance of ModelCheckAccountTransactionCheckAccount from a dict
model_check_account_transaction_check_account_from_dict = ModelCheckAccountTransactionCheckAccount.from_dict(model_check_account_transaction_check_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


