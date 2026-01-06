import requests
import uuid

# Official MTN Endpoints
BASE_URL = "https://sandbox.momodeveloper.mtn.com" # Change to production later
SUBSCRIPTION_KEY = "YOUR_MTN_SUBSCRIPTION_KEY"

def create_invoice(amount, msisdn, external_id):
    url = f"{BASE_URL}/collection/v1_0/invoice"
    headers = {
        "X-Reference-Id": str(uuid.uuid4()),
        "X-Target-Environment": "sandbox",
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "amount": amount,
        "currency": "ZAR",
        "externalId": external_id,
        "payer": {"partyIdType": "MSISDN", "partyId": msisdn},
        "payerMessage": "Humbu Nexus Service Payment",
        "payeeNote": "Thank you for supporting Humbu Enterprise"
    }
    # This sends the request to MTN to generate the invoice
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code

print("Humbu Invoice Logic Initialized.")
