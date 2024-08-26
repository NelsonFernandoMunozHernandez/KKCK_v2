from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el Index de app1</h1> <p style='color:red'>escribe /app1/vista1/ arribita</p> <a href='http://127.0.0.1:8000/app1/vista1/' <p>o aca</p> </a>")

def vista1(request):
    html="""
    <h1 style='color:green'>Soy un título de app1</h1>
    <h2 style='color:blue'>Soy un subtítulo de app1</h2>
    <p>ya puedes borrar /vista1/ de arribita</p>
    <a href='http://127.0.0.1:8000/app1/' <p>o aqui</p> </a>
    """
    return HttpResponse(html)