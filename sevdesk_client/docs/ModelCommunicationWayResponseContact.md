# ModelCommunicationWayResponseContact

The contact to which this communication way belongs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_communication_way_response_contact import ModelCommunicationWayResponseContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCommunicationWayResponseContact from a JSON string
model_communication_way_response_contact_instance = ModelCommunicationWayResponseContact.from_json(json)
# print the JSON string representation of the object
print(ModelCommunicationWayResponseContact.to_json())

# convert the object into a dict
model_communication_way_response_contact_dict = model_communication_way_response_contact_instance.to_dict()
# create an instance of ModelCommunicationWayResponseContact from a dict
model_communication_way_response_contact_from_dict = ModelCommunicationWayResponseContact.from_dict(model_communication_way_response_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


