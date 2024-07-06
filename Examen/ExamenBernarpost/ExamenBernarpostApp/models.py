from django.db import models
from django.utils import timezone

# Create your models here.

class Usuarios(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=50)
    clave =  models.CharField(max_length=50)

def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.nombre,self.clave)

class Posts(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

class Planes(models.Model):
    codigo = models.CharField(max_length=6)
    email = models.CharField(primary_key=True,max_length=50)
