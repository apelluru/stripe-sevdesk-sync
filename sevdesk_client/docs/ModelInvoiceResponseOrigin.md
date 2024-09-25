# ModelInvoiceResponseOrigin

Origin of the invoice. Could f.e. be an order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the object | 
**object_name** | **str** | Model name. Could f.e. be &#39;Order&#39;&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_response_origin import ModelInvoiceResponseOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoiceResponseOrigin from a JSON string
model_invoice_response_origin_instance = ModelInvoiceResponseOrigin.from_json(json)
# print the JSON string representation of the object
print(ModelInvoiceResponseOrigin.to_json())

# convert the object into a dict
model_invoice_response_origin_dict = model_invoice_response_origin_instance.to_dict()
# create an instance of ModelInvoiceResponseOrigin from a dict
model_invoice_response_origin_from_dict = ModelInvoiceResponseOrigin.from_dict(model_invoice_response_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


