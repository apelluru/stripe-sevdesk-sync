# openapi_client.ReportApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_contact**](ReportApi.md#report_contact) | **GET** /Report/contactlist | Export contact list
[**report_invoice**](ReportApi.md#report_invoice) | **GET** /Report/invoicelist | Export invoice list
[**report_order**](ReportApi.md#report_order) | **GET** /Report/orderlist | Export order list
[**report_voucher**](ReportApi.md#report_voucher) | **GET** /Report/voucherlist | Export voucher list


# **report_contact**
> ReportContact200Response report_contact(sev_query, download=download)

Export contact list

Export contact list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.report_contact200_response import ReportContact200Response
from sevdesk_client.openapi_client.models.report_contact_sev_query_parameter import ReportContactSevQueryParameter
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
    api_instance = openapi_client.ReportApi(api_client)
    sev_query = openapi_client.ReportContactSevQueryParameter() # ReportContactSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export contact list
        api_response = api_instance.report_contact(sev_query, download=download)
        print("The response of ReportApi->report_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ReportContactSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ReportContact200Response**](ReportContact200Response.md)

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_invoice**
> ReportInvoice200Response report_invoice(view, sev_query, download=download)

Export invoice list

Export invoice list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.report_invoice200_response import ReportInvoice200Response
from sevdesk_client.openapi_client.models.report_invoice_sev_query_parameter import ReportInvoiceSevQueryParameter
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
    api_instance = openapi_client.ReportApi(api_client)
    view = 'all' # str | 
    sev_query = openapi_client.ReportInvoiceSevQueryParameter() # ReportInvoiceSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export invoice list
        api_response = api_instance.report_invoice(view, sev_query, download=download)
        print("The response of ReportApi->report_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**|  | 
 **sev_query** | [**ReportInvoiceSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ReportInvoice200Response**](ReportInvoice200Response.md)

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_order**
> ReportOrder200Response report_order(view, sev_query, download=download)

Export order list

Export order list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.report_order200_response import ReportOrder200Response
from sevdesk_client.openapi_client.models.report_order_sev_query_parameter import ReportOrderSevQueryParameter
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
    api_instance = openapi_client.ReportApi(api_client)
    view = 'all' # str | 
    sev_query = openapi_client.ReportOrderSevQueryParameter() # ReportOrderSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export order list
        api_response = api_instance.report_order(view, sev_query, download=download)
        print("The response of ReportApi->report_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**|  | 
 **sev_query** | [**ReportOrderSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ReportOrder200Response**](ReportOrder200Response.md)

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_voucher**
> ReportVoucher200Response report_voucher(sev_query, download=download)

Export voucher list

Export voucher list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.report_voucher200_response import ReportVoucher200Response
from sevdesk_client.openapi_client.models.report_voucher_sev_query_parameter import ReportVoucherSevQueryParameter
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
    api_instance = openapi_client.ReportApi(api_client)
    sev_query = openapi_client.ReportVoucherSevQueryParameter() # ReportVoucherSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export voucher list
        api_response = api_instance.report_voucher(sev_query, download=download)
        print("The response of ReportApi->report_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ReportVoucherSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ReportVoucher200Response**](ReportVoucher200Response.md)

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

