# GetTransactions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelCheckAccountTransactionResponse]**](ModelCheckAccountTransactionResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_transactions200_response import GetTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactions200Response from a JSON string
get_transactions200_response_instance = GetTransactions200Response.from_json(json)
# print the JSON string representation of the object
print(GetTransactions200Response.to_json())

# convert the object into a dict
get_transactions200_response_dict = get_transactions200_response_instance.to_dict()
# create an instance of GetTransactions200Response from a dict
get_transactions200_response_from_dict = GetTransactions200Response.from_dict(get_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


