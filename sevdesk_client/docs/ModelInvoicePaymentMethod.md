# ModelInvoicePaymentMethod

Payment method used for the invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the payment method | 
**object_name** | **str** | Model name, which is &#39;PaymentMethod&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_payment_method import ModelInvoicePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoicePaymentMethod from a JSON string
model_invoice_payment_method_instance = ModelInvoicePaymentMethod.from_json(json)
# print the JSON string representation of the object
print(ModelInvoicePaymentMethod.to_json())

# convert the object into a dict
model_invoice_payment_method_dict = model_invoice_payment_method_instance.to_dict()
# create an instance of ModelInvoicePaymentMethod from a dict
model_invoice_payment_method_from_dict = ModelInvoicePaymentMethod.from_dict(model_invoice_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


