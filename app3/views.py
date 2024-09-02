from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Soy el index de la app3,</h1><h3>Hecho por Benjamin</h3><a href="127.0.0.1:8000"> <p>Click aqui para volver a la pagina "404 not found".</p> </a> ')