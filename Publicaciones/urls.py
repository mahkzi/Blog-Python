from django.urls import path
from Publicaciones.views import home

urlpatterns = [
     path("", home),
]
