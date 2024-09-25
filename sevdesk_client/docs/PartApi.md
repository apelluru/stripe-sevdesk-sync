# openapi_client.PartApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_part**](PartApi.md#create_part) | **POST** /Part | Create a new part
[**get_part_by_id**](PartApi.md#get_part_by_id) | **GET** /Part/{partId} | Find part by ID
[**get_parts**](PartApi.md#get_parts) | **GET** /Part | Retrieve parts
[**part_get_stock**](PartApi.md#part_get_stock) | **GET** /Part/{partId}/getStock | Get stock of a part
[**update_part**](PartApi.md#update_part) | **PUT** /Part/{partId} | Update an existing part


# **create_part**
> ModelPart create_part(model_part=model_part)

Create a new part

Creates a part in your sevdesk inventory.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_part import ModelPart
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
    api_instance = openapi_client.PartApi(api_client)
    model_part = openapi_client.ModelPart() # ModelPart | Creation data. Please be aware, that you need to provide at least all required parameter      of the part model! (optional)

    try:
        # Create a new part
        api_response = api_instance.create_part(model_part=model_part)
        print("The response of PartApi->create_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartApi->create_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_part** | [**ModelPart**](ModelPart.md)| Creation data. Please be aware, that you need to provide at least all required parameter      of the part model! | [optional] 

### Return type

[**ModelPart**](ModelPart.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created part |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_part_by_id**
> GetParts200Response get_part_by_id(part_id)

Find part by ID

Returns a single part

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_parts200_response import GetParts200Response
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
    api_instance = openapi_client.PartApi(api_client)
    part_id = 56 # int | ID of part to return

    try:
        # Find part by ID
        api_response = api_instance.get_part_by_id(part_id)
        print("The response of PartApi->get_part_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartApi->get_part_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_id** | **int**| ID of part to return | 

### Return type

[**GetParts200Response**](GetParts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Part was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parts**
> GetParts200Response get_parts(part_number=part_number, name=name)

Retrieve parts

Retrieve all parts in your sevdesk inventory according to the applied filters.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_parts200_response import GetParts200Response
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
    api_instance = openapi_client.PartApi(api_client)
    part_number = 'part_number_example' # str | Retrieve all parts with this part number (optional)
    name = 'name_example' # str | Retrieve all parts with this name (optional)

    try:
        # Retrieve parts
        api_response = api_instance.get_parts(part_number=part_number, name=name)
        print("The response of PartApi->get_parts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartApi->get_parts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_number** | **str**| Retrieve all parts with this part number | [optional] 
 **name** | **str**| Retrieve all parts with this name | [optional] 

### Return type

[**GetParts200Response**](GetParts200Response.md)

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

# **part_get_stock**
> PartGetStock200Response part_get_stock(part_id)

Get stock of a part

Returns the current stock amount of the given part.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.part_get_stock200_response import PartGetStock200Response
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
    api_instance = openapi_client.PartApi(api_client)
    part_id = 56 # int | ID of part for which you want the current stock.

    try:
        # Get stock of a part
        api_response = api_instance.part_get_stock(part_id)
        print("The response of PartApi->part_get_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartApi->part_get_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_id** | **int**| ID of part for which you want the current stock. | 

### Return type

[**PartGetStock200Response**](PartGetStock200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Part was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_part**
> ModelPart update_part(part_id, model_part_update=model_part_update)

Update an existing part

Update a part

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_part import ModelPart
from sevdesk_client.openapi_client.models.model_part_update import ModelPartUpdate
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
    api_instance = openapi_client.PartApi(api_client)
    part_id = 56 # int | ID of part to update
    model_part_update = openapi_client.ModelPartUpdate() # ModelPartUpdate | Update data (optional)

    try:
        # Update an existing part
        api_response = api_instance.update_part(part_id, model_part_update=model_part_update)
        print("The response of PartApi->update_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartApi->update_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_id** | **int**| ID of part to update | 
 **model_part_update** | [**ModelPartUpdate**](ModelPartUpdate.md)| Update data | [optional] 

### Return type

[**ModelPart**](ModelPart.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed part resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

