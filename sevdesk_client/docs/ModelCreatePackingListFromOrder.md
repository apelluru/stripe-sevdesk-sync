# ModelCreatePackingListFromOrder

order model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the order | 
**object_name** | **str** | Model name, which is &#39;Order&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.model_create_packing_list_from_order import ModelCreatePackingListFromOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreatePackingListFromOrder from a JSON string
model_create_packing_list_from_order_instance = ModelCreatePackingListFromOrder.from_json(json)
# print the JSON string representation of the object
print(ModelCreatePackingListFromOrder.to_json())

# convert the object into a dict
model_create_packing_list_from_order_dict = model_create_packing_list_from_order_instance.to_dict()
# create an instance of ModelCreatePackingListFromOrder from a dict
model_create_packing_list_from_order_from_dict = ModelCreatePackingListFromOrder.from_dict(model_create_packing_list_from_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


