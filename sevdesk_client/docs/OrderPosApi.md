# openapi_client.OrderPosApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order_pos**](OrderPosApi.md#delete_order_pos) | **DELETE** /OrderPos/{orderPosId} | Deletes an order Position
[**get_order_position_by_id**](OrderPosApi.md#get_order_position_by_id) | **GET** /OrderPos/{orderPosId} | Find order position by ID
[**get_order_positions**](OrderPosApi.md#get_order_positions) | **GET** /OrderPos | Retrieve order positions
[**update_order_position**](OrderPosApi.md#update_order_position) | **PUT** /OrderPos/{orderPosId} | Update an existing order position


# **delete_order_pos**
> DeleteCheckAccount200Response delete_order_pos(order_pos_id)

Deletes an order Position

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
    api_instance = openapi_client.OrderPosApi(api_client)
    order_pos_id = 56 # int | Id of order position resource to delete

    try:
        # Deletes an order Position
        api_response = api_instance.delete_order_pos(order_pos_id)
        print("The response of OrderPosApi->delete_order_pos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderPosApi->delete_order_pos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_pos_id** | **int**| Id of order position resource to delete | 

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
**200** | Successful operation - order position deleted |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**409** | Conflict - f.e occurs if the order is not a draft |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_position_by_id**
> GetOrderPositionsById200Response get_order_position_by_id(order_pos_id)

Find order position by ID

Returns a single order position

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
    api_instance = openapi_client.OrderPosApi(api_client)
    order_pos_id = 56 # int | ID of order position to return

    try:
        # Find order position by ID
        api_response = api_instance.get_order_position_by_id(order_pos_id)
        print("The response of OrderPosApi->get_order_position_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderPosApi->get_order_position_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_pos_id** | **int**| ID of order position to return | 

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
**400** | Bad request. Order position was not found |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_positions**
> GetOrderPositionsById200Response get_order_positions(order_id=order_id, order_object_name=order_object_name)

Retrieve order positions

Retrieve all order positions depending on the filters defined in the query.

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
    api_instance = openapi_client.OrderPosApi(api_client)
    order_id = 56 # int | Retrieve all order positions belonging to this order. Must be provided with voucher[objectName] (optional)
    order_object_name = 'order_object_name_example' # str | Only required if order[id] was provided. 'Order' should be used as value. (optional)

    try:
        # Retrieve order positions
        api_response = api_instance.get_order_positions(order_id=order_id, order_object_name=order_object_name)
        print("The response of OrderPosApi->get_order_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderPosApi->get_order_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Retrieve all order positions belonging to this order. Must be provided with voucher[objectName] | [optional] 
 **order_object_name** | **str**| Only required if order[id] was provided. &#39;Order&#39; should be used as value. | [optional] 

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
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_position**
> ModelOrderPosResponse update_order_position(order_pos_id, model_order_pos_update=model_order_pos_update)

Update an existing order position

Update an order position

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.model_order_pos_response import ModelOrderPosResponse
from sevdesk_client.openapi_client.models.model_order_pos_update import ModelOrderPosUpdate
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
    api_instance = openapi_client.OrderPosApi(api_client)
    order_pos_id = 56 # int | ID of order position to update
    model_order_pos_update = openapi_client.ModelOrderPosUpdate() # ModelOrderPosUpdate | Update data (optional)

    try:
        # Update an existing order position
        api_response = api_instance.update_order_position(order_pos_id, model_order_pos_update=model_order_pos_update)
        print("The response of OrderPosApi->update_order_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderPosApi->update_order_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_pos_id** | **int**| ID of order position to update | 
 **model_order_pos_update** | [**ModelOrderPosUpdate**](ModelOrderPosUpdate.md)| Update data | [optional] 

### Return type

[**ModelOrderPosResponse**](ModelOrderPosResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - Returns changed order position resource |  -  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

