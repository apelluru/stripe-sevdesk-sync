# ModelContactCustomField

Contact fields model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ModelContactCustomFieldContact**](ModelContactCustomFieldContact.md) |  | 
**contact_custom_field_setting** | [**ModelContactCustomFieldContactCustomFieldSetting**](ModelContactCustomFieldContactCustomFieldSetting.md) |  | 
**value** | **str** | The value of the contact field | 
**object_name** | **str** | Internal object name which is &#39;ContactCustomField&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_custom_field import ModelContactCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCustomField from a JSON string
model_contact_custom_field_instance = ModelContactCustomField.from_json(json)
# print the JSON string representation of the object
print(ModelContactCustomField.to_json())

# convert the object into a dict
model_contact_custom_field_dict = model_contact_custom_field_instance.to_dict()
# create an instance of ModelContactCustomField from a dict
model_contact_custom_field_from_dict = ModelContactCustomField.from_dict(model_contact_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


