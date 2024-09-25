# GetCommunicationWays200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelCommunicationWayResponse]**](ModelCommunicationWayResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_communication_ways200_response import GetCommunicationWays200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommunicationWays200Response from a JSON string
get_communication_ways200_response_instance = GetCommunicationWays200Response.from_json(json)
# print the JSON string representation of the object
print(GetCommunicationWays200Response.to_json())

# convert the object into a dict
get_communication_ways200_response_dict = get_communication_ways200_response_instance.to_dict()
# create an instance of GetCommunicationWays200Response from a dict
get_communication_ways200_response_from_dict = GetCommunicationWays200Response.from_dict(get_communication_ways200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


