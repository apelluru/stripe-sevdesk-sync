# openapi_client.ContactFieldApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_field**](ContactFieldApi.md#create_contact_field) | **POST** /ContactCustomField | Create contact field
[**create_contact_field_setting**](ContactFieldApi.md#create_contact_field_setting) | **POST** /ContactCustomFieldSetting | Create contact field setting
[**delete_contact_custom_field_id**](ContactFieldApi.md#delete_contact_custom_field_id) | **DELETE** /ContactCustomField/{contactCustomFieldId} | delete a contact field
[**delete_contact_field_setting**](ContactFieldApi.md#delete_contact_field_setting) | **DELETE** /ContactCustomFieldSetting/{contactCustomFieldSettingId} | Deletes a contact field setting
[**get_contact_field_setting_by_id**](ContactFieldApi.md#get_contact_field_setting_by_id) | **GET** /ContactCustomFieldSetting/{contactCustomFieldSettingId} | Find contact field setting by ID
[**get_contact_field_settings**](ContactFieldApi.md#get_contact_field_settings) | **GET** /ContactCustomFieldSetting | Retrieve contact field settings
[**get_contact_fields**](ContactFieldApi.md#get_contact_fields) | **GET** /ContactCustomField | Retrieve contact fields
[**get_contact_fields_by_id**](ContactFieldApi.md#get_contact_fields_by_id) | **GET** /ContactCustomField/{contactCustomFieldId} | Retrieve contact fields
[**get_placeholder**](ContactFieldApi.md#get_placeholder) | **GET** /Textparser/fetchDictionaryEntriesByType | Retrieve Placeholders
[**get_reference_count**](ContactFieldApi.md#get_reference_count) | **GET** /ContactCustomFieldSetting/{contactCustomFieldSettingId}/getReferenceCount | Receive count reference
[**update_contact_field_setting**](ContactFieldApi.md#update_contact_field_setting) | **PUT** /ContactCustomFieldSetting/{contactCustomFieldSettingId} | Update contact field setting
[**update_contactfield**](ContactFieldApi.md#update_contactfield) | **PUT** /ContactCustomField/{contactCustomFieldId} | Update a contact field


# **create_contact_field**
> ModelContactCustomFieldResponse create_contact_field(model_contact_custom_field=model_contact_custom_field)

Create contact field

Create contact field

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_contact_custom_field import ModelContactCustomField
from sevdesk_client.openapi_client.models.model_contact_custom_field_response import ModelContactCustomFieldResponse
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    model_contact_custom_field = openapi_client.ModelContactCustomField() # ModelContactCustomField |  (optional)

    try:
        # Create contact field
        api_response = api_instance.create_contact_field(model_contact_custom_field=model_contact_custom_field)
        print("The response of ContactFieldApi->create_contact_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->create_contact_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_contact_custom_field** | [**ModelContactCustomField**](ModelContactCustomField.md)|  | [optional] 

### Return type

[**ModelContactCustomFieldResponse**](ModelContactCustomFieldResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_field_setting**
> GetContactFieldSettings200Response create_contact_field_setting(model_contact_custom_field_setting=model_contact_custom_field_setting)

Create contact field setting

Create contact field setting

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_field_settings200_response import GetContactFieldSettings200Response
from sevdesk_client.openapi_client.models.model_contact_custom_field_setting import ModelContactCustomFieldSetting
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    model_contact_custom_field_setting = openapi_client.ModelContactCustomFieldSetting() # ModelContactCustomFieldSetting |  (optional)

    try:
        # Create contact field setting
        api_response = api_instance.create_contact_field_setting(model_contact_custom_field_setting=model_contact_custom_field_setting)
        print("The response of ContactFieldApi->create_contact_field_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->create_contact_field_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_contact_custom_field_setting** | [**ModelContactCustomFieldSetting**](ModelContactCustomFieldSetting.md)|  | [optional] 

### Return type

[**GetContactFieldSettings200Response**](GetContactFieldSettings200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_custom_field_id**
> DeleteCheckAccount200Response delete_contact_custom_field_id(contact_custom_field_id)

delete a contact field

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
    api_instance = openapi_client.ContactFieldApi(api_client)
    contact_custom_field_id = 56 # int | Id of contact field

    try:
        # delete a contact field
        api_response = api_instance.delete_contact_custom_field_id(contact_custom_field_id)
        print("The response of ContactFieldApi->delete_contact_custom_field_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->delete_contact_custom_field_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_custom_field_id** | **int**| Id of contact field | 

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
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_field_setting**
> DeleteCheckAccount200Response delete_contact_field_setting(contact_custom_field_setting_id)

Deletes a contact field setting

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
    api_instance = openapi_client.ContactFieldApi(api_client)
    contact_custom_field_setting_id = 56 # int | Id of contact field to delete

    try:
        # Deletes a contact field setting
        api_response = api_instance.delete_contact_field_setting(contact_custom_field_setting_id)
        print("The response of ContactFieldApi->delete_contact_field_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->delete_contact_field_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_custom_field_setting_id** | **int**| Id of contact field to delete | 

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
**200** | Successful operation - contact field deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_field_setting_by_id**
> GetContactFieldSettings200Response get_contact_field_setting_by_id(contact_custom_field_setting_id)

Find contact field setting by ID

Returns a single contact field setting

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_field_settings200_response import GetContactFieldSettings200Response
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    contact_custom_field_setting_id = 56 # int | ID of contact field to return

    try:
        # Find contact field setting by ID
        api_response = api_instance.get_contact_field_setting_by_id(contact_custom_field_setting_id)
        print("The response of ContactFieldApi->get_contact_field_setting_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->get_contact_field_setting_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_custom_field_setting_id** | **int**| ID of contact field to return | 

### Return type

[**GetContactFieldSettings200Response**](GetContactFieldSettings200Response.md)

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

# **get_contact_field_settings**
> GetContactFieldSettings200Response get_contact_field_settings()

Retrieve contact field settings

Retrieve all contact field settings

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_field_settings200_response import GetContactFieldSettings200Response
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
    api_instance = openapi_client.ContactFieldApi(api_client)

    try:
        # Retrieve contact field settings
        api_response = api_instance.get_contact_field_settings()
        print("The response of ContactFieldApi->get_contact_field_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->get_contact_field_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetContactFieldSettings200Response**](GetContactFieldSettings200Response.md)

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

# **get_contact_fields**
> GetContactFields200Response get_contact_fields()

Retrieve contact fields

Retrieve all contact fields

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_fields200_response import GetContactFields200Response
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
    api_instance = openapi_client.ContactFieldApi(api_client)

    try:
        # Retrieve contact fields
        api_response = api_instance.get_contact_fields()
        print("The response of ContactFieldApi->get_contact_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->get_contact_fields: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetContactFields200Response**](GetContactFields200Response.md)

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

# **get_contact_fields_by_id**
> GetContactFields200Response get_contact_fields_by_id(contact_custom_field_id)

Retrieve contact fields

Retrieve all contact fields

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_fields200_response import GetContactFields200Response
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    contact_custom_field_id = 3.4 # float | id of the contact field

    try:
        # Retrieve contact fields
        api_response = api_instance.get_contact_fields_by_id(contact_custom_field_id)
        print("The response of ContactFieldApi->get_contact_fields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->get_contact_fields_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_custom_field_id** | **float**| id of the contact field | 

### Return type

[**GetContactFields200Response**](GetContactFields200Response.md)

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

# **get_placeholder**
> GetPlaceholder200Response get_placeholder(object_name, sub_object_name=sub_object_name)

Retrieve Placeholders

Retrieve all Placeholders

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_placeholder200_response import GetPlaceholder200Response
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    object_name = 'object_name_example' # str | Model name
    sub_object_name = 'sub_object_name_example' # str | Sub model name, required if you have \"Email\" at objectName (optional)

    try:
        # Retrieve Placeholders
        api_response = api_instance.get_placeholder(object_name, sub_object_name=sub_object_name)
        print("The response of ContactFieldApi->get_placeholder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->get_placeholder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**| Model name | 
 **sub_object_name** | **str**| Sub model name, required if you have \&quot;Email\&quot; at objectName | [optional] 

### Return type

[**GetPlaceholder200Response**](GetPlaceholder200Response.md)

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

# **get_reference_count**
> GetReferenceCount200Response get_reference_count(contact_custom_field_setting_id)

Receive count reference

Receive count reference

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_reference_count200_response import GetReferenceCount200Response
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    contact_custom_field_setting_id = 56 # int | ID of contact field you want to get the reference count

    try:
        # Receive count reference
        api_response = api_instance.get_reference_count(contact_custom_field_setting_id)
        print("The response of ContactFieldApi->get_reference_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->get_reference_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_custom_field_setting_id** | **int**| ID of contact field you want to get the reference count | 

### Return type

[**GetReferenceCount200Response**](GetReferenceCount200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - contact field deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_field_setting**
> ModelContactCustomFieldSettingResponse update_contact_field_setting(contact_custom_field_setting_id, model_contact_custom_field_setting_update=model_contact_custom_field_setting_update)

Update contact field setting

Update an existing contact field  setting

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_contact_custom_field_setting_response import ModelContactCustomFieldSettingResponse
from sevdesk_client.openapi_client.models.model_contact_custom_field_setting_update import ModelContactCustomFieldSettingUpdate
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    contact_custom_field_setting_id = 56 # int | ID of contact field setting you want to update
    model_contact_custom_field_setting_update = openapi_client.ModelContactCustomFieldSettingUpdate() # ModelContactCustomFieldSettingUpdate |  (optional)

    try:
        # Update contact field setting
        api_response = api_instance.update_contact_field_setting(contact_custom_field_setting_id, model_contact_custom_field_setting_update=model_contact_custom_field_setting_update)
        print("The response of ContactFieldApi->update_contact_field_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->update_contact_field_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_custom_field_setting_id** | **int**| ID of contact field setting you want to update | 
 **model_contact_custom_field_setting_update** | [**ModelContactCustomFieldSettingUpdate**](ModelContactCustomFieldSettingUpdate.md)|  | [optional] 

### Return type

[**ModelContactCustomFieldSettingResponse**](ModelContactCustomFieldSettingResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contactfield**
> ModelContactCustomFieldResponse update_contactfield(contact_custom_field_id, model_contact_custom_field_update=model_contact_custom_field_update)

Update a contact field

Update a contact field

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_contact_custom_field_response import ModelContactCustomFieldResponse
from sevdesk_client.openapi_client.models.model_contact_custom_field_update import ModelContactCustomFieldUpdate
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
    api_instance = openapi_client.ContactFieldApi(api_client)
    contact_custom_field_id = 3.4 # float | id of the contact field
    model_contact_custom_field_update = openapi_client.ModelContactCustomFieldUpdate() # ModelContactCustomFieldUpdate | Update data (optional)

    try:
        # Update a contact field
        api_response = api_instance.update_contactfield(contact_custom_field_id, model_contact_custom_field_update=model_contact_custom_field_update)
        print("The response of ContactFieldApi->update_contactfield:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactFieldApi->update_contactfield: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_custom_field_id** | **float**| id of the contact field | 
 **model_contact_custom_field_update** | [**ModelContactCustomFieldUpdate**](ModelContactCustomFieldUpdate.md)| Update data | [optional] 

### Return type

[**ModelContactCustomFieldResponse**](ModelContactCustomFieldResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

