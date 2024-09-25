# openapi_client.VoucherApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_voucher**](VoucherApi.md#book_voucher) | **PUT** /Voucher/{voucherId}/bookAmount | Book a voucher
[**for_account_number**](VoucherApi.md#for_account_number) | **GET** /ReceiptGuidance/forAccountNumber | Get guidance by account number
[**for_all_accounts**](VoucherApi.md#for_all_accounts) | **GET** /ReceiptGuidance/forAllAccounts | Get all account guides
[**for_expense**](VoucherApi.md#for_expense) | **GET** /ReceiptGuidance/forExpense | Get guidance for expense accounts
[**for_revenue**](VoucherApi.md#for_revenue) | **GET** /ReceiptGuidance/forRevenue | Get guidance for revenue accounts
[**for_tax_rule**](VoucherApi.md#for_tax_rule) | **GET** /ReceiptGuidance/forTaxRule | Get guidance by Tax Rule
[**get_voucher_by_id**](VoucherApi.md#get_voucher_by_id) | **GET** /Voucher/{voucherId} | Find voucher by ID
[**get_vouchers**](VoucherApi.md#get_vouchers) | **GET** /Voucher | Retrieve vouchers
[**update_voucher**](VoucherApi.md#update_voucher) | **PUT** /Voucher/{voucherId} | Update an existing voucher
[**voucher_enshrine**](VoucherApi.md#voucher_enshrine) | **PUT** /Voucher/{voucherId}/enshrine | Enshrine
[**voucher_factory_save_voucher**](VoucherApi.md#voucher_factory_save_voucher) | **POST** /Voucher/Factory/saveVoucher | Create a new voucher
[**voucher_reset_to_draft**](VoucherApi.md#voucher_reset_to_draft) | **PUT** /Voucher/{voucherId}/resetToDraft | Reset status to draft
[**voucher_reset_to_open**](VoucherApi.md#voucher_reset_to_open) | **PUT** /Voucher/{voucherId}/resetToOpen | Reset status to open
[**voucher_upload_file**](VoucherApi.md#voucher_upload_file) | **POST** /Voucher/Factory/uploadTempFile | Upload voucher file


# **book_voucher**
> BookVoucher200Response book_voucher(voucher_id, book_voucher_request=book_voucher_request)

Book a voucher

Booking the voucher with a transaction is probably the most important part in the bookkeeping process.<br> There are several ways on correctly booking a voucher, all by using the same endpoint.<br> Conveniently, the booking process is exactly the same as the process for invoices.<br> For this reason, you can have a look at it <a href='#tag/Voucher/How-to-filter-for-certain-vouchers'>here</a> and all you need to to is to change \"Invoice\" into \"Voucher\" in the URL.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.book_voucher200_response import BookVoucher200Response
from sevdesk_client.openapi_client.models.book_voucher_request import BookVoucherRequest
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
    api_instance = openapi_client.VoucherApi(api_client)
    voucher_id = 56 # int | ID of voucher to book
    book_voucher_request = openapi_client.BookVoucherRequest() # BookVoucherRequest | Booking data (optional)

    try:
        # Book a voucher
        api_response = api_instance.book_voucher(voucher_id, book_voucher_request=book_voucher_request)
        print("The response of VoucherApi->book_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->book_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **int**| ID of voucher to book | 
 **book_voucher_request** | [**BookVoucherRequest**](BookVoucherRequest.md)| Booking data | [optional] 

### Return type

[**BookVoucher200Response**](BookVoucher200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed voucher log entry |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **for_account_number**
> ForAllAccounts200Response for_account_number(account_number)

Get guidance by account number

You can use this endpoint to get additional information about the account that you may want to use.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.for_all_accounts200_response import ForAllAccounts200Response
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
    api_instance = openapi_client.VoucherApi(api_client)
    account_number = 56 # int | The datev account number you want to get additional information of

    try:
        # Get guidance by account number
        api_response = api_instance.for_account_number(account_number)
        print("The response of VoucherApi->for_account_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->for_account_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **int**| The datev account number you want to get additional information of | 

### Return type

[**ForAllAccounts200Response**](ForAllAccounts200Response.md)

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
**422** | The account you requested could not be found. |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **for_all_accounts**
> ForAllAccounts200Response for_all_accounts()

Get all account guides

You can use this endpoint to help you decide which accounts you can use when creating a voucher

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.for_all_accounts200_response import ForAllAccounts200Response
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
    api_instance = openapi_client.VoucherApi(api_client)

    try:
        # Get all account guides
        api_response = api_instance.for_all_accounts()
        print("The response of VoucherApi->for_all_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->for_all_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ForAllAccounts200Response**](ForAllAccounts200Response.md)

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

# **for_expense**
> ForAllAccounts200Response for_expense()

Get guidance for expense accounts

Provides all possible combinations for expense accounts to be used with expense receipts/vouchers.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.for_all_accounts200_response import ForAllAccounts200Response
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
    api_instance = openapi_client.VoucherApi(api_client)

    try:
        # Get guidance for expense accounts
        api_response = api_instance.for_expense()
        print("The response of VoucherApi->for_expense:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->for_expense: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ForAllAccounts200Response**](ForAllAccounts200Response.md)

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

# **for_revenue**
> ForAllAccounts200Response for_revenue()

Get guidance for revenue accounts

Provides all possible combinations for revenue accounts to be used with revenue receipts/vouchers.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.for_all_accounts200_response import ForAllAccounts200Response
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
    api_instance = openapi_client.VoucherApi(api_client)

    try:
        # Get guidance for revenue accounts
        api_response = api_instance.for_revenue()
        print("The response of VoucherApi->for_revenue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->for_revenue: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ForAllAccounts200Response**](ForAllAccounts200Response.md)

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

# **for_tax_rule**
> ForAllAccounts200Response for_tax_rule(tax_rule)

Get guidance by Tax Rule

You can use this endpoint to get additional information about the tax rule (for example, USTPFL_UMS_EINN) that you may want to use.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.for_all_accounts200_response import ForAllAccounts200Response
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
    api_instance = openapi_client.VoucherApi(api_client)
    tax_rule = 'USTPFL_UMS_EINN' # str | The code of the tax rule you want to get guidance for.

    try:
        # Get guidance by Tax Rule
        api_response = api_instance.for_tax_rule(tax_rule)
        print("The response of VoucherApi->for_tax_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->for_tax_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rule** | **str**| The code of the tax rule you want to get guidance for. | 

### Return type

[**ForAllAccounts200Response**](ForAllAccounts200Response.md)

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
**422** | No account guides were found for the requested tax rule. |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher_by_id**
> GetVouchers200Response get_voucher_by_id(voucher_id)

Find voucher by ID

Returns a single voucher

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_vouchers200_response import GetVouchers200Response
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
    api_instance = openapi_client.VoucherApi(api_client)
    voucher_id = 56 # int | ID of voucher to return

    try:
        # Find voucher by ID
        api_response = api_instance.get_voucher_by_id(voucher_id)
        print("The response of VoucherApi->get_voucher_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->get_voucher_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **int**| ID of voucher to return | 

### Return type

[**GetVouchers200Response**](GetVouchers200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Voucher was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vouchers**
> GetVouchers200Response get_vouchers(status=status, credit_debit=credit_debit, description_like=description_like, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)

Retrieve vouchers

There are a multitude of parameter which can be used to filter. A few of them are attached but      for a complete list please check out <a href='#tag/Voucher/How-to-filter-for-certain-vouchers'>this</a> list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_vouchers200_response import GetVouchers200Response
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
    api_instance = openapi_client.VoucherApi(api_client)
    status = 3.4 # float | Status of the vouchers to retrieve. (optional)
    credit_debit = 'credit_debit_example' # str | Define if you only want credit or debit vouchers. (optional)
    description_like = 'description_like_example' # str | Retrieve all vouchers with a description like this. (optional)
    start_date = 01.01.2020 # int | Retrieve all vouchers with a date equal or higher (optional)
    end_date = 01.01.2020 # int | Retrieve all vouchers with a date equal or lower (optional)
    contact_id = 56 # int | Retrieve all vouchers with this contact. Must be provided with contact[objectName] (optional)
    contact_object_name = 'contact_object_name_example' # str | Only required if contact[id] was provided. 'Contact' should be used as value. (optional)

    try:
        # Retrieve vouchers
        api_response = api_instance.get_vouchers(status=status, credit_debit=credit_debit, description_like=description_like, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)
        print("The response of VoucherApi->get_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->get_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **float**| Status of the vouchers to retrieve. | [optional] 
 **credit_debit** | **str**| Define if you only want credit or debit vouchers. | [optional] 
 **description_like** | **str**| Retrieve all vouchers with a description like this. | [optional] 
 **start_date** | **int**| Retrieve all vouchers with a date equal or higher | [optional] 
 **end_date** | **int**| Retrieve all vouchers with a date equal or lower | [optional] 
 **contact_id** | **int**| Retrieve all vouchers with this contact. Must be provided with contact[objectName] | [optional] 
 **contact_object_name** | **str**| Only required if contact[id] was provided. &#39;Contact&#39; should be used as value. | [optional] 

### Return type

[**GetVouchers200Response**](GetVouchers200Response.md)

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

# **update_voucher**
> ModelVoucherResponse update_voucher(voucher_id, model_voucher_update=model_voucher_update)

Update an existing voucher

Update a draft voucher using this method if you want to change simple values like the description. Complex changes like adding a position should use /Voucher/Factory/saveVoucher.<br> You can not change the status using this endpoint.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_voucher_response import ModelVoucherResponse
from sevdesk_client.openapi_client.models.model_voucher_update import ModelVoucherUpdate
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
    api_instance = openapi_client.VoucherApi(api_client)
    voucher_id = 56 # int | ID of voucher to update
    model_voucher_update = openapi_client.ModelVoucherUpdate() # ModelVoucherUpdate | Update data (optional)

    try:
        # Update an existing voucher
        api_response = api_instance.update_voucher(voucher_id, model_voucher_update=model_voucher_update)
        print("The response of VoucherApi->update_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->update_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **int**| ID of voucher to update | 
 **model_voucher_update** | [**ModelVoucherUpdate**](ModelVoucherUpdate.md)| Update data | [optional] 

### Return type

[**ModelVoucherResponse**](ModelVoucherResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed voucher resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voucher_enshrine**
> CheckAccountTransactionEnshrine200Response voucher_enshrine(voucher_id)

Enshrine

Sets the current date and time as a value for the property `enshrined`.<br> This operation is only possible if the status is \"Open\" (`\"status\": \"100\"`) or higher.  Enshrined vouchers cannot be changed. This operation cannot be undone. 

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
    api_instance = openapi_client.VoucherApi(api_client)
    voucher_id = 56 # int | ID of the voucher to enshrine

    try:
        # Enshrine
        api_response = api_instance.voucher_enshrine(voucher_id)
        print("The response of VoucherApi->voucher_enshrine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->voucher_enshrine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **int**| ID of the voucher to enshrine | 

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

# **voucher_factory_save_voucher**
> SaveVoucherResponse voucher_factory_save_voucher(save_voucher=save_voucher)

Create a new voucher

Bundles the creation or updating of voucher and voucher position.<br> The list of parameters starts with the voucher model.<br> This contains all required attributes for a complete voucher.<br> Most of the attributes are covered in the voucher attribute list, there are only two parameters standing out, namely <b>mapAll</b> and <b>objectName</b>.<br> These are just needed for our system and you always need to provide them.<br><br> The list of parameters then continues with the voucher position array.<br> With this array you have the possibility to add multiple positions at once.<br> In the example it only contains one position, again together with the parameters <b>mapAll</b> and <b>objectName</b>, however, you can add more voucher positions by extending the array.<br> So if you wanted to add another position, you would add the same list of parameters with an incremented array index of \\\"1\\\" instead of \\\"0\\\".<br><br> The list ends with the two parameters voucherPosDelete and filename.<br> We will shortly explain what they can do.<br> With voucherPosDelete you can delete voucher positions as this request can also be used to update draft vouchers.<br> With filename you can attach a file to the voucher.<br> For most of our customers this is a really important step, as they need to digitize their receipts.<br> Finally, after covering all parameters, the only important information left, is that the order of the last two attributes always needs to be kept. <br><br> The only valid status values for this endpoint are 50 (draft) and 100 (open). You can only update draft vouchers. If you have to, you can downgrade the status by calling resetToOpen (from paid) and resetToDraft (from open).

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.save_voucher import SaveVoucher
from sevdesk_client.openapi_client.models.save_voucher_response import SaveVoucherResponse
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
    api_instance = openapi_client.VoucherApi(api_client)
    save_voucher = openapi_client.SaveVoucher() # SaveVoucher | Creation data. Please be aware, that you need to provide at least all required parameters of the voucher and voucher position model! (optional)

    try:
        # Create a new voucher
        api_response = api_instance.voucher_factory_save_voucher(save_voucher=save_voucher)
        print("The response of VoucherApi->voucher_factory_save_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->voucher_factory_save_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_voucher** | [**SaveVoucher**](SaveVoucher.md)| Creation data. Please be aware, that you need to provide at least all required parameters of the voucher and voucher position model! | [optional] 

### Return type

[**SaveVoucherResponse**](SaveVoucherResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created voucher |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voucher_reset_to_draft**
> VoucherResetToOpen200Response voucher_reset_to_draft(voucher_id)

Reset status to draft

Resets the status \"Draft\" (`\"status\": \"50\"`). Linked payments will be unlinked. Created asset depreciation will be reset.<br> This is not possible if the voucher is already enshrined!  You can only change the status from higher to lower (\"Open\" to \"Draft\").<br> To change to higher status use [/Voucher/Factory/saveVoucher](#tag/Voucher/operation/voucherFactorySaveVoucher). 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.voucher_reset_to_open200_response import VoucherResetToOpen200Response
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
    api_instance = openapi_client.VoucherApi(api_client)
    voucher_id = 56 # int | ID of the voucher to reset

    try:
        # Reset status to draft
        api_response = api_instance.voucher_reset_to_draft(voucher_id)
        print("The response of VoucherApi->voucher_reset_to_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->voucher_reset_to_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **int**| ID of the voucher to reset | 

### Return type

[**VoucherResetToOpen200Response**](VoucherResetToOpen200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed voucher |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voucher_reset_to_open**
> VoucherResetToOpen200Response voucher_reset_to_open(voucher_id)

Reset status to open

Resets the status to \"Open\" (`\"status\": \"100\"`). Linked payments will be unlinked. Created asset depreciation will be reset.<br> This is not possible if the voucher is already enshrined!  This endpoint can not be used to increase the status from \"Draft\" to \"Open\".<br> You can only change the status from higher to lower (\"Open\" to \"Draft\").<br> To change to higher status use [Voucher/{voucherId}/bookAmount](#tag/Voucher/operation/bookVoucher). To change to lower status use [Voucher/{voucherId}/resetToDraft](#tag/Voucher/operation/voucherResetToDraft). 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.voucher_reset_to_open200_response import VoucherResetToOpen200Response
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
    api_instance = openapi_client.VoucherApi(api_client)
    voucher_id = 56 # int | ID of the voucher to reset

    try:
        # Reset status to open
        api_response = api_instance.voucher_reset_to_open(voucher_id)
        print("The response of VoucherApi->voucher_reset_to_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->voucher_reset_to_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **int**| ID of the voucher to reset | 

### Return type

[**VoucherResetToOpen200Response**](VoucherResetToOpen200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed voucher |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voucher_upload_file**
> VoucherUploadFile201Response voucher_upload_file(voucher_upload_file_request=voucher_upload_file_request)

Upload voucher file

To attach a document to a voucher, you will need to upload it first for later use.<br> To do this, you can use this request.<br> When you successfully uploaded the file, you will get a sevdesk internal filename in the response.<br> The filename will be a hash generated from your uploaded file. You will need it in the next request!<br> After you got the just mentioned filename, you can enter it as a value for the filename parameter of the saveVoucher request.<br> If you provided all necessary parameters and kept all of them in the right order, the file will be attached to your voucher.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.voucher_upload_file201_response import VoucherUploadFile201Response
from sevdesk_client.openapi_client.models.voucher_upload_file_request import VoucherUploadFileRequest
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
    api_instance = openapi_client.VoucherApi(api_client)
    voucher_upload_file_request = openapi_client.VoucherUploadFileRequest() # VoucherUploadFileRequest | File to upload (optional)

    try:
        # Upload voucher file
        api_response = api_instance.voucher_upload_file(voucher_upload_file_request=voucher_upload_file_request)
        print("The response of VoucherApi->voucher_upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoucherApi->voucher_upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_upload_file_request** | [**VoucherUploadFileRequest**](VoucherUploadFileRequest.md)| File to upload | [optional] 

### Return type

[**VoucherUploadFile201Response**](VoucherUploadFile201Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A pdf file |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

