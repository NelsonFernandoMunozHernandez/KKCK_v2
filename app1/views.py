from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el Index de app1</h1><a href='http://127.0.0.1:8000/app1/vista1/' <p>Click aca para acceder a la '/vista 1/'. </p> </a> <a href='http://127.0.0.1:8000' <p>Click aca para volver a la pagina '404 not found'. </p> </a>")

def vista1(request):
    html="""
    <h1 style='color:green'>Soy un título de app1</h1>
    <h2 style='color:blue'>Soy un subtítulo de app1</h2>
    <a href='http://127.0.0.1:8000/app1/' <p>Click aqui para volver atras.</p> </a>
    <a href='http://127.0.0.1:8000' <p>Click aca para volver a la pagina '404 not found'. </p> </a>
    """
    return HttpResponse(html)