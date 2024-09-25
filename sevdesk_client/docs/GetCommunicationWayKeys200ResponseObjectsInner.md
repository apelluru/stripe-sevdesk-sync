# GetCommunicationWayKeys200ResponseObjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the communication way key 1. ID: 1 - Privat 2. ID: 2 - Arbeit 3. ID: 3 - Fax 4. ID: 4 - Mobil 5. ID: 5 - \&quot; \&quot; 6. ID: 6 - Autobox 7. ID: 7 - Newsletter 8. ID: 8 - Rechnungsadresse | [optional] 
**object_name** | **str** | object name which is &#39;CommunicationWayKey&#39;. | [optional] 
**create** | **datetime** | Date the communication way key was created | [optional] 
**upadate** | **datetime** | Date the communication way key was last updated | [optional] 
**name** | **str** | Name of the communication way key | [optional] 
**translation_code** | **str** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_communication_way_keys200_response_objects_inner import GetCommunicationWayKeys200ResponseObjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommunicationWayKeys200ResponseObjectsInner from a JSON string
get_communication_way_keys200_response_objects_inner_instance = GetCommunicationWayKeys200ResponseObjectsInner.from_json(json)
# print the JSON string representation of the object
print(GetCommunicationWayKeys200ResponseObjectsInner.to_json())

# convert the object into a dict
get_communication_way_keys200_response_objects_inner_dict = get_communication_way_keys200_response_objects_inner_instance.to_dict()
# create an instance of GetCommunicationWayKeys200ResponseObjectsInner from a dict
get_communication_way_keys200_response_objects_inner_from_dict = GetCommunicationWayKeys200ResponseObjectsInner.from_dict(get_communication_way_keys200_response_objects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


