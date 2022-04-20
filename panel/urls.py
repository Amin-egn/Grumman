from django.urls import path
# internal
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('all_board/', views.AllBoardView.as_view(), name='all_board'),
    path('all_board/<int:pk>/delete', views.DeleteBoardView.as_view(), name='board_delete'),
    path('tasks/<int:pk>', views.BoardTaskView.as_view(), name='tasks')
]
