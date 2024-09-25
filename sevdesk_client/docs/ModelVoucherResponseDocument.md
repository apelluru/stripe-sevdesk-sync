# ModelVoucherResponseDocument

The document of the voucher.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the document | 
**object_name** | **str** | Model name, which is &#39;Document&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_response_document import ModelVoucherResponseDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherResponseDocument from a JSON string
model_voucher_response_document_instance = ModelVoucherResponseDocument.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherResponseDocument.to_json())

# convert the object into a dict
model_voucher_response_document_dict = model_voucher_response_document_instance.to_dict()
# create an instance of ModelVoucherResponseDocument from a dict
model_voucher_response_document_from_dict = ModelVoucherResponseDocument.from_dict(model_voucher_response_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


