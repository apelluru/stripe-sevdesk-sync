import requests

class SevDeskAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://my.sevdesk.de/api/v1"  # Adjust to your SevDesk API URL

    def create_transaction(self, transaction_data):
        """
        Upload a transaction to SevDesk.
        :param transaction_data: Data of the transaction to upload
        :return: Response from SevDesk API
        """
        url = f"{self.base_url}/accounting_transaction"  # Replace with actual endpoint
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=transaction_data, headers=headers)
            if response.status_code == 200:
                print(f"Transaction {transaction_data['id']} uploaded successfully to SevDesk.")
            else:
                print(f"Failed to upload transaction: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error posting transaction to SevDesk: {e}")
