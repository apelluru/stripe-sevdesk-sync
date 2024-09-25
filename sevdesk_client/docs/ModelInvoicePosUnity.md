# ModelInvoicePosUnity

The unit in which the positions part is measured

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the unit | 
**object_name** | **str** | Model name, which is &#39;Unity&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_pos_unity import ModelInvoicePosUnity

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoicePosUnity from a JSON string
model_invoice_pos_unity_instance = ModelInvoicePosUnity.from_json(json)
# print the JSON string representation of the object
print(ModelInvoicePosUnity.to_json())

# convert the object into a dict
model_invoice_pos_unity_dict = model_invoice_pos_unity_instance.to_dict()
# create an instance of ModelInvoicePosUnity from a dict
model_invoice_pos_unity_from_dict = ModelInvoicePosUnity.from_dict(model_invoice_pos_unity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


