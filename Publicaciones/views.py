from django.shortcuts import render

def home(request):
    return render(request,"publicaciones/home.html",{})

def mostrar_productos(request):
    return render(request,"publicaciones/mostrar_productos.html",{}) 

def crear_productos(request):
    return render(request,"publicaciones/crear_productos.html",{} )

