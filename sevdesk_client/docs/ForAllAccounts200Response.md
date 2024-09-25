# ForAllAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ReceiptGuideDto]**](ReceiptGuideDto.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.for_all_accounts200_response import ForAllAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ForAllAccounts200Response from a JSON string
for_all_accounts200_response_instance = ForAllAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(ForAllAccounts200Response.to_json())

# convert the object into a dict
for_all_accounts200_response_dict = for_all_accounts200_response_instance.to_dict()
# create an instance of ForAllAccounts200Response from a dict
for_all_accounts200_response_from_dict = ForAllAccounts200Response.from_dict(for_all_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


