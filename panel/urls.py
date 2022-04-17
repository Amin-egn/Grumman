from django.urls import path
# internal
from . import views


urlpatterns = [
    path('', views.home_view, name='home')
]
