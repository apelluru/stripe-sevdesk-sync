# openapi_client.LayoutApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_letterpapers_with_thumb**](LayoutApi.md#get_letterpapers_with_thumb) | **GET** /DocServer/getLetterpapersWithThumb | Retrieve letterpapers
[**get_templates**](LayoutApi.md#get_templates) | **GET** /DocServer/getTemplatesWithThumb | Retrieve templates
[**update_credit_note_template**](LayoutApi.md#update_credit_note_template) | **PUT** /CreditNote/{creditNoteId}/changeParameter | Update an of credit note template
[**update_invoice_template**](LayoutApi.md#update_invoice_template) | **PUT** /Invoice/{invoiceId}/changeParameter | Update an invoice template
[**update_order_template**](LayoutApi.md#update_order_template) | **PUT** /Order/{orderId}/changeParameter | Update an order template


# **get_letterpapers_with_thumb**
> GetLetterpapersWithThumb200Response get_letterpapers_with_thumb()

Retrieve letterpapers

Retrieve all letterpapers with Thumb

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_letterpapers_with_thumb200_response import GetLetterpapersWithThumb200Response
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
    api_instance = openapi_client.LayoutApi(api_client)

    try:
        # Retrieve letterpapers
        api_response = api_instance.get_letterpapers_with_thumb()
        print("The response of LayoutApi->get_letterpapers_with_thumb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayoutApi->get_letterpapers_with_thumb: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetLetterpapersWithThumb200Response**](GetLetterpapersWithThumb200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> GetTemplates200Response get_templates(type=type)

Retrieve templates

Retrieve all templates

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_templates200_response import GetTemplates200Response
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
    api_instance = openapi_client.LayoutApi(api_client)
    type = 'type_example' # str | Type of the templates you want to get. (optional)

    try:
        # Retrieve templates
        api_response = api_instance.get_templates(type=type)
        print("The response of LayoutApi->get_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayoutApi->get_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of the templates you want to get. | [optional] 

### Return type

[**GetTemplates200Response**](GetTemplates200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_note_template**
> ModelChangeLayoutResponse update_credit_note_template(credit_note_id, model_change_layout=model_change_layout)

Update an of credit note template

Update an existing of credit note template

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_change_layout import ModelChangeLayout
from sevdesk_client.openapi_client.models.model_change_layout_response import ModelChangeLayoutResponse
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
    api_instance = openapi_client.LayoutApi(api_client)
    credit_note_id = 56 # int | ID of credit note to update
    model_change_layout = openapi_client.ModelChangeLayout() # ModelChangeLayout | Change Layout (optional)

    try:
        # Update an of credit note template
        api_response = api_instance.update_credit_note_template(credit_note_id, model_change_layout=model_change_layout)
        print("The response of LayoutApi->update_credit_note_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayoutApi->update_credit_note_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of credit note to update | 
 **model_change_layout** | [**ModelChangeLayout**](ModelChangeLayout.md)| Change Layout | [optional] 

### Return type

[**ModelChangeLayoutResponse**](ModelChangeLayoutResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_template**
> ModelChangeLayoutResponse update_invoice_template(invoice_id, model_change_layout=model_change_layout)

Update an invoice template

Update an existing invoice template

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_change_layout import ModelChangeLayout
from sevdesk_client.openapi_client.models.model_change_layout_response import ModelChangeLayoutResponse
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
    api_instance = openapi_client.LayoutApi(api_client)
    invoice_id = 56 # int | ID of invoice to update
    model_change_layout = openapi_client.ModelChangeLayout() # ModelChangeLayout | Change Layout (optional)

    try:
        # Update an invoice template
        api_response = api_instance.update_invoice_template(invoice_id, model_change_layout=model_change_layout)
        print("The response of LayoutApi->update_invoice_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayoutApi->update_invoice_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to update | 
 **model_change_layout** | [**ModelChangeLayout**](ModelChangeLayout.md)| Change Layout | [optional] 

### Return type

[**ModelChangeLayoutResponse**](ModelChangeLayoutResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_template**
> ModelChangeLayoutResponse update_order_template(order_id, model_change_layout=model_change_layout)

Update an order template

Update an existing order template

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_change_layout import ModelChangeLayout
from sevdesk_client.openapi_client.models.model_change_layout_response import ModelChangeLayoutResponse
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
    api_instance = openapi_client.LayoutApi(api_client)
    order_id = 56 # int | ID of order to update
    model_change_layout = openapi_client.ModelChangeLayout() # ModelChangeLayout | Change Layout (optional)

    try:
        # Update an order template
        api_response = api_instance.update_order_template(order_id, model_change_layout=model_change_layout)
        print("The response of LayoutApi->update_order_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayoutApi->update_order_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to update | 
 **model_change_layout** | [**ModelChangeLayout**](ModelChangeLayout.md)| Change Layout | [optional] 

### Return type

[**ModelChangeLayoutResponse**](ModelChangeLayoutResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

