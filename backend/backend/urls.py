from django.contrib import admin
from django.urls import path, include
from accounts.views import api_register, api_login

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # СНАЧАЛА ставим ваши кастомные API-пути
    path('accounts/register/', api_register, name='register'),
    path('accounts/login/', api_login, name='login'), # Исправлено: добавлено 'accounts/'
    
    # ПОТОМ подключаем встроенные пути Django (если они вообще вам нужны)
    # Django проверит верхние пути первыми, и ваш 'accounts/login/' сработает вместо дефолтного
    path('accounts/', include('django.contrib.auth.urls')), 
]
