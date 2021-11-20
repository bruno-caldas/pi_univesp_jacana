"""pijacana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
import parceiros

from pijacana.views import carrega_abrigo, carrega_index, carrega_contatos, carrega_ajuda, carrega_resgate

from cadastro import views
from eventos import urls, views
from parceiros import urls, views

app_name = 'pijacana'
urlpatterns = [
    #path('', include('cadastro.urls')),
    path('admin/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')), #ATIVAÇÃO DE RICH-TEXT
    path('', RedirectView.as_view(url='/abrigo/')),
    path('abrigo/', carrega_index, name="index"),
    path('abrigo/local', carrega_abrigo, name="abrigo"),
    path('abrigo/contatos', carrega_contatos, name="contatos"),
    path('abrigo/ajuda', carrega_ajuda, name="ajuda"),
    path('abrigo/resgate', carrega_resgate, name="resgate"),
    path('abrigo/parceiros',include("parceiros.urls")),
    path('abrigo/eventos', include("eventos.urls")),
    path('abrigo/mural_animais', include("cadastro.urls")),
    path('login/', include("login_users.urls")),
]
