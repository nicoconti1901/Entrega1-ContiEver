
from ast import Delete
from urllib import request
from django.shortcuts import render
from AppFut.forms import *
from AppFut.models import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




def inicio(request):
    """avatares = Avatar.objects.filter(user=request.user.id)
    contexto = {"url: avatares[0].imagen.url"}"""
    return render(request, "AppFut/inicio.html")

def about(request):
    
    return render(request, "AppFut/about.html")
    
"""def socio(request):
    if request.method == "POST":

        formulario1 = FormularioSocio(request.POST)

        if formulario1.is_valid(): 

            info = formulario1.cleaned_data

            socioF = Socio(nombre=info["nombre"], apellido=info["apellido"], direccion=info["direccion"], localidad=info["localidad"], telefono=info["telefono"], email=info["email"])
        
            socioF.save()
        
            return render(request, "AppFut/inicio.html")
    else:
        formulario1= FormularioSocio()
    return render(request, "AppFut/socio.html", {"socio": formulario1})"""

def proveedores(request):
    if request.method == "POST":

        formulario2 = FormularioProve(request.POST, request.FILES)

        if formulario2.is_valid(): 

            info = formulario2.cleaned_data

            proveF = Proveedores(nombre=info["nombre"], producto=info["producto"], email=info["email"], telefono=info["telefono"], imagenPerfil=info['imagenPerfil'])
        
            proveF.save()
        
            return render(request, "AppFut/inicio.html")
    else:
        formulario2= FormularioProve()
    return render(request, "AppFut/proveedores.html", {"proveedores": formulario2})

def busquedaProve(request):
    return render(request, "AppFut/busquedaProve.html")

def buscar(request):

    if request.GET["producto"]:

        busqueda = request.GET["producto"]
        proveedores = Proveedores.objects.filter(producto__iexact=busqueda)

        return render(request, "AppFut/resultadosProve.html", {"proveedores":proveedores, "busqueda":busqueda})
    else:
        mensaje = "Usted no ingreso datos"
        return HttpResponse(mensaje)

@login_required
def turno(request):
    if request.method == "POST":

        formulario3 = FormularioTurno(request.POST)

        if formulario3.is_valid(): 

            info = formulario3.cleaned_data

            turnoF = Turno(nombre=info["nombre"], apellido=info["apellido"], fecha=info["fecha"], hora=info["hora"], cancha=info["cancha"], esSocio=info["esSocio"])
        
            turnoF.save()
        
            return render(request, "AppFut/inicio.html")
    else:
        formulario3= FormularioTurno()
    return render(request, "AppFut/turno.html", {"turno": formulario3})

def verProve(request):
    listadeprove = Proveedores.objects.all()
    return render(request, "AppFut/listadeproveedores.html", {"listadeprove": listadeprove})

def eliminarprove(request, proveNombre):
    proveedor = Proveedores.objects.get(nombre=proveNombre)
    proveedor.delete() 

    listadeprove = Proveedores.objects.all()
    return render(request, "AppFut/listadeproveedores.html", {"listadeprove": listadeprove})

def editarProve(request, proveNombre):
    proveedor = Proveedores.objects.get(nombre=proveNombre)
    if request.method == "POST":

        formulario2 = FormularioProve(request.POST)

        if formulario2.is_valid(): 

            info = formulario2.cleaned_data

            proveedor.nombre = info["nombre"]
            proveedor.producto = info["producto"]
            proveedor.email = info["email"]
            proveedor.telefono = info["telefono"]

            proveedor.save()
        
            return render(request, "AppFut/inicio.html")
    else:
        formulario2= FormularioProve(initial={"nombre": proveedor.nombre, "producto": proveedor.producto, "email": proveedor.email, "telefono": proveedor.telefono})
    return render(request, "AppFut/editarprove.html", {"proveedores": formulario2, "proveNombre": proveNombre})

class SocioLista(ListView):
    model = Socio

class SocioCrear(CreateView):
    model = Socio
    success_url= "/AppFut/socio/nuevo"
    fields = ["nombre", "apellido", "direccion", "localidad", "telefono", "email"]

class SocioDetalle(DetailView):
    model = Socio
    

class SocioEditar(UpdateView):
    model = Socio
    success_url= "/AppFut/socio/nuevo"
    fields = ["nombre", "apellido", "direccion", "localidad", "telefono", "email"]

class SocioBorrar(DeleteView):
    model = Socio
    success_url= "/AppFut/socio"

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid(): 

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:
                login(request, user)
            return render(request, "AppFut/inicio.html", {"mensaje": f"Hola {user}"})
        else:
            return render(request, "AppFut/inicio.html", {"mensaje": f"Datos incorrectos!!"})
    else:
        form = AuthenticationForm()
    return render(request, "AppFut/login.html", {"formu3":form})

def registro(request):
    if request.method == "POST":
        """formu = UserCreationForm(request.POST)"""
        formu = FormularioRegistro(request.POST)
        if formu.is_valid(): 
            nombreUsuario = formu.cleaned_data["username"]
            formu.save()

            return render(request, "AppFut/inicio.html", {"mensaje": f"Usuario {nombreUsuario} creado"})
    
    else:
        
        """formu = UserCreationForm()"""
        formu = FormularioRegistro()
    
    return render(request, "AppFut/registro.html", {"formu4":formu})

def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":

        miformulario = FormularioEditarUsuario(request.POST)

        if miformulario.is_valid(): 

            info = miformulario.cleaned_data

            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
           

            usuario.save()
        
            return render(request, "AppFut/inicio.html")
    else:
        miformulario= FormularioEditarUsuario(initial={"email": usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name})
    return render(request, "AppFut/editarUsuarios.html", {"miForm": miformulario, "usuario": usuario})