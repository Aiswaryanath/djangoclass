from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexpage(request):
    return HttpResponse("Welcome to my Index Page")
def contactpage(request):
     return HttpResponse("contact page")   
def homepage(request):
    return HttpResponse("welcome to home page")     