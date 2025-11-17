from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cachorro

def home(request):
    return render(request, 'index.html')

def project(request):

    # Captura os filtros enviados pelo <select>
    especie = request.GET.get("especie")
    porte = request.GET.get("porte")
    idade = request.GET.get("idade")

    # Busca todos os registros
    cachorro = Cachorro.objects.all()

    # Aplica filtros se o usuário escolher algo
    if especie and especie != "all":
        cachorro = cachorro.filter(especie=especie)

    if porte and porte != "all":
        cachorro = cachorro.filter(porte=porte)

    # Se não existir nenhum registro, apenas renderiza a página
    if not cachorro.exists():
        return render(request, "project.html", {"cachorro": []})

    return render(request, "project.html", {"cachorro": cachorro})




def sponsorship(request):
    cachorro = Cachorro.objects.all()
    
    if not Cachorro.objects.exists():
        return render(request, 'sponsorship.html')
    else:
        return render(request, 'sponsorship.html', {'cachorro' : cachorro})

def success(request):
    cachorro = Cachorro.objects.all()
    if not Cachorro.objects.exists():
        return render(request, 'sponsorship.html')
    else:
        return render(request, 'success_stories.html', {'cachorro' : cachorro})

def contact(request):
    return render(request, 'contact.html')