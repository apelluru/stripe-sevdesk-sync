# GetInvoicePositionsById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelInvoicePosResponse]**](ModelInvoicePosResponse.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_invoice_positions_by_id200_response import GetInvoicePositionsById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoicePositionsById200Response from a JSON string
get_invoice_positions_by_id200_response_instance = GetInvoicePositionsById200Response.from_json(json)
# print the JSON string representation of the object
print(GetInvoicePositionsById200Response.to_json())

# convert the object into a dict
get_invoice_positions_by_id200_response_dict = get_invoice_positions_by_id200_response_instance.to_dict()
# create an instance of GetInvoicePositionsById200Response from a dict
get_invoice_positions_by_id200_response_from_dict = GetInvoicePositionsById200Response.from_dict(get_invoice_positions_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


