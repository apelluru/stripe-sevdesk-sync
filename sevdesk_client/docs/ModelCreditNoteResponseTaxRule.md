# ModelCreditNoteResponseTaxRule

**Use this in sevdesk-Update 2.0 (replaces taxType / taxSet).**

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | **Use this in sevdesk-Update 2.0 (replaces taxType / taxSet).**  Defines the vat-regulation. For \&quot;Regelbesteuerung\&quot; it can be one of:   - &#x60;1&#x60; - Umsatzsteuerpflichtige Umsätze - tax rates: 0.0, 7.0, 19.0 - replaces &#x60;\&quot;taxType\&quot;: \&quot;default\&quot;&#x60;   - &#x60;2&#x60; - Ausfuhren - allowedTaxRates: 0.0   - &#x60;3&#x60; - Innergemeinschaftliche Lieferungen - tax rates: 0.0, 7.0, 19.0 - replaces &#x60;\&quot;taxType\&quot;: \&quot;eu\&quot;&#x60;   - &#x60;4&#x60; - Steuerfreie Umsätze §4 UStG - tax rates: 0.0   - &#x60;5&#x60; - Reverse Charge gem. §13b UStG - tax rates: 0.0  For small business owner (\&quot;Kleinunternehmer\&quot;) it can be:   - &#x60;11&#x60; - Steuer nicht erhoben nach §19UStG - tax rates: 0.0 - replaces &#x60;\&quot;taxType\&quot;: \&quot;ss\&quot;&#x60; | 
**object_name** | **str** | Name of the object. Must always be TaxRule&#x60; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_credit_note_response_tax_rule import ModelCreditNoteResponseTaxRule

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreditNoteResponseTaxRule from a JSON string
model_credit_note_response_tax_rule_instance = ModelCreditNoteResponseTaxRule.from_json(json)
# print the JSON string representation of the object
print(ModelCreditNoteResponseTaxRule.to_json())

# convert the object into a dict
model_credit_note_response_tax_rule_dict = model_credit_note_response_tax_rule_instance.to_dict()
# create an instance of ModelCreditNoteResponseTaxRule from a dict
model_credit_note_response_tax_rule_from_dict = ModelCreditNoteResponseTaxRule.from_dict(model_credit_note_response_tax_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


