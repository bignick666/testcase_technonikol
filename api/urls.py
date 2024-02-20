from django.urls import path

from . import views


urlpatterns = [
    path('', views.api_overview, name='home'),
    # path('tasks/', views.APITask.as_view(), name='tasks'),
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/create', views.task_create, name='task_create'),
    path('tasks/destroy/<int:id>', views.task_delete, name='task_delete'),
    path('tasks/update/<int:id>', views.task_update, name='task_update')
]
