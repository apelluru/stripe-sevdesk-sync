# ModelCheckAccountTransactionSourceTransaction

The check account transaction serving as the source of the rebooking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the check account transaction | 
**object_name** | **str** | Model name, which is &#39;CheckAccountTransaction&#39; | [default to 'CheckAccountTransaction']

## Example

```python
from sevdesk_client.openapi_client.models.model_check_account_transaction_source_transaction import ModelCheckAccountTransactionSourceTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCheckAccountTransactionSourceTransaction from a JSON string
model_check_account_transaction_source_transaction_instance = ModelCheckAccountTransactionSourceTransaction.from_json(json)
# print the JSON string representation of the object
print(ModelCheckAccountTransactionSourceTransaction.to_json())

# convert the object into a dict
model_check_account_transaction_source_transaction_dict = model_check_account_transaction_source_transaction_instance.to_dict()
# create an instance of ModelCheckAccountTransactionSourceTransaction from a dict
model_check_account_transaction_source_transaction_from_dict = ModelCheckAccountTransactionSourceTransaction.from_dict(model_check_account_transaction_source_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


