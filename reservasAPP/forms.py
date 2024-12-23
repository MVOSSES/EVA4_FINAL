from django import forms
from django.core.exceptions import ValidationError
from reservasAPP.models import Reservas, Estado

#editar reservas
class CrearReservas(forms.Form):
    nombre= forms.CharField()
    telefono= forms.CharField()
    fecha_reserva= forms.DateField()
    hora= forms.TimeField()
    cantidad_personas= forms.IntegerField(
        validators=[
            lambda value: value > 0 or ValidationError('La cantidad de personas debe ser mayor a 0'),
            lambda value: value < 16 or ValidationError('La cantidad máxima es 16.')
        ]
    )
    estado= forms.ModelChoiceField(queryset=Estado.objects.all())
    observacion= forms.CharField(required=False)

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fecha_reserva = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    cantidad_personas.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'


#agregar reservas
# Definición de validadores personalizados
def validar_cantidad_minima(value):
    if value <= 0:
        raise ValidationError('La cantidad de personas debe ser mayor a 0.')

def validar_cantidad_maxima(value):
    if value >= 16:
        raise ValidationError('La cantidad máxima es 15.')

class CrearReservas(forms.ModelForm):
    nombre = forms.CharField()
    telefono = forms.CharField()
    fecha_reserva = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    cantidad_personas = forms.IntegerField(
        validators=[validar_cantidad_minima, validar_cantidad_maxima]
    )
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())
    observacion = forms.CharField(required=False)

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    cantidad_personas.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Reservas
        fields = '__all__'