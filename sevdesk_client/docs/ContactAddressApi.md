# openapi_client.ContactAddressApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_address_id**](ContactAddressApi.md#contact_address_id) | **GET** /ContactAddress/{contactAddressId} | Find contact address by ID
[**create_contact_address**](ContactAddressApi.md#create_contact_address) | **POST** /ContactAddress | Create a new contact address
[**delete_contact_address**](ContactAddressApi.md#delete_contact_address) | **DELETE** /ContactAddress/{contactAddressId} | Deletes a contact address
[**get_contact_addresses**](ContactAddressApi.md#get_contact_addresses) | **GET** /ContactAddress | Retrieve contact addresses
[**update_contact_address**](ContactAddressApi.md#update_contact_address) | **PUT** /ContactAddress/{contactAddressId} | update a existing contact address


# **contact_address_id**
> GetContactAddresses200Response contact_address_id(contact_address_id)

Find contact address by ID

Returns a single contact address

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_addresses200_response import GetContactAddresses200Response
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
    api_instance = openapi_client.ContactAddressApi(api_client)
    contact_address_id = 56 # int | ID of contact address to return

    try:
        # Find contact address by ID
        api_response = api_instance.contact_address_id(contact_address_id)
        print("The response of ContactAddressApi->contact_address_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactAddressApi->contact_address_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_address_id** | **int**| ID of contact address to return | 

### Return type

[**GetContactAddresses200Response**](GetContactAddresses200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Contact address was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_address**
> ModelContactAddressResponse create_contact_address(model_contact_address=model_contact_address)

Create a new contact address

Creates a new contact address.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_contact_address import ModelContactAddress
from sevdesk_client.openapi_client.models.model_contact_address_response import ModelContactAddressResponse
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
    api_instance = openapi_client.ContactAddressApi(api_client)
    model_contact_address = openapi_client.ModelContactAddress() # ModelContactAddress | Creation data (optional)

    try:
        # Create a new contact address
        api_response = api_instance.create_contact_address(model_contact_address=model_contact_address)
        print("The response of ContactAddressApi->create_contact_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactAddressApi->create_contact_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_contact_address** | [**ModelContactAddress**](ModelContactAddress.md)| Creation data | [optional] 

### Return type

[**ModelContactAddressResponse**](ModelContactAddressResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created contact address |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_address**
> DeleteCheckAccount200Response delete_contact_address(contact_address_id)

Deletes a contact address

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
    api_instance = openapi_client.ContactAddressApi(api_client)
    contact_address_id = 56 # int | Id of contact address resource to delete

    try:
        # Deletes a contact address
        api_response = api_instance.delete_contact_address(contact_address_id)
        print("The response of ContactAddressApi->delete_contact_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactAddressApi->delete_contact_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_address_id** | **int**| Id of contact address resource to delete | 

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
**200** | Successful operation - contact address deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_addresses**
> GetContactAddresses200Response get_contact_addresses()

Retrieve contact addresses

Retrieve all contact addresses

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_addresses200_response import GetContactAddresses200Response
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
    api_instance = openapi_client.ContactAddressApi(api_client)

    try:
        # Retrieve contact addresses
        api_response = api_instance.get_contact_addresses()
        print("The response of ContactAddressApi->get_contact_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactAddressApi->get_contact_addresses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetContactAddresses200Response**](GetContactAddresses200Response.md)

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

# **update_contact_address**
> ModelContactAddressResponse update_contact_address(contact_address_id, model_contact_address_update=model_contact_address_update)

update a existing contact address

update a existing contact address.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_contact_address_response import ModelContactAddressResponse
from sevdesk_client.openapi_client.models.model_contact_address_update import ModelContactAddressUpdate
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
    api_instance = openapi_client.ContactAddressApi(api_client)
    contact_address_id = 56 # int | ID of contact address to return
    model_contact_address_update = openapi_client.ModelContactAddressUpdate() # ModelContactAddressUpdate | Creation data (optional)

    try:
        # update a existing contact address
        api_response = api_instance.update_contact_address(contact_address_id, model_contact_address_update=model_contact_address_update)
        print("The response of ContactAddressApi->update_contact_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactAddressApi->update_contact_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_address_id** | **int**| ID of contact address to return | 
 **model_contact_address_update** | [**ModelContactAddressUpdate**](ModelContactAddressUpdate.md)| Creation data | [optional] 

### Return type

[**ModelContactAddressResponse**](ModelContactAddressResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created contact address |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

