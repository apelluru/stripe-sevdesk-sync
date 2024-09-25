# openapi_client.InvoiceApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_invoice**](InvoiceApi.md#book_invoice) | **PUT** /Invoice/{invoiceId}/bookAmount | Book an invoice
[**cancel_invoice**](InvoiceApi.md#cancel_invoice) | **POST** /Invoice/{invoiceId}/cancelInvoice | Cancel an invoice / Create cancellation invoice
[**create_invoice_by_factory**](InvoiceApi.md#create_invoice_by_factory) | **POST** /Invoice/Factory/saveInvoice | Create a new invoice
[**create_invoice_from_order**](InvoiceApi.md#create_invoice_from_order) | **POST** /Invoice/Factory/createInvoiceFromOrder | Create invoice from order
[**create_invoice_reminder**](InvoiceApi.md#create_invoice_reminder) | **POST** /Invoice/Factory/createInvoiceReminder | Create invoice reminder
[**get_invoice_by_id**](InvoiceApi.md#get_invoice_by_id) | **GET** /Invoice/{invoiceId} | Find invoice by ID
[**get_invoice_positions_by_id**](InvoiceApi.md#get_invoice_positions_by_id) | **GET** /Invoice/{invoiceId}/getPositions | Find invoice positions
[**get_invoices**](InvoiceApi.md#get_invoices) | **GET** /Invoice | Retrieve invoices
[**get_is_invoice_partially_paid**](InvoiceApi.md#get_is_invoice_partially_paid) | **GET** /Invoice/{invoiceId}/getIsPartiallyPaid | Check if an invoice is already partially paid
[**invoice_enshrine**](InvoiceApi.md#invoice_enshrine) | **PUT** /Invoice/{invoiceId}/enshrine | Enshrine
[**invoice_get_pdf**](InvoiceApi.md#invoice_get_pdf) | **GET** /Invoice/{invoiceId}/getPdf | Retrieve pdf document of an invoice
[**invoice_render**](InvoiceApi.md#invoice_render) | **POST** /Invoice/{invoiceId}/render | Render the pdf document of an invoice
[**invoice_reset_to_draft**](InvoiceApi.md#invoice_reset_to_draft) | **PUT** /Invoice/{invoiceId}/resetToDraft | Reset status to draft
[**invoice_reset_to_open**](InvoiceApi.md#invoice_reset_to_open) | **PUT** /Invoice/{invoiceId}/resetToOpen | Reset status to open
[**invoice_send_by**](InvoiceApi.md#invoice_send_by) | **PUT** /Invoice/{invoiceId}/sendBy | Mark invoice as sent
[**send_invoice_via_e_mail**](InvoiceApi.md#send_invoice_via_e_mail) | **POST** /Invoice/{invoiceId}/sendViaEmail | Send invoice via email


# **book_invoice**
> BookInvoice200Response book_invoice(invoice_id, book_invoice_request=book_invoice_request)

Book an invoice

Booking the invoice with a transaction is probably the most important part in the bookkeeping process.<br> There are several ways on correctly booking an invoice, all by using the same endpoint.<br> for more information look <a href='#tag/Invoice/How-to-book-an-invoice'>here</a>.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.book_invoice200_response import BookInvoice200Response
from sevdesk_client.openapi_client.models.book_invoice_request import BookInvoiceRequest
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to book
    book_invoice_request = openapi_client.BookInvoiceRequest() # BookInvoiceRequest | Booking data (optional)

    try:
        # Book an invoice
        api_response = api_instance.book_invoice(invoice_id, book_invoice_request=book_invoice_request)
        print("The response of InvoiceApi->book_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->book_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to book | 
 **book_invoice_request** | [**BookInvoiceRequest**](BookInvoiceRequest.md)| Booking data | [optional] 

### Return type

[**BookInvoice200Response**](BookInvoice200Response.md)

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

# **cancel_invoice**
> ModelInvoiceResponse cancel_invoice(invoice_id)

Cancel an invoice / Create cancellation invoice

This endpoint will cancel the specified invoice therefor creating a cancellation invoice.<br>       The cancellation invoice will be automatically paid and the source invoices status will change to 'cancelled'.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_invoice_response import ModelInvoiceResponse
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to be cancelled

    try:
        # Cancel an invoice / Create cancellation invoice
        api_response = api_instance.cancel_invoice(invoice_id)
        print("The response of InvoiceApi->cancel_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->cancel_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to be cancelled | 

### Return type

[**ModelInvoiceResponse**](ModelInvoiceResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns cancellation invoice |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_by_factory**
> SaveInvoiceResponse create_invoice_by_factory(save_invoice=save_invoice)

Create a new invoice

This endpoint offers you the following functionality.       <ul>          <li>Create invoices together with positions and discounts</li>          <li>Delete positions while adding new ones</li>          <li>Delete or add discounts, or both at the same time</li>          <li>Automatically fill the address of the supplied contact into the invoice address</li>       </ul>       To make your own request sample slimmer, you can omit all parameters which are not required and nullable.       However, for a valid and logical bookkeeping document, you will also need some of them to ensure that all the necessary data is in the invoice.<br><br> The list of parameters starts with the invoice array.<br> This array contains all required attributes for a complete invoice.<br> Most of the attributes are covered in the invoice attribute list, there are only two parameters standing out, namely <b>mapAll</b> and <b>objectName</b>.<br> These are just needed for our system and you always need to provide them.<br><br> The list of parameters then continues with the invoice position array.<br> With this array you have the possibility to add multiple positions at once.<br> In the example it only contains one position, again together with the parameters <b>mapAll</b> and <b>objectName</b>, however, you can add more invoice positions by extending the array.<br> So if you wanted to add another position, you would add the same list of parameters with an incremented array index of \"1\" instead of \"0\".<br><br> The list ends with the four parameters invoicePosDelete, discountSave, discountDelete and takeDefaultAddress.<br> They only play a minor role if you only want to create an invoice but we will shortly explain what they can do.<br> With invoicePosDelete you have to option to delete invoice positions as this request can also be used to update invoices.<br> With discountSave you can add discounts to your invoice.<br> With discountDelete you can delete discounts from your invoice.<br> With takeDefaultAddress you can specify that the first address of the contact you are using for the invoice is taken for the invoice address attribute automatically, so you don't need to provide the address yourself.<br> If you want to know more about these parameters, for example if you want to use this request to update invoices, feel free to contact our support.<br><br> Finally, after covering all parameters, they only important information left, is that the order of the last four attributes always needs to be kept.<br> You will also always need to provide all of them, as otherwise the request won't work properly.<br><br> <b>Warning:</b> You can not create a regular invoice with the <b>deliveryDate</b> being later than the <b>invoiceDate</b>.<br> To do that you will need to create a so called <b>Abschlagsrechnung</b> by setting the <b>invoiceType</b> parameter to <b>AR</b>.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.save_invoice import SaveInvoice
from sevdesk_client.openapi_client.models.save_invoice_response import SaveInvoiceResponse
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
    api_instance = openapi_client.InvoiceApi(api_client)
    save_invoice = openapi_client.SaveInvoice() # SaveInvoice | Creation data. Please be aware, that you need to provide at least all required parameter      of the invoice model! (optional)

    try:
        # Create a new invoice
        api_response = api_instance.create_invoice_by_factory(save_invoice=save_invoice)
        print("The response of InvoiceApi->create_invoice_by_factory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->create_invoice_by_factory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_invoice** | [**SaveInvoice**](SaveInvoice.md)| Creation data. Please be aware, that you need to provide at least all required parameter      of the invoice model! | [optional] 

### Return type

[**SaveInvoiceResponse**](SaveInvoiceResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - Returns created invoice |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_from_order**
> ModelInvoiceResponse create_invoice_from_order(model_create_invoice_from_order=model_create_invoice_from_order)

Create invoice from order

Create an invoice from an order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_create_invoice_from_order import ModelCreateInvoiceFromOrder
from sevdesk_client.openapi_client.models.model_invoice_response import ModelInvoiceResponse
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
    api_instance = openapi_client.InvoiceApi(api_client)
    model_create_invoice_from_order = openapi_client.ModelCreateInvoiceFromOrder() # ModelCreateInvoiceFromOrder | Create invoice (optional)

    try:
        # Create invoice from order
        api_response = api_instance.create_invoice_from_order(model_create_invoice_from_order=model_create_invoice_from_order)
        print("The response of InvoiceApi->create_invoice_from_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->create_invoice_from_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_create_invoice_from_order** | [**ModelCreateInvoiceFromOrder**](ModelCreateInvoiceFromOrder.md)| Create invoice | [optional] 

### Return type

[**ModelInvoiceResponse**](ModelInvoiceResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_reminder**
> ModelInvoiceResponse create_invoice_reminder(invoice_id, invoice_object_name, create_invoice_reminder_request=create_invoice_reminder_request)

Create invoice reminder

Create an reminder from an invoice

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.create_invoice_reminder_request import CreateInvoiceReminderRequest
from sevdesk_client.openapi_client.models.model_invoice_response import ModelInvoiceResponse
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | the id of the invoice
    invoice_object_name = 'Invoice' # str | Model name, which is 'Invoice'
    create_invoice_reminder_request = openapi_client.CreateInvoiceReminderRequest() # CreateInvoiceReminderRequest | Create invoice (optional)

    try:
        # Create invoice reminder
        api_response = api_instance.create_invoice_reminder(invoice_id, invoice_object_name, create_invoice_reminder_request=create_invoice_reminder_request)
        print("The response of InvoiceApi->create_invoice_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->create_invoice_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| the id of the invoice | 
 **invoice_object_name** | **str**| Model name, which is &#39;Invoice&#39; | 
 **create_invoice_reminder_request** | [**CreateInvoiceReminderRequest**](CreateInvoiceReminderRequest.md)| Create invoice | [optional] 

### Return type

[**ModelInvoiceResponse**](ModelInvoiceResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_id**
> GetInvoices200Response get_invoice_by_id(invoice_id)

Find invoice by ID

Returns a single invoice

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_invoices200_response import GetInvoices200Response
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to return

    try:
        # Find invoice by ID
        api_response = api_instance.get_invoice_by_id(invoice_id)
        print("The response of InvoiceApi->get_invoice_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->get_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to return | 

### Return type

[**GetInvoices200Response**](GetInvoices200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Invoice was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_positions_by_id**
> GetInvoicePositionsById200Response get_invoice_positions_by_id(invoice_id, limit=limit, offset=offset, embed=embed)

Find invoice positions

Returns all positions of an invoice

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_invoice_positions_by_id200_response import GetInvoicePositionsById200Response
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to return the positions
    limit = 56 # int | limits the number of entries returned (optional)
    offset = 56 # int | set the index where the returned entries start (optional)
    embed = ['embed_example'] # List[str] | Get some additional information. Embed can handle multiple values, they must be separated by comma. (optional)

    try:
        # Find invoice positions
        api_response = api_instance.get_invoice_positions_by_id(invoice_id, limit=limit, offset=offset, embed=embed)
        print("The response of InvoiceApi->get_invoice_positions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->get_invoice_positions_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to return the positions | 
 **limit** | **int**| limits the number of entries returned | [optional] 
 **offset** | **int**| set the index where the returned entries start | [optional] 
 **embed** | [**List[str]**](str.md)| Get some additional information. Embed can handle multiple values, they must be separated by comma. | [optional] 

### Return type

[**GetInvoicePositionsById200Response**](GetInvoicePositionsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Invoice was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> GetInvoices200Response get_invoices(status=status, invoice_number=invoice_number, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)

Retrieve invoices

There are a multitude of parameter which can be used to filter. A few of them are attached but       for a complete list please check out <a href='#tag/Invoice/How-to-filter-for-certain-invoices'>this</a> list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_invoices200_response import GetInvoices200Response
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
    api_instance = openapi_client.InvoiceApi(api_client)
    status = 3.4 # float | Status of the invoices (optional)
    invoice_number = 'invoice_number_example' # str | Retrieve all invoices with this invoice number (optional)
    start_date = 56 # int | Retrieve all invoices with a date equal or higher (optional)
    end_date = 56 # int | Retrieve all invoices with a date equal or lower (optional)
    contact_id = 56 # int | Retrieve all invoices with this contact. Must be provided with contact[objectName] (optional)
    contact_object_name = 'contact_object_name_example' # str | Only required if contact[id] was provided. 'Contact' should be used as value. (optional)

    try:
        # Retrieve invoices
        api_response = api_instance.get_invoices(status=status, invoice_number=invoice_number, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)
        print("The response of InvoiceApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **float**| Status of the invoices | [optional] 
 **invoice_number** | **str**| Retrieve all invoices with this invoice number | [optional] 
 **start_date** | **int**| Retrieve all invoices with a date equal or higher | [optional] 
 **end_date** | **int**| Retrieve all invoices with a date equal or lower | [optional] 
 **contact_id** | **int**| Retrieve all invoices with this contact. Must be provided with contact[objectName] | [optional] 
 **contact_object_name** | **str**| Only required if contact[id] was provided. &#39;Contact&#39; should be used as value. | [optional] 

### Return type

[**GetInvoices200Response**](GetInvoices200Response.md)

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

# **get_is_invoice_partially_paid**
> ContactCustomerNumberAvailabilityCheck200Response get_is_invoice_partially_paid(invoice_id)

Check if an invoice is already partially paid

Returns 'true' if the given invoice is partially paid - 'false' if it is not.      Invoices which are completely paid are regarded as not partially paid.

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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to return

    try:
        # Check if an invoice is already partially paid
        api_response = api_instance.get_is_invoice_partially_paid(invoice_id)
        print("The response of InvoiceApi->get_is_invoice_partially_paid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->get_is_invoice_partially_paid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to return | 

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
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_enshrine**
> CheckAccountTransactionEnshrine200Response invoice_enshrine(invoice_id)

Enshrine

Sets the current date and time as a value for the property `enshrined`.<br> This operation is only possible if the status is \"Open\" (`\"status\": \"200\"`) or higher.  Enshrined invoices cannot be changed. This operation cannot be undone. 

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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of the invoice to enshrine

    try:
        # Enshrine
        api_response = api_instance.invoice_enshrine(invoice_id)
        print("The response of InvoiceApi->invoice_enshrine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->invoice_enshrine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of the invoice to enshrine | 

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

# **invoice_get_pdf**
> InvoiceGetPdf200Response invoice_get_pdf(invoice_id, download=download, prevent_send_by=prevent_send_by)

Retrieve pdf document of an invoice

Retrieves the pdf document of an invoice with additional metadata.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.invoice_get_pdf200_response import InvoiceGetPdf200Response
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice from which you want the pdf
    download = true # bool | If u want to download the pdf of the invoice. (optional)
    prevent_send_by = true # bool | Defines if u want to send the invoice. (optional)

    try:
        # Retrieve pdf document of an invoice
        api_response = api_instance.invoice_get_pdf(invoice_id, download=download, prevent_send_by=prevent_send_by)
        print("The response of InvoiceApi->invoice_get_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->invoice_get_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice from which you want the pdf | 
 **download** | **bool**| If u want to download the pdf of the invoice. | [optional] 
 **prevent_send_by** | **bool**| Defines if u want to send the invoice. | [optional] 

### Return type

[**InvoiceGetPdf200Response**](InvoiceGetPdf200Response.md)

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

# **invoice_render**
> InvoiceRender201Response invoice_render(invoice_id, invoice_render_request=invoice_render_request)

Render the pdf document of an invoice

Using this endpoint you can render the pdf document of an invoice.<br>       Use cases for this are the retrieval of the pdf location or the forceful re-render of a already sent invoice.<br>       Please be aware that changing an invoice after it has been sent to a customer is not an allowed bookkeeping process.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.invoice_render201_response import InvoiceRender201Response
from sevdesk_client.openapi_client.models.invoice_render_request import InvoiceRenderRequest
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to render
    invoice_render_request = openapi_client.InvoiceRenderRequest() # InvoiceRenderRequest | Define if the document should be forcefully re-rendered. (optional)

    try:
        # Render the pdf document of an invoice
        api_response = api_instance.invoice_render(invoice_id, invoice_render_request=invoice_render_request)
        print("The response of InvoiceApi->invoice_render:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->invoice_render: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to render | 
 **invoice_render_request** | [**InvoiceRenderRequest**](InvoiceRenderRequest.md)| Define if the document should be forcefully re-rendered. | [optional] 

### Return type

[**InvoiceRender201Response**](InvoiceRender201Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns meta-data about pdf. |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_reset_to_draft**
> InvoiceResetToDraft200Response invoice_reset_to_draft(invoice_id)

Reset status to draft

Resets the status to \"Draft\" (`\"status\": \"100\"`).<br> This is only possible if the invoice has the status \"Open\" (`\"status\": \"200\"`).<br> If it has a higher status use [Invoice/{invoiceId}/resetToOpen](#tag/Invoice/operation/invoiceResetToOpen) first.  This endpoint cannot be used for recurring invoices (`\"invoiceType\": \"WKR\"`).<br> Use [Invoice/Factory/saveInvoice](#tag/Invoice/operation/createInvoiceByFactory) instead. 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.invoice_reset_to_draft200_response import InvoiceResetToDraft200Response
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of the invoice to reset

    try:
        # Reset status to draft
        api_response = api_instance.invoice_reset_to_draft(invoice_id)
        print("The response of InvoiceApi->invoice_reset_to_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->invoice_reset_to_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of the invoice to reset | 

### Return type

[**InvoiceResetToDraft200Response**](InvoiceResetToDraft200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed invoice |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_reset_to_open**
> InvoiceResetToOpen200Response invoice_reset_to_open(invoice_id)

Reset status to open

Resets the status \"Open\" (`\"status\": \"200\"`). Linked transactions will be unlinked.<br> This is not possible if the invoice itself or one of its transactions (CheckAccountTransaction) is already enshrined.  This endpoint cannot be used to increase the status to \"Open\" (`\"status\": \"200\"`).<br> Use [Invoice/{invoiceId}/sendBy](#tag/Invoice/operation/invoiceSendBy) / [Invoice/{invoiceId}/sendViaEmail](#tag/Invoice/operation/sendInvoiceViaEMail) instead.  This endpoint cannot be used for recurring invoices (`\"invoiceType\": \"WKR\"`). Use [Invoice/Factory/saveInvoice](#tag/Invoice/operation/createInvoiceByFactory) instead. 

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.invoice_reset_to_open200_response import InvoiceResetToOpen200Response
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of the invoice to reset

    try:
        # Reset status to open
        api_response = api_instance.invoice_reset_to_open(invoice_id)
        print("The response of InvoiceApi->invoice_reset_to_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->invoice_reset_to_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of the invoice to reset | 

### Return type

[**InvoiceResetToOpen200Response**](InvoiceResetToOpen200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed invoice |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**422** | Validation error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_send_by**
> ModelInvoiceResponse invoice_send_by(invoice_id, invoice_send_by_request=invoice_send_by_request)

Mark invoice as sent

Marks an invoice as sent by a chosen send type.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.invoice_send_by_request import InvoiceSendByRequest
from sevdesk_client.openapi_client.models.model_invoice_response import ModelInvoiceResponse
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to mark as sent
    invoice_send_by_request = openapi_client.InvoiceSendByRequest() # InvoiceSendByRequest | Specify the send type (optional)

    try:
        # Mark invoice as sent
        api_response = api_instance.invoice_send_by(invoice_id, invoice_send_by_request=invoice_send_by_request)
        print("The response of InvoiceApi->invoice_send_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->invoice_send_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to mark as sent | 
 **invoice_send_by_request** | [**InvoiceSendByRequest**](InvoiceSendByRequest.md)| Specify the send type | [optional] 

### Return type

[**ModelInvoiceResponse**](ModelInvoiceResponse.md)

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

# **send_invoice_via_e_mail**
> ModelEmail send_invoice_via_e_mail(invoice_id, send_invoice_via_e_mail_request=send_invoice_via_e_mail_request)

Send invoice via email

This endpoint sends the specified invoice to a customer via email.<br>      This will automatically mark the invoice as sent.<br>      Please note, that in production an invoice is not allowed to be changed after this happened!

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_email import ModelEmail
from sevdesk_client.openapi_client.models.send_invoice_via_e_mail_request import SendInvoiceViaEMailRequest
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
    api_instance = openapi_client.InvoiceApi(api_client)
    invoice_id = 56 # int | ID of invoice to be sent via email
    send_invoice_via_e_mail_request = openapi_client.SendInvoiceViaEMailRequest() # SendInvoiceViaEMailRequest | Mail data (optional)

    try:
        # Send invoice via email
        api_response = api_instance.send_invoice_via_e_mail(invoice_id, send_invoice_via_e_mail_request=send_invoice_via_e_mail_request)
        print("The response of InvoiceApi->send_invoice_via_e_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->send_invoice_via_e_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| ID of invoice to be sent via email | 
 **send_invoice_via_e_mail_request** | [**SendInvoiceViaEMailRequest**](SendInvoiceViaEMailRequest.md)| Mail data | [optional] 

### Return type

[**ModelEmail**](ModelEmail.md)

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

