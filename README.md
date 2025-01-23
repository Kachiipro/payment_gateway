# Payment Gateway Integration with Paystack


# Overview
This project integrates Paystack payment gateway with Django, allowing users to make payments online.

# Features
- Initiate payment with Paystack
- Retrieve payment status from Paystack
- Store payment records in the database

# Requirements
- Python 3.x
- Django 3.x
- Paystack account with API keys

# Installation
1. Clone the repository: git clone https://github.com/your-username/payment-gateway.git
2. Install dependencies: pip install -r requirements.txt
3. Configure Paystack API keys in settings.py
4. Run migrations: python manage.py migrate
5. Start the server: python manage.py runserver

# API Endpoints
- POST /api/v1/payments/: Initiate payment
- GET /api/v1/payments/{payment_id}/: Retrieve payment status



