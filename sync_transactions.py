from datetime import datetime

from sevdesk_client.openapi_client import ModelCheckAccountTransactionCheckAccount, \
    ModelCheckAccountTransaction
from sevdesk_client.openapi_client.api.check_account_transaction_api import CheckAccountTransactionApi
from sevdesk_client.openapi_client.api_client import ApiClient
from sevdesk_client.openapi_client.configuration import Configuration
from stripe_integration.stripe_api import StripeAPI

# Initialize API clients
stripe_api_key = "your secret key"
sevdesk_api_key = "api key"
sevdesk_checkaccount_number = check account number

stripe_client = StripeAPI(stripe_api_key)


def sync_transactions(start_date=None, end_date=None, limit=10):
    """
    Fetch transactions from Stripe within a date range and create them in SevDesk.

    :param start_date: Start date for filtering transactions (Unix timestamp or datetime)
    :param end_date: End date for filtering transactions (Unix timestamp or datetime)
    :param limit: Limit on the number of transactions to retrieve from Stripe
    """
    # Retrieve balance transactions from Stripe with date range
    stripe_transactions = stripe_client.retrieve_balance_transactions(limit=limit, start_date=start_date,
                                                                      end_date=end_date)

    if not stripe_transactions:
        print("No transactions retrieved from Stripe.")
        return

    configuration = Configuration(
        host="https://my.sevdesk.de/api/v1",
        api_key={'api_key': sevdesk_api_key},  # Dictionary format
        debug=True
    )
    api_client = ApiClient(configuration)
    savedesk_api_instance = CheckAccountTransactionApi(api_client)

    # Loop over transactions and create them in SevDesk
    for transaction in stripe_transactions:

        if transaction['type'] == "stripe_fee":
            payee_payer_name = "Stripe"
        elif transaction['type'] == "payout":
            payee_payer_name = "Bankkonto"
        else:
            payee_payer_name = "Customer"

        print(f"Processing transaction {transaction['id']}... {transaction['description']}")

        # Prepare transaction data for SevDesk API
        model_check_account_transaction = ModelCheckAccountTransaction(
            value_date=transaction['created'],  # Assuming Stripe created date is the booking date
            entry_date=transaction['created'],
            amount=transaction['amount'] / 100,  # Stripe amount is in cents, converting to standard units
            paymt_purpose=f"{transaction['description']}; Stripe id: {transaction['id']}",
            payee_payer_name=payee_payer_name,  # Can map the Stripe source to this field
            check_account=ModelCheckAccountTransactionCheckAccount(id=sevdesk_checkaccount_number,
                                                                   object_name="CheckAccount"),
            # Set your check account ID here
            status=100  # Created status
        )
        # ModelCheckAccountTransaction | Creation data. Please be aware, that you need to provide at least all
        # required parameter of the CheckAccountTransaction model! (optional)

        # Create a new transaction
        api_response = savedesk_api_instance.create_transaction(
            model_check_account_transaction=model_check_account_transaction)

        # Handle any fee details as separate transactions
        fee_details = stripe_client.extract_fee_details(transaction)
        if fee_details:
            for fee in fee_details:
                print(f"Processing transaction {fee['id']}... {fee['description']}")
                model_check_account_fee_transaction = ModelCheckAccountTransaction(
                    value_date=transaction['created'],  # Assuming Stripe created date is the booking date
                    entry_date=transaction['created'],
                    amount=-(fee['amount'] / 100),  # Convert cents to euros and make it negative
                    paymt_purpose=f"Fee, Stripe processing fees for {transaction['id']}",
                    payee_payer_name="Stripe",
                    check_account=ModelCheckAccountTransactionCheckAccount(id=sevdesk_checkaccount_number,
                                                                           object_name="CheckAccount"),
                    # Same check account
                    status=100  # Created status
                )

                model_check_account_transaction_response = savedesk_api_instance.create_transaction(
                    model_check_account_transaction=model_check_account_fee_transaction)


if __name__ == "__main__":
    # Define a date range (for example, last 30 days)
    start_date = datetime(2024, 9, 1)
    end_date = datetime(2024, 9, 24)

    # Sync transactions within the date range
    sync_transactions(start_date=start_date, end_date=end_date, limit=100)
