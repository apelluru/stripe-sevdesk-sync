# ModelChangeLayout

Layout model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | the type to be changed | 
**value** | **str** | the id/value of the template/letterpaper/language/payPal. | 

## Example

```python
from sevdesk_client.openapi_client.models.model_change_layout import ModelChangeLayout

# TODO update the JSON string below
json = "{}"
# create an instance of ModelChangeLayout from a JSON string
model_change_layout_instance = ModelChangeLayout.from_json(json)
# print the JSON string representation of the object
print(ModelChangeLayout.to_json())

# convert the object into a dict
model_change_layout_dict = model_change_layout_instance.to_dict()
# create an instance of ModelChangeLayout from a dict
model_change_layout_from_dict = ModelChangeLayout.from_dict(model_change_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


