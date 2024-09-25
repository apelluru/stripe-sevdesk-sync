# ModelCommunicationWay

Contact communication way model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The communication way id | [optional] [readonly] 
**object_name** | **str** | The communication way object name | [optional] [readonly] 
**create** | **datetime** | Date of communication way creation | [optional] [readonly] 
**update** | **datetime** | Date of last communication way update | [optional] [readonly] 
**contact** | [**ModelCommunicationWayContact**](ModelCommunicationWayContact.md) |  | [optional] 
**type** | **str** | Type of the communication way | 
**value** | **str** | The value of the communication way.&lt;br&gt;       For example the phone number, e-mail address or website. | 
**key** | [**ModelCommunicationWayKey**](ModelCommunicationWayKey.md) |  | 
**main** | **bool** | Defines whether the communication way is the main communication way for the contact. | [optional] 
**sev_client** | [**ModelCommunicationWaySevClient**](ModelCommunicationWaySevClient.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_communication_way import ModelCommunicationWay

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCommunicationWay from a JSON string
model_communication_way_instance = ModelCommunicationWay.from_json(json)
# print the JSON string representation of the object
print(ModelCommunicationWay.to_json())

# convert the object into a dict
model_communication_way_dict = model_communication_way_instance.to_dict()
# create an instance of ModelCommunicationWay from a dict
model_communication_way_from_dict = ModelCommunicationWay.from_dict(model_communication_way_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


