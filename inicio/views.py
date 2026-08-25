from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>maldito perro negro, ven y dale un abraazo a la abuela</h1>")