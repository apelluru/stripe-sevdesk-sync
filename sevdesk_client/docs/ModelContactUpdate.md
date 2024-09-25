# ModelContactUpdate

Contact model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The organization name.&lt;br&gt; Be aware that the type of contact will depend on this attribute.&lt;br&gt; If it holds a value, the contact will be regarded as an organization. | [optional] 
**status** | **int** | Defines the status of the contact. 100 &lt;-&gt; Lead - 500 &lt;-&gt; Pending - 1000 &lt;-&gt; Active. | [optional] [default to 100]
**customer_number** | **str** | The customer number | [optional] 
**parent** | [**ModelContactUpdateParent**](ModelContactUpdateParent.md) |  | [optional] 
**surename** | **str** | The &lt;b&gt;first&lt;/b&gt; name of the contact.&lt;br&gt; Yeah... not quite right in literally every way. We know.&lt;br&gt; Not to be used for organizations. | [optional] 
**familyname** | **str** | The last name of the contact.&lt;br&gt; Not to be used for organizations. | [optional] 
**titel** | **str** | A non-academic title for the contact. Not to be used for organizations. | [optional] 
**category** | [**ModelContactUpdateCategory**](ModelContactUpdateCategory.md) |  | [optional] 
**description** | **str** | A description for the contact. | [optional] 
**academic_title** | **str** | A academic title for the contact. Not to be used for organizations. | [optional] 
**gender** | **str** | Gender of the contact.&lt;br&gt; Not to be used for organizations. | [optional] 
**name2** | **str** | Second name of the contact.&lt;br&gt; Not to be used for organizations. | [optional] 
**birthday** | **date** | Birthday of the contact.&lt;br&gt; Not to be used for organizations. | [optional] 
**vat_number** | **str** | Vat number of the contact. | [optional] 
**bank_account** | **str** | Bank account number (IBAN) of the contact. | [optional] 
**bank_number** | **str** | Bank number of the bank used by the contact. | [optional] 
**default_cashback_time** | **int** | Absolute time in days which the contact has to pay his invoices and subsequently get a cashback. | [optional] 
**default_cashback_percent** | **float** | Percentage of the invoice sum the contact gets back if he paid invoices in time. | [optional] 
**default_time_to_pay** | **int** | The payment goal in days which is set for every invoice of the contact. | [optional] 
**tax_number** | **str** | The tax number of the contact. | [optional] 
**tax_office** | **str** | The tax office of the contact (only for greek customers). | [optional] 
**exempt_vat** | **bool** | Defines if the contact is freed from paying vat. | [optional] 
**default_discount_amount** | **float** | The default discount the contact gets for every invoice.&lt;br&gt; Depending on defaultDiscountPercentage attribute, in percent or absolute value. | [optional] 
**default_discount_percentage** | **bool** | Defines if the discount is a percentage (true) or an absolute value (false). | [optional] 
**buyer_reference** | **str** | Buyer reference of the contact. | [optional] 
**government_agency** | **bool** | Defines whether the contact is a government agency (true) or not (false). | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_update import ModelContactUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactUpdate from a JSON string
model_contact_update_instance = ModelContactUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelContactUpdate.to_json())

# convert the object into a dict
model_contact_update_dict = model_contact_update_instance.to_dict()
# create an instance of ModelContactUpdate from a dict
model_contact_update_from_dict = ModelContactUpdate.from_dict(model_contact_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


