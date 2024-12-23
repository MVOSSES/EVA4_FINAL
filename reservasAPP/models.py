from django.db import models

# Create your models here.
#modelo estado
class Estado(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self): #para que se muestre el estado al agregar una reserva   
        return self.estado
    

#modelo reservas
#campo observacion es opcional
class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_reserva = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.telefono