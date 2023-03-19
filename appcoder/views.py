from django.shortcuts import render
from appcoder.models import Curso
from django.http import HttpResponse


# Create your views here.
def agrega_curso (request):
    curso = Curso (nombre="Python", camada= "48601")
    curso.save()
    texto = f'Se guardo {curso.nombre} con la camada {curso.camada}'
    return HttpResponse (texto)