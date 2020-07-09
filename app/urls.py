from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar_tarefas/', listar_taferas, name='listar_tarefas'),
]