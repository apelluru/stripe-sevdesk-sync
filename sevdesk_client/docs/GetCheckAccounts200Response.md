# GetCheckAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelCheckAccountResponse]**](ModelCheckAccountResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_check_accounts200_response import GetCheckAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCheckAccounts200Response from a JSON string
get_check_accounts200_response_instance = GetCheckAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetCheckAccounts200Response.to_json())

# convert the object into a dict
get_check_accounts200_response_dict = get_check_accounts200_response_instance.to_dict()
# create an instance of GetCheckAccounts200Response from a dict
get_check_accounts200_response_from_dict = GetCheckAccounts200Response.from_dict(get_check_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


