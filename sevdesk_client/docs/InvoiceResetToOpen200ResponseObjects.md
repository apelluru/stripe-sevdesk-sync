# InvoiceResetToOpen200ResponseObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The invoice id | [optional] [readonly] 
**object_name** | **str** | The invoice object name | [optional] [readonly] 
**invoice_number** | **str** | The invoice number | [optional] [readonly] 
**contact** | [**ModelInvoiceResponseContact**](ModelInvoiceResponseContact.md) |  | [optional] 
**create** | **datetime** | Date of invoice creation | [optional] [readonly] 
**update** | **datetime** | Date of last invoice update | [optional] [readonly] 
**sev_client** | [**ModelInvoiceResponseSevClient**](ModelInvoiceResponseSevClient.md) |  | [optional] 
**invoice_date** | **str** | The invoice date. | [optional] [readonly] 
**header** | **str** | Normally consist of prefix plus the invoice number | [optional] [readonly] 
**head_text** | **str** | Certain html tags can be used here to format your text | [optional] [readonly] 
**foot_text** | **str** | Certain html tags can be used here to format your text | [optional] [readonly] 
**time_to_pay** | **str** | The time the customer has to pay the invoice in days | [optional] [readonly] 
**discount_time** | **str** | If a value other than zero is used for the discount attribute,      you need to specify the amount of days for which the discount is granted. | [optional] [readonly] 
**discount** | **str** | If you want to give a discount, define the percentage here. Otherwise provide zero as value | [optional] [readonly] 
**address_country** | [**ModelInvoiceResponseAddressCountry**](ModelInvoiceResponseAddressCountry.md) |  | [optional] 
**pay_date** | **object** |  | [optional] 
**create_user** | [**ModelCreditNoteResponseCreateUser**](ModelCreditNoteResponseCreateUser.md) |  | [optional] 
**delivery_date** | **datetime** | Timestamp. This can also be a date range if you also use the attribute deliveryDateUntil | [optional] [readonly] 
**status** | **object** |  | [optional] 
**small_settlement** | **bool** | Defines if the client uses the small settlement scheme.      If yes, the invoice must not contain any vat | [optional] [readonly] 
**contact_person** | [**ModelInvoiceResponseContactPerson**](ModelInvoiceResponseContactPerson.md) |  | [optional] 
**tax_rate** | **str** | This is not used anymore. Use the taxRate of the individual positions instead. | [optional] [readonly] 
**tax_rule** | [**ModelCreditNoteResponseTaxRule**](ModelCreditNoteResponseTaxRule.md) |  | [optional] 
**tax_text** | **str** | A common tax text would be &#39;Umsatzsteuer 19%&#39; | [optional] [readonly] 
**dunning_level** | **str** | Defines how many reminders have already been sent for the invoice.      Starts with 1 (Payment reminder) and should be incremented by one every time another reminder is sent. | [optional] [readonly] 
**tax_type** | **str** | **Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax type of the invoice. There are four tax types: 1. default - Umsatzsteuer ausweisen 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union) 3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz) 4. custom - Using custom tax set 5. ss - Not subject to VAT according to §19 1 UStG Tax rates are heavily connected to the tax type used. | [optional] [readonly] 
**payment_method** | [**ModelInvoiceResponsePaymentMethod**](ModelInvoiceResponsePaymentMethod.md) |  | [optional] 
**cost_centre** | [**ModelInvoiceResponseCostCentre**](ModelInvoiceResponseCostCentre.md) |  | [optional] 
**send_date** | **datetime** | The date the invoice was sent to the customer | [optional] [readonly] 
**origin** | [**ModelInvoiceResponseOrigin**](ModelInvoiceResponseOrigin.md) |  | [optional] 
**invoice_type** | **str** | Type of the invoice. For more information on the different types, check       &lt;a href&#x3D;&#39;#tag/Invoice/Types-and-status-of-invoices&#39;&gt;this&lt;/a&gt; section   | [optional] [readonly] 
**account_intervall** | **object** |  | [optional] 
**account_next_invoice** | **object** |  | [optional] 
**reminder_total** | **str** | Total reminder amount | [optional] [readonly] 
**reminder_debit** | **str** | Debit of the reminder | [optional] [readonly] 
**reminder_deadline** | **datetime** | Deadline of the reminder as timestamp | [optional] [readonly] 
**reminder_charge** | **str** | The additional reminder charge | [optional] [readonly] 
**tax_set** | [**ModelInvoiceResponseTaxSet**](ModelInvoiceResponseTaxSet.md) |  | [optional] 
**address** | **str** | Complete address of the recipient including name, street, city, zip and country.       * Line breaks can be used and will be displayed on the invoice pdf. | [optional] [readonly] 
**currency** | **str** | Currency used in the invoice. Needs to be currency code according to ISO-4217 | [optional] [readonly] 
**sum_net** | **str** | Net sum of the invoice | [optional] [readonly] 
**sum_tax** | **str** | Tax sum of the invoice | [optional] [readonly] 
**sum_gross** | **str** | Gross sum of the invoice | [optional] [readonly] 
**sum_discounts** | **str** | Sum of all discounts in the invoice | [optional] [readonly] 
**sum_net_foreign_currency** | **str** | Net sum of the invoice in the foreign currency | [optional] [readonly] 
**sum_tax_foreign_currency** | **str** | Tax sum of the invoice in the foreign currency | [optional] [readonly] 
**sum_gross_foreign_currency** | **str** | Gross sum of the invoice in the foreign currency | [optional] [readonly] 
**sum_discounts_foreign_currency** | **str** | Discounts sum of the invoice in the foreign currency | [optional] [readonly] 
**sum_net_accounting** | **str** | Net accounting sum of the invoice. Is usually the same as sumNet | [optional] [readonly] 
**sum_tax_accounting** | **str** | Tax accounting sum of the invoice. Is usually the same as sumTax | [optional] [readonly] 
**sum_gross_accounting** | **str** | Gross accounting sum of the invoice. Is usually the same as sumGross | [optional] [readonly] 
**paid_amount** | **float** | Amount which has already been paid for this invoice by the customer | [optional] [readonly] 
**customer_internal_note** | **str** | Internal note of the customer. Contains data entered into field &#39;Referenz/Bestellnummer&#39; | [optional] [readonly] 
**show_net** | **bool** | If true, the net amount of each position will be shown on the invoice. Otherwise gross amount | [optional] [readonly] 
**enshrined** | **object** |  | [optional] 
**send_type** | **str** | Type which was used to send the invoice. IMPORTANT: Please refer to the invoice section of the       *     API-Overview to understand how this attribute can be used before using it! | [optional] [readonly] 
**delivery_date_until** | **str** | If the delivery date should be a time range, another timestamp can be provided in this attribute       * to define a range from timestamp used in deliveryDate attribute to the timestamp used here. | [optional] [readonly] 
**datev_connect_online** | **object** | Internal attribute | [optional] [readonly] 
**send_payment_received_notification_date** | **str** | Internal attribute | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.invoice_reset_to_open200_response_objects import InvoiceResetToOpen200ResponseObjects

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceResetToOpen200ResponseObjects from a JSON string
invoice_reset_to_open200_response_objects_instance = InvoiceResetToOpen200ResponseObjects.from_json(json)
# print the JSON string representation of the object
print(InvoiceResetToOpen200ResponseObjects.to_json())

# convert the object into a dict
invoice_reset_to_open200_response_objects_dict = invoice_reset_to_open200_response_objects_instance.to_dict()
# create an instance of InvoiceResetToOpen200ResponseObjects from a dict
invoice_reset_to_open200_response_objects_from_dict = InvoiceResetToOpen200ResponseObjects.from_dict(invoice_reset_to_open200_response_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


