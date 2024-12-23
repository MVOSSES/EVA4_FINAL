from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

#importaciones para api
from reservasAPP.models import *
from reservasAPP.serializers import ReservasSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from reservasAPP.forms import *


#Views Formularios Crear, Editar y Eliminar Reservas
#Ver Reservas
def reservasData(request):
    reservas = Reservas.objects.all()
    data={'reservas': reservas}
    return render(request, 'reservasAPP/reservasData.html', data)

#Agregar Reservas
def reservasAgregar(request):
    form=CrearReservas()
    if request.method=='POST':
        form=CrearReservas(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('verReservas'))
    data={'form':form}
    return render(request, 'reservasAPP/reservasAgregar.html', data)

#Editar Reservas
def reservasEditar(request, id):
    reserva=Reservas.objects.get(id=id) 
    form=CrearReservas(instance=reserva)
    if request.method=='POST':
        form=CrearReservas(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('verReservas'))
    data={'form':form}
    return render(request, 'reservasAPP/reservasAgregar.html', data)

#Eliminar Reservas
def reservasEliminar(request, id):
    reserva=Reservas.objects.get(id=id)
    reserva.delete()
    return HttpResponseRedirect(reverse('verReservas'))


#####################################################################################
#Views API
def ver_reservas(request):
    reservas = Reservas.objects.all()
    data = {'reservas': list(reservas.values())}
    return JsonResponse(data)

#creación api, metodos GET y POST
@api_view(['GET', 'POST'])
def reservas_list(request): 
    if request.method == 'GET':
        reservas = Reservas.objects.all()   
        serializer = ReservasSerializer(reservas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReservasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#api  metodo GET por id, metodo PUT y metodo DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def reservas_detail(request, pk):
    try:
        reserva = Reservas.objects.get(pk=pk)
    except Reservas.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservasSerializer(reserva)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservasSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
