from django.urls import path
from django.contrib.auth.decorators import login_required
from frontend import views
from .views import AdminView, CreatePlan, PlanList, EdithPlan, CreateServ, ServList, EdithServ, CreateInt, IntList, EditInt, CreateDes, DesList, EditDes

urlpatterns = [
    path('', views.login_page , name='login'),
    path('home/', views.home_page , name='home'),
    path('logout/', login_required(views.LogoutView.as_view()), name="logout"),
    path('administrador/', login_required(views.AdminView), name='admin'),
    path('personal/', login_required(views.PersonalView), name='personal'),
    path('add_planeacion/', login_required(CreatePlan.as_view()), name='addplan'),
    path('planeacion_admin/', login_required(PlanList.as_view()), name='adminplan'),
    path('editar_actividad/<int:pk>/', login_required(EdithPlan.as_view()), name='editarplan'),
    # -- Servicios Educativos
    path('add_servicios_educativos/', login_required(CreateServ.as_view()), name='addserv'),
    path('servicios_educativos_admin/', login_required(ServList.as_view()), name='adminserv'),
    path('editar/<int:pk>/', login_required(EdithServ.as_view()), name='editarserv'),
    # -- Internacionalización
    path('add_internacionalizacion/', login_required(CreateInt.as_view()),  name='addint'),
    path('internacionalizacion_admin/', login_required(IntList.as_view()), name='adminint'),
    path('edit_internacionalizacion/<int:pk>/', login_required(EditInt.as_view()), name='editarint'),
    # -- Desarrollo y Fort
    path('add_desarrollo_y_fortalecimiento/', login_required(CreateDes.as_view()), name='adddes'),
    path('desarrollo_y_fortalecimiento_admin/', login_required(DesList.as_view()), name='admindes'),
    path('edit_des_y_fort_acad/<int:pk>', login_required(EditDes.as_view()), name='editardes'),
]
