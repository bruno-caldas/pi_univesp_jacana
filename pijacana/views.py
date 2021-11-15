from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

#CARREGA AS PÁGINAS PRINCIPAIS

def carrega_index(request):
    return render(request, "templates/../index.html")

def carrega_index2(request):
    return render(request, "templates/../index2.html")

def carrega_parceiros(request):
    return render(request, "templates/../parceiros.html")

def carrega_eventos(request):
    return render(request, "templates/../projetos_eventos.html")