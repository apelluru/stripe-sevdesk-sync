# GetContactTabsItemCountById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | **float** |  | [optional] 
**invoices** | **float** |  | [optional] 
**credit_notes** | **float** |  | [optional] 
**documents** | **float** |  | [optional] 
**persons** | **float** |  | [optional] 
**vouchers** | **float** |  | [optional] 
**letters** | **float** |  | [optional] 
**parts** | **str** |  | [optional] 
**invoice_pos** | **float** |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_contact_tabs_item_count_by_id200_response import GetContactTabsItemCountById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactTabsItemCountById200Response from a JSON string
get_contact_tabs_item_count_by_id200_response_instance = GetContactTabsItemCountById200Response.from_json(json)
# print the JSON string representation of the object
print(GetContactTabsItemCountById200Response.to_json())

# convert the object into a dict
get_contact_tabs_item_count_by_id200_response_dict = get_contact_tabs_item_count_by_id200_response_instance.to_dict()
# create an instance of GetContactTabsItemCountById200Response from a dict
get_contact_tabs_item_count_by_id200_response_from_dict = GetContactTabsItemCountById200Response.from_dict(get_contact_tabs_item_count_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


