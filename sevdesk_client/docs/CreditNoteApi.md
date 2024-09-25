# openapi_client.CreditNoteApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_credit_note**](CreditNoteApi.md#book_credit_note) | **PUT** /CreditNote/{creditNoteId}/bookAmount | Book a credit note
[**create_credit_note_from_invoice**](CreditNoteApi.md#create_credit_note_from_invoice) | **POST** /CreditNote/Factory/createFromInvoice | Creates a new creditNote from an invoice
[**create_credit_note_from_voucher**](CreditNoteApi.md#create_credit_note_from_voucher) | **POST** /CreditNote/Factory/createFromVoucher | Creates a new creditNote from a voucher
[**createcredit_note**](CreditNoteApi.md#createcredit_note) | **POST** /CreditNote/Factory/saveCreditNote | Create a new creditNote
[**credit_note_enshrine**](CreditNoteApi.md#credit_note_enshrine) | **PUT** /CreditNote/{creditNoteId}/enshrine | Enshrine
[**credit_note_get_pdf**](CreditNoteApi.md#credit_note_get_pdf) | **GET** /CreditNote/{creditNoteId}/getPdf | Retrieve pdf document of a credit note
[**credit_note_reset_to_draft**](CreditNoteApi.md#credit_note_reset_to_draft) | **PUT** /CreditNote/{creditNoteId}/resetToDraft | Reset status to draft
[**credit_note_reset_to_open**](CreditNoteApi.md#credit_note_reset_to_open) | **PUT** /CreditNote/{creditNoteId}/resetToOpen | Reset status to open
[**credit_note_send_by**](CreditNoteApi.md#credit_note_send_by) | **PUT** /CreditNote/{creditNoteId}/sendBy | Mark credit note as sent
[**deletecredit_note**](CreditNoteApi.md#deletecredit_note) | **DELETE** /CreditNote/{creditNoteId} | Deletes an creditNote
[**get_credit_notes**](CreditNoteApi.md#get_credit_notes) | **GET** /CreditNote | Retrieve CreditNote
[**getcredit_note_by_id**](CreditNoteApi.md#getcredit_note_by_id) | **GET** /CreditNote/{creditNoteId} | Find creditNote by ID
[**send_credit_note_by_printing**](CreditNoteApi.md#send_credit_note_by_printing) | **GET** /CreditNote/{creditNoteId}/sendByWithRender | Send credit note by printing
[**send_credit_note_via_e_mail**](CreditNoteApi.md#send_credit_note_via_e_mail) | **POST** /CreditNote/{creditNoteId}/sendViaEmail | Send credit note via email
[**updatecredit_note**](CreditNoteApi.md#updatecredit_note) | **PUT** /CreditNote/{creditNoteId} | Update an existing creditNote


# **book_credit_note**
> BookCreditNote200Response book_credit_note(credit_note_id, book_credit_note_request=book_credit_note_request)

Book a credit note

Booking the credit note with a transaction is probably the most important part in the bookkeeping process.<br> There are several ways on correctly booking a credit note, all by using the same endpoint.<br> Conveniently, the booking process is exactly the same as the process for invoices and vouchers.<br> For this reason, you can have a look at it in the <a href='#tag/Invoice/How-to-book-an-invoice'>invoice chapter</a> and all you need to do is to change \"Invoice\" into \"CreditNote\" in the URL.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.book_credit_note200_response import BookCreditNote200Response
from sevdesk_client.openapi_client.models.book_credit_note_request import BookCreditNoteRequest
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of credit note to book
    book_credit_note_request = openapi_client.BookCreditNoteRequest() # BookCreditNoteRequest | Booking data (optional)

    try:
        # Book a credit note
        api_response = api_instance.book_credit_note(credit_note_id, book_credit_note_request=book_credit_note_request)
        print("The response of CreditNoteApi->book_credit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->book_credit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of credit note to book | 
 **book_credit_note_request** | [**BookCreditNoteRequest**](BookCreditNoteRequest.md)| Booking data | [optional] 

### Return type

[**BookCreditNote200Response**](BookCreditNote200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed invoice log entry |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_from_invoice**
> CreateCreditNoteFromInvoice201Response create_credit_note_from_invoice(create_credit_note_from_invoice_request=create_credit_note_from_invoice_request)

Creates a new creditNote from an invoice

Use this endpoint to create a new creditNote from an invoice.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.create_credit_note_from_invoice201_response import CreateCreditNoteFromInvoice201Response
from sevdesk_client.openapi_client.models.create_credit_note_from_invoice_request import CreateCreditNoteFromInvoiceRequest
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    create_credit_note_from_invoice_request = openapi_client.CreateCreditNoteFromInvoiceRequest() # CreateCreditNoteFromInvoiceRequest |  (optional)

    try:
        # Creates a new creditNote from an invoice
        api_response = api_instance.create_credit_note_from_invoice(create_credit_note_from_invoice_request=create_credit_note_from_invoice_request)
        print("The response of CreditNoteApi->create_credit_note_from_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->create_credit_note_from_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credit_note_from_invoice_request** | [**CreateCreditNoteFromInvoiceRequest**](CreateCreditNoteFromInvoiceRequest.md)|  | [optional] 

### Return type

[**CreateCreditNoteFromInvoice201Response**](CreateCreditNoteFromInvoice201Response.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_from_voucher**
> CreateCreditNoteFromInvoice201Response create_credit_note_from_voucher(create_credit_note_from_voucher_request=create_credit_note_from_voucher_request)

Creates a new creditNote from a voucher

**Not supported with sevdesk-Update 2.0**  Use this endpoint to create a new creditNote from a voucher. 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.create_credit_note_from_invoice201_response import CreateCreditNoteFromInvoice201Response
from sevdesk_client.openapi_client.models.create_credit_note_from_voucher_request import CreateCreditNoteFromVoucherRequest
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    create_credit_note_from_voucher_request = openapi_client.CreateCreditNoteFromVoucherRequest() # CreateCreditNoteFromVoucherRequest |  (optional)

    try:
        # Creates a new creditNote from a voucher
        api_response = api_instance.create_credit_note_from_voucher(create_credit_note_from_voucher_request=create_credit_note_from_voucher_request)
        print("The response of CreditNoteApi->create_credit_note_from_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->create_credit_note_from_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credit_note_from_voucher_request** | [**CreateCreditNoteFromVoucherRequest**](CreateCreditNoteFromVoucherRequest.md)|  | [optional] 

### Return type

[**CreateCreditNoteFromInvoice201Response**](CreateCreditNoteFromInvoice201Response.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createcredit_note**
> SaveCreditNoteResponse createcredit_note(save_credit_note=save_credit_note)

Create a new creditNote

The list of parameters starts with the credit note array.<br> This array contains all required attributes for a complete credit note.<br> Most of the attributes are covered in the credit note attribute list, there are only two parameters standing out, namely <b>mapAll</b> and <b>objectName</b>.<br> These are just needed for our system and you always need to provide them.<br> The list of parameters then continues with the credit note position array.<br> With this array you have the possibility to add multiple positions at once.<br> In the example it only contains one position, again together with the parameters <b>mapAll</b> and <b>objectName</b>, however, you can add more credit note positions by extending the array.<br> So if you wanted to add another position, you would add the same list of parameters with an incremented array index of \"1\" instead of \"0\".<br><br> The list ends with the five parameters creditNotePosDelete, discountSave, discountDelete, takeDefaultAddress and forCashRegister.<br> They only play a minor role if you only want to create a credit note but we will shortly explain what they can do.<br> With creditNotePosDelete you have to option to delete credit note positions as this request can also be used to update credit notes.<br> Both discount parameters are deprecated and have no use for credit notes, however they need to be provided in case you want to use the following two parameters.<br> With takeDefaultAddress you can specify that the first address of the contact you are using for the credit note is taken for the credit note address attribute automatically, so you don't need to provide the address yourself.<br> Finally, the forCashRegister parameter needs to be set to <b>true</b> if your credit note is to be booked on the cash register.<br> If you want to know more about these parameters, for example if you want to use this request to update credit notes, feel free to contact our support.<br> Finally, after covering all parameters, they only important information left, is that the order of the last five attributes always needs to be kept.<br> You will also always need to provide all of them, as otherwise the request won't work properly.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.save_credit_note import SaveCreditNote
from sevdesk_client.openapi_client.models.save_credit_note_response import SaveCreditNoteResponse
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    save_credit_note = openapi_client.SaveCreditNote() # SaveCreditNote | Creation data. Please be aware, that you need to provide at least all required parameter      of the credit note model! (optional)

    try:
        # Create a new creditNote
        api_response = api_instance.createcredit_note(save_credit_note=save_credit_note)
        print("The response of CreditNoteApi->createcredit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->createcredit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_credit_note** | [**SaveCreditNote**](SaveCreditNote.md)| Creation data. Please be aware, that you need to provide at least all required parameter      of the credit note model! | [optional] 

### Return type

[**SaveCreditNoteResponse**](SaveCreditNoteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created credit note |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_note_enshrine**
> CheckAccountTransactionEnshrine200Response credit_note_enshrine(credit_note_id)

Enshrine

Sets the current date and time as a value for the property `enshrined`.<br> This operation is only possible if the status is \"Open\" (`\"status\": \"200\"`) or higher.  Enshrined credit notes cannot be changed. This operation cannot be undone. 

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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of the credit note to enshrine

    try:
        # Enshrine
        api_response = api_instance.credit_note_enshrine(credit_note_id)
        print("The response of CreditNoteApi->credit_note_enshrine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->credit_note_enshrine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of the credit note to enshrine | 

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

# **credit_note_get_pdf**
> CreditNoteGetPdf200Response credit_note_get_pdf(credit_note_id, download=download, prevent_send_by=prevent_send_by)

Retrieve pdf document of a credit note

Retrieves the pdf document of a credit note with additional metadata.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.credit_note_get_pdf200_response import CreditNoteGetPdf200Response
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of credit note from which you want the pdf
    download = true # bool | If u want to download the pdf of the credit note. (optional)
    prevent_send_by = true # bool | Defines if u want to send the credit note. (optional)

    try:
        # Retrieve pdf document of a credit note
        api_response = api_instance.credit_note_get_pdf(credit_note_id, download=download, prevent_send_by=prevent_send_by)
        print("The response of CreditNoteApi->credit_note_get_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->credit_note_get_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of credit note from which you want the pdf | 
 **download** | **bool**| If u want to download the pdf of the credit note. | [optional] 
 **prevent_send_by** | **bool**| Defines if u want to send the credit note. | [optional] 

### Return type

[**CreditNoteGetPdf200Response**](CreditNoteGetPdf200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A pdf file |  -  |
**400** | Bad request. Invoice was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_note_reset_to_draft**
> CreditNoteResetToDraft200Response credit_note_reset_to_draft(credit_note_id)

Reset status to draft

Resets the status to \"Draft\" (`\"status\": \"100\"`).<br> This is only possible if the credit note has the status \"Open\" (`\"status\": \"200\"`).<br> If it has a higher status use [CreditNote/{creditNoteId}/resetToOpen](#tag/CreditNote/operation/creditNoteResetToOpen) first. 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.credit_note_reset_to_draft200_response import CreditNoteResetToDraft200Response
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of the credit note to reset

    try:
        # Reset status to draft
        api_response = api_instance.credit_note_reset_to_draft(credit_note_id)
        print("The response of CreditNoteApi->credit_note_reset_to_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->credit_note_reset_to_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of the credit note to reset | 

### Return type

[**CreditNoteResetToDraft200Response**](CreditNoteResetToDraft200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed credit note |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_note_reset_to_open**
> CreditNoteResetToOpen200Response credit_note_reset_to_open(credit_note_id)

Reset status to open

Resets the status \"Open\" (`\"status\": \"200\"`). Linked transactions will be unlinked.<br> This is not possible if the credit note itself or one of its transactions (CheckAccountTransaction) is already enshrined.  This endpoint cannot be used to increase the status to \"Open\" (`\"status\": \"200\"`).<br> Use [CreditNote/{creditNoteId}/sendBy](#tag/CreditNote/operation/creditNoteSendBy) / [CreditNote/{creditNoteId}/sendViaEmail](#tag/CreditNote/operation/sendCreditNoteViaEMail) instead. 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.credit_note_reset_to_open200_response import CreditNoteResetToOpen200Response
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of the credit note to reset

    try:
        # Reset status to open
        api_response = api_instance.credit_note_reset_to_open(credit_note_id)
        print("The response of CreditNoteApi->credit_note_reset_to_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->credit_note_reset_to_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of the credit note to reset | 

### Return type

[**CreditNoteResetToOpen200Response**](CreditNoteResetToOpen200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed credit note |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_note_send_by**
> ModelCreditNoteResponse credit_note_send_by(credit_note_id, credit_note_send_by_request=credit_note_send_by_request)

Mark credit note as sent

Marks an credit note as sent by a chosen send type.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.credit_note_send_by_request import CreditNoteSendByRequest
from sevdesk_client.openapi_client.models.model_credit_note_response import ModelCreditNoteResponse
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of credit note to mark as sent
    credit_note_send_by_request = openapi_client.CreditNoteSendByRequest() # CreditNoteSendByRequest | Specify the send type (optional)

    try:
        # Mark credit note as sent
        api_response = api_instance.credit_note_send_by(credit_note_id, credit_note_send_by_request=credit_note_send_by_request)
        print("The response of CreditNoteApi->credit_note_send_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->credit_note_send_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of credit note to mark as sent | 
 **credit_note_send_by_request** | [**CreditNoteSendByRequest**](CreditNoteSendByRequest.md)| Specify the send type | [optional] 

### Return type

[**ModelCreditNoteResponse**](ModelCreditNoteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed credit note log entry |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecredit_note**
> DeleteCheckAccount200Response deletecredit_note(credit_note_id)

Deletes an creditNote

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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | Id of creditNote resource to delete

    try:
        # Deletes an creditNote
        api_response = api_instance.deletecredit_note(credit_note_id)
        print("The response of CreditNoteApi->deletecredit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->deletecredit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| Id of creditNote resource to delete | 

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
**200** | Successful operation - creditNote deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict - f.e occurs if the creditNote is not a draft |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_notes**
> GetCreditNotes200Response get_credit_notes(status=status, credit_note_number=credit_note_number, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)

Retrieve CreditNote

There are a multitude of parameter which can be used to filter.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_credit_notes200_response import GetCreditNotes200Response
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    status = 'status_example' # str | Status of the CreditNote (optional)
    credit_note_number = 'credit_note_number_example' # str | Retrieve all CreditNotes with this creditNote number (optional)
    start_date = 01.01.2020 # int | Retrieve all CreditNotes with a date equal or higher (optional)
    end_date = 01.01.2021 # int | Retrieve all CreditNotes with a date equal or lower (optional)
    contact_id = 56 # int | Retrieve all CreditNotes with this contact. Must be provided with contact[objectName] (optional)
    contact_object_name = 'contact_object_name_example' # str | Only required if contact[id] was provided. 'Contact' should be used as value. (optional)

    try:
        # Retrieve CreditNote
        api_response = api_instance.get_credit_notes(status=status, credit_note_number=credit_note_number, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)
        print("The response of CreditNoteApi->get_credit_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->get_credit_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Status of the CreditNote | [optional] 
 **credit_note_number** | **str**| Retrieve all CreditNotes with this creditNote number | [optional] 
 **start_date** | **int**| Retrieve all CreditNotes with a date equal or higher | [optional] 
 **end_date** | **int**| Retrieve all CreditNotes with a date equal or lower | [optional] 
 **contact_id** | **int**| Retrieve all CreditNotes with this contact. Must be provided with contact[objectName] | [optional] 
 **contact_object_name** | **str**| Only required if contact[id] was provided. &#39;Contact&#39; should be used as value. | [optional] 

### Return type

[**GetCreditNotes200Response**](GetCreditNotes200Response.md)

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

# **getcredit_note_by_id**
> GetCreditNotes200Response getcredit_note_by_id(credit_note_id)

Find creditNote by ID

Returns a single creditNote

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_credit_notes200_response import GetCreditNotes200Response
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of creditNote to return

    try:
        # Find creditNote by ID
        api_response = api_instance.getcredit_note_by_id(credit_note_id)
        print("The response of CreditNoteApi->getcredit_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->getcredit_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of creditNote to return | 

### Return type

[**GetCreditNotes200Response**](GetCreditNotes200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. creditNote was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_credit_note_by_printing**
> ModelCreditNoteSendByWithRender send_credit_note_by_printing(credit_note_id, send_type)

Send credit note by printing

Sending a credit note to end-customers is an important part of the bookkeeping process.<br> Depending on the way you want to send the credit note, you need to use different endpoints.<br> Let's start with just printing out the credit note, meaning we only need to render the pdf.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_credit_note_send_by_with_render import ModelCreditNoteSendByWithRender
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of creditNote to return
    send_type = 'PRN' # str | the type you want to print.

    try:
        # Send credit note by printing
        api_response = api_instance.send_credit_note_by_printing(credit_note_id, send_type)
        print("The response of CreditNoteApi->send_credit_note_by_printing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->send_credit_note_by_printing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of creditNote to return | 
 **send_type** | **str**| the type you want to print. | 

### Return type

[**ModelCreditNoteSendByWithRender**](ModelCreditNoteSendByWithRender.md)

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

# **send_credit_note_via_e_mail**
> SendCreditNoteViaEMail201Response send_credit_note_via_e_mail(credit_note_id, send_credit_note_via_e_mail_request=send_credit_note_via_e_mail_request)

Send credit note via email

This endpoint sends the specified credit note to a customer via email.<br>      This will automatically mark the credit note as sent.<br>      Please note, that in production an credit note is not allowed to be changed after this happened!

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.send_credit_note_via_e_mail201_response import SendCreditNoteViaEMail201Response
from sevdesk_client.openapi_client.models.send_credit_note_via_e_mail_request import SendCreditNoteViaEMailRequest
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of credit note to be sent via email
    send_credit_note_via_e_mail_request = openapi_client.SendCreditNoteViaEMailRequest() # SendCreditNoteViaEMailRequest | Mail data (optional)

    try:
        # Send credit note via email
        api_response = api_instance.send_credit_note_via_e_mail(credit_note_id, send_credit_note_via_e_mail_request=send_credit_note_via_e_mail_request)
        print("The response of CreditNoteApi->send_credit_note_via_e_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->send_credit_note_via_e_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of credit note to be sent via email | 
 **send_credit_note_via_e_mail_request** | [**SendCreditNoteViaEMailRequest**](SendCreditNoteViaEMailRequest.md)| Mail data | [optional] 

### Return type

[**SendCreditNoteViaEMail201Response**](SendCreditNoteViaEMail201Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created mail object |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatecredit_note**
> ModelCreditNoteResponse updatecredit_note(credit_note_id, model_credit_note_update=model_credit_note_update)

Update an existing creditNote

Update a creditNote

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_credit_note_response import ModelCreditNoteResponse
from sevdesk_client.openapi_client.models.model_credit_note_update import ModelCreditNoteUpdate
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
    api_instance = openapi_client.CreditNoteApi(api_client)
    credit_note_id = 56 # int | ID of creditNote to update
    model_credit_note_update = openapi_client.ModelCreditNoteUpdate() # ModelCreditNoteUpdate | Update data (optional)

    try:
        # Update an existing creditNote
        api_response = api_instance.updatecredit_note(credit_note_id, model_credit_note_update=model_credit_note_update)
        print("The response of CreditNoteApi->updatecredit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNoteApi->updatecredit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| ID of creditNote to update | 
 **model_credit_note_update** | [**ModelCreditNoteUpdate**](ModelCreditNoteUpdate.md)| Update data | [optional] 

### Return type

[**ModelCreditNoteResponse**](ModelCreditNoteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed creditNote resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

