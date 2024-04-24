from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.get_tarefas, name='get_all_tarefas'),
    path('tarefa/<int:id>', views.get_by_id),
    path('data/', views.tarefa_manager)
]
