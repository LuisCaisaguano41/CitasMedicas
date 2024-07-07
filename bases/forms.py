from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms
from django.forms.widgets import PasswordInput

class UsuarioCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioCreationForm,self).__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        fields = ("email",)

class UsuarioChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm,self).__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        fields = '__all__'

from django import forms
from django.forms import PasswordInput
from .models import Usuario  # Asegúrate de importar tu modelo Usuario correctamente

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)

    class Meta:
        model = Usuario  # Asegúrate de que 'Usuario' sea el nombre correcto de tu modelo
        fields = ['email', 'first_name', 'last_name', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
