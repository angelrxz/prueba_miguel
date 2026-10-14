from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_equipo = models.DecimalField(
        "Valor del equipo (CLP)", max_digits=12, decimal_places=0, default=0
    )

    def __str__(self):
        return self.nombre

class arriendo_equipo(models.Model):
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    usuario_arrendatario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_arriendo = models.DecimalField(
        "Valor del arriendo (CLP)", max_digits=12, decimal_places=0, default=0
    )

    def dias_arriendo(self):
        if self.fecha_fin < self.fecha_inicio:
            raise ValidationError({"fecha_fin": "La fecha de término debe ser posterior al inicio."})
        return max(1, (self.fecha_fin.date() - self.fecha_inicio.date()).days)

    def clean(self):
        super().clean()
        if self.fecha_inicio and self.fecha_fin:
            self.dias_arriendo()

    def save(self, *args, **kwargs):
        self.valor_arriendo = self.equipo.valor_equipo * self.dias_arriendo()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Arriendo de {self.equipo.nombre} por {self.usuario_arrendatario.username}"



