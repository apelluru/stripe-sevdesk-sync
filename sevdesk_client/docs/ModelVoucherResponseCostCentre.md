# ModelVoucherResponseCostCentre

Cost centre for the voucher

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the cost centre | 
**object_name** | **str** | Model name, which is &#39;CostCentre&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_response_cost_centre import ModelVoucherResponseCostCentre

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherResponseCostCentre from a JSON string
model_voucher_response_cost_centre_instance = ModelVoucherResponseCostCentre.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherResponseCostCentre.to_json())

# convert the object into a dict
model_voucher_response_cost_centre_dict = model_voucher_response_cost_centre_instance.to_dict()
# create an instance of ModelVoucherResponseCostCentre from a dict
model_voucher_response_cost_centre_from_dict = ModelVoucherResponseCostCentre.from_dict(model_voucher_response_cost_centre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


