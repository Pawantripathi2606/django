from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    a=10+20
    return HttpResponse(f"About Page: {a}")


# Create your views here.
