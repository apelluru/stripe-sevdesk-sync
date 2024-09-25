# ModelCreditNoteSendByWithRender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbs** | **List[object]** |  | [optional] 
**pages** | **int** |  | [optional] 
**doc_id** | **str** |  | [optional] 
**parameters** | [**List[InvoiceRender201ResponseParametersInner]**](InvoiceRender201ResponseParametersInner.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_send_by_with_render import ModelCreditNoteSendByWithRender

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNoteSendByWithRender from a JSON string
model_credit_note_send_by_with_render_instance = ModelCreditNoteSendByWithRender.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNoteSendByWithRender.to_json())

# convert the object into a dict
model_credit_note_send_by_with_render_dict = model_credit_note_send_by_with_render_instance.to_dict()
# create an instance of ModelCreditNoteSendByWithRender from a dict
model_credit_note_send_by_with_render_from_dict = ModelCreditNoteSendByWithRender.from_dict(model_credit_note_send_by_with_render_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


