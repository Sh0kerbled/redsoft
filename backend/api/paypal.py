import requests
import base64
from django.conf import settings

BASE_URLS = {
    "sandbox": "https://api-m.sandbox.paypal.com",
    "live": "https://api-m.paypal.com",
}

def _base_url():
    return BASE_URLS.get(settings.PAYPAL_MODE, BASE_URLS["sandbox"])

def get_access_token():
    credentials = base64.b64encode(
        f"{settings.PAYPAL_CLIENT_ID}:{settings.PAYPAL_CLIENT_SECRET}".encode()
    ).decode()
    r = requests.post(
        f"{_base_url()}/v1/oauth2/token",
        headers={"Authorization": f"Basic {credentials}"},
        data={"grant_type": "client_credentials"},
    )
    r.raise_for_status()
    return r.json()["access_token"]

def create_subscription(plan_id, user_email, return_url, cancel_url):
    token = get_access_token()
    r = requests.post(
        f"{_base_url()}/v1/billing/subscriptions",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "plan_id": plan_id,
            "subscriber": {"email_address": user_email},
            "application_context": {
                "return_url": return_url,
                "cancel_url": cancel_url,
                "user_action": "SUBSCRIBE_NOW",
                "shipping_preference": "NO_SHIPPING",
            },
        },
    )
    r.raise_for_status()
    return r.json()

def get_subscription(subscription_id):
    token = get_access_token()
    r = requests.get(
        f"{_base_url()}/v1/billing/subscriptions/{subscription_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    r.raise_for_status()
    return r.json()

def cancel_subscription(subscription_id, reason="User cancelled"):
    token = get_access_token()
    r = requests.post(
        f"{_base_url()}/v1/billing/subscriptions/{subscription_id}/cancel",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={"reason": reason},
    )
    return r.status_code == 204