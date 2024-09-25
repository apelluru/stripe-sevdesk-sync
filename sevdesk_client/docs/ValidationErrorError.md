# ValidationErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**exception_uuid** | **str** | An identifier of this exact problem that can be given to the support team. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.validation_error_error import ValidationErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorError from a JSON string
validation_error_error_instance = ValidationErrorError.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorError.to_json())

# convert the object into a dict
validation_error_error_dict = validation_error_error_instance.to_dict()
# create an instance of ValidationErrorError from a dict
validation_error_error_from_dict = ValidationErrorError.from_dict(validation_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


