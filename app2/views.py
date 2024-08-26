from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>index app2</h1><p style='color:red'>escribe /app2/parrafo/ arribita</p><a href='http://127.0.0.1:8000/app2/parrafo/'<p> o aca </p></a>")

def texto(request):
    html="<p>Soy un parrafo de app2</p><p>ya puedes borrar el /parrafo/ de arribita</p><a href='http://127.0.0.1:8000/app2/'<p> o aqui </p></a>"
    return HttpResponse(html)