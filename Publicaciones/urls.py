from django.urls import path
from Publicaciones.views import home, blog

urlpatterns = [
     path("", home),
     path("blog/", blog)
]
