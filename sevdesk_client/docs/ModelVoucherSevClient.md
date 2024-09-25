# ModelVoucherSevClient

Client to which voucher belongs. Will be filled automatically

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the client | 
**object_name** | **str** | Model name, which is &#39;SevClient&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_sev_client import ModelVoucherSevClient

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherSevClient from a JSON string
model_voucher_sev_client_instance = ModelVoucherSevClient.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherSevClient.to_json())

# convert the object into a dict
model_voucher_sev_client_dict = model_voucher_sev_client_instance.to_dict()
# create an instance of ModelVoucherSevClient from a dict
model_voucher_sev_client_from_dict = ModelVoucherSevClient.from_dict(model_voucher_sev_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


