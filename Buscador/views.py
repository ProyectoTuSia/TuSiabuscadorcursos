from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from Buscador.models import Campus
from Buscador.models import Faculty

# Create your views here.
def list_task(request):
    Campus_Info = Campus.objects.all()
    return render(request, "Filtrador.html", {'Campus_Info': Campus_Info})

def list_task2(request):

    Campus_Info = Campus.objects.all()
    result = request.POST["Filtro_Campus"]
    Faculty_Info = Faculty.objects.all()
    return (request, "Filtrador.html", {'Campus_Info': Campus_Info, 'Faculty_Info': Faculty_Info})