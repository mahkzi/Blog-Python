from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio =models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
