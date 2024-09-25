# openapi_client.InvoicePosApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_pos**](InvoicePosApi.md#get_invoice_pos) | **GET** /InvoicePos | Retrieve InvoicePos


# **get_invoice_pos**
> GetInvoicePositionsById200Response get_invoice_pos(id=id, invoice_id=invoice_id, invoice_object_name=invoice_object_name, part_id=part_id, part_object_name=part_object_name)

Retrieve InvoicePos

There are a multitude of parameter which can be used to filter.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_invoice_positions_by_id200_response import GetInvoicePositionsById200Response
from sevdesk_client.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://my.sevdesk.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://my.sevdesk.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.InvoicePosApi(api_client)
    id = 3.4 # float | Retrieve all InvoicePos with this InvoicePos id (optional)
    invoice_id = 3.4 # float | Retrieve all invoices positions with this invoice. Must be provided with invoice[objectName] (optional)
    invoice_object_name = 'invoice_object_name_example' # str | Only required if invoice[id] was provided. 'Invoice' should be used as value. (optional)
    part_id = 3.4 # float | Retrieve all invoices positions with this part. Must be provided with part[objectName] (optional)
    part_object_name = 'part_object_name_example' # str | Only required if part[id] was provided. 'Part' should be used as value. (optional)

    try:
        # Retrieve InvoicePos
        api_response = api_instance.get_invoice_pos(id=id, invoice_id=invoice_id, invoice_object_name=invoice_object_name, part_id=part_id, part_object_name=part_object_name)
        print("The response of InvoicePosApi->get_invoice_pos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicePosApi->get_invoice_pos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Retrieve all InvoicePos with this InvoicePos id | [optional] 
 **invoice_id** | **float**| Retrieve all invoices positions with this invoice. Must be provided with invoice[objectName] | [optional] 
 **invoice_object_name** | **str**| Only required if invoice[id] was provided. &#39;Invoice&#39; should be used as value. | [optional] 
 **part_id** | **float**| Retrieve all invoices positions with this part. Must be provided with part[objectName] | [optional] 
 **part_object_name** | **str**| Only required if part[id] was provided. &#39;Part&#39; should be used as value. | [optional] 

### Return type

[**GetInvoicePositionsById200Response**](GetInvoicePositionsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

