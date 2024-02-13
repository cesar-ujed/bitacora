from django.contrib.auth.forms import UserCreationForm
from api.models import Planeacion, Servicios, Internacionalizacion, Desarrollo, Subsecretaria
from django import forms

class PlanForm(forms.ModelForm):

    class Meta:
        model = Planeacion
        fields='__all__'
        exclude = ['autorizacion', 'observacion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Marcamos los campos que pueden ser null como no requeridos
        for field_name, field in self.fields.items():
            if field_name in ['evidencia']:
                field.required = False  

        

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
        

# DIRECCIÓN DE INTERNACIONALIZACIÓN
class IntForm(forms.ModelForm):

    class Meta:
        model = Internacionalizacion
        fields='__all__'
        exclude = ['autorizacion', 'observacion']


class IntAdminForm(forms.ModelForm):

    class Meta:
        model = Internacionalizacion
        fields=['autorizacion', 'observacion']
        widgets = {
            'autorizacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        

# DIRECCIÓN DE DESARROLLO Y FORTALECIMIENTO ACADÉMICO
class DesForm(forms.ModelForm):

    class Meta:
        model = Desarrollo
        fields='__all__'
        exclude = ['autorizacion', 'observacion']


class DesAdminForm(forms.ModelForm):

    class Meta:
        model = Desarrollo
        fields=['autorizacion', 'observacion']
        widgets = {
            'autorizacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        

class SubseForm(forms.ModelForm):

    class Meta:
        model = Subsecretaria
        fields='__all__'
        exclude = ['autorizacion', 'observacion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Marcamos los campos que pueden ser null como no requeridos
        for field_name, field in self.fields.items():
            if field_name in ['evidencia']:
                field.required = False    


class SubAdminForm(forms.ModelForm):

    class Meta:
        model = Subsecretaria
        fields=['autorizacion', 'observacion']
        widgets = {
            'autorizacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }           