# ModelVoucherUpdate

Voucher model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**supplier** | [**ModelVoucherUpdateSupplier**](ModelVoucherUpdateSupplier.md) |  | [optional] 
**supplier_name** | **str** | The supplier name.&lt;br&gt;       The value you provide here will determine what supplier name is shown for the voucher in case you did not provide a supplier. | [optional] 
**description** | **str** | The description of the voucher. Essentially the voucher number. | [optional] 
**pay_date** | **datetime** | Needs to be timestamp or dd.mm.yyyy | [optional] 
**status** | **float** | &lt;b&gt;Not supported in sevdesk-Update 2.0.&lt;/b&gt;&lt;br&gt;&lt;br&gt;    Please have a look in &lt;a href&#x3D;&#39;#tag/Voucher/Types-and-status-of-vouchers&#39;&gt;status of vouchers&lt;/a&gt;    to see what the different status codes mean | [optional] 
**paid_amount** | **float** | Amount which has already been paid for this voucher by the customer | [optional] [readonly] 
**tax_rule** | [**ModelVoucherTaxRule**](ModelVoucherTaxRule.md) |  | [optional] 
**tax_type** | **str** | **Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax type of the voucher. There are four tax types: 1. default - Umsatzsteuer ausweisen 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union) 3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz) 4. custom - Using custom tax set 5. ss - Not subject to VAT according to §19 1 UStG Tax rates are heavily connected to the tax type used. | [optional] 
**credit_debit** | **str** | Defines if your voucher is a credit (C) or debit (D) | [optional] 
**voucher_type** | **str** | Type of the voucher. For more information on the different types, check   &lt;a href&#x3D;&#39;#tag/Voucher/Types-and-status-of-vouchers&#39;&gt;this&lt;/a&gt;   | [optional] 
**currency** | **str** | specifies which currency the voucher should have. Attention: If the currency differs from the default currency stored in the account, then either the \&quot;propertyForeignCurrencyDeadline\&quot; or \&quot;propertyExchangeRate\&quot; parameter must be specified. If both parameters are specified, then the \&quot;propertyForeignCurrencyDeadline\&quot; parameter is preferred | [optional] 
**property_foreign_currency_deadline** | **datetime** | Defines the exchange rate day and and then the exchange rate is set from sevdesk. Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**property_exchange_rate** | **float** | Defines the exchange rate | [optional] 
**tax_set** | [**ModelVoucherUpdateTaxSet**](ModelVoucherUpdateTaxSet.md) |  | [optional] 
**payment_deadline** | **datetime** | Payment deadline of the voucher. | [optional] 
**delivery_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**delivery_date_until** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**document** | [**ModelVoucherDocument**](ModelVoucherDocument.md) |  | [optional] 
**cost_centre** | [**ModelVoucherCostCentre**](ModelVoucherCostCentre.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_voucher_update import ModelVoucherUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVoucherUpdate from a JSON string
model_voucher_update_instance = ModelVoucherUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelVoucherUpdate.to_json())

# convert the object into a dict
model_voucher_update_dict = model_voucher_update_instance.to_dict()
# create an instance of ModelVoucherUpdate from a dict
model_voucher_update_from_dict = ModelVoucherUpdate.from_dict(model_voucher_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


