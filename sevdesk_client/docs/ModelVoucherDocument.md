# ModelVoucherDocument

The document of the voucher.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the document | 
**object_name** | **str** | Model name, which is &#39;Document&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_document import ModelVoucherDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherDocument from a JSON string
model_voucher_document_instance = ModelVoucherDocument.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherDocument.to_json())

# convert the object into a dict
model_voucher_document_dict = model_voucher_document_instance.to_dict()
# create an instance of ModelVoucherDocument from a dict
model_voucher_document_from_dict = ModelVoucherDocument.from_dict(model_voucher_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


