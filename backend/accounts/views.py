from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model() 

def page(request):
    return render(request, 'pages/page.html')

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})