# ReceiptGuideDto

Model holds data about a single selectable account with additional information matching to that account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_datev_id** | **int** | The ID of the matching account datev | [optional] 
**account_number** | **str** | The account number of the account datev (dependent on the active accounting system of the client) | [optional] 
**account_name** | **str** | The name of the account | [optional] 
**description** | **str** | The description of the account and/or what the account is used for | [optional] 
**allowed_tax_rules** | [**List[ReceiptGuideDtoAllowedTaxRulesInner]**](ReceiptGuideDtoAllowedTaxRulesInner.md) | An array that holds all possible tax rules for this account | [optional] 
**allowed_receipt_types** | **List[str]** | An array that holds the viable receipt types for this account | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.receipt_guide_dto import ReceiptGuideDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptGuideDto from a JSON string
receipt_guide_dto_instance = ReceiptGuideDto.from_json(json)
# print the JSON string representation of the object
print(ReceiptGuideDto.to_json())

# convert the object into a dict
receipt_guide_dto_dict = receipt_guide_dto_instance.to_dict()
# create an instance of ReceiptGuideDto from a dict
receipt_guide_dto_from_dict = ReceiptGuideDto.from_dict(receipt_guide_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


