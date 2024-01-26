from django.urls import path
from django.contrib.auth.decorators import login_required
from frontend import views
from .views import AdminView, CreatePlan, PlanList, EdithPlan

urlpatterns = [
    path('', views.login_page , name='login'),
    path('home/', views.home_page , name='home'),
    path('logout/', login_required(views.LogoutView.as_view()), name="logout"),
    path('administrador/', login_required(views.AdminView), name='admin'),
    path('personal/', login_required(views.PersonalView), name='personal'),
    path('add_planeacion/', login_required(CreatePlan.as_view()), name='addplan'),
    path('planeacion_admin/', login_required(PlanList.as_view()), name='adminplan'),
    path('editar_actividad/<int:pk>/', login_required(EdithPlan.as_view()), name='editarplan'),
]
