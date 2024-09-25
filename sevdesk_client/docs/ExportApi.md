# openapi_client.ExportApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_contact**](ExportApi.md#export_contact) | **GET** /Export/contactListCsv | Export contact
[**export_credit_note**](ExportApi.md#export_credit_note) | **GET** /Export/creditNoteCsv | Export creditNote
[**export_datev**](ExportApi.md#export_datev) | **GET** /Export/datevCSV | Export datev
[**export_invoice**](ExportApi.md#export_invoice) | **GET** /Export/invoiceCsv | Export invoice
[**export_invoice_zip**](ExportApi.md#export_invoice_zip) | **GET** /Export/invoiceZip | Export Invoice as zip
[**export_transactions**](ExportApi.md#export_transactions) | **GET** /Export/transactionsCsv | Export transaction
[**export_voucher**](ExportApi.md#export_voucher) | **GET** /Export/voucherListCsv | Export voucher as zip
[**export_voucher_zip**](ExportApi.md#export_voucher_zip) | **GET** /Export/voucherZip | Export voucher zip
[**update_export_config**](ExportApi.md#update_export_config) | **PUT** /SevClient/{SevClientId}/updateExportConfig | Update export config


# **export_contact**
> ExportContact200Response export_contact(sev_query, download=download)

Export contact

Contact export as csv

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.export_contact200_response import ExportContact200Response
from sevdesk_client.openapi_client.models.export_contact_sev_query_parameter import ExportContactSevQueryParameter
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_query = openapi_client.ExportContactSevQueryParameter() # ExportContactSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export contact
        api_response = api_instance.export_contact(sev_query, download=download)
        print("The response of ExportApi->export_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ExportContactSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ExportContact200Response**](ExportContact200Response.md)

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_credit_note**
> ExportCreditNote200Response export_credit_note(sev_query, download=download)

Export creditNote

Export all credit notes as csv

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.export_credit_note200_response import ExportCreditNote200Response
from sevdesk_client.openapi_client.models.export_credit_note_sev_query_parameter import ExportCreditNoteSevQueryParameter
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_query = openapi_client.ExportCreditNoteSevQueryParameter() # ExportCreditNoteSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export creditNote
        api_response = api_instance.export_credit_note(sev_query, download=download)
        print("The response of ExportApi->export_credit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_credit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ExportCreditNoteSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ExportCreditNote200Response**](ExportCreditNote200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation with download |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_datev**
> object export_datev(start_date, end_date, scope, download=download, with_unpaid_documents=with_unpaid_documents, with_enshrined_documents=with_enshrined_documents, enshrine=enshrine)

Export datev

Datev export as zip with csv´s. Before you can perform the datev export, you must first set the \"accountingYearBegin\". To do this, you must use the <a href='#tag/Export/operation/updateExportConfig'>updateExportConfig</a> endpoint.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
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
    api_instance = openapi_client.ExportApi(api_client)
    start_date = 1641032867 # int | the start date of the export as timestamp
    end_date = 1648805267 # int | the end date of the export as timestamp
    scope = 'EXTCD' # str | Define what you want to include in the datev export. This parameter takes a string of 5 letters. Each stands for a model that should be included. Possible letters are: ‘E’ (Earnings), ‘X’ (Expenditure), ‘T’ (Transactions), ‘C’ (Cashregister), ‘D’ (Assets). By providing one of those letter you specify that it should be included in the datev export. Some combinations are: ‘EXTCD’, ‘EXTD’ …
    download = true # bool | Specifies if the document is downloaded (optional)
    with_unpaid_documents = true # bool | include unpaid documents (optional)
    with_enshrined_documents = true # bool | include enshrined documents (optional)
    enshrine = false # bool | Specify if you want to enshrine all models which were included in the export (optional)

    try:
        # Export datev
        api_response = api_instance.export_datev(start_date, end_date, scope, download=download, with_unpaid_documents=with_unpaid_documents, with_enshrined_documents=with_enshrined_documents, enshrine=enshrine)
        print("The response of ExportApi->export_datev:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_datev: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| the start date of the export as timestamp | 
 **end_date** | **int**| the end date of the export as timestamp | 
 **scope** | **str**| Define what you want to include in the datev export. This parameter takes a string of 5 letters. Each stands for a model that should be included. Possible letters are: ‘E’ (Earnings), ‘X’ (Expenditure), ‘T’ (Transactions), ‘C’ (Cashregister), ‘D’ (Assets). By providing one of those letter you specify that it should be included in the datev export. Some combinations are: ‘EXTCD’, ‘EXTD’ … | 
 **download** | **bool**| Specifies if the document is downloaded | [optional] 
 **with_unpaid_documents** | **bool**| include unpaid documents | [optional] 
 **with_enshrined_documents** | **bool**| include enshrined documents | [optional] 
 **enshrine** | **bool**| Specify if you want to enshrine all models which were included in the export | [optional] 

### Return type

**object**

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_invoice**
> ExportInvoice200Response export_invoice(sev_query, download=download)

Export invoice

Export all invoices as csv

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.export_invoice200_response import ExportInvoice200Response
from sevdesk_client.openapi_client.models.export_invoice_sev_query_parameter import ExportInvoiceSevQueryParameter
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_query = openapi_client.ExportInvoiceSevQueryParameter() # ExportInvoiceSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export invoice
        api_response = api_instance.export_invoice(sev_query, download=download)
        print("The response of ExportApi->export_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ExportInvoiceSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ExportInvoice200Response**](ExportInvoice200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation without download |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_invoice_zip**
> ExportInvoiceZip200Response export_invoice_zip(sev_query, download=download)

Export Invoice as zip

Export all invoices as zip

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.export_invoice_zip200_response import ExportInvoiceZip200Response
from sevdesk_client.openapi_client.models.export_invoice_zip_sev_query_parameter import ExportInvoiceZipSevQueryParameter
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_query = openapi_client.ExportInvoiceZipSevQueryParameter() # ExportInvoiceZipSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export Invoice as zip
        api_response = api_instance.export_invoice_zip(sev_query, download=download)
        print("The response of ExportApi->export_invoice_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_invoice_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ExportInvoiceZipSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ExportInvoiceZip200Response**](ExportInvoiceZip200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation without download |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_transactions**
> ExportTransactions200Response export_transactions(sev_query, download=download)

Export transaction

Export all transactions as csv

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.export_transactions200_response import ExportTransactions200Response
from sevdesk_client.openapi_client.models.export_transactions_sev_query_parameter import ExportTransactionsSevQueryParameter
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_query = openapi_client.ExportTransactionsSevQueryParameter() # ExportTransactionsSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export transaction
        api_response = api_instance.export_transactions(sev_query, download=download)
        print("The response of ExportApi->export_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ExportTransactionsSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ExportTransactions200Response**](ExportTransactions200Response.md)

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
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_voucher**
> ExportVoucher200Response export_voucher(sev_query, download=download)

Export voucher as zip

Export all vouchers as zip

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.export_voucher200_response import ExportVoucher200Response
from sevdesk_client.openapi_client.models.export_voucher_sev_query_parameter import ExportVoucherSevQueryParameter
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_query = openapi_client.ExportVoucherSevQueryParameter() # ExportVoucherSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export voucher as zip
        api_response = api_instance.export_voucher(sev_query, download=download)
        print("The response of ExportApi->export_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ExportVoucherSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ExportVoucher200Response**](ExportVoucher200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation without download |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_voucher_zip**
> ExportVoucherZip200Response export_voucher_zip(sev_query, download=download)

Export voucher zip

export all vouchers as zip

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.export_voucher_zip200_response import ExportVoucherZip200Response
from sevdesk_client.openapi_client.models.export_voucher_zip_sev_query_parameter import ExportVoucherZipSevQueryParameter
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_query = openapi_client.ExportVoucherZipSevQueryParameter() # ExportVoucherZipSevQueryParameter | 
    download = True # bool |  (optional)

    try:
        # Export voucher zip
        api_response = api_instance.export_voucher_zip(sev_query, download=download)
        print("The response of ExportApi->export_voucher_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_voucher_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_query** | [**ExportVoucherZipSevQueryParameter**](.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

[**ExportVoucherZip200Response**](ExportVoucherZip200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation without download |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_export_config**
> CheckAccountTransactionEnshrine200Response update_export_config(sev_client_id, update_export_config_request=update_export_config_request)

Update export config

Update export config to export datev CSV

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.check_account_transaction_enshrine200_response import CheckAccountTransactionEnshrine200Response
from sevdesk_client.openapi_client.models.update_export_config_request import UpdateExportConfigRequest
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
    api_instance = openapi_client.ExportApi(api_client)
    sev_client_id = 3.4 # float | id of sevClient
    update_export_config_request = openapi_client.UpdateExportConfigRequest() # UpdateExportConfigRequest | Specify the update (optional)

    try:
        # Update export config
        api_response = api_instance.update_export_config(sev_client_id, update_export_config_request=update_export_config_request)
        print("The response of ExportApi->update_export_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->update_export_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sev_client_id** | **float**| id of sevClient | 
 **update_export_config_request** | [**UpdateExportConfigRequest**](UpdateExportConfigRequest.md)| Specify the update | [optional] 

### Return type

[**CheckAccountTransactionEnshrine200Response**](CheckAccountTransactionEnshrine200Response.md)

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

