from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class arriendo_equipo(models.Model):
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    usuario_arrendatario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Arriendo de {self.equipo.nombre} por {self.usuario_arrendatario.username}"


