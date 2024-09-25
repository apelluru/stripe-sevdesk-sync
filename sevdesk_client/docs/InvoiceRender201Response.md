# InvoiceRender201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbs** | **List[object]** |  | [optional] 
**pages** | **int** |  | [optional] 
**doc_id** | **str** |  | [optional] 
**parameters** | [**List[InvoiceRender201ResponseParametersInner]**](InvoiceRender201ResponseParametersInner.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.invoice_render201_response import InvoiceRender201Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceRender201Response from a JSON string
invoice_render201_response_instance = InvoiceRender201Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceRender201Response.to_json())

# convert the object into a dict
invoice_render201_response_dict = invoice_render201_response_instance.to_dict()
# create an instance of InvoiceRender201Response from a dict
invoice_render201_response_from_dict = InvoiceRender201Response.from_dict(invoice_render201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


