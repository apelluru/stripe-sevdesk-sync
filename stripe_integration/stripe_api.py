from datetime import datetime
import stripe


class StripeAPI:
    def __init__(self, api_key):
        # Initialize with the Stripe API key
        stripe.api_key = api_key

    def retrieve_balance_transactions(self, limit=10, start_date=None, end_date=None):
        """
        Fetch balance transactions from Stripe within a specified date range.

        :param limit: Number of transactions to retrieve
        :param start_date: Unix timestamp or datetime for filtering transactions (optional)
        :param end_date: Unix timestamp or datetime for filtering transactions (optional)
        :return: List of balance transactions
        """
        try:
            params = {"limit": limit}

            # Add date range to params if provided
            if start_date:
                params["created[gte]"] = int(start_date.timestamp()) if hasattr(start_date, 'timestamp') else start_date
            if end_date:
                params["created[lte]"] = int(end_date.timestamp()) if hasattr(end_date, 'timestamp') else end_date

            transactions = stripe.BalanceTransaction.list(**params)
            return transactions['data']
        except Exception as e:
            print(f"Error retrieving transactions from Stripe: {e}")
            return None

    def extract_fee_details(self, transaction):
        """
        Extract fee details from a Stripe transaction if available.
        Append '_fee' to the transaction ID for each fee entry.

        :param transaction: A Stripe balance transaction
        :return: Fee details as a list of dictionaries, or None if no fees exist
        """
        fee_entries = []
        if 'fee_details' in transaction and transaction['fee_details']:
            for fee in transaction['fee_details']:
                fee_entries.append({
                    "id": f"{transaction['id']}_fee",  # Append '_fee' to the transaction ID
                    "description": fee['description'],
                    "amount": fee['amount'],
                    "currency": fee['currency'],
                    "type": fee['type'],
                    "transaction_id": transaction['id'],  # Reference to the original transaction ID
                    "created": transaction['created'],  # Use the same created date as the original transaction
                })
        return fee_entries if fee_entries else None

