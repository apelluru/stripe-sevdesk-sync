# ModelContactResponse

Contact model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The contact id | [optional] [readonly] 
**object_name** | **str** | The contact object name | [optional] [readonly] 
**create** | **datetime** | Date of contact creation | [optional] [readonly] 
**update** | **datetime** | Date of last contact update | [optional] [readonly] 
**name** | **str** | The organization name.&lt;br&gt; Be aware that the type of contact will depend on this attribute.&lt;br&gt; If it holds a value, the contact will be regarded as an organization. | [optional] [readonly] 
**status** | **str** | Defines the status of the contact. 100 &lt;-&gt; Lead - 500 &lt;-&gt; Pending - 1000 &lt;-&gt; Active. | [optional] [readonly] 
**customer_number** | **str** | The customer number | [optional] [readonly] 
**parent** | [**ModelContactResponseParent**](ModelContactResponseParent.md) |  | [optional] 
**surename** | **str** | The &lt;b&gt;first&lt;/b&gt; name of the contact.&lt;br&gt; Yeah... not quite right in literally every way. We know.&lt;br&gt; Not to be used for organizations. | [optional] [readonly] 
**familyname** | **str** | The last name of the contact.&lt;br&gt; Not to be used for organizations. | [optional] [readonly] 
**titel** | **str** | A non-academic title for the contact. Not to be used for organizations. | [optional] [readonly] 
**category** | [**ModelContactResponseCategory**](ModelContactResponseCategory.md) |  | [optional] 
**description** | **str** | A description for the contact. | [optional] [readonly] 
**academic_title** | **str** | A academic title for the contact. Not to be used for organizations. | [optional] [readonly] 
**gender** | **str** | Gender of the contact.&lt;br&gt; Not to be used for organizations. | [optional] [readonly] 
**sev_client** | [**ModelContactResponseSevClient**](ModelContactResponseSevClient.md) |  | [optional] 
**name2** | **str** | Second name of the contact.&lt;br&gt; Not to be used for organizations. | [optional] [readonly] 
**birthday** | **date** | Birthday of the contact.&lt;br&gt; Not to be used for organizations. | [optional] [readonly] 
**vat_number** | **str** | Vat number of the contact. | [optional] [readonly] 
**bank_account** | **str** | Bank account number (IBAN) of the contact. | [optional] [readonly] 
**bank_number** | **str** | Bank number of the bank used by the contact. | [optional] [readonly] 
**default_cashback_time** | **str** | Absolute time in days which the contact has to pay his invoices and subsequently get a cashback. | [optional] [readonly] 
**default_cashback_percent** | **float** | Percentage of the invoice sum the contact gets back if he paid invoices in time. | [optional] [readonly] 
**default_time_to_pay** | **str** | The payment goal in days which is set for every invoice of the contact. | [optional] [readonly] 
**tax_number** | **str** | The tax number of the contact. | [optional] [readonly] 
**tax_office** | **str** | The tax office of the contact (only for greek customers). | [optional] [readonly] 
**exempt_vat** | **str** | Defines if the contact is freed from paying vat. | [optional] [readonly] 
**default_discount_amount** | **float** | The default discount the contact gets for every invoice.&lt;br&gt; Depending on defaultDiscountPercentage attribute, in percent or absolute value. | [optional] [readonly] 
**default_discount_percentage** | **str** | Defines if the discount is a percentage (true) or an absolute value (false). | [optional] [readonly] 
**buyer_reference** | **str** | Buyer reference of the contact. | [optional] [readonly] 
**government_agency** | **str** | Defines whether the contact is a government agency (true) or not (false). | [optional] [readonly] 
**additional_information** | **str** | Additional information stored for the contact. | [optional] [readonly] 

## Example

```python
from sevdesk_client.openapi_client.models.model_contact_response import ModelContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContactResponse from a JSON string
model_contact_response_instance = ModelContactResponse.from_json(json)
# print the JSON string representation of the object
print(ModelContactResponse.to_json())

# convert the object into a dict
model_contact_response_dict = model_contact_response_instance.to_dict()
# create an instance of ModelContactResponse from a dict
model_contact_response_from_dict = ModelContactResponse.from_dict(model_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


