# CreditNoteResetToOpen200ResponseObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The creditNote id | [optional] [readonly] 
**object_name** | **str** | The creditNote object name | [optional] [readonly] 
**create** | **datetime** | Date of creditNote creation | [optional] [readonly] 
**update** | **datetime** | Date of last creditNote update | [optional] [readonly] 
**credit_note_number** | **str** | The creditNote number | [optional] 
**contact** | [**ModelCreditNoteResponseContact**](ModelCreditNoteResponseContact.md) |  | [optional] 
**credit_note_date** | **datetime** | The credit note date | [optional] 
**status** | **object** |  | [optional] 
**header** | **str** | Normally consist of prefix plus the creditNote number | [optional] 
**head_text** | **str** | Certain html tags can be used here to format your text | [optional] 
**foot_text** | **str** | Certain html tags can be used here to format your text | [optional] 
**address_country** | [**ModelCreditNoteResponseAddressCountry**](ModelCreditNoteResponseAddressCountry.md) |  | [optional] 
**create_user** | [**ModelCreditNoteResponseCreateUser**](ModelCreditNoteResponseCreateUser.md) |  | [optional] 
**sev_client** | [**ModelCreditNoteResponseSevClient**](ModelCreditNoteResponseSevClient.md) |  | [optional] 
**delivery_date** | **datetime** | Timestamp. This can also be a date range if you also use the attribute deliveryDateUntil | [optional] 
**small_settlement** | **bool** | Defines if the client uses the small settlement scheme.      If yes, the creditNote must not contain any vat | [optional] 
**contact_person** | [**ModelCreditNoteResponseContactPerson**](ModelCreditNoteResponseContactPerson.md) |  | [optional] 
**tax_rate** | **str** | This is not used anymore. Use the taxRate of the individual positions instead. | [optional] 
**tax_rule** | [**ModelCreditNoteResponseTaxRule**](ModelCreditNoteResponseTaxRule.md) |  | [optional] 
**tax_set** | [**ModelCreditNoteResponseTaxSet**](ModelCreditNoteResponseTaxSet.md) |  | [optional] 
**tax_text** | **str** | A common tax text would be &#39;Umsatzsteuer 19%&#39; | [optional] 
**tax_type** | **str** | **Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax type of the creditNote. There are four tax types: 1. default - Umsatzsteuer ausweisen 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union) 3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz) 4. custom - Using custom tax set 5. ss - Not subject to VAT according to §19 1 UStG Tax rates are heavily connected to the tax type used. | [optional] 
**send_date** | **datetime** | The date the creditNote was sent to the customer | [optional] 
**address** | **str** | Complete address of the recipient including name, street, city, zip and country.&lt;br&gt;       Line breaks can be used and will be displayed on the invoice pdf. | [optional] 
**currency** | **str** | Currency used in the creditNote. Needs to be currency code according to ISO-4217 | [optional] 
**sum_net** | **str** | Net sum of the creditNote | [optional] [readonly] 
**sum_tax** | **str** | Tax sum of the creditNote | [optional] [readonly] 
**sum_gross** | **str** | Gross sum of the creditNote | [optional] [readonly] 
**sum_discounts** | **str** | Sum of all discounts in the creditNote | [optional] [readonly] 
**sum_net_foreign_currency** | **str** | Net sum of the creditNote in the foreign currency | [optional] [readonly] 
**sum_tax_foreign_currency** | **str** | Tax sum of the creditNote in the foreign currency | [optional] [readonly] 
**sum_gross_foreign_currency** | **str** | Gross sum of the creditNote in the foreign currency | [optional] [readonly] 
**sum_discounts_foreign_currency** | **str** | Discounts sum of the creditNote in the foreign currency | [optional] [readonly] 
**customer_internal_note** | **str** | Internal note of the customer. Contains data entered into field &#39;Referenz/Bestellnummer&#39; | [optional] 
**show_net** | **bool** | If true, the net amount of each position will be shown on the creditNote. Otherwise gross amount | [optional] 
**send_type** | **str** | Type which was used to send the creditNote. IMPORTANT: Please refer to the creditNote section of the       *     API-Overview to understand how this attribute can be used before using it! | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.credit_note_reset_to_open200_response_objects import CreditNoteResetToOpen200ResponseObjects

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteResetToOpen200ResponseObjects from a JSON string
credit_note_reset_to_open200_response_objects_instance = CreditNoteResetToOpen200ResponseObjects.from_json(json)
# print the JSON string representation of the object
print(CreditNoteResetToOpen200ResponseObjects.to_json())

# convert the object into a dict
credit_note_reset_to_open200_response_objects_dict = credit_note_reset_to_open200_response_objects_instance.to_dict()
# create an instance of CreditNoteResetToOpen200ResponseObjects from a dict
credit_note_reset_to_open200_response_objects_from_dict = CreditNoteResetToOpen200ResponseObjects.from_dict(credit_note_reset_to_open200_response_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


