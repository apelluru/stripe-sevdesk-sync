# ModelVoucherPosResponse

Voucher position model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The voucher position id | [optional] [readonly] 
**object_name** | **str** | The voucher position object name | [optional] [readonly] 
**create** | **str** | Date of voucher position creation | [optional] [readonly] 
**update** | **str** | Date of last voucher position update | [optional] [readonly] 
**sev_client** | [**ModelVoucherPosResponseSevClient**](ModelVoucherPosResponseSevClient.md) |  | [optional] 
**voucher** | [**ModelVoucherPosResponseVoucher**](ModelVoucherPosResponseVoucher.md) |  | 
**account_datev** | [**ModelVoucherPosAccountDatev**](ModelVoucherPosAccountDatev.md) |  | 
**accounting_type** | [**ModelVoucherPosResponseAccountingType**](ModelVoucherPosResponseAccountingType.md) |  | 
**estimated_accounting_type** | [**ModelVoucherPosResponseEstimatedAccountingType**](ModelVoucherPosResponseEstimatedAccountingType.md) |  | [optional] 
**tax_rate** | **str** | Tax rate of the voucher position. | 
**net** | **bool** | Determines whether &#39;sumNet&#39; or &#39;sumGross&#39; is regarded.&lt;br&gt;       If both are not given, &#39;sum&#39; is regarded and treated as net or gross depending on &#39;net&#39;.  All positions must be either net or gross, a mixture of the two is not possible. | 
**is_asset** | **bool** | Determines whether position is regarded as an asset which can be depreciated. | [optional] 
**sum_net** | **str** | Net sum of the voucher position.&lt;br&gt;      Only regarded if &#39;net&#39; is &#39;true&#39;, otherwise its readOnly. | 
**sum_tax** | **str** | Tax sum of the voucher position. | [optional] [readonly] 
**sum_gross** | **str** | Gross sum of the voucher position.&lt;br&gt;      Only regarded if &#39;net&#39; is &#39;false&#39;, otherwise its readOnly. | 
**sum_net_accounting** | **str** | Net accounting sum. Is equal to sumNet. | [optional] [readonly] 
**sum_tax_accounting** | **str** | Tax accounting sum. Is equal to sumTax. | [optional] [readonly] 
**sum_gross_accounting** | **str** | Gross accounting sum. Is equal to sumGross. | [optional] [readonly] 
**comment** | **str** | Comment for the voucher position. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_pos_response import ModelVoucherPosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherPosResponse from a JSON string
model_voucher_pos_response_instance = ModelVoucherPosResponse.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherPosResponse.to_json())

# convert the object into a dict
model_voucher_pos_response_dict = model_voucher_pos_response_instance.to_dict()
# create an instance of ModelVoucherPosResponse from a dict
model_voucher_pos_response_from_dict = ModelVoucherPosResponse.from_dict(model_voucher_pos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


