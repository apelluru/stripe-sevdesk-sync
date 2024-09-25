# ModelVoucherResponseCreateUser

User who created the voucher. Will be filled automatically.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the user | 
**object_name** | **str** | Model name, which is &#39;SevUser&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_response_create_user import ModelVoucherResponseCreateUser

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherResponseCreateUser from a JSON string
model_voucher_response_create_user_instance = ModelVoucherResponseCreateUser.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherResponseCreateUser.to_json())

# convert the object into a dict
model_voucher_response_create_user_dict = model_voucher_response_create_user_instance.to_dict()
# create an instance of ModelVoucherResponseCreateUser from a dict
model_voucher_response_create_user_from_dict = ModelVoucherResponseCreateUser.from_dict(model_voucher_response_create_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


