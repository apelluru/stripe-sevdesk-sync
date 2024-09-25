# GetLetterpapersWithThumb200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**letterpapers** | [**List[GetLetterpapersWithThumb200ResponseLetterpapersInner]**](GetLetterpapersWithThumb200ResponseLetterpapersInner.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_letterpapers_with_thumb200_response import GetLetterpapersWithThumb200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLetterpapersWithThumb200Response from a JSON string
get_letterpapers_with_thumb200_response_instance = GetLetterpapersWithThumb200Response.from_json(json)
# print the JSON string representation of the object
print(GetLetterpapersWithThumb200Response.to_json())

# convert the object into a dict
get_letterpapers_with_thumb200_response_dict = get_letterpapers_with_thumb200_response_instance.to_dict()
# create an instance of GetLetterpapersWithThumb200Response from a dict
get_letterpapers_with_thumb200_response_from_dict = GetLetterpapersWithThumb200Response.from_dict(get_letterpapers_with_thumb200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


