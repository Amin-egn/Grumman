# django
from django.urls import path
from django.contrib.auth import views as auth_views
# internal
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
