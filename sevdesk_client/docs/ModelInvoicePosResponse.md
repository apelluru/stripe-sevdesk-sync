# ModelInvoicePosResponse

Invoice position model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The invoice position id | [optional] [readonly] 
**object_name** | **str** | The invoice position object name | [optional] [readonly] 
**create** | **datetime** | Date of invoice position creation | [optional] [readonly] 
**update** | **datetime** | Date of last invoice position update | [optional] [readonly] 
**invoice** | [**ModelInvoicePosResponseInvoice**](ModelInvoicePosResponseInvoice.md) |  | [optional] 
**part** | [**ModelInvoicePosResponsePart**](ModelInvoicePosResponsePart.md) |  | [optional] 
**quantity** | **bool** | Quantity of the article/part | [optional] [readonly] 
**price** | **str** | Price of the article/part. Is either gross or net, depending on the sevdesk account setting. | [optional] [readonly] 
**name** | **str** | Name of the article/part. | [optional] [readonly] 
**unity** | [**ModelInvoicePosResponseUnity**](ModelInvoicePosResponseUnity.md) |  | [optional] 
**sev_client** | [**ModelInvoicePosResponseSevClient**](ModelInvoicePosResponseSevClient.md) |  | [optional] 
**position_number** | **str** | Position number of your position. Can be used to order multiple positions. | [optional] [readonly] 
**text** | **str** | A text describing your position. | [optional] [readonly] 
**discount** | **str** | An optional discount of the position. | [optional] [readonly] 
**tax_rate** | **str** | Tax rate of the position. | [optional] [readonly] 
**sum_discount** | **str** | Discount sum of the position | [optional] [readonly] 
**sum_net_accounting** | **str** | Net accounting sum of the position | [optional] [readonly] 
**sum_tax_accounting** | **str** | Tax accounting sum of the position | [optional] [readonly] 
**sum_gross_accounting** | **str** | Gross accounting sum of the position | [optional] [readonly] 
**price_net** | **str** | Net price of the part | [optional] [readonly] 
**price_gross** | **str** | Gross price of the part | [optional] [readonly] 
**price_tax** | **str** | Tax on the price of the part | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_pos_response import ModelInvoicePosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoicePosResponse from a JSON string
model_invoice_pos_response_instance = ModelInvoicePosResponse.from_json(json)
# print the JSON string representation of the object
print(ModelInvoicePosResponse.to_json())

# convert the object into a dict
model_invoice_pos_response_dict = model_invoice_pos_response_instance.to_dict()
# create an instance of ModelInvoicePosResponse from a dict
model_invoice_pos_response_from_dict = ModelInvoicePosResponse.from_dict(model_invoice_pos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


