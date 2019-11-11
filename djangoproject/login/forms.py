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


    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            User._default_manager.get(username=username)
            raise forms.ValidationError( 
                'El usuario ya existe.',
                code='username_exists',
            )
        except User.DoesNotExist:
            return username


    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User._default_manager.get(email=email)
            raise forms.ValidationError( 
                'El correo electrónico ya está en uso.',
                code='email_exists',
            )
        except User.DoesNotExist:
            return email


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'La contraseña no coincide.',
                code='password_mismatch',
            )
        return password2