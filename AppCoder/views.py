from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Curso

# Create your views here.

def curso(self, nombre, camada):
   
    curso = Curso(nombre = nombre, camada = camada)
    curso.save()

    return HttpResponse(f'''
    <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado<p>
    ''')

def lista_curso(self):
   
    lista = Curso.objects.all()

    return render(self, 'lista_cursos.html', {'lista_cursos': lista})

def inicio(self):
    return render(self, 'inicio.html')

    # return HttpResponse("Vista de inicio")

def estudiante(self):
       return render(self, 'estudiantes.html')
    
    # return HttpResponse("Vista de estudiantes")

def profesores(self):
       return render(self, 'profesores.html')

    # return HttpResponse("Vista de profesores")

def cursos(self):
       return render(self, 'cursos.html')

    # return HttpResponse("Vista de cursos")

def entregables(self):
       return render(self, 'entregables.html')

    # return HttpResponse("Vista de entregables")