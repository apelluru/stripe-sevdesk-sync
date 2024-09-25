# GetCommunicationWayKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[GetCommunicationWayKeys200ResponseObjectsInner]**](GetCommunicationWayKeys200ResponseObjectsInner.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_communication_way_keys200_response import GetCommunicationWayKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommunicationWayKeys200Response from a JSON string
get_communication_way_keys200_response_instance = GetCommunicationWayKeys200Response.from_json(json)
# print the JSON string representation of the object
print(GetCommunicationWayKeys200Response.to_json())

# convert the object into a dict
get_communication_way_keys200_response_dict = get_communication_way_keys200_response_instance.to_dict()
# create an instance of GetCommunicationWayKeys200Response from a dict
get_communication_way_keys200_response_from_dict = GetCommunicationWayKeys200Response.from_dict(get_communication_way_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


