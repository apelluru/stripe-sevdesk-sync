# Stripe to SevDesk Sync

This project syncs transactions from Stripe to SevDesk using their respective APIs. It uses a modular approach with separate modules for pulling data from Stripe and pushing it to SevDesk.

## Project Structure

- `pull-from-stripe/`: Contains logic to interact with the Stripe API.
- `push-to-sevdesk/`: Contains logic to interact with the SevDesk API.
- `main.py`: Orchestrates the data flow from Stripe to SevDesk.

## Requirements

- Python 3.x
- A Stripe account and API key
- A SevDesk account and API key

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:apelluru/stripe-sevdesk-sync.git
   cd stripe-sevdesk-sync
   ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac  
    #source venv\Scripts\activate # On Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Update the Stripe and SevDesk API keys in `main.py`

```bash
   STRIPE_API_KEY = "your_stripe_secret_key"
   SEVDESK_API_KEY = "your_sevdesk_api_key"
```