from django.shortcuts import render
from django.http import HttpResponse

def v1_app1(request):
    return HttpResponse("<h1>Vista 1 App1</h1>"
    "<p>Todo a tu alcanze</p>")

def v2_app1(request):
    return HttpResponse("<h2>Vista 2 App2<h1>")
