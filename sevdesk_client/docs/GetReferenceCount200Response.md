# GetReferenceCount200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | **int** | the count of all references | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_reference_count200_response import GetReferenceCount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferenceCount200Response from a JSON string
get_reference_count200_response_instance = GetReferenceCount200Response.from_json(json)
# print the JSON string representation of the object
print(GetReferenceCount200Response.to_json())

# convert the object into a dict
get_reference_count200_response_dict = get_reference_count200_response_instance.to_dict()
# create an instance of GetReferenceCount200Response from a dict
get_reference_count200_response_from_dict = GetReferenceCount200Response.from_dict(get_reference_count200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


