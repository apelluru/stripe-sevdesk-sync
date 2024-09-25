# ModelCreateInvoiceFromOrder

Invoice model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**ModelCreateInvoiceFromOrderOrder**](ModelCreateInvoiceFromOrderOrder.md) |  | 
**type** | **str** | defines the type of amount | [optional] 
**amount** | **float** | Amount which has already been paid for this Invoice | [optional] 
**partial_type** | **str** | defines the type of the invoice 1. RE - Schlussrechnung 2. TR - Teilrechnung 3. AR - Abschlagsrechnung | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_create_invoice_from_order import ModelCreateInvoiceFromOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreateInvoiceFromOrder from a JSON string
model_create_invoice_from_order_instance = ModelCreateInvoiceFromOrder.from_json(json)
# print the JSON string representation of the object
print(ModelCreateInvoiceFromOrder.to_json())

# convert the object into a dict
model_create_invoice_from_order_dict = model_create_invoice_from_order_instance.to_dict()
# create an instance of ModelCreateInvoiceFromOrder from a dict
model_create_invoice_from_order_from_dict = ModelCreateInvoiceFromOrder.from_dict(model_create_invoice_from_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


