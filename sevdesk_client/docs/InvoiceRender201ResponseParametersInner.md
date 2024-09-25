# InvoiceRender201ResponseParametersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**values** | [**List[InvoiceRender201ResponseParametersInnerValuesInner]**](InvoiceRender201ResponseParametersInnerValuesInner.md) |  | [optional] 
**visible** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.invoice_render201_response_parameters_inner import InvoiceRender201ResponseParametersInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceRender201ResponseParametersInner from a JSON string
invoice_render201_response_parameters_inner_instance = InvoiceRender201ResponseParametersInner.from_json(json)
# print the JSON string representation of the object
print(InvoiceRender201ResponseParametersInner.to_json())

# convert the object into a dict
invoice_render201_response_parameters_inner_dict = invoice_render201_response_parameters_inner_instance.to_dict()
# create an instance of InvoiceRender201ResponseParametersInner from a dict
invoice_render201_response_parameters_inner_from_dict = InvoiceRender201ResponseParametersInner.from_dict(invoice_render201_response_parameters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


