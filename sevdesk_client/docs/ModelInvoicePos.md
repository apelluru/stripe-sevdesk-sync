# ModelInvoicePos

Invoice position model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The invoice position id. &lt;span style&#x3D;&#39;color:red&#39;&gt;Required&lt;/span&gt; if you want to update an invoice position for an existing invoice | [optional] 
**object_name** | **str** | The invoice position object name | 
**map_all** | **bool** |  | 
**create** | **datetime** | Date of invoice position creation | [optional] [readonly] 
**update** | **datetime** | Date of last invoice position update | [optional] [readonly] 
**invoice** | [**ModelInvoicePosInvoice**](ModelInvoicePosInvoice.md) |  | [optional] 
**part** | [**ModelCreditNotePosPart**](ModelCreditNotePosPart.md) |  | [optional] 
**quantity** | **float** | Quantity of the article/part | 
**price** | **float** | Price of the article/part. Is either gross or net, depending on the sevdesk account setting. | [optional] 
**name** | **str** | Name of the article/part. | [optional] 
**unity** | [**ModelInvoicePosUnity**](ModelInvoicePosUnity.md) |  | 
**sev_client** | [**ModelInvoicePosSevClient**](ModelInvoicePosSevClient.md) |  | [optional] 
**position_number** | **int** | Position number of your position. Can be used to order multiple positions. | [optional] 
**text** | **str** | A text describing your position. | [optional] 
**discount** | **float** | An optional discount of the position. | [optional] 
**tax_rate** | **float** | Tax rate of the position. | 
**sum_discount** | **float** | Discount sum of the position | [optional] [readonly] 
**sum_net_accounting** | **float** | Net accounting sum of the position | [optional] [readonly] 
**sum_tax_accounting** | **float** | Tax accounting sum of the position | [optional] [readonly] 
**sum_gross_accounting** | **float** | Gross accounting sum of the position | [optional] [readonly] 
**price_net** | **float** | Net price of the part | [optional] [readonly] 
**price_gross** | **float** | Gross price of the part | [optional] 
**price_tax** | **float** | Tax on the price of the part | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_invoice_pos import ModelInvoicePos

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInvoicePos from a JSON string
model_invoice_pos_instance = ModelInvoicePos.from_json(json)
# print the JSON string representation of the object
print(ModelInvoicePos.to_json())

# convert the object into a dict
model_invoice_pos_dict = model_invoice_pos_instance.to_dict()
# create an instance of ModelInvoicePos from a dict
model_invoice_pos_from_dict = ModelInvoicePos.from_dict(model_invoice_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


