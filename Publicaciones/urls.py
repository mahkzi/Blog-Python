from django.urls import path
from Publicaciones.views import home,mostrar_productos,crear_productos, detalle_producto

app_name = "Publicaciones"

urlpatterns = [
     path("", home, name="Home"),
     path("mostrar_productos/",mostrar_productos, name="mostrar_productos"),
     path("crear_productos/",crear_productos, name="crear_productos"),
     path("detalle_producto/<int:id_producto>/",detalle_producto, name="detalle_producto")
]
