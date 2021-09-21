from django.shortcuts import render

from parceiros.models import Parceiros

# Create your views here.
def carrega_parceiros(request):
    parceiro = Parceiros.objects.all()
    response = {'parceiros':parceiro}
    return render(request,'parceiros/parceiros.html',response)
