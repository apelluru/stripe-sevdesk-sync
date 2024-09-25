# VoucherResetToOpen200ResponseObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The voucher id | [optional] [readonly] 
**object_name** | **str** | The voucher object name | [optional] [readonly] 
**map_all** | **bool** |  | [optional] 
**create** | **datetime** | Date of voucher creation | [optional] [readonly] 
**update** | **datetime** | Date of last voucher update | [optional] [readonly] 
**sev_client** | [**ModelVoucherResponseSevClient**](ModelVoucherResponseSevClient.md) |  | [optional] 
**create_user** | [**ModelVoucherResponseCreateUser**](ModelVoucherResponseCreateUser.md) |  | [optional] 
**voucher_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**supplier** | [**ModelVoucherResponseSupplier**](ModelVoucherResponseSupplier.md) |  | [optional] 
**supplier_name** | **str** | The supplier name.&lt;br&gt;       The value you provide here will determine what supplier name is shown for the voucher in case you did not provide a supplier. | [optional] 
**description** | **str** | The description of the voucher. Essentially the voucher number. | [optional] 
**document** | [**ModelVoucherResponseDocument**](ModelVoucherResponseDocument.md) |  | [optional] 
**pay_date** | **datetime** | Needs to be timestamp or dd.mm.yyyy | [optional] 
**status** | **object** |  | [optional] 
**sum_net** | **str** | Net sum of the voucher | [optional] [readonly] 
**sum_tax** | **str** | Tax sum of the voucher | [optional] [readonly] 
**sum_gross** | **str** | Gross sum of the voucher | [optional] [readonly] 
**sum_net_accounting** | **str** | Net accounting sum of the voucher. Is usually the same as sumNet | [optional] [readonly] 
**sum_tax_accounting** | **str** | Tax accounting sum of the voucher. Is usually the same as sumTax | [optional] [readonly] 
**sum_gross_accounting** | **str** | Gross accounting sum of the voucher. Is usually the same as sumGross | [optional] [readonly] 
**sum_discounts** | **str** | Sum of all discounts in the voucher | [optional] [readonly] 
**sum_discounts_foreign_currency** | **str** | Discounts sum of the voucher in the foreign currency | [optional] [readonly] 
**paid_amount** | **float** | Amount which has already been paid for this voucher by the customer | [optional] [readonly] 
**tax_rule** | [**ModelVoucherTaxRule**](ModelVoucherTaxRule.md) |  | [optional] 
**tax_type** | **str** | **Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax type of the voucher. There are four tax types: 1. default - Umsatzsteuer ausweisen 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union) 3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz) 4. custom - Using custom tax set 5. ss - Not subject to VAT according to §19 1 UStG Tax rates are heavily connected to the tax type used. | [optional] 
**credit_debit** | **str** | Defines if your voucher is a credit (C) or debit (D) | [optional] 
**cost_centre** | [**ModelVoucherResponseCostCentre**](ModelVoucherResponseCostCentre.md) |  | [optional] 
**voucher_type** | **str** | Type of the voucher. For more information on the different types, check       &lt;a href&#x3D;&#39;#tag/Voucher/Types-and-status-of-vouchers&#39;&gt;this&lt;/a&gt;   | [optional] 
**currency** | **str** | specifies which currency the voucher should have. Attention: If the currency differs from the default currency stored in the account, then either the \&quot;propertyForeignCurrencyDeadline\&quot; or \&quot;propertyExchangeRate\&quot; parameter must be specified. If both parameters are specified, then the \&quot;propertyForeignCurrencyDeadline\&quot; parameter is preferred | [optional] 
**property_foreign_currency_deadline** | **datetime** | Defines the exchange rate day and and then the exchange rate is set from sevdesk. Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**property_exchange_rate** | **str** | Defines the exchange rate | [optional] 
**recurring_interval** | **str** | The DateInterval in which recurring vouchers are generated.&lt;br&gt;       Necessary attribute for all recurring vouchers. | [optional] 
**recurring_start_date** | **datetime** | The date when the recurring vouchers start being generated.&lt;br&gt;       Necessary attribute for all recurring vouchers. | [optional] 
**recurring_next_voucher** | **datetime** | The date when the next voucher should be generated.&lt;br&gt;       Necessary attribute for all recurring vouchers. | [optional] 
**recurring_last_voucher** | **datetime** | The date when the last voucher was generated. | [optional] 
**recurring_end_date** | **datetime** | The date when the recurring vouchers end being generated.&lt;br&gt;      Necessary attribute for all recurring vouchers. | [optional] 
**enshrined** | **datetime** | Enshrined vouchers cannot be changed. Can only be set via [Voucher/{voucherId}/enshrine](#tag/Voucher/operation/voucherEnshrine). This operation cannot be undone. | [optional] [readonly] 
**tax_set** | [**ModelVoucherResponseTaxSet**](ModelVoucherResponseTaxSet.md) |  | [optional] 
**payment_deadline** | **datetime** | Payment deadline of the voucher. | [optional] 
**delivery_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**delivery_date_until** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.voucher_reset_to_open200_response_objects import VoucherResetToOpen200ResponseObjects

# TODO update the JSON string below
json = "{}"
# create an instance of VoucherResetToOpen200ResponseObjects from a JSON string
voucher_reset_to_open200_response_objects_instance = VoucherResetToOpen200ResponseObjects.from_json(json)
# print the JSON string representation of the object
print(VoucherResetToOpen200ResponseObjects.to_json())

# convert the object into a dict
voucher_reset_to_open200_response_objects_dict = voucher_reset_to_open200_response_objects_instance.to_dict()
# create an instance of VoucherResetToOpen200ResponseObjects from a dict
voucher_reset_to_open200_response_objects_from_dict = VoucherResetToOpen200ResponseObjects.from_dict(voucher_reset_to_open200_response_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


