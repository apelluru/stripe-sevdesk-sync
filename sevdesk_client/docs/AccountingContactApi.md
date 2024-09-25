# openapi_client.AccountingContactApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_accounting_contact**](AccountingContactApi.md#create_accounting_contact) | **POST** /AccountingContact | Create a new accounting contact
[**delete_accounting_contact**](AccountingContactApi.md#delete_accounting_contact) | **DELETE** /AccountingContact/{accountingContactId} | Deletes an accounting contact
[**get_accounting_contact**](AccountingContactApi.md#get_accounting_contact) | **GET** /AccountingContact | Retrieve accounting contact
[**get_accounting_contact_by_id**](AccountingContactApi.md#get_accounting_contact_by_id) | **GET** /AccountingContact/{accountingContactId} | Find accounting contact by ID
[**update_accounting_contact**](AccountingContactApi.md#update_accounting_contact) | **PUT** /AccountingContact/{accountingContactId} | Update an existing accounting contact


# **create_accounting_contact**
> ModelAccountingContactResponse create_accounting_contact(model_accounting_contact=model_accounting_contact)

Create a new accounting contact

Creates a new accounting contact.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_accounting_contact import ModelAccountingContact
from sevdesk_client.openapi_client.models.model_accounting_contact_response import ModelAccountingContactResponse
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
    api_instance = openapi_client.AccountingContactApi(api_client)
    model_accounting_contact = openapi_client.ModelAccountingContact() # ModelAccountingContact | Creation data (optional)

    try:
        # Create a new accounting contact
        api_response = api_instance.create_accounting_contact(model_accounting_contact=model_accounting_contact)
        print("The response of AccountingContactApi->create_accounting_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingContactApi->create_accounting_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_accounting_contact** | [**ModelAccountingContact**](ModelAccountingContact.md)| Creation data | [optional] 

### Return type

[**ModelAccountingContactResponse**](ModelAccountingContactResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created accounting contact |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_accounting_contact**
> DeleteCheckAccount200Response delete_accounting_contact(accounting_contact_id)

Deletes an accounting contact

Attention, deleting an existing AccountingContact can lead to **booking errors**, especially in the **DATEV export**. Compatibility of sevdesk with DATEV is no longer guaranteed.

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
    api_instance = openapi_client.AccountingContactApi(api_client)
    accounting_contact_id = 56 # int | Id of accounting contact resource to delete

    try:
        # Deletes an accounting contact
        api_response = api_instance.delete_accounting_contact(accounting_contact_id)
        print("The response of AccountingContactApi->delete_accounting_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingContactApi->delete_accounting_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_contact_id** | **int**| Id of accounting contact resource to delete | 

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
**200** | Successful operation - accounting contact deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounting_contact**
> GetAccountingContact200Response get_accounting_contact(contact_id=contact_id, contact_object_name=contact_object_name)

Retrieve accounting contact

Returns all accounting contact which have been added up until now. Filters can be added.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_accounting_contact200_response import GetAccountingContact200Response
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
    api_instance = openapi_client.AccountingContactApi(api_client)
    contact_id = 'contact_id_example' # str | ID of contact for which you want the accounting contact. (optional)
    contact_object_name = 'Contact' # str | Object name. Only needed if you also defined the ID of a contact. (optional)

    try:
        # Retrieve accounting contact
        api_response = api_instance.get_accounting_contact(contact_id=contact_id, contact_object_name=contact_object_name)
        print("The response of AccountingContactApi->get_accounting_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingContactApi->get_accounting_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| ID of contact for which you want the accounting contact. | [optional] 
 **contact_object_name** | **str**| Object name. Only needed if you also defined the ID of a contact. | [optional] 

### Return type

[**GetAccountingContact200Response**](GetAccountingContact200Response.md)

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

# **get_accounting_contact_by_id**
> GetAccountingContact200Response get_accounting_contact_by_id(accounting_contact_id)

Find accounting contact by ID

Returns a single accounting contac

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_accounting_contact200_response import GetAccountingContact200Response
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
    api_instance = openapi_client.AccountingContactApi(api_client)
    accounting_contact_id = 56 # int | ID of accounting contact to return

    try:
        # Find accounting contact by ID
        api_response = api_instance.get_accounting_contact_by_id(accounting_contact_id)
        print("The response of AccountingContactApi->get_accounting_contact_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingContactApi->get_accounting_contact_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_contact_id** | **int**| ID of accounting contact to return | 

### Return type

[**GetAccountingContact200Response**](GetAccountingContact200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Accounting contact was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_accounting_contact**
> ModelAccountingContactResponse update_accounting_contact(accounting_contact_id, model_accounting_contact_update=model_accounting_contact_update)

Update an existing accounting contact

Attention, updating an existing AccountingContact can lead to **booking errors**, especially in the **DATEV export**. Compatibility of sevdesk with DATEV is no longer guaranteed.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_accounting_contact_response import ModelAccountingContactResponse
from sevdesk_client.openapi_client.models.model_accounting_contact_update import ModelAccountingContactUpdate
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
    api_instance = openapi_client.AccountingContactApi(api_client)
    accounting_contact_id = 56 # int | ID of accounting contact to update
    model_accounting_contact_update = openapi_client.ModelAccountingContactUpdate() # ModelAccountingContactUpdate | Update data (optional)

    try:
        # Update an existing accounting contact
        api_response = api_instance.update_accounting_contact(accounting_contact_id, model_accounting_contact_update=model_accounting_contact_update)
        print("The response of AccountingContactApi->update_accounting_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingContactApi->update_accounting_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_contact_id** | **int**| ID of accounting contact to update | 
 **model_accounting_contact_update** | [**ModelAccountingContactUpdate**](ModelAccountingContactUpdate.md)| Update data | [optional] 

### Return type

[**ModelAccountingContactResponse**](ModelAccountingContactResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed accounting contact resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

