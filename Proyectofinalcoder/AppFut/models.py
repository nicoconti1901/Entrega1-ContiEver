
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Turno(models.Model):
    
    def __str__(self):
        return f"Turno {self.nombre} {self.apellido}"
    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha=models.DateField()
    hora=models.CharField(max_length=30)
    cancha=models.IntegerField()
    esSocio=models.BooleanField()

class Socio(models.Model):
    def __str__(self):
        return f"Socio {self.nombre} {self.apellido}"
    
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=60)
    localidad=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

class Proveedores(models.Model):
    def __str__(self):
        return f"Proveedor {self.nombre}"
    nombre=models.CharField(max_length=60)
    producto=models.CharField(max_length=60)
    email=models.EmailField()
    telefono=models.IntegerField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)



    