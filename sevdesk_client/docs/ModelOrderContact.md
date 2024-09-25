# ModelOrderContact

The contact used in the order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the contact | 
**object_name** | **str** | Model name, which is &#39;Contact&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_contact import ModelOrderContact

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderContact from a JSON string
model_order_contact_instance = ModelOrderContact.from_json(json)
# print the JSON string representation of the object
print(ModelOrderContact.to_json())

# convert the object into a dict
model_order_contact_dict = model_order_contact_instance.to_dict()
# create an instance of ModelOrderContact from a dict
model_order_contact_from_dict = ModelOrderContact.from_dict(model_order_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


