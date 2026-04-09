from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    informacion =models.TextField()
