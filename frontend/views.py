from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.views import View

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

