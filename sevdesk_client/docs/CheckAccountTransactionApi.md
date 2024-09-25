# openapi_client.CheckAccountTransactionApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_account_transaction_enshrine**](CheckAccountTransactionApi.md#check_account_transaction_enshrine) | **PUT** /CheckAccountTransaction/{checkAccountTransactionId}/enshrine | Enshrine
[**create_transaction**](CheckAccountTransactionApi.md#create_transaction) | **POST** /CheckAccountTransaction | Create a new transaction
[**delete_check_account_transaction**](CheckAccountTransactionApi.md#delete_check_account_transaction) | **DELETE** /CheckAccountTransaction/{checkAccountTransactionId} | Deletes a check account transaction
[**get_check_account_transaction_by_id**](CheckAccountTransactionApi.md#get_check_account_transaction_by_id) | **GET** /CheckAccountTransaction/{checkAccountTransactionId} | Find check account transaction by ID
[**get_transactions**](CheckAccountTransactionApi.md#get_transactions) | **GET** /CheckAccountTransaction | Retrieve transactions
[**update_check_account_transaction**](CheckAccountTransactionApi.md#update_check_account_transaction) | **PUT** /CheckAccountTransaction/{checkAccountTransactionId} | Update an existing check account transaction


# **check_account_transaction_enshrine**
> CheckAccountTransactionEnshrine200Response check_account_transaction_enshrine(check_account_transaction_id)

Enshrine

Sets the current date and time as a value for the property `enshrined`.<br> This operation is only possible if the status is \"Linked\" (`\"status\": \"200\"`) or higher.  Linked invoices, credit notes or vouchers cannot be changed when the transaction is enshrined. 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.check_account_transaction_enshrine200_response import CheckAccountTransactionEnshrine200Response
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
    api_instance = openapi_client.CheckAccountTransactionApi(api_client)
    check_account_transaction_id = 56 # int | ID of the transaction to enshrine

    try:
        # Enshrine
        api_response = api_instance.check_account_transaction_enshrine(check_account_transaction_id)
        print("The response of CheckAccountTransactionApi->check_account_transaction_enshrine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountTransactionApi->check_account_transaction_enshrine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_transaction_id** | **int**| ID of the transaction to enshrine | 

### Return type

[**CheckAccountTransactionEnshrine200Response**](CheckAccountTransactionEnshrine200Response.md)

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
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction**
> ModelCheckAccountTransactionResponse create_transaction(model_check_account_transaction=model_check_account_transaction)

Create a new transaction

Creates a new transaction on a check account.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_check_account_transaction import ModelCheckAccountTransaction
from sevdesk_client.openapi_client.models.model_check_account_transaction_response import ModelCheckAccountTransactionResponse
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
    api_instance = openapi_client.CheckAccountTransactionApi(api_client)
    model_check_account_transaction = openapi_client.ModelCheckAccountTransaction() # ModelCheckAccountTransaction | Creation data. Please be aware, that you need to provide at least all required parameter      of the CheckAccountTransaction model! (optional)

    try:
        # Create a new transaction
        api_response = api_instance.create_transaction(model_check_account_transaction=model_check_account_transaction)
        print("The response of CheckAccountTransactionApi->create_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountTransactionApi->create_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_check_account_transaction** | [**ModelCheckAccountTransaction**](ModelCheckAccountTransaction.md)| Creation data. Please be aware, that you need to provide at least all required parameter      of the CheckAccountTransaction model! | [optional] 

### Return type

[**ModelCheckAccountTransactionResponse**](ModelCheckAccountTransactionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created transaction |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_check_account_transaction**
> DeleteCheckAccount200Response delete_check_account_transaction(check_account_transaction_id)

Deletes a check account transaction

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
    api_instance = openapi_client.CheckAccountTransactionApi(api_client)
    check_account_transaction_id = 56 # int | Id of check account transaction to delete

    try:
        # Deletes a check account transaction
        api_response = api_instance.delete_check_account_transaction(check_account_transaction_id)
        print("The response of CheckAccountTransactionApi->delete_check_account_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountTransactionApi->delete_check_account_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_transaction_id** | **int**| Id of check account transaction to delete | 

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
**200** | Successful operation - check account transaction deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_account_transaction_by_id**
> GetTransactions200Response get_check_account_transaction_by_id(check_account_transaction_id)

Find check account transaction by ID

Retrieve an existing check account transaction

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_transactions200_response import GetTransactions200Response
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
    api_instance = openapi_client.CheckAccountTransactionApi(api_client)
    check_account_transaction_id = 56 # int | ID of check account transaction

    try:
        # Find check account transaction by ID
        api_response = api_instance.get_check_account_transaction_by_id(check_account_transaction_id)
        print("The response of CheckAccountTransactionApi->get_check_account_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountTransactionApi->get_check_account_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_transaction_id** | **int**| ID of check account transaction | 

### Return type

[**GetTransactions200Response**](GetTransactions200Response.md)

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

# **get_transactions**
> GetTransactions200Response get_transactions(check_account_id=check_account_id, check_account_object_name=check_account_object_name, is_booked=is_booked, paymt_purpose=paymt_purpose, start_date=start_date, end_date=end_date, payee_payer_name=payee_payer_name, only_credit=only_credit, only_debit=only_debit)

Retrieve transactions

Retrieve all transactions depending on the filters defined in the query.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_transactions200_response import GetTransactions200Response
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
    api_instance = openapi_client.CheckAccountTransactionApi(api_client)
    check_account_id = 56 # int | Retrieve all transactions on this check account. Must be provided with checkAccount[objectName] (optional)
    check_account_object_name = 'check_account_object_name_example' # str | Only required if checkAccount[id] was provided. 'CheckAccount' should be used as value. (optional)
    is_booked = True # bool | Only retrieve booked transactions (optional)
    paymt_purpose = 'paymt_purpose_example' # str | Only retrieve transactions with this payment purpose (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Only retrieve transactions from this date on (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Only retrieve transactions up to this date (optional)
    payee_payer_name = 'payee_payer_name_example' # str | Only retrieve transactions with this payee / payer (optional)
    only_credit = True # bool | Only retrieve credit transactions (optional)
    only_debit = True # bool | Only retrieve debit transactions (optional)

    try:
        # Retrieve transactions
        api_response = api_instance.get_transactions(check_account_id=check_account_id, check_account_object_name=check_account_object_name, is_booked=is_booked, paymt_purpose=paymt_purpose, start_date=start_date, end_date=end_date, payee_payer_name=payee_payer_name, only_credit=only_credit, only_debit=only_debit)
        print("The response of CheckAccountTransactionApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountTransactionApi->get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_id** | **int**| Retrieve all transactions on this check account. Must be provided with checkAccount[objectName] | [optional] 
 **check_account_object_name** | **str**| Only required if checkAccount[id] was provided. &#39;CheckAccount&#39; should be used as value. | [optional] 
 **is_booked** | **bool**| Only retrieve booked transactions | [optional] 
 **paymt_purpose** | **str**| Only retrieve transactions with this payment purpose | [optional] 
 **start_date** | **datetime**| Only retrieve transactions from this date on | [optional] 
 **end_date** | **datetime**| Only retrieve transactions up to this date | [optional] 
 **payee_payer_name** | **str**| Only retrieve transactions with this payee / payer | [optional] 
 **only_credit** | **bool**| Only retrieve credit transactions | [optional] 
 **only_debit** | **bool**| Only retrieve debit transactions | [optional] 

### Return type

[**GetTransactions200Response**](GetTransactions200Response.md)

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

# **update_check_account_transaction**
> ModelCheckAccountTransactionResponse update_check_account_transaction(check_account_transaction_id, model_check_account_transaction_update=model_check_account_transaction_update)

Update an existing check account transaction

Update a check account transaction

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_check_account_transaction_response import ModelCheckAccountTransactionResponse
from sevdesk_client.openapi_client.models.model_check_account_transaction_update import ModelCheckAccountTransactionUpdate
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
    api_instance = openapi_client.CheckAccountTransactionApi(api_client)
    check_account_transaction_id = 56 # int | ID of check account to update transaction
    model_check_account_transaction_update = openapi_client.ModelCheckAccountTransactionUpdate() # ModelCheckAccountTransactionUpdate | Update data (optional)

    try:
        # Update an existing check account transaction
        api_response = api_instance.update_check_account_transaction(check_account_transaction_id, model_check_account_transaction_update=model_check_account_transaction_update)
        print("The response of CheckAccountTransactionApi->update_check_account_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckAccountTransactionApi->update_check_account_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_account_transaction_id** | **int**| ID of check account to update transaction | 
 **model_check_account_transaction_update** | [**ModelCheckAccountTransactionUpdate**](ModelCheckAccountTransactionUpdate.md)| Update data | [optional] 

### Return type

[**ModelCheckAccountTransactionResponse**](ModelCheckAccountTransactionResponse.md)

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

