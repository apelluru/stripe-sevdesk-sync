# ModelInvoiceResponsePaymentMethod

Payment method used for the invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the payment method | 
**object_name** | **str** | Model name, which is &#39;PaymentMethod&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_response_payment_method import ModelInvoiceResponsePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoiceResponsePaymentMethod from a JSON string
model_invoice_response_payment_method_instance = ModelInvoiceResponsePaymentMethod.from_json(json)
# print the JSON string representation of the object
print(ModelInvoiceResponsePaymentMethod.to_json())

# convert the object into a dict
model_invoice_response_payment_method_dict = model_invoice_response_payment_method_instance.to_dict()
# create an instance of ModelInvoiceResponsePaymentMethod from a dict
model_invoice_response_payment_method_from_dict = ModelInvoiceResponsePaymentMethod.from_dict(model_invoice_response_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


