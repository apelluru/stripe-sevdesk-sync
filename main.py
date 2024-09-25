# Configure your Stripe API key

from stripe_integration.stripe_api import StripeAPI
from sevdesk_client.openapi_client.api.basics_api import BasicsApi
from sevdesk_client.openapi_client.api_client import ApiClient
from sevdesk_client.openapi_client.configuration import Configuration
import urllib3
import logging
from sevdesk_client.openapi_client.models.bookkeeping_system_version200_response import BookkeepingSystemVersion200Response


# Your API keys
STRIPE_API_KEY = "Your secret key from stripe"
SEVDESK_API_KEY = "SevDesk api key"


# Basic logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Set urllib3 logging level
logging.getLogger("urllib3").setLevel(logging.DEBUG)  # or WARNING, INFO, etc.
logging.getLogger("urllib3.connectionpool").setLevel(logging.DEBUG)

def test_sevdesk_api_version():
    # Configure SevDesk API client
    configuration = Configuration(
        host="https://my.sevdesk.de/api/v1",
        api_key={'api_key': SEVDESK_API_KEY},  # Dictionary format
        debug=True
    )

    api_client = ApiClient(configuration)
    basics_api = BasicsApi(api_client)

    try:
        # Fetch the SevDesk API version
        bookkeeping_system_version200_response = basics_api.bookkeeping_system_version()  # Replace with correct method if needed

        print("The response of BasicsApi->bookkeeping_system_version:\n")
        print(bookkeeping_system_version200_response)

        print(f"SevDesk API Version: {bookkeeping_system_version200_response.to_json()}")
    except Exception as e:
        print(f"Error fetching SevDesk API version: {e}")


def test_stripe_transactions(stripe_api):
    # Fetch transactions from Stripe
    transactions = stripe_api.retrieve_balance_transactions(limit=10)

    if transactions:
        num_transactions = len(transactions)
        print(f"Number of Stripe transactions retrieved: {num_transactions}")
    else:
        print("No transactions found.")


if __name__ == "__main__":
    # Initialize the Stripe API
    stripe_api = StripeAPI(api_key=STRIPE_API_KEY)

    # Test Stripe transactions
    test_stripe_transactions(stripe_api)

    # Test SevDesk API version
    test_sevdesk_api_version()

