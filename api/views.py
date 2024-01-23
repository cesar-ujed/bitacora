from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class PlaneacionViewSet(viewsets.ModelViewSet):
    queryset = Planeacion.objects.all()
    serializer_class = PlaneacionSerializer


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer    


class InternacionalizacionViewSet(viewsets.ModelViewSet):
    queryset = Internacionalizacion.objects.all()
    serializer_class = InternacionalizacionSerializer


class DesarrolloViewSet(viewsets.ModelViewSet):
    queryset = Desarrollo.objects.all()
    serializer_class = DesarrolloSerializer    



