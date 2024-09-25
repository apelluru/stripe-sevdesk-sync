# FindContactsByCustomFieldValue200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelContactResponse]**](ModelContactResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.find_contacts_by_custom_field_value200_response import FindContactsByCustomFieldValue200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindContactsByCustomFieldValue200Response from a JSON string
find_contacts_by_custom_field_value200_response_instance = FindContactsByCustomFieldValue200Response.from_json(json)
# print the JSON string representation of the object
print(FindContactsByCustomFieldValue200Response.to_json())

# convert the object into a dict
find_contacts_by_custom_field_value200_response_dict = find_contacts_by_custom_field_value200_response_instance.to_dict()
# create an instance of FindContactsByCustomFieldValue200Response from a dict
find_contacts_by_custom_field_value200_response_from_dict = FindContactsByCustomFieldValue200Response.from_dict(find_contacts_by_custom_field_value200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


