# ModelInvoicePosInvoice

The invoice to which the position belongs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the invoice | 
**object_name** | **str** | Model name, which is &#39;Invoice&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_pos_invoice import ModelInvoicePosInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoicePosInvoice from a JSON string
model_invoice_pos_invoice_instance = ModelInvoicePosInvoice.from_json(json)
# print the JSON string representation of the object
print(ModelInvoicePosInvoice.to_json())

# convert the object into a dict
model_invoice_pos_invoice_dict = model_invoice_pos_invoice_instance.to_dict()
# create an instance of ModelInvoicePosInvoice from a dict
model_invoice_pos_invoice_from_dict = ModelInvoicePosInvoice.from_dict(model_invoice_pos_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


