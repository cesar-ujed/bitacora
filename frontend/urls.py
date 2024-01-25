from django.urls import path
from django.contrib.auth.decorators import login_required
from frontend import views
from .views import AdminView

urlpatterns = [
    path('', views.login_page , name='login'),
    path('home/', views.home_page , name='home'),
    path('logout/', login_required(views.LogoutView.as_view()), name="logout"),
    path('administrador/', login_required(views.AdminView), name='admin'),
    path('personal/', login_required(views.PersonalView), name='personal'),

]
