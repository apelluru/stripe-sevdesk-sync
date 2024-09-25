# GetNextCustomerNumber200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | **str** | Next available customer number | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_next_customer_number200_response import GetNextCustomerNumber200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNextCustomerNumber200Response from a JSON string
get_next_customer_number200_response_instance = GetNextCustomerNumber200Response.from_json(json)
# print the JSON string representation of the object
print(GetNextCustomerNumber200Response.to_json())

# convert the object into a dict
get_next_customer_number200_response_dict = get_next_customer_number200_response_instance.to_dict()
# create an instance of GetNextCustomerNumber200Response from a dict
get_next_customer_number200_response_from_dict = GetNextCustomerNumber200Response.from_dict(get_next_customer_number200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


