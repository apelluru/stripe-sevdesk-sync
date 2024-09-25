# ModelCommunicationWayUpdate

Contact communication way model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ModelCommunicationWayUpdateContact**](ModelCommunicationWayUpdateContact.md) |  | [optional] 
**type** | **str** | Type of the communication way | [optional] 
**value** | **str** | The value of the communication way.&lt;br&gt;       For example the phone number, e-mail address or website. | [optional] 
**key** | [**ModelCommunicationWayUpdateKey**](ModelCommunicationWayUpdateKey.md) |  | [optional] 
**main** | **bool** | Defines whether the communication way is the main communication way for the contact. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_communication_way_update import ModelCommunicationWayUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCommunicationWayUpdate from a JSON string
model_communication_way_update_instance = ModelCommunicationWayUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelCommunicationWayUpdate.to_json())

# convert the object into a dict
model_communication_way_update_dict = model_communication_way_update_instance.to_dict()
# create an instance of ModelCommunicationWayUpdate from a dict
model_communication_way_update_from_dict = ModelCommunicationWayUpdate.from_dict(model_communication_way_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


