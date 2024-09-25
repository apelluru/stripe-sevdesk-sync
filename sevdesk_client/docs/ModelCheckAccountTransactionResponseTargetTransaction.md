# ModelCheckAccountTransactionResponseTargetTransaction

The check account transaction serving as the target of the rebooking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the check account transaction | 
**object_name** | **str** | Model name, which is &#39;CheckAccountTransaction&#39; | [default to 'CheckAccountTransaction']

## Example

```python
from sevdesk_client.openapi_client.models.model_check_account_transaction_response_target_transaction import ModelCheckAccountTransactionResponseTargetTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCheckAccountTransactionResponseTargetTransaction from a JSON string
model_check_account_transaction_response_target_transaction_instance = ModelCheckAccountTransactionResponseTargetTransaction.from_json(json)
# print the JSON string representation of the object
print(ModelCheckAccountTransactionResponseTargetTransaction.to_json())

# convert the object into a dict
model_check_account_transaction_response_target_transaction_dict = model_check_account_transaction_response_target_transaction_instance.to_dict()
# create an instance of ModelCheckAccountTransactionResponseTargetTransaction from a dict
model_check_account_transaction_response_target_transaction_from_dict = ModelCheckAccountTransactionResponseTargetTransaction.from_dict(model_check_account_transaction_response_target_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


