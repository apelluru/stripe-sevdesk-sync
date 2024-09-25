# ModelDiscountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the discount | [optional] 
**object_name** | **str** | Model name, which is &#39;Discounts&#39; | [optional] 
**create** | **str** | Date of discount creation | [optional] 
**update** | **str** | Date of last discount update | [optional] 
**sev_client** | **str** | Client to which the discount belongs | [optional] 
**discount** | **str** | Indicates that this is a discount or a surcharge (0 &#x3D; surcharge, 1 &#x3D; discount) | [optional] 
**text** | **str** | A text describing your position. | [optional] 
**percentage** | **str** | Defines if this is a percentage or an absolute discount | [optional] 
**value** | **str** | Value of the discount | [optional] 
**is_net** | **str** | Defines is the Discount net or gross (0 &#x3D; net, 1 &#x3D; gross) | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.model_discounts_response import ModelDiscountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDiscountsResponse from a JSON string
model_discounts_response_instance = ModelDiscountsResponse.from_json(json)
# print the JSON string representation of the object
print(ModelDiscountsResponse.to_json())

# convert the object into a dict
model_discounts_response_dict = model_discounts_response_instance.to_dict()
# create an instance of ModelDiscountsResponse from a dict
model_discounts_response_from_dict = ModelDiscountsResponse.from_dict(model_discounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


