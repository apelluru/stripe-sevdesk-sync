# openapi_client.VoucherPosApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_voucher_positions**](VoucherPosApi.md#get_voucher_positions) | **GET** /VoucherPos | Retrieve voucher positions


# **get_voucher_positions**
> GetVoucherPositions200Response get_voucher_positions(voucher_id=voucher_id, voucher_object_name=voucher_object_name)

Retrieve voucher positions

Retrieve all voucher positions depending on the filters defined in the query.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_voucher_positions200_response import GetVoucherPositions200Response
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
    api_instance = openapi_client.VoucherPosApi(api_client)
    voucher_id = 56 # int | Retrieve all vouchers positions belonging to this voucher. Must be provided with voucher[objectName] (optional)
    voucher_object_name = 'voucher_object_name_example' # str | Only required if voucher[id] was provided. 'Voucher' should be used as value. (optional)

    try:
        # Retrieve voucher positions
        api_response = api_instance.get_voucher_positions(voucher_id=voucher_id, voucher_object_name=voucher_object_name)
        print("The response of VoucherPosApi->get_voucher_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherPosApi->get_voucher_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **int**| Retrieve all vouchers positions belonging to this voucher. Must be provided with voucher[objectName] | [optional] 
 **voucher_object_name** | **str**| Only required if voucher[id] was provided. &#39;Voucher&#39; should be used as value. | [optional] 

### Return type

[**GetVoucherPositions200Response**](GetVoucherPositions200Response.md)

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

