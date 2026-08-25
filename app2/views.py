from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def v1_inicio(request):
    return HttpResponse("<h1 style='color green;'> Bienvenido waza</h1>");

def v2_inicio(request):
    return HttpResponse("<h1 style='color green;'> Me pica un pulmon</h1>");