from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def catalog(request):
    return HttpResponse("<h1> catalog")
