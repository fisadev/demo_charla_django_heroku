from django.contrib import admin

from sitio.models import Opcion, Respuesta


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = "nombre",


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = "fecha", "opcion"
    list_filter = "opcion",
    date_hierarchy = "fecha"
