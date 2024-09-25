# ModelTextparserFetchDictionaryEntriesByTypeResponse

Textparser fetchDictionaryEntriesByType model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | [**List[ModelTextparserFetchDictionaryEntriesByTypeResponseValueInner]**](ModelTextparserFetchDictionaryEntriesByTypeResponseValueInner.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_textparser_fetch_dictionary_entries_by_type_response import ModelTextparserFetchDictionaryEntriesByTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelTextparserFetchDictionaryEntriesByTypeResponse from a JSON string
model_textparser_fetch_dictionary_entries_by_type_response_instance = ModelTextparserFetchDictionaryEntriesByTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ModelTextparserFetchDictionaryEntriesByTypeResponse.to_json())

# convert the object into a dict
model_textparser_fetch_dictionary_entries_by_type_response_dict = model_textparser_fetch_dictionary_entries_by_type_response_instance.to_dict()
# create an instance of ModelTextparserFetchDictionaryEntriesByTypeResponse from a dict
model_textparser_fetch_dictionary_entries_by_type_response_from_dict = ModelTextparserFetchDictionaryEntriesByTypeResponse.from_dict(model_textparser_fetch_dictionary_entries_by_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


