import stripe

class StripeAPI:
    def __init__(self, api_key):
        # Initialize with the Stripe API key
        stripe.api_key = api_key

    def retrieve_transactions(self, limit=10):
        """
        Fetch recent transactions from Stripe.
        :param limit: Number of transactions to retrieve
        :return: List of Stripe transactions
        """
        try:
            transactions = stripe.Charge.list(limit=limit)
            return transactions['data']
        except Exception as e:
            print(f"Error retrieving transactions from Stripe: {e}")
            return None
