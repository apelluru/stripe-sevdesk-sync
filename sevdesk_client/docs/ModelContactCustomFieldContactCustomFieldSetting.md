# ModelContactCustomFieldContactCustomFieldSetting

name of the contact custom field setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of contact custom field setting | 
**object_name** | **str** | Model name, which is &#39;contactCustomFieldSetting&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_custom_field_contact_custom_field_setting import ModelContactCustomFieldContactCustomFieldSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCustomFieldContactCustomFieldSetting from a JSON string
model_contact_custom_field_contact_custom_field_setting_instance = ModelContactCustomFieldContactCustomFieldSetting.from_json(json)
# print the JSON string representation of the object
print(ModelContactCustomFieldContactCustomFieldSetting.to_json())

# convert the object into a dict
model_contact_custom_field_contact_custom_field_setting_dict = model_contact_custom_field_contact_custom_field_setting_instance.to_dict()
# create an instance of ModelContactCustomFieldContactCustomFieldSetting from a dict
model_contact_custom_field_contact_custom_field_setting_from_dict = ModelContactCustomFieldContactCustomFieldSetting.from_dict(model_contact_custom_field_contact_custom_field_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


