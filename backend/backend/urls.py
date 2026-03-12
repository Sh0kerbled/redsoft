from django.contrib import admin
from django.urls import path, include
from accounts.views import api_register, api_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', api_register, name='register'),
    path('accounts/login/', api_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')), 
]
