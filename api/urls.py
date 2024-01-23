from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'departamentos', views.DepartamentoViewSet)
router.register(r'planeacion', views.PlaneacionViewSet)
router.register(r'servicios', views.ServiciosViewSet)
router.register(r'internacionalizacion', views.InternacionalizacionViewSet)
router.register(r'desarrollo', views.DesarrolloViewSet)


urlpatterns = [
    path('', include(router.urls))
]