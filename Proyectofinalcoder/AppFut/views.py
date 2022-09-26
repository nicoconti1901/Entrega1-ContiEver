
from django.shortcuts import render
from AppFut.forms import *
from AppFut.models import *
from django.http import HttpResponse

def inicio(request):
    
    return render(request, "AppFut/inicio.html")

def socio(request):
    if request.method == "POST":

        formulario1 = FormularioSocio(request.POST)

        if formulario1.is_valid(): 

            info = formulario1.cleaned_data

            socioF = Socio(nombre=info["nombre"], apellido=info["apellido"], direccion=info["direccion"], localidad=info["localidad"], telefono=info["telefono"], email=info["email"])
        
            socioF.save()
        
            return render(request, "AppFut/inicio.html")
    else:
        formulario1= FormularioSocio()
    return render(request, "AppFut/socio.html", {"socio": formulario1})

def proveedores(request):
    if request.method == "POST":

        formulario2 = FormularioProve(request.POST)

        if formulario2.is_valid(): 

            info = formulario2.cleaned_data

            proveF = Proveedores(nombre=info["nombre"], producto=info["producto"], email=info["email"], telefono=info["telefono"])
        
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
    listadeprove = Proveedores.objets.all()
    return render(request, "AppFut/proveedores.html", {"listadeprove": listadeprove})