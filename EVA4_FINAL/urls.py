"""
URL configuration for EVA4_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservasAPP.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('reservasAll/', ver_reservas),
    path('reservasAPI/', reservas_list,name='reservasAPI'),
    path('reservasAPI/<int:pk>/', reservas_detail,name='reservasAPI'),
    path('verReservas/',reservasData,name="verReservas"),
    path('reservasCrear/',reservasAgregar,name="reservasCrear"),
    path('reservasEditar/<int:id>/',reservasEditar,name="reservasEditar"),
    path('reservasEliminar/<int:id>/',reservasEliminar,name="reservasEliminar"),
    path('',TemplateView.as_view(template_name="index.html"),name="index"),
]
