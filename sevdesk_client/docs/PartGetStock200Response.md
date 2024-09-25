# PartGetStock200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | **int** | Stock amount | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.part_get_stock200_response import PartGetStock200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PartGetStock200Response from a JSON string
part_get_stock200_response_instance = PartGetStock200Response.from_json(json)
# print the JSON string representation of the object
print(PartGetStock200Response.to_json())

# convert the object into a dict
part_get_stock200_response_dict = part_get_stock200_response_instance.to_dict()
# create an instance of PartGetStock200Response from a dict
part_get_stock200_response_from_dict = PartGetStock200Response.from_dict(part_get_stock200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


