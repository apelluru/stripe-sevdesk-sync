# ReceiptGuideDtoAllowedTaxRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tax rule | [optional] 
**description** | **str** | A readable description of the tax rule | [optional] 
**id** | **int** | The id of the tax rule to use in different scenarios | [optional] 
**tax_rates** | **List[str]** | An array of tax rates which are combinable with this tax rule | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.receipt_guide_dto_allowed_tax_rules_inner import ReceiptGuideDtoAllowedTaxRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptGuideDtoAllowedTaxRulesInner from a JSON string
receipt_guide_dto_allowed_tax_rules_inner_instance = ReceiptGuideDtoAllowedTaxRulesInner.from_json(json)
# print the JSON string representation of the object
print(ReceiptGuideDtoAllowedTaxRulesInner.to_json())

# convert the object into a dict
receipt_guide_dto_allowed_tax_rules_inner_dict = receipt_guide_dto_allowed_tax_rules_inner_instance.to_dict()
# create an instance of ReceiptGuideDtoAllowedTaxRulesInner from a dict
receipt_guide_dto_allowed_tax_rules_inner_from_dict = ReceiptGuideDtoAllowedTaxRulesInner.from_dict(receipt_guide_dto_allowed_tax_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


