from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellidos', required=False)
    email = forms.EmailField(label='Correo Electrónico', required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )