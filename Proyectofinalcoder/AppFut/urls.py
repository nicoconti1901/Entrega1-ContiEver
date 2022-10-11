
from re import template
from django.urls import path
from AppFut.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", inicio, name= "Inicio"),
    path("about/", about, name ="About"),
    path("proveedores/", proveedores, name = "Proveedores"),
    path("buscarproveedor/", busquedaProve, name = "BuscarProve"),
    path("buscar/",buscar),
    path("turno/", turno, name = "Turno"),
    path("listadeprove/", verProve, name = "Listadeprove"),
    path("eliminarprove/<proveNombre>", eliminarprove, name = "EliminarProveedor"),
    path("editarprove/<proveNombre>", editarProve, name = "EditarProveedor"),
    path("socio/", SocioLista.as_view(), name = "LeerSocio"),
    path("socio/nuevo", SocioCrear.as_view(), name = "CrearSocio"),
    path("socio/<int:pk>", SocioDetalle.as_view(), name = "DetalleSocio"),
    path("socio/editar/<int:pk>", SocioEditar.as_view(), name = "EditarSocio"),
    path("socio/borrar/<int:pk>", SocioBorrar.as_view(), name = "BorrarSocio"),
    path("login/", iniciar_sesion, name = "Login"),
    path("registro/", registro, name = "Registro"),
    path("logout/", LogoutView.as_view(template_name= "AppFut/inicio.html"), name = "Logout"),
    path("editarusuario", editarUsuario, name = "EditarUsuario"),
]