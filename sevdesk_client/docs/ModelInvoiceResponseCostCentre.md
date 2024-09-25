# ModelInvoiceResponseCostCentre

Cost centre for the invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the cost centre | 
**object_name** | **str** | Model name, which is &#39;CostCentre&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_response_cost_centre import ModelInvoiceResponseCostCentre

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoiceResponseCostCentre from a JSON string
model_invoice_response_cost_centre_instance = ModelInvoiceResponseCostCentre.from_json(json)
# print the JSON string representation of the object
print(ModelInvoiceResponseCostCentre.to_json())

# convert the object into a dict
model_invoice_response_cost_centre_dict = model_invoice_response_cost_centre_instance.to_dict()
# create an instance of ModelInvoiceResponseCostCentre from a dict
model_invoice_response_cost_centre_from_dict = ModelInvoiceResponseCostCentre.from_dict(model_invoice_response_cost_centre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


