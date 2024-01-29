from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from api.models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView

# Create your views here.
def login_page(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
             return redirect('home')
        
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
        password=request.POST['password'])

        if user is None:
                return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'username or password incorrect'
            })
        else:
            login(request, user)
            return redirect('home')
        

def home_page(request):
     return render(request, 'home.html')


class LogoutView(View):
    def get(self, request):
        # Cierra la sesión del usuario
        logout(request)
        # Redirige a la página de inicio u otra página después de cerrar la sesión
        return redirect(reverse('login'))


def AdminView(request):
     return render(request, 'admin.html')


def PersonalView(request):
     return render(request, 'personal.html')


class CreatePlan(UserPassesTestMixin, CreateView):
    model = Planeacion
    template_name='addplan.html'
    form_class = PlanForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamento.objects.filter(id=1)
        context['usuarios'] = User.objects.all()
        return context
    

    def test_func(self):
        allowed_groups = ['planeacion', 'Planeacion_admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()
    

# PLANEACION ADMIN    
class PlanList(UserPassesTestMixin, ListView):
    model = Planeacion
    template_name = "plan_admin.html"
    context_object_name = "plan_actividades"
    # paginate_by = 5

    def test_func(self):
        return self.request.user.groups.filter(name='Planeacion_admin').exists()



# UPDATE PLANEACION
class EdithPlan(UpdateView):
    model = Planeacion
    template_name = 'editplan.html'
    form_class = PlanAdminForm
    success_url = reverse_lazy('adminplan')



# DIRECCIÓN DE SERVICIOS EDUCATIVOS

class CreateServ(UserPassesTestMixin, CreateView):
    model = Servicios
    template_name='addserv.html'
    form_class = ServForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamento.objects.filter(id=2)
        context['usuarios'] = User.objects.all()
        return context
    

    def test_func(self):
        allowed_groups = ['servicios', 'Servicios_admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()        


# --ListView SE
class ServList(UserPassesTestMixin, ListView):
    model = Servicios
    template_name = "serv_admin.html"
    context_object_name = "serv_actividades"
    # paginate_by = 5

    def test_func(self):
        return self.request.user.groups.filter(name='Servicios_admin').exists()
    

# --Update SE (autorizacion e observación)
class EdithServ(UpdateView):
    model = Servicios
    template_name = 'editserv.html'
    form_class = ServAdminForm
    success_url = reverse_lazy('adminserv')    
