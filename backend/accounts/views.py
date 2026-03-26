import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def api_register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        form = RegisterForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Регистрация прошла успешно'}, status=201)
    else:
        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Разрешены только POST запросы'}, status=405)
    # print('hello world')

@csrf_exempt
def api_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            try:
                user_obj = User.objects.get(email=email)
                username = user_obj.username
            except User.DoesNotExist:
                return JsonResponse({"error": "Пользователь с таким email не найден."}, status=400)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                setattr(request, '_dont_enforce_csrf_checks', True)
                
                login(request, user)
                
                return JsonResponse({
                    "message": "Успешный вход!", 
                    "user": {"username": user.username, "email": user.email}
                }, status=200)
            else:
                return JsonResponse({"error": "Неверный пароль."}, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({"error": "Неверный формат данных."}, status=400)
            
    return JsonResponse({"error": "Разрешены только POST-запросы."}, status=405)