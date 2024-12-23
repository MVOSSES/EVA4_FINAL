from rest_framework import serializers
from reservasAPP.models import Reservas

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = ['id', 'nombre', 'telefono' ,'fecha_reserva', 'hora', 'cantidad_personas', 'observacion', 'estado']

    def validate_cantidad_personas(self, value):
        if value <= 0:
            raise serializers.ValidationError("Debe ser mayor a 0.")
        if value >= 16:
            raise serializers.ValidationError("Debe ser menor a 16.")
        return value