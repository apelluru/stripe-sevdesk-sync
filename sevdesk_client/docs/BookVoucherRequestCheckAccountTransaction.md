# BookVoucherRequestCheckAccountTransaction

The check account transaction on which should be booked.<br>      The transaction will be linked to the voucher.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the check account transaction on which should be booked. | 
**object_name** | **str** | Internal object name which is &#39;CheckAccountTransaction&#39;. | 

## Example

```python
from sevdesk_client.openapi_client.models.book_voucher_request_check_account_transaction import BookVoucherRequestCheckAccountTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BookVoucherRequestCheckAccountTransaction from a JSON string
book_voucher_request_check_account_transaction_instance = BookVoucherRequestCheckAccountTransaction.from_json(json)
# print the JSON string representation of the object
print(BookVoucherRequestCheckAccountTransaction.to_json())

# convert the object into a dict
book_voucher_request_check_account_transaction_dict = book_voucher_request_check_account_transaction_instance.to_dict()
# create an instance of BookVoucherRequestCheckAccountTransaction from a dict
book_voucher_request_check_account_transaction_from_dict = BookVoucherRequestCheckAccountTransaction.from_dict(book_voucher_request_check_account_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


