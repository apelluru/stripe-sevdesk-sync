# ModelCommunicationWayKey

The key of the communication way.<br> Similar to the category of addresses.<br> For all communication way keys please send a GET to /CommunicationWayKey.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the key | 
**object_name** | **str** | Model name, which is &#39;CommunicationWayKey&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_communication_way_key import ModelCommunicationWayKey

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCommunicationWayKey from a JSON string
model_communication_way_key_instance = ModelCommunicationWayKey.from_json(json)
# print the JSON string representation of the object
print(ModelCommunicationWayKey.to_json())

# convert the object into a dict
model_communication_way_key_dict = model_communication_way_key_instance.to_dict()
# create an instance of ModelCommunicationWayKey from a dict
model_communication_way_key_from_dict = ModelCommunicationWayKey.from_dict(model_communication_way_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


