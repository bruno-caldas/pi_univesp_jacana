from django.db import reset_queries
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

from eventos.models import Evento

#CARREGA AS PÁGINAS PRINCIPAIS

def carrega_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos':evento}
    return render(request, 'eventos/eventos.html',response)

# Create your views here.
