from django.shortcuts import render
from Publicaciones.forms import FormularioCreacionProducto,FormDeBusqueda
from Publicaciones.models import Producto

def home(request):
    return render(request,"publicaciones/home.html",{})

def mostrar_productos(request):
    formulario = FormDeBusqueda(request.GET)
    if formulario.is_valid():
        filtrar_nombre = formulario.cleaned_data["nombre"]
        productos=Producto.objects.filter(nombre__icontains=filtrar_nombre)
    else:
        productos =Producto.objects.all() 
    return render(request,"publicaciones/mostrar_productos.html",{"productos":productos, "formulario":formulario}) 

def crear_productos(request):
    if request.method =="POST":
        formulario = FormularioCreacionProducto(request.POST)
        if formulario.is_valid():
            producto = Producto(
                nombre=formulario.cleaned_data["nombre"],
                precio=formulario.cleaned_data["precio"],
                descripcion= formulario.cleaned_data["descripcion"])
            producto.save()
    formulario = FormularioCreacionProducto()
    return render(request,"publicaciones/crear_productos.html",{"formulario" : formulario} )

def detalle_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto) 
    return render(request,"publicaciones/detalle_producto.html",{"producto":producto})