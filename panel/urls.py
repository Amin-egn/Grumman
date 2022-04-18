from django.urls import path
# internal
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/new/', views.NewProjectView.as_view(), name='new_project')
]
