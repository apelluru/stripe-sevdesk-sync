# openapi_client.CommunicationWayApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_communication_way**](CommunicationWayApi.md#create_communication_way) | **POST** /CommunicationWay | Create a new contact communication way
[**delete_communication_way**](CommunicationWayApi.md#delete_communication_way) | **DELETE** /CommunicationWay/{communicationWayId} | Deletes a communication way
[**get_communication_way_by_id**](CommunicationWayApi.md#get_communication_way_by_id) | **GET** /CommunicationWay/{communicationWayId} | Find communication way by ID
[**get_communication_way_keys**](CommunicationWayApi.md#get_communication_way_keys) | **GET** /CommunicationWayKey | Retrieve communication way keys
[**get_communication_ways**](CommunicationWayApi.md#get_communication_ways) | **GET** /CommunicationWay | Retrieve communication ways
[**update_communication_way**](CommunicationWayApi.md#update_communication_way) | **PUT** /CommunicationWay/{communicationWayId} | Update a existing communication way


# **create_communication_way**
> ModelCommunicationWayResponse create_communication_way(model_communication_way=model_communication_way)

Create a new contact communication way

Creates a new contact communication way.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_communication_way import ModelCommunicationWay
from sevdesk_client.openapi_client.models.model_communication_way_response import ModelCommunicationWayResponse
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
    api_instance = openapi_client.CommunicationWayApi(api_client)
    model_communication_way = openapi_client.ModelCommunicationWay() # ModelCommunicationWay | Creation data (optional)

    try:
        # Create a new contact communication way
        api_response = api_instance.create_communication_way(model_communication_way=model_communication_way)
        print("The response of CommunicationWayApi->create_communication_way:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationWayApi->create_communication_way: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_communication_way** | [**ModelCommunicationWay**](ModelCommunicationWay.md)| Creation data | [optional] 

### Return type

[**ModelCommunicationWayResponse**](ModelCommunicationWayResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created contact communication way |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_communication_way**
> DeleteCheckAccount200Response delete_communication_way(communication_way_id)

Deletes a communication way

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.delete_check_account200_response import DeleteCheckAccount200Response
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
    api_instance = openapi_client.CommunicationWayApi(api_client)
    communication_way_id = 56 # int | Id of communication way resource to delete

    try:
        # Deletes a communication way
        api_response = api_instance.delete_communication_way(communication_way_id)
        print("The response of CommunicationWayApi->delete_communication_way:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationWayApi->delete_communication_way: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_way_id** | **int**| Id of communication way resource to delete | 

### Return type

[**DeleteCheckAccount200Response**](DeleteCheckAccount200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Communication way deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_communication_way_by_id**
> GetCommunicationWays200Response get_communication_way_by_id(communication_way_id)

Find communication way by ID

Returns a single communication way

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_communication_ways200_response import GetCommunicationWays200Response
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
    api_instance = openapi_client.CommunicationWayApi(api_client)
    communication_way_id = 56 # int | ID of communication way to return

    try:
        # Find communication way by ID
        api_response = api_instance.get_communication_way_by_id(communication_way_id)
        print("The response of CommunicationWayApi->get_communication_way_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationWayApi->get_communication_way_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_way_id** | **int**| ID of communication way to return | 

### Return type

[**GetCommunicationWays200Response**](GetCommunicationWays200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. communication way was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_communication_way_keys**
> GetCommunicationWayKeys200Response get_communication_way_keys()

Retrieve communication way keys

Returns all communication way keys.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_communication_way_keys200_response import GetCommunicationWayKeys200Response
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
    api_instance = openapi_client.CommunicationWayApi(api_client)

    try:
        # Retrieve communication way keys
        api_response = api_instance.get_communication_way_keys()
        print("The response of CommunicationWayApi->get_communication_way_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationWayApi->get_communication_way_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCommunicationWayKeys200Response**](GetCommunicationWayKeys200Response.md)

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

# **get_communication_ways**
> GetCommunicationWays200Response get_communication_ways(contact_id=contact_id, contact_object_name=contact_object_name, type=type, main=main)

Retrieve communication ways

Returns all communication ways which have been added up until now. Filters can be added.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_communication_ways200_response import GetCommunicationWays200Response
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
    api_instance = openapi_client.CommunicationWayApi(api_client)
    contact_id = 'contact_id_example' # str | ID of contact for which you want the communication ways. (optional)
    contact_object_name = 'Contact' # str | Object name. Only needed if you also defined the ID of a contact. (optional)
    type = 'type_example' # str | Type of the communication ways you want to get. (optional)
    main = 'main_example' # str | Define if you only want the main communication way. (optional)

    try:
        # Retrieve communication ways
        api_response = api_instance.get_communication_ways(contact_id=contact_id, contact_object_name=contact_object_name, type=type, main=main)
        print("The response of CommunicationWayApi->get_communication_ways:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationWayApi->get_communication_ways: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| ID of contact for which you want the communication ways. | [optional] 
 **contact_object_name** | **str**| Object name. Only needed if you also defined the ID of a contact. | [optional] 
 **type** | **str**| Type of the communication ways you want to get. | [optional] 
 **main** | **str**| Define if you only want the main communication way. | [optional] 

### Return type

[**GetCommunicationWays200Response**](GetCommunicationWays200Response.md)

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

# **update_communication_way**
> ModelCommunicationWayResponse update_communication_way(communication_way_id, model_communication_way_update=model_communication_way_update)

Update a existing communication way

Update a communication way

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_communication_way_response import ModelCommunicationWayResponse
from sevdesk_client.openapi_client.models.model_communication_way_update import ModelCommunicationWayUpdate
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
    api_instance = openapi_client.CommunicationWayApi(api_client)
    communication_way_id = 56 # int | ID of CommunicationWay to update
    model_communication_way_update = openapi_client.ModelCommunicationWayUpdate() # ModelCommunicationWayUpdate | Update data (optional)

    try:
        # Update a existing communication way
        api_response = api_instance.update_communication_way(communication_way_id, model_communication_way_update=model_communication_way_update)
        print("The response of CommunicationWayApi->update_communication_way:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationWayApi->update_communication_way: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_way_id** | **int**| ID of CommunicationWay to update | 
 **model_communication_way_update** | [**ModelCommunicationWayUpdate**](ModelCommunicationWayUpdate.md)| Update data | [optional] 

### Return type

[**ModelCommunicationWayResponse**](ModelCommunicationWayResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed CommunicationWay resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

