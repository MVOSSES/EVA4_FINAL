from django.contrib import admin
from reservasAPP.models import *
# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'fecha_reserva', 'hora', 'cantidad_personas', 'observacion', 'estado')

admin.site.register(Reservas, ReservasAdmin)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('estado',)

admin.site.register(Estado, EstadoAdmin)