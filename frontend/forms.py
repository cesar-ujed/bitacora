from django.contrib.auth.forms import UserCreationForm
from api.models import Planeacion
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