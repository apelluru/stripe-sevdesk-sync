# openapi_client.CreditNotePosApi

All URIs are relative to *https://my.sevdesk.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcredit_note_positions**](CreditNotePosApi.md#getcredit_note_positions) | **GET** /CreditNotePos | Retrieve creditNote positions


# **getcredit_note_positions**
> GetcreditNotePositions200Response getcredit_note_positions(credit_note_id=credit_note_id, credit_note_object_name=credit_note_object_name)

Retrieve creditNote positions

Retrieve all creditNote positions depending on the filters defined in the query.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from sevdesk_client.openapi_client.models.getcredit_note_positions200_response import GetcreditNotePositions200Response
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
    api_instance = openapi_client.CreditNotePosApi(api_client)
    credit_note_id = 56 # int | Retrieve all creditNote positions belonging to this creditNote. Must be provided with creditNote[objectName] (optional)
    credit_note_object_name = 'credit_note_object_name_example' # str | Only required if creditNote[id] was provided. 'creditNote' should be used as value. (optional)

    try:
        # Retrieve creditNote positions
        api_response = api_instance.getcredit_note_positions(credit_note_id=credit_note_id, credit_note_object_name=credit_note_object_name)
        print("The response of CreditNotePosApi->getcredit_note_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotePosApi->getcredit_note_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | **int**| Retrieve all creditNote positions belonging to this creditNote. Must be provided with creditNote[objectName] | [optional] 
 **credit_note_object_name** | **str**| Only required if creditNote[id] was provided. &#39;creditNote&#39; should be used as value. | [optional] 

### Return type

[**GetcreditNotePositions200Response**](GetcreditNotePositions200Response.md)

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

