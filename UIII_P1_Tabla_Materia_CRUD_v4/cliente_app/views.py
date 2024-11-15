from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarCliente.html",{"misclientes":losclientes})

def registrarCliente(request):
    id_cliente=request.POST["txtid_cliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    telefono=request.POST["numtelefono"]
    fecha_nac=request.POST["numfecha_nac"]
    direccion=request.POST["txtdireccion"]
    cp=request.POST["numcp"]
    curp=request.POST["txtcurp"]


    guardarcliente=Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        apellido=apellido,
        telefono=telefono,
        fecha_nac=fecha_nac,
        direccion=direccion,
        cp=cp,
        curp=curp

    )# GUARDA EL REGISTRO

    return redirect ("/")

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarcliente.html",{"misclientes": cliente})

def editarCliente(request):
    id_codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]
    materia=Cliente.objects.get(id_codigo=id_codigo)
    materia.nombre=nombre
    materia.credito=credito
    materia.save() #guarda registro actualizado
    return redirect("/")

def borrarCliente(request,id_codigo):
    materia=Cliente.objects.get(id_codigo=id_codigo)
    materia.delete() # borra el registro
    return redirect ("/")