# CreateTagRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the invoice/order/voucher/creditNote | 
**object_name** | **str** | Model name | 

## Example

```python
from sevdesk_client.openapi_client.models.create_tag_request_object import CreateTagRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagRequestObject from a JSON string
create_tag_request_object_instance = CreateTagRequestObject.from_json(json)
# print the JSON string representation of the object
print(CreateTagRequestObject.to_json())

# convert the object into a dict
create_tag_request_object_dict = create_tag_request_object_instance.to_dict()
# create an instance of CreateTagRequestObject from a dict
create_tag_request_object_from_dict = CreateTagRequestObject.from_dict(create_tag_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


