import requests
import base64
import json

CLIENT_ID = "AWZrV9uQ24x_djk35_BCVQAPGLPdhzImCBCCpvA-swwlLMqXa-JKfdR2-yWjRJrSVqvbLHo_FHwNOkjN"
CLIENT_SECRET = "EOkl2J3RB70ejKnwfSJH_D-4R9AM51cM-nv3NG_5TgDjMq_ZGHJud2Q0-Qm6uF86JyBXohq5Ea3tufQb"
BASE_URL = "https://api-m.sandbox.paypal.com"

def get_token():
    credentials = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    r = requests.post(
        f"{BASE_URL}/v1/oauth2/token",
        headers={"Authorization": f"Basic {credentials}"},
        data={"grant_type": "client_credentials"},
    )
    return r.json()["access_token"]

def create_product(token):
    r = requests.post(
        f"{BASE_URL}/v1/catalogs/products",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={
            "name": "RedSoft",
            "description": "Steam automation software",
            "type": "SERVICE",
            "category": "SOFTWARE",
        },
    )
    product = r.json()
    print(f"Product ID: {product['id']}")
    return product["id"]

def create_plan(token, product_id, name, price):
    r = requests.post(
        f"{BASE_URL}/v1/billing/plans",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={
            "product_id": product_id,
            "name": f"RedSoft {name}",
            "status": "ACTIVE",
            "billing_cycles": [
                {
                    "frequency": {"interval_unit": "MONTH", "interval_count": 1},
                    "tenure_type": "REGULAR",
                    "sequence": 1,
                    "total_cycles": 0,
                    "pricing_scheme": {
                        "fixed_price": {"value": price, "currency_code": "USD"}
                    },
                }
            ],
            "payment_preferences": {
                "auto_bill_outstanding": True,
                "setup_fee": {"value": "0", "currency_code": "USD"},
                "payment_failure_threshold": 3,
            },
        },
    )
    plan = r.json()
    print(f"{name} Plan ID: {plan['id']}")
    return plan["id"]

token = get_token()
product_id = create_product(token)
create_plan(token, product_id, "Pro", "9.99")
create_plan(token, product_id, "Ultimate", "19.99")