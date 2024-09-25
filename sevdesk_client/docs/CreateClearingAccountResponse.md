# CreateClearingAccountResponse

CheckAccount model. Showing the properties relevant to clearing accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The check account id | [optional] 
**object_name** | **str** | The check account object name, always &#39;CheckAccount&#39; | [optional] 
**create** | **datetime** | Date of check account creation | [optional] 
**update** | **datetime** | Date of last check account update | [optional] 
**sev_client** | [**CreateFileImportAccountResponseSevClient**](CreateFileImportAccountResponseSevClient.md) |  | [optional] 
**name** | **str** | Name of the check account | [optional] 
**type** | **str** | The type of the check account. Clearing accounts are regarded as offline. | [optional] 
**currency** | **str** | The currency of the check account. | [optional] 
**default_account** | **str** | Defines if this check account is the default account. | [optional] [default to '0']
**status** | **str** | Status of the check account. 0 &lt;-&gt; Archived - 100 &lt;-&gt; Active | [optional] [default to '100']
**accounting_number** | **str** | The booking account used for this clearing account. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.create_clearing_account_response import CreateClearingAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClearingAccountResponse from a JSON string
create_clearing_account_response_instance = CreateClearingAccountResponse.from_json(json)
# print the JSON string representation of the object
print(CreateClearingAccountResponse.to_json())

# convert the object into a dict
create_clearing_account_response_dict = create_clearing_account_response_instance.to_dict()
# create an instance of CreateClearingAccountResponse from a dict
create_clearing_account_response_from_dict = CreateClearingAccountResponse.from_dict(create_clearing_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


