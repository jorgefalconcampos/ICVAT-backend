import os
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login, logout as do_logout
from django.shortcuts import redirect
from django.contrib import messages
from . forms import RegisterForm

from users.models import User
from django.http import HttpResponseRedirect, HttpResponse



TEMPLATES_DIR =  settings.TEMPLATES_DIR #importing



def index(request):
    """Main entry point of the app"""
    return HttpResponse("Hello")




def login(request):
    """User login"""
    
    template = TEMPLATES_DIR / 'user' / 'login.html'


    if request.user.is_authenticated:
        return redirect ('index')  

    usr = request.POST.get('username')
    pwd  = request.POST.get('password')

    if request.method == 'POST':
        if usr or pwd:
            user_auth = authenticate(username=usr, password=pwd)

            if user_auth:
                do_login(request, user_auth)
                print(f"\nSession created for the user: {usr}\n")
                messages.success(request, f"Bienvenido {usr}")

                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET['next'])

                return redirect('index')
            else:
                print(f"No autenticado: {usr}")
                messages.error(request, "Usuario o contraseña inválidos")
        else:
            print("no autenticado (campos vacíos)")
    return render(request, template, {})


def logout(request):
    """User logout"""
    do_logout(request)
    messages.success(request, 'Logged out')
    return redirect('login')

def register(request):
    """Register a new user"""

    if request.user.is_authenticated:
        return redirect ('index')

    template = TEMPLATES / 'user' / 'register.html'
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()

        if user:
            do_login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
        else:
            messages.error(request, 'Error creando el usuario')

    context = {
        'form': form
    }
    return render(request, template, context)

def page_not_found_view(request, exception):
    template = TEMPLATES_DIR / 'http_states' / '404.html'

    return render(request, template, status=404)