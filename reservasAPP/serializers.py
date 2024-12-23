from rest_framework import serializers
from reservasAPP.models import Reservas

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        #mostrar todos los datos menos el id y telefono
        fields = ['id', 'nombre', 'fecha_reserva', 'hora', 'cantidad_personas', 'observacion', 'estado']