# ModelEmailOrder

Email model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The email id | [optional] [readonly] 
**object_name** | **str** | The email object name | [optional] [readonly] 
**create** | **datetime** | Date of mail creation | [optional] [readonly] 
**update** | **datetime** | Date of last mail update | [optional] [readonly] 
**object** | [**ModelOrderResponse**](ModelOrderResponse.md) |  | [optional] 
**var_from** | **str** | The sender of the email | 
**to** | **str** | The recipient of the email | 
**subject** | **str** | The subject of the email | 
**text** | **str** | The text of the email | [optional] 
**sev_client** | [**ModelEmailSevClient**](ModelEmailSevClient.md) |  | [optional] 
**cc** | **str** | A list of mail addresses which are in the cc | [optional] 
**bcc** | **str** | A list of mail addresses which are in the bcc | [optional] 
**arrived** | **datetime** | Date the mail arrived | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_email_order import ModelEmailOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ModelEmailOrder from a JSON string
model_email_order_instance = ModelEmailOrder.from_json(json)
# print the JSON string representation of the object
print(ModelEmailOrder.to_json())

# convert the object into a dict
model_email_order_dict = model_email_order_instance.to_dict()
# create an instance of ModelEmailOrder from a dict
model_email_order_from_dict = ModelEmailOrder.from_dict(model_email_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


