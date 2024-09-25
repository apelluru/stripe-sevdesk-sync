# openapi_client.CheckAccountApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_check_account**](CheckAccountApi.md#create_check_account) | **POST** /CheckAccount | Create a new check account
[**create_clearing_account**](CheckAccountApi.md#create_clearing_account) | **POST** /CheckAccount/Factory/clearingAccount | Create a new clearing account
[**create_file_import_account**](CheckAccountApi.md#create_file_import_account) | **POST** /CheckAccount/Factory/fileImportAccount | Create a new file import account
[**delete_check_account**](CheckAccountApi.md#delete_check_account) | **DELETE** /CheckAccount/{checkAccountId} | Deletes a check account
[**get_balance_at_date**](CheckAccountApi.md#get_balance_at_date) | **GET** /CheckAccount/{checkAccountId}/getBalanceAtDate | Get the balance at a given date
[**get_check_account_by_id**](CheckAccountApi.md#get_check_account_by_id) | **GET** /CheckAccount/{checkAccountId} | Find check account by ID
[**get_check_accounts**](CheckAccountApi.md#get_check_accounts) | **GET** /CheckAccount | Retrieve check accounts
[**update_check_account**](CheckAccountApi.md#update_check_account) | **PUT** /CheckAccount/{checkAccountId} | Update an existing check account


# **create_check_account**
> GetCheckAccounts200Response create_check_account(model_check_account=model_check_account)

Create a new check account

Creates a new banking account on which transactions can be created.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_check_accounts200_response import GetCheckAccounts200Response
from sevdesk_client.openapi_client.models.model_check_account import ModelCheckAccount
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
    api_instance = openapi_client.CheckAccountApi(api_client)
    model_check_account = openapi_client.ModelCheckAccount() # ModelCheckAccount | Creation data. Please be aware, that you need to provide at least all required parameter      of the CheckAccount model! (optional)

    try:
        # Create a new check account
        api_response = api_instance.create_check_account(model_check_account=model_check_account)
        print("The response of CheckAccountApi->create_check_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->create_check_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_check_account** | [**ModelCheckAccount**](ModelCheckAccount.md)| Creation data. Please be aware, that you need to provide at least all required parameter      of the CheckAccount model! | [optional] 

### Return type

[**GetCheckAccounts200Response**](GetCheckAccounts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created check account |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clearing_account**
> CreateClearingAccount201Response create_clearing_account(create_clearing_account=create_clearing_account)

Create a new clearing account

Creates a new clearing account.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.create_clearing_account import CreateClearingAccount
from sevdesk_client.openapi_client.models.create_clearing_account201_response import CreateClearingAccount201Response
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
    api_instance = openapi_client.CheckAccountApi(api_client)
    create_clearing_account = openapi_client.CreateClearingAccount() # CreateClearingAccount | Data to create a clearning account (optional)

    try:
        # Create a new clearing account
        api_response = api_instance.create_clearing_account(create_clearing_account=create_clearing_account)
        print("The response of CheckAccountApi->create_clearing_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->create_clearing_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_clearing_account** | [**CreateClearingAccount**](CreateClearingAccount.md)| Data to create a clearning account | [optional] 

### Return type

[**CreateClearingAccount201Response**](CreateClearingAccount201Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Invalid value given |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_import_account**
> CreateFileImportAccount201Response create_file_import_account(create_file_import_account=create_file_import_account)

Create a new file import account

Creates a new banking account for file imports (CSV, MT940).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.create_file_import_account import CreateFileImportAccount
from sevdesk_client.openapi_client.models.create_file_import_account201_response import CreateFileImportAccount201Response
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
    api_instance = openapi_client.CheckAccountApi(api_client)
    create_file_import_account = openapi_client.CreateFileImportAccount() # CreateFileImportAccount | Data to create a file import account (optional)

    try:
        # Create a new file import account
        api_response = api_instance.create_file_import_account(create_file_import_account=create_file_import_account)
        print("The response of CheckAccountApi->create_file_import_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->create_file_import_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_file_import_account** | [**CreateFileImportAccount**](CreateFileImportAccount.md)| Data to create a file import account | [optional] 

### Return type

[**CreateFileImportAccount201Response**](CreateFileImportAccount201Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Invalid value given |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_check_account**
> DeleteCheckAccount200Response delete_check_account(check_account_id)

Deletes a check account

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
    api_instance = openapi_client.CheckAccountApi(api_client)
    check_account_id = 56 # int | Id of check account to delete

    try:
        # Deletes a check account
        api_response = api_instance.delete_check_account(check_account_id)
        print("The response of CheckAccountApi->delete_check_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->delete_check_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_id** | **int**| Id of check account to delete | 

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
**200** | Successful operation - check account deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_at_date**
> GetBalanceAtDate200Response get_balance_at_date(check_account_id, var_date)

Get the balance at a given date

Get the balance, calculated as the sum of all transactions sevdesk knows, up to and including the given date. Note that this balance does not have to be the actual bank account balance, e.g. if sevdesk did not import old transactions.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_balance_at_date200_response import GetBalanceAtDate200Response
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
    api_instance = openapi_client.CheckAccountApi(api_client)
    check_account_id = 56 # int | ID of check account
    var_date = '2013-10-20' # date | Only consider transactions up to this date at 23:59:59

    try:
        # Get the balance at a given date
        api_response = api_instance.get_balance_at_date(check_account_id, var_date)
        print("The response of CheckAccountApi->get_balance_at_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->get_balance_at_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_id** | **int**| ID of check account | 
 **var_date** | **date**| Only consider transactions up to this date at 23:59:59 | 

### Return type

[**GetBalanceAtDate200Response**](GetBalanceAtDate200Response.md)

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_account_by_id**
> GetCheckAccounts200Response get_check_account_by_id(check_account_id)

Find check account by ID

Retrieve an existing check account

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_check_accounts200_response import GetCheckAccounts200Response
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
    api_instance = openapi_client.CheckAccountApi(api_client)
    check_account_id = 56 # int | ID of check account

    try:
        # Find check account by ID
        api_response = api_instance.get_check_account_by_id(check_account_id)
        print("The response of CheckAccountApi->get_check_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->get_check_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_id** | **int**| ID of check account | 

### Return type

[**GetCheckAccounts200Response**](GetCheckAccounts200Response.md)

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_accounts**
> GetCheckAccounts200Response get_check_accounts()

Retrieve check accounts

Retrieve all check accounts

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_check_accounts200_response import GetCheckAccounts200Response
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
    api_instance = openapi_client.CheckAccountApi(api_client)

    try:
        # Retrieve check accounts
        api_response = api_instance.get_check_accounts()
        print("The response of CheckAccountApi->get_check_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->get_check_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCheckAccounts200Response**](GetCheckAccounts200Response.md)

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_check_account**
> ModelCheckAccountResponse update_check_account(check_account_id, model_check_account_update=model_check_account_update)

Update an existing check account

Update a check account

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_check_account_response import ModelCheckAccountResponse
from sevdesk_client.openapi_client.models.model_check_account_update import ModelCheckAccountUpdate
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
    api_instance = openapi_client.CheckAccountApi(api_client)
    check_account_id = 56 # int | ID of check account to update
    model_check_account_update = openapi_client.ModelCheckAccountUpdate() # ModelCheckAccountUpdate | Update data (optional)

    try:
        # Update an existing check account
        api_response = api_instance.update_check_account(check_account_id, model_check_account_update=model_check_account_update)
        print("The response of CheckAccountApi->update_check_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountApi->update_check_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_id** | **int**| ID of check account to update | 
 **model_check_account_update** | [**ModelCheckAccountUpdate**](ModelCheckAccountUpdate.md)| Update data | [optional] 

### Return type

[**ModelCheckAccountResponse**](ModelCheckAccountResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed check account resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

