from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    informacion =models.TextField()
