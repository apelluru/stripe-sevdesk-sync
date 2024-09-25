# ModelPart

Part model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The part id | [optional] [readonly] 
**object_name** | **str** | The part object name | [optional] [readonly] 
**create** | **datetime** | Date of part creation | [optional] [readonly] 
**update** | **datetime** | Date of last part update | [optional] [readonly] 
**name** | **str** | Name of the part | 
**part_number** | **str** | The part number | 
**text** | **str** | A text describing the part | [optional] 
**category** | [**ModelPartCategory**](ModelPartCategory.md) |  | [optional] 
**stock** | **float** | The stock of the part | 
**stock_enabled** | **bool** | Defines if the stock should be enabled | [optional] 
**unity** | [**ModelPartUnity**](ModelPartUnity.md) |  | 
**price** | **float** | Net price for which the part is sold. we will change this parameter so that the gross price is calculated automatically, until then the priceGross parameter must be used. | [optional] 
**price_net** | **float** | Net price for which the part is sold | [optional] 
**price_gross** | **float** | Gross price for which the part is sold | [optional] 
**sev_client** | [**ModelPartSevClient**](ModelPartSevClient.md) |  | [optional] 
**price_purchase** | **float** | Purchase price of the part | [optional] 
**tax_rate** | **float** | Tax rate of the part | 
**status** | **int** | Status of the part. 50 &lt;-&gt; Inactive - 100 &lt;-&gt; Active | [optional] 
**internal_comment** | **str** | An internal comment for the part.&lt;br&gt;       Does not appear on invoices and orders. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_part import ModelPart

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPart from a JSON string
model_part_instance = ModelPart.from_json(json)
# print the JSON string representation of the object
print(ModelPart.to_json())

# convert the object into a dict
model_part_dict = model_part_instance.to_dict()
# create an instance of ModelPart from a dict
model_part_from_dict = ModelPart.from_dict(model_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


