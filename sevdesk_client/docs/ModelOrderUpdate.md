# ModelOrderUpdate

Order model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The order id | [optional] [readonly] 
**object_name** | **str** | The order object name | [optional] [readonly] 
**create** | **datetime** | Date of order creation | [optional] [readonly] 
**update** | **datetime** | Date of last order update | [optional] [readonly] 
**order_number** | **str** | The order number | [optional] 
**contact** | [**ModelOrderUpdateContact**](ModelOrderUpdateContact.md) |  | [optional] 
**order_date** | **datetime** | Needs to be provided as timestamp or dd.mm.yyyy | [optional] 
**status** | **int** | Please have a look in       &lt;a href&#x3D;&#39;#tag/Order/Types-and-status-of-orders&#39;&gt;status of orders&lt;/a&gt;      to see what the different status codes mean | [optional] 
**header** | **str** | Normally consist of prefix plus the order number | [optional] 
**head_text** | **str** | Certain html tags can be used here to format your text | [optional] 
**foot_text** | **str** | Certain html tags can be used here to format your text | [optional] 
**address_country** | [**ModelOrderUpdateAddressCountry**](ModelOrderUpdateAddressCountry.md) |  | [optional] 
**create_user** | [**ModelOrderUpdateCreateUser**](ModelOrderUpdateCreateUser.md) |  | [optional] 
**sev_client** | [**ModelOrderUpdateSevClient**](ModelOrderUpdateSevClient.md) |  | [optional] 
**delivery_terms** | **str** | Delivery terms of the order | [optional] 
**payment_terms** | **str** | Payment terms of the order | [optional] 
**origin** | [**ModelOrderOrigin**](ModelOrderOrigin.md) |  | [optional] 
**version** | **int** | Version of the order.&lt;br&gt;      Can be used if you have multiple drafts for the same order.&lt;br&gt;      Should start with 0 | [optional] 
**small_settlement** | **bool** | Defines if the client uses the small settlement scheme.      If yes, the order must not contain any vat | [optional] 
**contact_person** | [**ModelOrderUpdateContactPerson**](ModelOrderUpdateContactPerson.md) |  | [optional] 
**tax_rate** | **float** | This is not used anymore. Use the taxRate of the individual positions instead. | [optional] 
**tax_rule** | [**ModelCreditNoteResponseTaxRule**](ModelCreditNoteResponseTaxRule.md) |  | [optional] 
**tax_set** | [**ModelOrderUpdateTaxSet**](ModelOrderUpdateTaxSet.md) |  | [optional] 
**tax_text** | **str** | A common tax text would be &#39;Umsatzsteuer 19%&#39; | [optional] 
**tax_type** | **str** | **Use this in sevdesk-Update 1.0 (instead of taxRule).**  Tax type of the order. There are four tax types: 1. default - Umsatzsteuer ausweisen 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union) 3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz) 4. custom - Using custom tax set 5. ss - Not subject to VAT according to §19 1 UStG Tax rates are heavily connected to the tax type used. | [optional] 
**order_type** | **str** | Type of the order. For more information on the different types, check      &lt;a href&#x3D;&#39;#tag/Order/Types-and-status-of-orders&#39;&gt;this&lt;/a&gt;   | [optional] 
**send_date** | **datetime** | The date the order was sent to the customer | [optional] 
**address** | **str** | Complete address of the recipient including name, street, city, zip and country.&lt;br&gt;       Line breaks can be used and will be displayed on the invoice pdf. | [optional] 
**currency** | **str** | Currency used in the order. Needs to be currency code according to ISO-4217 | [optional] 
**sum_net** | **float** | Net sum of the order | [optional] [readonly] 
**sum_tax** | **float** | Tax sum of the order | [optional] [readonly] 
**sum_gross** | **float** | Gross sum of the order | [optional] [readonly] 
**sum_discounts** | **float** | Sum of all discounts in the order | [optional] [readonly] 
**sum_net_foreign_currency** | **float** | Net sum of the order in the foreign currency | [optional] [readonly] 
**sum_tax_foreign_currency** | **float** | Tax sum of the order in the foreign currency | [optional] [readonly] 
**sum_gross_foreign_currency** | **float** | Gross sum of the order in the foreign currency | [optional] [readonly] 
**sum_discounts_foreign_currency** | **float** | Discounts sum of the order in the foreign currency | [optional] [readonly] 
**customer_internal_note** | **str** | Internal note of the customer. Contains data entered into field &#39;Referenz/Bestellnummer&#39; | [optional] 
**show_net** | **bool** | If true, the net amount of each position will be shown on the order. Otherwise gross amount | [optional] 
**send_type** | **str** | Type which was used to send the order. IMPORTANT: Please refer to the order section of the       *     API-Overview to understand how this attribute can be used before using it! | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_order_update import ModelOrderUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrderUpdate from a JSON string
model_order_update_instance = ModelOrderUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelOrderUpdate.to_json())

# convert the object into a dict
model_order_update_dict = model_order_update_instance.to_dict()
# create an instance of ModelOrderUpdate from a dict
model_order_update_from_dict = ModelOrderUpdate.from_dict(model_order_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

