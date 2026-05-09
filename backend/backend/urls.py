from django.contrib import admin
from django.urls import path, include
from accounts.views import api_register, api_login
from api.views import create_subscription, activate_subscription, cancel_subscription, my_subscription, paypal_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', api_register, name='register'),
    path('accounts/login/', api_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('payments/create-subscription/', create_subscription),
    path('payments/activate-subscription/', activate_subscription),
    path('payments/cancel-subscription/', cancel_subscription),
    path('payments/my-subscription/', my_subscription),
    path('payments/webhook/', paypal_webhook),
]
