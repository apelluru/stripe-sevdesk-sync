# ModelInvoiceResponseSevClient

Client to which invoice belongs. Will be filled automatically

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the client | 
**object_name** | **str** | Model name, which is &#39;SevClient&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_response_sev_client import ModelInvoiceResponseSevClient

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoiceResponseSevClient from a JSON string
model_invoice_response_sev_client_instance = ModelInvoiceResponseSevClient.from_json(json)
# print the JSON string representation of the object
print(ModelInvoiceResponseSevClient.to_json())

# convert the object into a dict
model_invoice_response_sev_client_dict = model_invoice_response_sev_client_instance.to_dict()
# create an instance of ModelInvoiceResponseSevClient from a dict
model_invoice_response_sev_client_from_dict = ModelInvoiceResponseSevClient.from_dict(model_invoice_response_sev_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


