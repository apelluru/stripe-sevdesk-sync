# ModelContactCustomFieldUpdate

contact fields model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ModelContactCustomFieldContact**](ModelContactCustomFieldContact.md) |  | [optional] 
**contact_custom_field_setting** | [**ModelContactCustomFieldContactCustomFieldSetting**](ModelContactCustomFieldContactCustomFieldSetting.md) |  | [optional] 
**value** | **str** | The value of the contact field | [optional] 
**object_name** | **str** | Internal object name which is &#39;ContactCustomField&#39;. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_custom_field_update import ModelContactCustomFieldUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCustomFieldUpdate from a JSON string
model_contact_custom_field_update_instance = ModelContactCustomFieldUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelContactCustomFieldUpdate.to_json())

# convert the object into a dict
model_contact_custom_field_update_dict = model_contact_custom_field_update_instance.to_dict()
# create an instance of ModelContactCustomFieldUpdate from a dict
model_contact_custom_field_update_from_dict = ModelContactCustomFieldUpdate.from_dict(model_contact_custom_field_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


