<<<<<<< HEAD
from django.urls import path
from AppFut import views

urlpatterns = [
    
    path("Inicio", views.inicio, name= "Inicio"),
    path("socio/", views.socio, name = "Socio"),
    path("proveedores/", views.proveedores, name = "Proveedores"),
    path("buscarproveedor/", views.busquedaProve, name = "BuscarProve"),
    path("buscar/",views.buscar),
    path("turno/", views.turno, name = "Turno"),
=======
from django.urls import path
from AppFut import views

urlpatterns = [
    
    path("Inicio", views.inicio, name= "Inicio"),
    path("socio/", views.socio, name = "Socio"),
    path("proveedores/", views.proveedores, name = "Proveedores"),
    path("buscarproveedor/", views.busquedaProve, name = "BuscarProve"),
    path("buscar/",views.buscar),
    path("turno/", views.turno, name = "Turno"),
>>>>>>> 6c7c70af40c3c22414841de5994e786f2607dce8
]