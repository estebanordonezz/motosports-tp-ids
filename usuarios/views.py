from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'usuarios/registro.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, 'Iniciaste sesión correctamente.')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form})


def logout_usuario(request):
    logout(request)
    messages.success(request, 'Cerraste sesión correctamente.')
    return redirect('index')