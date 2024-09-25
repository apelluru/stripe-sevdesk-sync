# ModelCreditNote

creditNote model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The creditNote id. &lt;span style&#x3D;&#39;color:red&#39;&gt;Required&lt;/span&gt; if you want to create/update an credit note position for an existing credit note\&quot; | [optional] 
**object_name** | **str** | The creditNote object name | 
**map_all** | **bool** |  | 
**create** | **datetime** | Date of creditNote creation | [optional] [readonly] 
**update** | **datetime** | Date of last creditNote update | [optional] [readonly] 
**credit_note_number** | **str** | The creditNote number | 
**contact** | [**ModelCreditNoteContact**](ModelCreditNoteContact.md) |  | 
**credit_note_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | 
**status** | **str** | Please have a look in       &lt;a href&#x3D;&#39;#tag/CreditNote/Status-of-credit-notes&#39;&gt;status of credit note&lt;/a&gt;      to see what the different status codes mean | 
**header** | **str** | Normally consist of prefix plus the creditNote number | 
**head_text** | **str** | Certain html tags can be used here to format your text | [optional] 
**foot_text** | **str** | Certain html tags can be used here to format your text | [optional] 
**address_country** | [**ModelCreditNoteAddressCountry**](ModelCreditNoteAddressCountry.md) |  | 
**create_user** | [**ModelCreditNoteCreateUser**](ModelCreditNoteCreateUser.md) |  | [optional] 
**sev_client** | [**ModelCreditNoteSevClient**](ModelCreditNoteSevClient.md) |  | [optional] 
**small_settlement** | **bool** | Defines if the client uses the small settlement scheme.      If yes, the creditNote must not contain any vat | [optional] 
**contact_person** | [**ModelCreditNoteContactPerson**](ModelCreditNoteContactPerson.md) |  | 
**tax_rule** | [**ModelCreditNoteResponseTaxRule**](ModelCreditNoteResponseTaxRule.md) |  | 
**tax_rate** | **float** | This is not used anymore. Use the taxRate of the individual positions instead. | 
**tax_set** | [**ModelCreditNoteTaxSet**](ModelCreditNoteTaxSet.md) |  | [optional] 
**tax_text** | **str** | A common tax text would be &#39;Umsatzsteuer 19%&#39; | 
**tax_type** | **str** | **Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax type of the creditNote. There are four tax types: 1. default - Umsatzsteuer ausweisen 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union) 3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz) 4. custom - Using custom tax set 5. ss - Not subject to VAT according to §19 1 UStG Tax rates are heavily connected to the tax type used. | 
**send_date** | **datetime** | The date the creditNote was sent to the customer | [optional] 
**address** | **str** | Complete address of the recipient including name, street, city, zip and country.&lt;br&gt;       Line breaks can be used and will be displayed on the invoice pdf. | [optional] 
**booking_category** | **str** | Defines the booking category, for more information see the section [Credit note booking categories](#tag/CreditNote/Credit-note-booking-categories)  The booking category of the credit note.  **Must be &lt;code&gt;UNDERACHIEVEMENT&lt;/code&gt; in sevdesk-Update 2.0.** | 
**currency** | **str** | Currency used in the creditNote. Needs to be currency code according to ISO-4217 | 
**sum_net** | **float** | Net sum of the creditNote | [optional] [readonly] 
**sum_tax** | **float** | Tax sum of the creditNote | [optional] [readonly] 
**sum_gross** | **float** | Gross sum of the creditNote | [optional] [readonly] 
**sum_discounts** | **float** | Sum of all discounts in the creditNote | [optional] [readonly] 
**sum_net_foreign_currency** | **float** | Net sum of the creditNote in the foreign currency | [optional] [readonly] 
**sum_tax_foreign_currency** | **float** | Tax sum of the creditNote in the foreign currency | [optional] [readonly] 
**sum_gross_foreign_currency** | **float** | Gross sum of the creditNote in the foreign currency | [optional] [readonly] 
**sum_discounts_foreign_currency** | **float** | Discounts sum of the creditNote in the foreign currency | [optional] [readonly] 
**customer_internal_note** | **str** | Internal note of the customer. Contains data entered into field &#39;Referenz/Bestellnummer&#39; | [optional] 
**show_net** | **bool** | If true, the net amount of each position will be shown on the creditNote. Otherwise gross amount | [optional] 
**send_type** | **str** | Type which was used to send the creditNote. IMPORTANT: Please refer to the creditNote section of the       *     API-Overview to understand how this attribute can be used before using it! | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note import ModelCreditNote

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNote from a JSON string
model_credit_note_instance = ModelCreditNote.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNote.to_json())

# convert the object into a dict
model_credit_note_dict = model_credit_note_instance.to_dict()
# create an instance of ModelCreditNote from a dict
model_credit_note_from_dict = ModelCreditNote.from_dict(model_credit_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


