# openapi_client.BasicsApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookkeeping_system_version**](BasicsApi.md#bookkeeping_system_version) | **GET** /Tools/bookkeepingSystemVersion | Retrieve bookkeeping system version


# **bookkeeping_system_version**
> BookkeepingSystemVersion200Response bookkeeping_system_version()

Retrieve bookkeeping system version

To check if you already received the update to version 2.0 you can use this endpoint.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.bookkeeping_system_version200_response import BookkeepingSystemVersion200Response
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
    api_instance = openapi_client.BasicsApi(api_client)

    try:
        # Retrieve bookkeeping system version
        api_response = api_instance.bookkeeping_system_version()
        print("The response of BasicsApi->bookkeeping_system_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicsApi->bookkeeping_system_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BookkeepingSystemVersion200Response**](BookkeepingSystemVersion200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Request |  -  |
**401** | Authentication required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

