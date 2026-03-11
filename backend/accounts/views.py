import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm

@csrf_exempt
def api_register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        form = RegisterForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Регистрация прошла успешно'}, status=201)
    else:
        return JsonResponse({'errors': form.error}, status=400)

    return JsonResponse({'error': 'Разрешены только POST запросы'}, status=405)