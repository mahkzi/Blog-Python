from django.shortcuts import render

def home(request):
    return render(request,"publicaciones/home.html",{})
def blog(request):
    return render(request,"publicaciones/blog.html",{})

