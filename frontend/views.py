from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from api.models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView
from itertools import chain


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


def user_register(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm 
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # usuario
                #login(request, user)
                return redirect('login')
            except:
                # return HttpResponse('el usuario ya existe')
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error' : 'usario ya existe' 
                })
        # return HttpResponse('passwords no coinciden')
        return render(request, 'signup.html', {
            'form': UserCreationForm, 
            'error': 'passwords no coinciden'
    })

def AdminView(request):
     return render(request, 'admin.html')


def PersonalView(request):
     return render(request, 'personal.html')


class CreatePlan(UserPassesTestMixin, CreateView):
    model = Planeacion
    template_name='addplan.html'
    form_class = PlanForm
    success_url = reverse_lazy('success')

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
    ordering = '-id'

    def test_func(self):
        allowed_groups = ['Administrador', 'Planeacion_admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()



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
    success_url = reverse_lazy('success_serv')

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
    ordering = '-id'

    def test_func(self):
        allowed_groups = ['Administrador', 'Servicios_admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()
    

# --Update SE (autorizacion e observación)
class EdithServ(UpdateView):
    model = Servicios
    template_name = 'editserv.html'
    form_class = ServAdminForm
    success_url = reverse_lazy('adminserv')    



# DIRECCIÓN DE INTERNACIONALIZACÓN
class CreateInt(UserPassesTestMixin, CreateView):
    model = Internacionalizacion
    template_name='addint.html'
    form_class = IntForm
    success_url = reverse_lazy('success_int')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamento.objects.filter(id=3)
        context['usuarios'] = User.objects.all()
        return context
    

    def test_func(self):
        allowed_groups = ['internacionalizacion', 'Internacionalizacion_Admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()        


# --ListView DI
class IntList(UserPassesTestMixin, ListView):
    model = Internacionalizacion
    template_name = "int_admin.html"
    context_object_name = "int_actividades"
    # paginate_by = 5

    def test_func(self):
        allowed_groups = ['Administrador', 'Internacionalizacion_Admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()
    

# --Update DI (autorizacion e observación)
class EditInt(UpdateView):
    model = Internacionalizacion
    template_name = 'editint.html'
    form_class = IntAdminForm
    success_url = reverse_lazy('adminint')   


# DIRECCIÓN DE DESARROLLO Y FORTALECIMIENTO ACADÉMICO
class CreateDes(UserPassesTestMixin, CreateView):
    model = Desarrollo
    template_name='adddes.html'
    form_class = DesForm
    success_url = reverse_lazy('success_des')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamento.objects.filter(id=4)
        context['usuarios'] = User.objects.all()
        return context
    

    def test_func(self):
        allowed_groups = ['desarrollo', 'Desarrollo_Admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()


# --ListView DFA
class DesList(UserPassesTestMixin, ListView):
    model = Desarrollo
    template_name = "des_admin.html"
    context_object_name = "des_actividades"

    def test_func(self):
        allowed_groups = ['Administrador', 'Desarrollo_Admin']
        return self.request.user.groups.filter(name__in=allowed_groups).exists()  


# --Update DFA (autorizacion e observación)
class EditDes(UpdateView):
    model = Desarrollo
    template_name = 'editdes.html'
    form_class = DesAdminForm
    success_url = reverse_lazy('admindes')   


# View de guardado con exito
class SuccessView(View):
    template_name = 'success.html' 

    def get(self, request):
        return render(request, self.template_name)
    

# View de guardado con exito
class SuccessSEView(View):
    template_name = 'success_se.html' 

    def get(self, request):
        return render(request, self.template_name) 


# View de guardado con exito
class SuccessIView(View):
    template_name = 'success_i.html' 

    def get(self, request):
        return render(request, self.template_name)
    

# View de guardado con exito
class SuccessDesView(View):
    template_name = 'success_des.html' 

    def get(self, request):
        return render(request, self.template_name)



# Vista para Perfil
class UserRecordsView(ListView):
    template_name = 'perfil.html'
    context_object_name = 'records'
    ordering = '-id'

    def get_queryset(self):
        registros_modelo1 = Planeacion.objects.filter(usuario=self.request.user).order_by('-id')
        registros_modelo2 = Servicios.objects.filter(usuario=self.request.user).order_by('-id')
        registros_modelo3 = Internacionalizacion.objects.filter(usuario=self.request.user).order_by('-id')
        registros_modelo4 = Desarrollo.objects.filter(usuario=self.request.user).order_by('-id')

        return list(chain(registros_modelo1, registros_modelo2, registros_modelo3, registros_modelo4))
