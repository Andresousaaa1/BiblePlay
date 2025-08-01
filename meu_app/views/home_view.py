from django.shortcuts import render
from django.http import HttpResponse
from meu_app.controllers import Listar_Usuarios

def home(request):
    users = Listar_Usuarios()
    return render(request, 'meu_app/index.html', {'users': users})