from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()

            # você pode salvar o nível em um modelo separado se quiser

            return redirect('/accounts/login/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("password")

        user = authenticate(request, username=username, password=senha)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("/accounts/login/")
