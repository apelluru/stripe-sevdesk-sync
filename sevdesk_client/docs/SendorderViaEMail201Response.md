# SendorderViaEMail201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ModelEmailOrder]**](ModelEmailOrder.md) |  | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.sendorder_via_e_mail201_response import SendorderViaEMail201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendorderViaEMail201Response from a JSON string
sendorder_via_e_mail201_response_instance = SendorderViaEMail201Response.from_json(json)
# print the JSON string representation of the object
print(SendorderViaEMail201Response.to_json())

# convert the object into a dict
sendorder_via_e_mail201_response_dict = sendorder_via_e_mail201_response_instance.to_dict()
# create an instance of SendorderViaEMail201Response from a dict
sendorder_via_e_mail201_response_from_dict = SendorderViaEMail201Response.from_dict(sendorder_via_e_mail201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


