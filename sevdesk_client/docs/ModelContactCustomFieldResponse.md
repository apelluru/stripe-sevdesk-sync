# ModelContactCustomFieldResponse

contact fields model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the contact field | [optional] 
**object_name** | **str** | Internal object name which is &#39;ContactCustomField&#39;. | [optional] 
**create** | **datetime** | Date of contact field creation | [optional] 
**update** | **datetime** | Date of contact field update | [optional] 
**sev_client** | [**ModelContactCustomFieldResponseSevClient**](ModelContactCustomFieldResponseSevClient.md) |  | [optional] 
**contact** | [**ModelContactCustomFieldResponseContact**](ModelContactCustomFieldResponseContact.md) |  | [optional] 
**contact_custom_field_setting** | [**ModelContactCustomFieldSettingResponse**](ModelContactCustomFieldSettingResponse.md) | the contact custom field setting | [optional] 
**value** | **str** | The value of the contact field | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_custom_field_response import ModelContactCustomFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactCustomFieldResponse from a JSON string
model_contact_custom_field_response_instance = ModelContactCustomFieldResponse.from_json(json)
# print the JSON string representation of the object
print(ModelContactCustomFieldResponse.to_json())

# convert the object into a dict
model_contact_custom_field_response_dict = model_contact_custom_field_response_instance.to_dict()
# create an instance of ModelContactCustomFieldResponse from a dict
model_contact_custom_field_response_from_dict = ModelContactCustomFieldResponse.from_dict(model_contact_custom_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


