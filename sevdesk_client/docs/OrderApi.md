# openapi_client.OrderApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract_note_from_order**](OrderApi.md#create_contract_note_from_order) | **POST** /Order/Factory/createContractNoteFromOrder | Create contract note from order
[**create_order**](OrderApi.md#create_order) | **POST** /Order/Factory/saveOrder | Create a new order
[**create_packing_list_from_order**](OrderApi.md#create_packing_list_from_order) | **POST** /Order/Factory/createPackingListFromOrder | Create packing list from order
[**delete_order**](OrderApi.md#delete_order) | **DELETE** /Order/{orderId} | Deletes an order
[**get_discounts**](OrderApi.md#get_discounts) | **GET** /Order/{orderId}/getDiscounts | Find order discounts
[**get_order_by_id**](OrderApi.md#get_order_by_id) | **GET** /Order/{orderId} | Find order by ID
[**get_order_positions_by_id**](OrderApi.md#get_order_positions_by_id) | **GET** /Order/{orderId}/getPositions | Find order positions
[**get_orders**](OrderApi.md#get_orders) | **GET** /Order | Retrieve orders
[**get_related_objects**](OrderApi.md#get_related_objects) | **GET** /Order/{orderId}/getRelatedObjects | Find related objects
[**order_get_pdf**](OrderApi.md#order_get_pdf) | **GET** /Order/{orderId}/getPdf | Retrieve pdf document of an order
[**order_send_by**](OrderApi.md#order_send_by) | **PUT** /Order/{orderId}/sendBy | Mark order as sent
[**sendorder_via_e_mail**](OrderApi.md#sendorder_via_e_mail) | **POST** /Order/{orderId}/sendViaEmail | Send order via email
[**update_order**](OrderApi.md#update_order) | **PUT** /Order/{orderId} | Update an existing order


# **create_contract_note_from_order**
> ModelOrderResponse create_contract_note_from_order(order_id, order_object_name, model_create_packing_list_from_order=model_create_packing_list_from_order)

Create contract note from order

Create contract note from order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_create_packing_list_from_order import ModelCreatePackingListFromOrder
from sevdesk_client.openapi_client.models.model_order_response import ModelOrderResponse
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | the id of the order
    order_object_name = 'Order' # str | Model name, which is 'Order'
    model_create_packing_list_from_order = openapi_client.ModelCreatePackingListFromOrder() # ModelCreatePackingListFromOrder | Create contract note (optional)

    try:
        # Create contract note from order
        api_response = api_instance.create_contract_note_from_order(order_id, order_object_name, model_create_packing_list_from_order=model_create_packing_list_from_order)
        print("The response of OrderApi->create_contract_note_from_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_contract_note_from_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| the id of the order | 
 **order_object_name** | **str**| Model name, which is &#39;Order&#39; | 
 **model_create_packing_list_from_order** | [**ModelCreatePackingListFromOrder**](ModelCreatePackingListFromOrder.md)| Create contract note | [optional] 

### Return type

[**ModelOrderResponse**](ModelOrderResponse.md)

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

# **create_order**
> SaveOrderResponse create_order(save_order=save_order)

Create a new order

Creates an order to which positions can be added later.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.save_order import SaveOrder
from sevdesk_client.openapi_client.models.save_order_response import SaveOrderResponse
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
    api_instance = openapi_client.OrderApi(api_client)
    save_order = openapi_client.SaveOrder() # SaveOrder | Creation data. Please be aware, that you need to provide at least all required parameter      of the order model! (optional)

    try:
        # Create a new order
        api_response = api_instance.create_order(save_order=save_order)
        print("The response of OrderApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_order** | [**SaveOrder**](SaveOrder.md)| Creation data. Please be aware, that you need to provide at least all required parameter      of the order model! | [optional] 

### Return type

[**SaveOrderResponse**](SaveOrderResponse.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_packing_list_from_order**
> ModelOrderResponse create_packing_list_from_order(order_id, order_object_name, model_create_packing_list_from_order=model_create_packing_list_from_order)

Create packing list from order

Create packing list from order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_create_packing_list_from_order import ModelCreatePackingListFromOrder
from sevdesk_client.openapi_client.models.model_order_response import ModelOrderResponse
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | the id of the order
    order_object_name = 'Order' # str | Model name, which is 'Order'
    model_create_packing_list_from_order = openapi_client.ModelCreatePackingListFromOrder() # ModelCreatePackingListFromOrder | Create packing list (optional)

    try:
        # Create packing list from order
        api_response = api_instance.create_packing_list_from_order(order_id, order_object_name, model_create_packing_list_from_order=model_create_packing_list_from_order)
        print("The response of OrderApi->create_packing_list_from_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_packing_list_from_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| the id of the order | 
 **order_object_name** | **str**| Model name, which is &#39;Order&#39; | 
 **model_create_packing_list_from_order** | [**ModelCreatePackingListFromOrder**](ModelCreatePackingListFromOrder.md)| Create packing list | [optional] 

### Return type

[**ModelOrderResponse**](ModelOrderResponse.md)

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

# **delete_order**
> DeleteCheckAccount200Response delete_order(order_id)

Deletes an order

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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | Id of order resource to delete

    try:
        # Deletes an order
        api_response = api_instance.delete_order(order_id)
        print("The response of OrderApi->delete_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->delete_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Id of order resource to delete | 

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
**200** | Successful operation - Order deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict - f.e occurs if the order is not a draft |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discounts**
> GetDiscounts200Response get_discounts(order_id, limit=limit, offset=offset, embed=embed)

Find order discounts

Returns all discounts of an order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_discounts200_response import GetDiscounts200Response
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order to return the positions
    limit = 56 # int | limits the number of entries returned (optional)
    offset = 56 # int | set the index where the returned entries start (optional)
    embed = ['embed_example'] # List[str] | Get some additional information. Embed can handle multiple values, they must be separated by comma. (optional)

    try:
        # Find order discounts
        api_response = api_instance.get_discounts(order_id, limit=limit, offset=offset, embed=embed)
        print("The response of OrderApi->get_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_discounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to return the positions | 
 **limit** | **int**| limits the number of entries returned | [optional] 
 **offset** | **int**| set the index where the returned entries start | [optional] 
 **embed** | [**List[str]**](str.md)| Get some additional information. Embed can handle multiple values, they must be separated by comma. | [optional] 

### Return type

[**GetDiscounts200Response**](GetDiscounts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. order was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> GetOrders200Response get_order_by_id(order_id)

Find order by ID

Returns a single order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_orders200_response import GetOrders200Response
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order to return

    try:
        # Find order by ID
        api_response = api_instance.get_order_by_id(order_id)
        print("The response of OrderApi->get_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to return | 

### Return type

[**GetOrders200Response**](GetOrders200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Order was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_positions_by_id**
> GetOrderPositionsById200Response get_order_positions_by_id(order_id, limit=limit, offset=offset, embed=embed)

Find order positions

Returns all positions of an order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_order_positions_by_id200_response import GetOrderPositionsById200Response
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order to return the positions
    limit = 56 # int | limits the number of entries returned (optional)
    offset = 56 # int | set the index where the returned entries start (optional)
    embed = ['embed_example'] # List[str] | Get some additional information. Embed can handle multiple values, they must be separated by comma. (optional)

    try:
        # Find order positions
        api_response = api_instance.get_order_positions_by_id(order_id, limit=limit, offset=offset, embed=embed)
        print("The response of OrderApi->get_order_positions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_order_positions_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to return the positions | 
 **limit** | **int**| limits the number of entries returned | [optional] 
 **offset** | **int**| set the index where the returned entries start | [optional] 
 **embed** | [**List[str]**](str.md)| Get some additional information. Embed can handle multiple values, they must be separated by comma. | [optional] 

### Return type

[**GetOrderPositionsById200Response**](GetOrderPositionsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. order was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> GetOrders200Response get_orders(status=status, order_number=order_number, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)

Retrieve orders

There are a multitude of parameter which can be used to filter. A few of them are attached but      for a complete list please check out <a href='#tag/Order/How-to-filter-for-certain-orders'>this</a> list

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_orders200_response import GetOrders200Response
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
    api_instance = openapi_client.OrderApi(api_client)
    status = 56 # int | Status of the order (optional)
    order_number = 'order_number_example' # str | Retrieve all orders with this order number (optional)
    start_date = 56 # int | Retrieve all orders with a date equal or higher (optional)
    end_date = 56 # int | Retrieve all orders with a date equal or lower (optional)
    contact_id = 56 # int | Retrieve all orders with this contact. Must be provided with contact[objectName] (optional)
    contact_object_name = 'contact_object_name_example' # str | Only required if contact[id] was provided. 'Contact' should be used as value. (optional)

    try:
        # Retrieve orders
        api_response = api_instance.get_orders(status=status, order_number=order_number, start_date=start_date, end_date=end_date, contact_id=contact_id, contact_object_name=contact_object_name)
        print("The response of OrderApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**| Status of the order | [optional] 
 **order_number** | **str**| Retrieve all orders with this order number | [optional] 
 **start_date** | **int**| Retrieve all orders with a date equal or higher | [optional] 
 **end_date** | **int**| Retrieve all orders with a date equal or lower | [optional] 
 **contact_id** | **int**| Retrieve all orders with this contact. Must be provided with contact[objectName] | [optional] 
 **contact_object_name** | **str**| Only required if contact[id] was provided. &#39;Contact&#39; should be used as value. | [optional] 

### Return type

[**GetOrders200Response**](GetOrders200Response.md)

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

# **get_related_objects**
> GetOrderPositionsById200Response get_related_objects(order_id, include_itself=include_itself, sort_by_type=sort_by_type, embed=embed)

Find related objects

Get related objects of a specified order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.get_order_positions_by_id200_response import GetOrderPositionsById200Response
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order to return the positions
    include_itself = True # bool | Define if the related objects include the order itself (optional)
    sort_by_type = True # bool | Define if you want the related objects sorted by type (optional)
    embed = ['embed_example'] # List[str] | Get some additional information. Embed can handle multiple values, they must be separated by comma. (optional)

    try:
        # Find related objects
        api_response = api_instance.get_related_objects(order_id, include_itself=include_itself, sort_by_type=sort_by_type, embed=embed)
        print("The response of OrderApi->get_related_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_related_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to return the positions | 
 **include_itself** | **bool**| Define if the related objects include the order itself | [optional] 
 **sort_by_type** | **bool**| Define if you want the related objects sorted by type | [optional] 
 **embed** | [**List[str]**](str.md)| Get some additional information. Embed can handle multiple values, they must be separated by comma. | [optional] 

### Return type

[**GetOrderPositionsById200Response**](GetOrderPositionsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. order was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_pdf**
> OrderGetPdf200Response order_get_pdf(order_id, download=download, prevent_send_by=prevent_send_by)

Retrieve pdf document of an order

Retrieves the pdf document of an order with additional metadata and commit the order.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.order_get_pdf200_response import OrderGetPdf200Response
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order from which you want the pdf
    download = true # bool | If u want to download the pdf of the order. (optional)
    prevent_send_by = true # bool | Defines if u want to send the order. (optional)

    try:
        # Retrieve pdf document of an order
        api_response = api_instance.order_get_pdf(order_id, download=download, prevent_send_by=prevent_send_by)
        print("The response of OrderApi->order_get_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_get_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order from which you want the pdf | 
 **download** | **bool**| If u want to download the pdf of the order. | [optional] 
 **prevent_send_by** | **bool**| Defines if u want to send the order. | [optional] 

### Return type

[**OrderGetPdf200Response**](OrderGetPdf200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A pdf file |  -  |
**400** | Bad request. order was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_send_by**
> ModelOrderResponse order_send_by(order_id, order_send_by_request=order_send_by_request)

Mark order as sent

Marks an order as sent by a chosen send type.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_order_response import ModelOrderResponse
from sevdesk_client.openapi_client.models.order_send_by_request import OrderSendByRequest
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order to mark as sent
    order_send_by_request = openapi_client.OrderSendByRequest() # OrderSendByRequest | Specify the send type (optional)

    try:
        # Mark order as sent
        api_response = api_instance.order_send_by(order_id, order_send_by_request=order_send_by_request)
        print("The response of OrderApi->order_send_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_send_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to mark as sent | 
 **order_send_by_request** | [**OrderSendByRequest**](OrderSendByRequest.md)| Specify the send type | [optional] 

### Return type

[**ModelOrderResponse**](ModelOrderResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed order log entry |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendorder_via_e_mail**
> SendorderViaEMail201Response sendorder_via_e_mail(order_id, send_invoice_via_e_mail_request=send_invoice_via_e_mail_request)

Send order via email

This endpoint sends the specified order to a customer via email.<br>      This will automatically mark the order as sent.<br>      Please note, that in production an order is not allowed to be changed after this happened!

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.send_invoice_via_e_mail_request import SendInvoiceViaEMailRequest
from sevdesk_client.openapi_client.models.sendorder_via_e_mail201_response import SendorderViaEMail201Response
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order to be sent via email
    send_invoice_via_e_mail_request = openapi_client.SendInvoiceViaEMailRequest() # SendInvoiceViaEMailRequest | Mail data (optional)

    try:
        # Send order via email
        api_response = api_instance.sendorder_via_e_mail(order_id, send_invoice_via_e_mail_request=send_invoice_via_e_mail_request)
        print("The response of OrderApi->sendorder_via_e_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->sendorder_via_e_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to be sent via email | 
 **send_invoice_via_e_mail_request** | [**SendInvoiceViaEMailRequest**](SendInvoiceViaEMailRequest.md)| Mail data | [optional] 

### Return type

[**SendorderViaEMail201Response**](SendorderViaEMail201Response.md)

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

# **update_order**
> ModelOrderResponse update_order(order_id, model_order_update=model_order_update)

Update an existing order

Update an order

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_order_response import ModelOrderResponse
from sevdesk_client.openapi_client.models.model_order_update import ModelOrderUpdate
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
    api_instance = openapi_client.OrderApi(api_client)
    order_id = 56 # int | ID of order to update
    model_order_update = openapi_client.ModelOrderUpdate() # ModelOrderUpdate | Update data (optional)

    try:
        # Update an existing order
        api_response = api_instance.update_order(order_id, model_order_update=model_order_update)
        print("The response of OrderApi->update_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->update_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID of order to update | 
 **model_order_update** | [**ModelOrderUpdate**](ModelOrderUpdate.md)| Update data | [optional] 

### Return type

[**ModelOrderResponse**](ModelOrderResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed order resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

