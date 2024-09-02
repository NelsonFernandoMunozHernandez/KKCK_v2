from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>index app2</h1><a href='http://127.0.0.1:8000/app2/parrafo/'<p> Click aqui para acceder a la pagina '/parrafo/'. </p></a> <a href='http://127.0.0.1:8000'<p> Click aqui para volver a la pagina '404 not found'. </p></a>")

def texto(request):
    html="<p>Soy un parrafo de app2</p><a href='http://127.0.0.1:8000/app2/'<p> Click aqui para volver atras. </p></a><a href='http://127.0.0.1:8000'<p> Click aqui para volver a la pagina '404 not found'. </p></a>"
    return HttpResponse(html)