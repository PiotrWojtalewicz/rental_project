from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Witamy w wypożyczalni samochodów!")

# Create your views here.
