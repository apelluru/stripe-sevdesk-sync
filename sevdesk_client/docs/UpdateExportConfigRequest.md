# UpdateExportConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountant_number** | **float** |  | 
**accountant_client_number** | **float** |  | 
**accounting_year_begin** | **float** |  | 

## Example

```python
from sevdesk_client.openapi_client.models.update_export_config_request import UpdateExportConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExportConfigRequest from a JSON string
update_export_config_request_instance = UpdateExportConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateExportConfigRequest.to_json())

# convert the object into a dict
update_export_config_request_dict = update_export_config_request_instance.to_dict()
# create an instance of UpdateExportConfigRequest from a dict
update_export_config_request_from_dict = UpdateExportConfigRequest.from_dict(update_export_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


