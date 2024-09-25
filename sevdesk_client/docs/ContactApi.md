# openapi_client.ContactApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_customer_number_availability_check**](ContactApi.md#contact_customer_number_availability_check) | **GET** /Contact/Mapper/checkCustomerNumberAvailability | Check if a customer number is available
[**create_contact**](ContactApi.md#create_contact) | **POST** /Contact | Create a new contact
[**delete_contact**](ContactApi.md#delete_contact) | **DELETE** /Contact/{contactId} | Deletes a contact
[**find_contacts_by_custom_field_value**](ContactApi.md#find_contacts_by_custom_field_value) | **GET** /Contact/Factory/findContactsByCustomFieldValue | Find contacts by custom field value
[**get_contact_by_id**](ContactApi.md#get_contact_by_id) | **GET** /Contact/{contactId} | Find contact by ID
[**get_contact_tabs_item_count_by_id**](ContactApi.md#get_contact_tabs_item_count_by_id) | **GET** /Contact/{contactId}/getTabsItemCount | Get number of all items
[**get_contacts**](ContactApi.md#get_contacts) | **GET** /Contact | Retrieve contacts
[**get_next_customer_number**](ContactApi.md#get_next_customer_number) | **GET** /Contact/Factory/getNextCustomerNumber | Get next free customer number
[**update_contact**](ContactApi.md#update_contact) | **PUT** /Contact/{contactId} | Update a existing contact


# **contact_customer_number_availability_check**
> ContactCustomerNumberAvailabilityCheck200Response contact_customer_number_availability_check(customer_number=customer_number)

Check if a customer number is available

Checks if a given customer number is available or already used.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.contact_customer_number_availability_check200_response import ContactCustomerNumberAvailabilityCheck200Response
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
    api_instance = openapi_client.ContactApi(api_client)
    customer_number = 'customer_number_example' # str | The customer number to be checked. (optional)

    try:
        # Check if a customer number is available
        api_response = api_instance.contact_customer_number_availability_check(customer_number=customer_number)
        print("The response of ContactApi->contact_customer_number_availability_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->contact_customer_number_availability_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_number** | **str**| The customer number to be checked. | [optional] 

### Return type

[**ContactCustomerNumberAvailabilityCheck200Response**](ContactCustomerNumberAvailabilityCheck200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns whether given customer number is available. |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ModelContactResponse create_contact(model_contact=model_contact)

Create a new contact

Creates a new contact.<br>       For adding addresses and communication ways, you will need to use the ContactAddress and CommunicationWay endpoints.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_contact import ModelContact
from sevdesk_client.openapi_client.models.model_contact_response import ModelContactResponse
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
    api_instance = openapi_client.ContactApi(api_client)
    model_contact = openapi_client.ModelContact() # ModelContact | Creation data (optional)

    try:
        # Create a new contact
        api_response = api_instance.create_contact(model_contact=model_contact)
        print("The response of ContactApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_contact** | [**ModelContact**](ModelContact.md)| Creation data | [optional] 

### Return type

[**ModelContactResponse**](ModelContactResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created contact |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> DeleteCheckAccount200Response delete_contact(contact_id)

Deletes a contact

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
    api_instance = openapi_client.ContactApi(api_client)
    contact_id = 56 # int | Id of contact resource to delete

    try:
        # Deletes a contact
        api_response = api_instance.delete_contact(contact_id)
        print("The response of ContactApi->delete_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->delete_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Id of contact resource to delete | 

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
**200** | Successful operation - contact deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_contacts_by_custom_field_value**
> FindContactsByCustomFieldValue200Response find_contacts_by_custom_field_value(value, custom_field_name, custom_field_setting_id=custom_field_setting_id, custom_field_setting_object_name=custom_field_setting_object_name)

Find contacts by custom field value

Returns an array of contacts having a certain custom field value set.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.find_contacts_by_custom_field_value200_response import FindContactsByCustomFieldValue200Response
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
    api_instance = openapi_client.ContactApi(api_client)
    value = 'value_example' # str | The value to be checked.
    custom_field_name = 'custom_field_name_example' # str | The ContactCustomFieldSetting name, if no ContactCustomFieldSetting is provided.
    custom_field_setting_id = 'custom_field_setting_id_example' # str | ID of ContactCustomFieldSetting for which the value has to be checked. (optional)
    custom_field_setting_object_name = 'ContactCustomFieldSetting' # str | Object name. Only needed if you also defined the ID of a ContactCustomFieldSetting. (optional)

    try:
        # Find contacts by custom field value
        api_response = api_instance.find_contacts_by_custom_field_value(value, custom_field_name, custom_field_setting_id=custom_field_setting_id, custom_field_setting_object_name=custom_field_setting_object_name)
        print("The response of ContactApi->find_contacts_by_custom_field_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->find_contacts_by_custom_field_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| The value to be checked. | 
 **custom_field_name** | **str**| The ContactCustomFieldSetting name, if no ContactCustomFieldSetting is provided. | 
 **custom_field_setting_id** | **str**| ID of ContactCustomFieldSetting for which the value has to be checked. | [optional] 
 **custom_field_setting_object_name** | **str**| Object name. Only needed if you also defined the ID of a ContactCustomFieldSetting. | [optional] 

### Return type

[**FindContactsByCustomFieldValue200Response**](FindContactsByCustomFieldValue200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of contacts having a certain custom field value set. |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_id**
> FindContactsByCustomFieldValue200Response get_contact_by_id(contact_id)

Find contact by ID

Returns a single contact

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.find_contacts_by_custom_field_value200_response import FindContactsByCustomFieldValue200Response
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
    api_instance = openapi_client.ContactApi(api_client)
    contact_id = 56 # int | ID of contact to return

    try:
        # Find contact by ID
        api_response = api_instance.get_contact_by_id(contact_id)
        print("The response of ContactApi->get_contact_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_contact_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| ID of contact to return | 

### Return type

[**FindContactsByCustomFieldValue200Response**](FindContactsByCustomFieldValue200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Contact was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_tabs_item_count_by_id**
> GetContactTabsItemCountById200Response get_contact_tabs_item_count_by_id(contact_id)

Get number of all items

Get number of all invoices, orders, etc. of a specified contact

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_contact_tabs_item_count_by_id200_response import GetContactTabsItemCountById200Response
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
    api_instance = openapi_client.ContactApi(api_client)
    contact_id = 56 # int | ID of contact to return

    try:
        # Get number of all items
        api_response = api_instance.get_contact_tabs_item_count_by_id(contact_id)
        print("The response of ContactApi->get_contact_tabs_item_count_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_contact_tabs_item_count_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| ID of contact to return | 

### Return type

[**GetContactTabsItemCountById200Response**](GetContactTabsItemCountById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> FindContactsByCustomFieldValue200Response get_contacts(depth=depth, customer_number=customer_number)

Retrieve contacts

There are a multitude of parameter which can be used to filter.<br>       A few of them are attached but       for a complete list please check out <a href='#tag/Contact/How-to-filter-for-certain-contacts'>this</a> list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.find_contacts_by_custom_field_value200_response import FindContactsByCustomFieldValue200Response
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
    api_instance = openapi_client.ContactApi(api_client)
    depth = 'depth_example' # str | Defines if both organizations <b>and</b> persons should be returned.<br>       '0' -> only organizations, '1' -> organizations and persons (optional)
    customer_number = 'customer_number_example' # str | Retrieve all contacts with this customer number (optional)

    try:
        # Retrieve contacts
        api_response = api_instance.get_contacts(depth=depth, customer_number=customer_number)
        print("The response of ContactApi->get_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **str**| Defines if both organizations &lt;b&gt;and&lt;/b&gt; persons should be returned.&lt;br&gt;       &#39;0&#39; -&gt; only organizations, &#39;1&#39; -&gt; organizations and persons | [optional] 
 **customer_number** | **str**| Retrieve all contacts with this customer number | [optional] 

### Return type

[**FindContactsByCustomFieldValue200Response**](FindContactsByCustomFieldValue200Response.md)

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

# **get_next_customer_number**
> GetNextCustomerNumber200Response get_next_customer_number()

Get next free customer number

Retrieves the next available customer number. Avoids duplicates.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_next_customer_number200_response import GetNextCustomerNumber200Response
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
    api_instance = openapi_client.ContactApi(api_client)

    try:
        # Get next free customer number
        api_response = api_instance.get_next_customer_number()
        print("The response of ContactApi->get_next_customer_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_next_customer_number: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNextCustomerNumber200Response**](GetNextCustomerNumber200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns next available customer number |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ModelContactResponse update_contact(contact_id, model_contact_update=model_contact_update)

Update a existing contact

Update a contact

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_contact_response import ModelContactResponse
from sevdesk_client.openapi_client.models.model_contact_update import ModelContactUpdate
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
    api_instance = openapi_client.ContactApi(api_client)
    contact_id = 56 # int | ID of contact to update
    model_contact_update = openapi_client.ModelContactUpdate() # ModelContactUpdate | Update data (optional)

    try:
        # Update a existing contact
        api_response = api_instance.update_contact(contact_id, model_contact_update=model_contact_update)
        print("The response of ContactApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| ID of contact to update | 
 **model_contact_update** | [**ModelContactUpdate**](ModelContactUpdate.md)| Update data | [optional] 

### Return type

[**ModelContactResponse**](ModelContactResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed contact resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

