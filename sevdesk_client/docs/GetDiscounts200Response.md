# GetDiscounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelDiscount]**](ModelDiscount.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.get_discounts200_response import GetDiscounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiscounts200Response from a JSON string
get_discounts200_response_instance = GetDiscounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetDiscounts200Response.to_json())

# convert the object into a dict
get_discounts200_response_dict = get_discounts200_response_instance.to_dict()
# create an instance of GetDiscounts200Response from a dict
get_discounts200_response_from_dict = GetDiscounts200Response.from_dict(get_discounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


