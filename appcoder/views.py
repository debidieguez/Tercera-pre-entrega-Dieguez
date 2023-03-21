from django.shortcuts import render
from appcoder.models import *
from django.http import HttpResponse


# Create your views here.
def agrega_curso (request):
    curso = Curso (nombre="Python", camada= "48601")
    curso.save()
    texto = f'Se guardo {curso.nombre} con la camada {curso.camada}'
    return HttpResponse (texto)


def inicio (request):
    return HttpResponse ("Vista inicio")

#def cursos (request):
    return HttpResponse ("Vista cursos")

def profesores (request):
    return HttpResponse ("Vista profesores")

def estudiantes (request):
    return HttpResponse ("Vista estudiantes")

def entregables (request):
    return HttpResponse ("Vista entregables")



def index (request):
    return render(request, 'appcoder/index.html')

def curso (request):

    if request.method == "POST":
        print (f"\\n\n{request.POST}\n\n")
        nombre= request.POST ["curso"]
        camada= request.POST ["camada"]
        curso= Curso(nombre=nombre, camada=camada)
        curso.save()

    return render(request, 'appcoder/curso.html')


def profesores (request):

    if request.method == "POST":
        print (f"\\n\n{request.POST}\n\n")
        nombre= request.POST ["nombre"]
        apellido= request.POST ["apellido"]
        email= request.POST ["email"]
        profesion= request.POST ["profesion"]
        profesores= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
        profesores.save()

    return render(request, 'appcoder/profesores.html')


def estudiantes (request):

    if request.method == "POST":
        print (f"\\n\n{request.POST}\n\n")
        nombre= request.POST ["nombre"]
        apellido= request.POST ["apellido"]
        email= request.POST ["email"]
        estudiantes= Estudiante(nombre=nombre, apellido=apellido, email=email)
        estudiantes.save()

    return render(request, 'appcoder/estudiantes.html')
    

def entregables (request):

    if request.method == "POST":
        print (f"\\n\n{request.POST}\n\n")
        nombre= request.POST ["nombre"]
        fechaDeEntrega = request.POST ["fechaDeEntrega"]
        entregado = False
        if "entregado" in request.POST and request.POST ["entregado"] == "on":
            entregado = True
        entregables= Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entregado=entregado)
        entregables.save()    

    return render(request, 'appcoder/entregables.html')





def buscar_curso (request):

    if request.method == "POST":
        print (f"\\n\n{request.POST}\n\n")
        nombre= request.POST ["curso"]
        camada= request.POST ["camada"]
        curso= Curso(nombre=nombre, camada=camada)
        curso.save()

    return render(request, 'appcoder/buscar_curso.html')


def busqueda_camada (request):
    return render(request, 'appcoder/busqueda_camada.html')

def buscar(request):

    if request.GET["camada"]:
        camada= request.GET['camada']
        cursos= Curso.objects.filter(camada__icontains=camada)

        return render(request, 'appcoder/resultados_busqueda.html', {"cursos":cursos, "camada":camada})


    respuesta= f"ESTOY BUSCANDO LA CAMADA NUM: {request.GET['camada']}"
    return HttpResponse (respuesta)