from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Usuario

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label=('Username'),
        max_length=150,
        help_text=(None),        
        # error_messages={'unique': ("A user with that username already exists.")},
        #widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label=('Contraseña'),
        max_length=150,
        help_text=(None), 
        widget=forms.PasswordInput(),
        # error_messages={'unique': ("A user with that username already exists.")},
        #widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label=('Confirme contraseña'),
        max_length=150,
        help_text=(None), 
        widget=forms.PasswordInput(),       
        # error_messages={'unique': ("A user with that username already exists.")},
        #widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    Nombre = forms.CharField(max_length=140, required=True)
    Apellido = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    
    class Meta:
        model = User
        fields = (
            'username',
            'Nombre',
            'Apellido',
            'email',
            'password1',
            'password2',
            )