# ModelContactCustomFieldSettingResponse

contact fields model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the contact field | [optional] [readonly] 
**object_name** | **str** | Internal object name which is &#39;ContactCustomFieldSetting&#39;. | [optional] [readonly] 
**create** | **datetime** | Date of contact field creation | [optional] [readonly] 
**update** | **datetime** | Date of contact field updated | [optional] [readonly] 
**sev_client** | [**ModelContactCustomFieldSettingResponseSevClient**](ModelContactCustomFieldSettingResponseSevClient.md) |  | [optional] 
**name** | **str** | name of the contact fields | [optional] [readonly] 
**identifier** | **str** | Unique identifier for the contact field | [optional] [readonly] 
**description** | **str** | The description of the contact field | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_custom_field_setting_response import ModelContactCustomFieldSettingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCustomFieldSettingResponse from a JSON string
model_contact_custom_field_setting_response_instance = ModelContactCustomFieldSettingResponse.from_json(json)
# print the JSON string representation of the object
print(ModelContactCustomFieldSettingResponse.to_json())

# convert the object into a dict
model_contact_custom_field_setting_response_dict = model_contact_custom_field_setting_response_instance.to_dict()
# create an instance of ModelContactCustomFieldSettingResponse from a dict
model_contact_custom_field_setting_response_from_dict = ModelContactCustomFieldSettingResponse.from_dict(model_contact_custom_field_setting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


