from django.urls import path
from Publicaciones.views import home,mostrar_productos,crear_productos

app_name = "Publicaciones"

urlpatterns = [
     path("", home, name="Home"),
     path("mostrar_productos/",mostrar_productos, name="mostrar_productos"),
     path("crear_productos/",crear_productos, name="crear_productos")
]
