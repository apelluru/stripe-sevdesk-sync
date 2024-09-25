# ModelContactCustomFieldSettingUpdate

contact fields model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the contact fields | [optional] 
**description** | **str** | The description of the contact field | [optional] 
**object_name** | **str** | Internal object name which is &#39;ContactCustomFieldSetting&#39;. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_custom_field_setting_update import ModelContactCustomFieldSettingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCustomFieldSettingUpdate from a JSON string
model_contact_custom_field_setting_update_instance = ModelContactCustomFieldSettingUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelContactCustomFieldSettingUpdate.to_json())

# convert the object into a dict
model_contact_custom_field_setting_update_dict = model_contact_custom_field_setting_update_instance.to_dict()
# create an instance of ModelContactCustomFieldSettingUpdate from a dict
model_contact_custom_field_setting_update_from_dict = ModelContactCustomFieldSettingUpdate.from_dict(model_contact_custom_field_setting_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


