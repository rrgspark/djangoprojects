from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import RegisterForm
from .models import Usuario



def loginForm(request):
    return render(request,'loginForm.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request,'main.html')
    else:
        messages.info(request,'Usuario o Contraseña inválidos')
        return render(request,'loginForm.html',{'username':username})


def logout(request):
    auth.logout(request)
    return redirect('main')


def registrar(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RegisterForm()
    return render(request,'registrar.html', {'form':form})