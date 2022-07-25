
from django.contrib import admin
from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_curso),
    path('cursos/', cursos),
    path('estudiantes/', estudiante),
    path('profesores/', profesores),
    path('entregables/', entregables),
    path('', inicio),
    
    
]
