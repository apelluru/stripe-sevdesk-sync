# BookVoucherRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount which should be booked. Can also be a partial amount. | 
**var_date** | **datetime** | The booking date. Most likely the current date. | 
**type** | **str** | Define a type for the booking.&lt;br&gt;      The following type abbreviations are available (abbreviation &lt;-&gt; meaning).&lt;br&gt;      &lt;ul&gt;  &lt;li&gt;FULL_PAYMENT &lt;-&gt; Normal booking&lt;/li&gt;&lt;li&gt;N &lt;-&gt; Partial booking (historically used for normal booking)&lt;/li&gt;      &lt;li&gt;CB &lt;-&gt; Reduced amount due to discount (skonto)&lt;/li&gt;      &lt;li&gt;CF &lt;-&gt; Reduced/Higher amount due to currency fluctuations (deprecated)&lt;/li&gt;      &lt;li&gt;O &lt;-&gt; Reduced/Higher amount due to other reasons&lt;/li&gt;      &lt;li&gt;OF &lt;-&gt; Higher amount due to reminder charges&lt;/li&gt;      &lt;li&gt;MTC &lt;-&gt; Reduced amount due to the monetary traffic costs&lt;/li&gt;      &lt;/ul&gt; | 
**check_account** | [**BookCreditNoteRequestCheckAccount**](BookCreditNoteRequestCheckAccount.md) |  | 
**check_account_transaction** | [**BookVoucherRequestCheckAccountTransaction**](BookVoucherRequestCheckAccountTransaction.md) |  | [optional] 
**create_feed** | **bool** | Determines if a feed is created for the booking process. | [optional] 

## Example

```python
from sevdesk_client.openapi_client.models.book_voucher_request import BookVoucherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BookVoucherRequest from a JSON string
book_voucher_request_instance = BookVoucherRequest.from_json(json)
# print the JSON string representation of the object
print(BookVoucherRequest.to_json())

# convert the object into a dict
book_voucher_request_dict = book_voucher_request_instance.to_dict()
# create an instance of BookVoucherRequest from a dict
book_voucher_request_from_dict = BookVoucherRequest.from_dict(book_voucher_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


