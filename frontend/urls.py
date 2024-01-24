from django.urls import path
from django.contrib.auth.decorators import login_required
from frontend import views

urlpatterns = [
    path('', views.login_page , name='login'),
    path('home/', views.home_page , name='home'),
    path('logout/', login_required(views.LogoutView.as_view()), name="logout"),
]
