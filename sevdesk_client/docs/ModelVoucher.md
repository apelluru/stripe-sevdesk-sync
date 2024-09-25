# ModelVoucher

Voucher model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The voucher id | [optional] [readonly] 
**object_name** | **str** | The voucher object name | 
**map_all** | **bool** |  | 
**create** | **datetime** | Date of voucher creation | [optional] [readonly] 
**update** | **datetime** | Date of last voucher update | [optional] [readonly] 
**sev_client** | [**ModelVoucherSevClient**](ModelVoucherSevClient.md) |  | [optional] 
**create_user** | [**ModelVoucherCreateUser**](ModelVoucherCreateUser.md) |  | [optional] 
**voucher_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**supplier** | [**ModelVoucherSupplier**](ModelVoucherSupplier.md) |  | [optional] 
**supplier_name** | **str** | The supplier name.&lt;br&gt;       The value you provide here will determine what supplier name is shown for the voucher in case you did not provide a supplier. | [optional] 
**description** | **str** | The description of the voucher. Essentially the voucher number. | [optional] 
**pay_date** | **datetime** | Needs to be timestamp or dd.mm.yyyy | [optional] 
**status** | **float** | Please have a look in       &lt;a href&#x3D;&#39;#tag/Voucher/Types-and-status-of-vouchers&#39;&gt;status of vouchers&lt;/a&gt;      to see what the different status codes mean | 
**sum_net** | **float** | Net sum of the voucher | [optional] [readonly] 
**sum_tax** | **float** | Tax sum of the voucher | [optional] [readonly] 
**sum_gross** | **float** | Gross sum of the voucher | [optional] [readonly] 
**sum_net_accounting** | **float** | Net accounting sum of the voucher. Is usually the same as sumNet | [optional] [readonly] 
**sum_tax_accounting** | **float** | Tax accounting sum of the voucher. Is usually the same as sumTax | [optional] [readonly] 
**sum_gross_accounting** | **float** | Gross accounting sum of the voucher. Is usually the same as sumGross | [optional] [readonly] 
**sum_discounts** | **float** | Sum of all discounts in the voucher | [optional] [readonly] 
**sum_discounts_foreign_currency** | **float** | Discounts sum of the voucher in the foreign currency | [optional] [readonly] 
**paid_amount** | **float** | Amount which has already been paid for this voucher by the customer | [optional] [readonly] 
**tax_rule** | [**ModelVoucherTaxRule**](ModelVoucherTaxRule.md) |  | 
**tax_type** | **str** | **Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax type of the voucher. There are four tax types: 1. default - Umsatzsteuer ausweisen 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union) 3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz) 4. custom - Using custom tax set 5. ss - Not subject to VAT according to §19 1 UStG Tax rates are heavily connected to the tax type used. | 
**credit_debit** | **str** | Defines if your voucher is a credit (C) or debit (D) | 
**voucher_type** | **str** | Type of the voucher. For more information on the different types, check       &lt;a href&#x3D;&#39;#tag/Voucher/Types-and-status-of-vouchers&#39;&gt;this&lt;/a&gt;   | 
**currency** | **str** | specifies which currency the voucher should have. Attention: If the currency differs from the default currency stored in the account, then either the \&quot;propertyForeignCurrencyDeadline\&quot; or \&quot;propertyExchangeRate\&quot; parameter must be specified. If both parameters are specified, then the \&quot;propertyForeignCurrencyDeadline\&quot; parameter is preferred | [optional] 
**property_foreign_currency_deadline** | **datetime** | Defines the exchange rate day and and then the exchange rate is set from sevdesk. Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**property_exchange_rate** | **float** | Defines the exchange rate | [optional] 
**recurring_interval** | **str** | The DateInterval in which recurring vouchers are generated.&lt;br&gt;       Necessary attribute for all recurring vouchers. | [optional] [readonly] 
**recurring_start_date** | **datetime** | The date when the recurring vouchers start being generated.&lt;br&gt;       Necessary attribute for all recurring vouchers. | [optional] [readonly] 
**recurring_next_voucher** | **datetime** | The date when the next voucher should be generated.&lt;br&gt;       Necessary attribute for all recurring vouchers. | [optional] [readonly] 
**recurring_last_voucher** | **datetime** | The date when the last voucher was generated. | [optional] [readonly] 
**recurring_end_date** | **datetime** | The date when the recurring vouchers end being generated.&lt;br&gt;      Necessary attribute for all recurring vouchers. | [optional] [readonly] 
**enshrined** | **datetime** | Enshrined vouchers cannot be changed. Can only be set via [Voucher/{voucherId}/enshrine](#tag/Voucher/operation/voucherEnshrine). This operation cannot be undone. | [optional] [readonly] 
**tax_set** | [**ModelVoucherTaxSet**](ModelVoucherTaxSet.md) |  | [optional] 
**payment_deadline** | **datetime** | Payment deadline of the voucher. | [optional] 
**delivery_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**delivery_date_until** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**document** | [**ModelVoucherDocument**](ModelVoucherDocument.md) |  | [optional] 
**cost_centre** | [**ModelVoucherCostCentre**](ModelVoucherCostCentre.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher import ModelVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucher from a JSON string
model_voucher_instance = ModelVoucher.from_json(json)
# print the JSON string representation of the object
print(ModelVoucher.to_json())

# convert the object into a dict
model_voucher_dict = model_voucher_instance.to_dict()
# create an instance of ModelVoucher from a dict
model_voucher_from_dict = ModelVoucher.from_dict(model_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

