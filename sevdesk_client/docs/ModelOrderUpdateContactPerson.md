# ModelOrderUpdateContactPerson

The user who acts as a contact person for the order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the user | 
**object_name** | **str** | Model name, which is &#39;SevUser&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_update_contact_person import ModelOrderUpdateContactPerson

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderUpdateContactPerson from a JSON string
model_order_update_contact_person_instance = ModelOrderUpdateContactPerson.from_json(json)
# print the JSON string representation of the object
print(ModelOrderUpdateContactPerson.to_json())

# convert the object into a dict
model_order_update_contact_person_dict = model_order_update_contact_person_instance.to_dict()
# create an instance of ModelOrderUpdateContactPerson from a dict
model_order_update_contact_person_from_dict = ModelOrderUpdateContactPerson.from_dict(model_order_update_contact_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


