from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'
        ordering=['-id']

    def _str_(self):
        return self.user.username   
     

class Planeacion(models.Model):
    fecha           = models.DateField(auto_now_add=True)
    hora_inicio     = models.DateTimeField(auto_now_add=False)
    hora_final      = models.DateTimeField(auto_now_add=False)
    horas_total     = models.FloatField(null=True)
    actividad       = models.CharField(max_length=255)
    autorizacion    = models.BooleanField(default=False, null=True)
    observacion     = models.CharField(max_length=255, null=True)
    usuario         = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.actividad
    

class Servicios(models.Model):
    fecha           = models.DateField(auto_now_add=True)
    hora_inicio     = models.DateTimeField(auto_now_add=False)
    hora_final      = models.DateTimeField(auto_now_add=False)
    horas_total     = models.FloatField(null=True)
    actividad       = models.CharField(max_length=255)
    autorizacion    = models.BooleanField(default=False, null=True)
    observacion     = models.CharField(max_length=255, null=True)
    usuario         = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.actividad
    

class Internacionalizacion(models.Model):
    fecha           = models.DateField(auto_now_add=True)
    hora_inicio     = models.DateTimeField(auto_now_add=False)
    hora_final      = models.DateTimeField(auto_now_add=False)
    horas_total     = models.FloatField(null=True)
    actividad       = models.CharField(max_length=255)
    autorizacion    = models.BooleanField(default=False, null=True)
    observacion     = models.CharField(max_length=255, null=True)
    usuario         = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.actividad


class Desarrollo(models.Model):
    fecha           = models.DateField(auto_now_add=True)
    hora_inicio     = models.DateTimeField(auto_now_add=False)
    hora_final      = models.DateTimeField(auto_now_add=False)
    horas_total     = models.FloatField(null=True)
    actividad       = models.CharField(max_length=255)
    autorizacion    = models.BooleanField(default=False, null=True)
    observacion     = models.CharField(max_length=255, null=True)
    usuario         = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.actividad        
        
