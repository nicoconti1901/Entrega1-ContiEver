
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioSocio(forms.Form):

    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    direccion=forms.CharField(max_length=60)
    localidad=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    email=forms.EmailField()

class FormularioProve(forms.Form):
    nombre=forms.CharField(max_length=60)
    producto=forms.CharField(max_length=60)
    email=forms.EmailField()
    telefono=forms.IntegerField()
    
class FormularioTurno(forms.Form):

    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    fecha=forms.DateField()
    hora=forms.CharField(max_length=50)
    cancha=forms.IntegerField()
    esSocio=forms.BooleanField()

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label= "Ingrese su email")
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label= "Ingrese su nombre")
    last_name = forms.CharField(label= "Ingrese su apellido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","first_name", "last_name"]

class FormularioEditarUsuario(UserCreationForm):
    email = forms.EmailField(label= "Ingrese su email")
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label= "Ingrese su nombre")
    last_name = forms.CharField(label= "Ingrese su apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]





    

    