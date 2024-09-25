# ModelInvoicePosResponseUnity

The unit in which the positions part is measured

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the unit | 
**object_name** | **str** | Model name, which is &#39;Unity&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_pos_response_unity import ModelInvoicePosResponseUnity

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoicePosResponseUnity from a JSON string
model_invoice_pos_response_unity_instance = ModelInvoicePosResponseUnity.from_json(json)
# print the JSON string representation of the object
print(ModelInvoicePosResponseUnity.to_json())

# convert the object into a dict
model_invoice_pos_response_unity_dict = model_invoice_pos_response_unity_instance.to_dict()
# create an instance of ModelInvoicePosResponseUnity from a dict
model_invoice_pos_response_unity_from_dict = ModelInvoicePosResponseUnity.from_dict(model_invoice_pos_response_unity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


