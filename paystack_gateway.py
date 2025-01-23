import requests
from django.conf import settings

class PaystackGateway:
    def __init__(self):
        self.api_key = settings.PAYSTACK_SECRET_KEY
        self.public_key = settings.PAYSTACK_PUBLIC_KEY
        self.api_url = 'https://api.paystack.co'
        

    def initiate_payment(self, customer_name, customer_email, amount):
        payload = {
            'email': customer_email,
            'amount': amount * 100,  # Convert to kobo
            'currency': 'NGN'
        }
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(f'{self.api_url}/transaction/initialize', json=payload, headers=headers)
        data = response.json()
        payment_id = data ['data']['reference']
        authorization_url = data['data']['authorization_url']
        return payment_id, authorization_url
    
    def retrieve_payment_status(self, payment_id):
        url = f"{self.api_url}/transaction/verify/{payment_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["status"]  # e.g., "success", "failed", or "pending"
        else:
            raise Exception(f"Failed to retrieve payment status: {response.text}")

