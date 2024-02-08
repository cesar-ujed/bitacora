from rest_framework import serializers
from .models import *

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('nombre',)


class PlaneacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeacion
        fields='__all__'


class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields='__all__'


class InternacionalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internacionalizacion
        fields='__all__'      


class DesarrolloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollo
        fields='_all_'       


class SubsecretariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsecretaria
        fields='__all__'   