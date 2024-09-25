# ModelInvoiceResponseContactPerson

The user who acts as a contact person for the invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the user | 
**object_name** | **str** | Model name, which is &#39;SevUser&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_response_contact_person import ModelInvoiceResponseContactPerson

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoiceResponseContactPerson from a JSON string
model_invoice_response_contact_person_instance = ModelInvoiceResponseContactPerson.from_json(json)
# print the JSON string representation of the object
print(ModelInvoiceResponseContactPerson.to_json())

# convert the object into a dict
model_invoice_response_contact_person_dict = model_invoice_response_contact_person_instance.to_dict()
# create an instance of ModelInvoiceResponseContactPerson from a dict
model_invoice_response_contact_person_from_dict = ModelInvoiceResponseContactPerson.from_dict(model_invoice_response_contact_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


