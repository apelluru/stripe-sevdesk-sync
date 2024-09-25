# ModelCommunicationWayResponse

Contact communication way model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The communication way id | [optional] [readonly] 
**object_name** | **str** | The communication way object name | [optional] [readonly] 
**create** | **datetime** | Date of communication way creation | [optional] [readonly] 
**update** | **datetime** | Date of last communication way update | [optional] [readonly] 
**contact** | [**ModelCommunicationWayResponseContact**](ModelCommunicationWayResponseContact.md) |  | [optional] 
**type** | **str** | Type of the communication way | [optional] [readonly] 
**value** | **str** | The value of the communication way.&lt;br&gt;       For example the phone number, e-mail address or website. | [optional] [readonly] 
**key** | [**ModelCommunicationWayResponseKey**](ModelCommunicationWayResponseKey.md) |  | [optional] 
**main** | **str** | Defines whether the communication way is the main communication way for the contact. | [optional] [readonly] 
**sev_client** | [**ModelCommunicationWayResponseSevClient**](ModelCommunicationWayResponseSevClient.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_communication_way_response import ModelCommunicationWayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCommunicationWayResponse from a JSON string
model_communication_way_response_instance = ModelCommunicationWayResponse.from_json(json)
# print the JSON string representation of the object
print(ModelCommunicationWayResponse.to_json())

# convert the object into a dict
model_communication_way_response_dict = model_communication_way_response_instance.to_dict()
# create an instance of ModelCommunicationWayResponse from a dict
model_communication_way_response_from_dict = ModelCommunicationWayResponse.from_dict(model_communication_way_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


