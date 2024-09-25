# CreateCreditNoteFromVoucherRequestVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the existing Voucher | 
**object_name** | **str** | The objectName must be &#39;Voucher&#39; | 

## Example

```python
from sevdesk_client.openapi_client.models.create_credit_note_from_voucher_request_voucher import CreateCreditNoteFromVoucherRequestVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteFromVoucherRequestVoucher from a JSON string
create_credit_note_from_voucher_request_voucher_instance = CreateCreditNoteFromVoucherRequestVoucher.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteFromVoucherRequestVoucher.to_json())

# convert the object into a dict
create_credit_note_from_voucher_request_voucher_dict = create_credit_note_from_voucher_request_voucher_instance.to_dict()
# create an instance of CreateCreditNoteFromVoucherRequestVoucher from a dict
create_credit_note_from_voucher_request_voucher_from_dict = CreateCreditNoteFromVoucherRequestVoucher.from_dict(create_credit_note_from_voucher_request_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


