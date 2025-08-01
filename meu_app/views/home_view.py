from django.shortcuts import render
from django.http import HttpResponse
from meu_app.controllers import Listar_Usuarios

def home(request):
    users = Listar_Usuarios()
    html = "<h1>Usuarios:</h1>"
    for user in users:
        html += f"<p><strong>{user.login}</strong>: {user.senha}</p>"
    return HttpResponse(html)