# ModelInvoiceOrigin

Origin of the invoice. Could f.e. be an order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the object | 
**object_name** | **str** | Model name, which could be &#39;Order&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_origin import ModelInvoiceOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoiceOrigin from a JSON string
model_invoice_origin_instance = ModelInvoiceOrigin.from_json(json)
# print the JSON string representation of the object
print(ModelInvoiceOrigin.to_json())

# convert the object into a dict
model_invoice_origin_dict = model_invoice_origin_instance.to_dict()
# create an instance of ModelInvoiceOrigin from a dict
model_invoice_origin_from_dict = ModelInvoiceOrigin.from_dict(model_invoice_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


