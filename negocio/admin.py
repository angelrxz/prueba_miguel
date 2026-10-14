from django.contrib import admin
from .models import equipo, arriendo_equipo



@admin.register(equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion', 'fecha_actualizacion', 'usuario_creador', 'valor_equipo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion', 'fecha_actualizacion', 'usuario_creador')

@admin.register(arriendo_equipo)


class ArriendoEquipoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha_inicio', 'fecha_fin', 'usuario_arrendatario', 'valor_arriendo')
    readonly_fields = ('valor_arriendo',)
    search_fields = ('equipo__nombre', 'usuario_arrendatario__username')
    list_filter = ('fecha_inicio', 'fecha_fin', 'usuario_arrendatario')
