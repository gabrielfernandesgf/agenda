from http.client import responses

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Evento
from core.models import Evento

# Create your views here.

def index(request):
    return redirect('/agenda/')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos' : evento}
    return render(request, 'agenda.html', dados)


