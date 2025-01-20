"""
Versión antigua, provocaba el error en que al editar una reserva no se recuperaba el dato de fecha_reserva original

from django import forms
from django.core.exceptions import ValidationError
from reservasAPP.models import Reservas, Estado

#editar reservas
def validar_cantidad_minima(value):
    if value <= 0:
        raise ValidationError('La cantidad de personas debe ser mayor a 0.')
def validar_cantidad_maxima(value):
    if value >= 16:
        raise ValidationError('La cantidad máxima es 15.')
class CrearReservas(forms.Form):
    nombre= forms.CharField()
    telefono= forms.CharField()
    fecha_reserva= forms.DateField()
    hora= forms.TimeField()
    cantidad_personas= forms.IntegerField(
        validators=[validar_cantidad_minima, validar_cantidad_maxima]
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
        """

from django import forms
from django.core.exceptions import ValidationError
from reservasAPP.models import Reservas, Estado

# Validaciones
def validar_cantidad_minima(value):
    if value <= 0:
        raise ValidationError('La cantidad de personas debe ser mayor a 0.')

def validar_cantidad_maxima(value):
    if value >= 16:
        raise ValidationError('La cantidad máxima es 15.')

# Formulario basado en ModelForm
class CrearReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            # Configuración personalizada para el campo fecha_reserva para solucionar el problema de recuperación del dato
            'fecha_reserva': forms.DateInput( 
                format='%Y-%m-%d',  # Asegura que el formato sea compatible
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
        }

    cantidad_personas = forms.IntegerField(
        validators=[validar_cantidad_minima, validar_cantidad_maxima]
    )

    def __init__(self, *args, **kwargs):
        super(CrearReservas, self).__init__(*args, **kwargs)
        # Verifica si ya hay un valor en fecha_reserva y lo formatea correctamente
        if self.instance and self.instance.pk:
            self.fields['fecha_reserva'].initial = self.instance.fecha_reserva.strftime('%Y-%m-%d')
