from django.contrib.auth.forms import UserCreationForm
from api.models import Planeacion, Servicios
from django import forms

class PlanForm(forms.ModelForm):

    class Meta:
        model = Planeacion
        fields='__all__'
        exclude = ['autorizacion', 'observacion']

        

class PlanAdminForm(forms.ModelForm):

    class Meta:
        model = Planeacion
        fields=['autorizacion', 'observacion']
        widgets = {
            'autorizacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        

# DIRECCIÓN DE SERVICIOS EDUCATIVOS

class ServForm(forms.ModelForm):

    class Meta:
        model = Servicios
        fields='__all__'
        exclude = ['autorizacion', 'observacion']     


class ServAdminForm(forms.ModelForm):

    class Meta:
        model = Servicios
        fields=['autorizacion', 'observacion']
        widgets = {
            'autorizacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }