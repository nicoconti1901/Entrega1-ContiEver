<<<<<<< HEAD

from django.db import models

class Turno(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    hora=models.CharField(max_length=30)
    cancha=models.IntegerField()
    esSocio=models.BooleanField()

class Socio(models.Model):
    nombre=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    localidad=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

class Proveedores(models.Model):
    nombre=models.CharField(max_length=60)
    producto=models.CharField(max_length=60)
    email=models.EmailField()
=======

from django.db import models

class Turno(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    hora=models.CharField(max_length=30)
    cancha=models.IntegerField()
    esSocio=models.BooleanField()

class Socio(models.Model):
    nombre=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    localidad=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

class Proveedores(models.Model):
    nombre=models.CharField(max_length=60)
    producto=models.CharField(max_length=60)
    email=models.EmailField()
>>>>>>> 6c7c70af40c3c22414841de5994e786f2607dce8
    telefono=models.IntegerField()