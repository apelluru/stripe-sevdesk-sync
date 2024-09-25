# ModelCommunicationWayResponseSevClient

Client to which communication way key belongs. Will be filled automatically

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the client | 
**object_name** | **str** | Model name, which is &#39;SevClient&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_communication_way_response_sev_client import ModelCommunicationWayResponseSevClient

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCommunicationWayResponseSevClient from a JSON string
model_communication_way_response_sev_client_instance = ModelCommunicationWayResponseSevClient.from_json(json)
# print the JSON string representation of the object
print(ModelCommunicationWayResponseSevClient.to_json())

# convert the object into a dict
model_communication_way_response_sev_client_dict = model_communication_way_response_sev_client_instance.to_dict()
# create an instance of ModelCommunicationWayResponseSevClient from a dict
model_communication_way_response_sev_client_from_dict = ModelCommunicationWayResponseSevClient.from_dict(model_communication_way_response_sev_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


