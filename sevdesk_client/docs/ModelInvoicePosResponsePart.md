# ModelInvoicePosResponsePart

Part from your inventory which is used in the position.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the part | 
**object_name** | **str** | Model name, which is &#39;Part&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_pos_response_part import ModelInvoicePosResponsePart

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoicePosResponsePart from a JSON string
model_invoice_pos_response_part_instance = ModelInvoicePosResponsePart.from_json(json)
# print the JSON string representation of the object
print(ModelInvoicePosResponsePart.to_json())

# convert the object into a dict
model_invoice_pos_response_part_dict = model_invoice_pos_response_part_instance.to_dict()
# create an instance of ModelInvoicePosResponsePart from a dict
model_invoice_pos_response_part_from_dict = ModelInvoicePosResponsePart.from_dict(model_invoice_pos_response_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


