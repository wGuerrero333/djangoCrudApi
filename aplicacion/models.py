from django.db import models

# Create your models here.
class modelo ( models.Model):
    titulo= models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)