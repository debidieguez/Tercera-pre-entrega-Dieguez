from django.urls import path
from appcoder.views import *


urlpatterns = [
    path('', index, name="Index"),
    path('curso/', curso, name="Curso"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('buscar_curso/', buscar_curso, name="Buscar_Curso"),
    path('busqueda_camada/', busqueda_camada, name="Busqueda_Camada"),
    path('buscar/', buscar, name="Buscar")
]
