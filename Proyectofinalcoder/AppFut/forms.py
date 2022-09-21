<<<<<<< HEAD

from django import forms


class FormularioSocio(forms.Form):

    nombre=forms.CharField(max_length=60)
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
    fecha=forms.DateField()
    hora=forms.CharField(max_length=50)
    cancha=forms.IntegerField()
=======

from django import forms


class FormularioSocio(forms.Form):

    nombre=forms.CharField(max_length=60)
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
    fecha=forms.DateField()
    hora=forms.CharField(max_length=50)
    cancha=forms.IntegerField()
>>>>>>> 6c7c70af40c3c22414841de5994e786f2607dce8
    esSocio=forms.BooleanField()