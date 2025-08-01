from django.urls import path
from meu_app.views import home

urlpatterns = [
    path('', home, name='home'),
]