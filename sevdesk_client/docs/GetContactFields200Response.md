# GetContactFields200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelContactCustomFieldResponse]**](ModelContactCustomFieldResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_contact_fields200_response import GetContactFields200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactFields200Response from a JSON string
get_contact_fields200_response_instance = GetContactFields200Response.from_json(json)
# print the JSON string representation of the object
print(GetContactFields200Response.to_json())

# convert the object into a dict
get_contact_fields200_response_dict = get_contact_fields200_response_instance.to_dict()
# create an instance of GetContactFields200Response from a dict
get_contact_fields200_response_from_dict = GetContactFields200Response.from_dict(get_contact_fields200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


