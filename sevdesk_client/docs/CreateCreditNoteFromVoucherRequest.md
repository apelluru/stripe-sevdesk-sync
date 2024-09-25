# CreateCreditNoteFromVoucherRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher** | [**CreateCreditNoteFromVoucherRequestVoucher**](CreateCreditNoteFromVoucherRequestVoucher.md) |  | 

## Example

```python
from sevdesk_client.openapi_client.models.create_credit_note_from_voucher_request import CreateCreditNoteFromVoucherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteFromVoucherRequest from a JSON string
create_credit_note_from_voucher_request_instance = CreateCreditNoteFromVoucherRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteFromVoucherRequest.to_json())

# convert the object into a dict
create_credit_note_from_voucher_request_dict = create_credit_note_from_voucher_request_instance.to_dict()
# create an instance of CreateCreditNoteFromVoucherRequest from a dict
create_credit_note_from_voucher_request_from_dict = CreateCreditNoteFromVoucherRequest.from_dict(create_credit_note_from_voucher_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


