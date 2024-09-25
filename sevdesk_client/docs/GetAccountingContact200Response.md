# GetAccountingContact200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelAccountingContactResponse]**](ModelAccountingContactResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_accounting_contact200_response import GetAccountingContact200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountingContact200Response from a JSON string
get_accounting_contact200_response_instance = GetAccountingContact200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountingContact200Response.to_json())

# convert the object into a dict
get_accounting_contact200_response_dict = get_accounting_contact200_response_instance.to_dict()
# create an instance of GetAccountingContact200Response from a dict
get_accounting_contact200_response_from_dict = GetAccountingContact200Response.from_dict(get_accounting_contact200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


