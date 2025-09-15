from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Task CRUD
    path('tasks/', views.task_index, name='task_index'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Subtask CRUD (nested to task)
    path('tasks/<int:task_pk>/subtasks/new/', views.subtask_create, name='subtask_create'),
    path('subtasks/<int:pk>/edit/', views.subtask_update, name='subtask_update'),
    path('subtasks/<int:pk>/delete/', views.subtask_delete, name='subtask_delete'),
]
