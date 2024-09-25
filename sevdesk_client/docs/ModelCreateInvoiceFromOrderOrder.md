# ModelCreateInvoiceFromOrderOrder

select the order for which you want to create the invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the order | 
**object_name** | **str** | Model name, which is &#39;Order&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_create_invoice_from_order_order import ModelCreateInvoiceFromOrderOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreateInvoiceFromOrderOrder from a JSON string
model_create_invoice_from_order_order_instance = ModelCreateInvoiceFromOrderOrder.from_json(json)
# print the JSON string representation of the object
print(ModelCreateInvoiceFromOrderOrder.to_json())

# convert the object into a dict
model_create_invoice_from_order_order_dict = model_create_invoice_from_order_order_instance.to_dict()
# create an instance of ModelCreateInvoiceFromOrderOrder from a dict
model_create_invoice_from_order_order_from_dict = ModelCreateInvoiceFromOrderOrder.from_dict(model_create_invoice_from_order_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


