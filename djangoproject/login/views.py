from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Usuario

# Create your views here.
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
    return redirect('loginForm')

def registrar(request):
    if request.method == 'POST':
        nombre = request.POST['first_name']
        apellido=  request.POST['last_name']
        username = request.POST['username']
        email  =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'El usuario ya está registrado')
                return render(request,'registrar.html',{'nombre':nombre,'apellido':apellido, 'username':username, 'email':email, 'password1':password1, 'password2':password2})
            elif User.objects.filter(email=email).exists():
                messages.info(request,'El correo ya está registrado')
                return render(request,'registrar.html',{'nombre':nombre,'apellido':apellido, 'username':username, 'email':email, 'password1':password1, 'password2':password2})
            else:
                usuario = User.objects.create_user(
                    first_name = nombre,
                    last_name = apellido,
                    username = username,
                    email = email,
                    password = password1
                )
                usuario.save()
        else:
            messages.info(request,'La contraseña no coincide')
            return render(request,'registrar.html',{'nombre':nombre,'apellido':apellido, 'username':username, 'email':email, 'password1':password1, 'password2':password2})
            #return redirect('registrar')
        return redirect('loginForm')
    else:
        return render(request,'registrar.html')