# usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class UsuarioCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Requerido. 30 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.')
    email = forms.EmailField(max_length=200, help_text='Requerido. Informe un email válido.')
    nombre_completo = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('username', 'nombre_completo', 'email', 'password1', 'password2', )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario ya existe.")
        return username

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', password):
            raise ValidationError('La contraseña debe tener al menos 8 caracteres, al menos una letra mayúscula y al menos un número.')
        return password
