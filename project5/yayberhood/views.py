from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "yayberhood/landingPage.html")

def littleProjects(request):
    return render(request, "yayberhood/littleProjects.html")

def hobbies(request):
    return render(request, "yayberhood/hobbies.html")

def borrowIt(request):
    return render(request, "yayberhood/borrowIt.html")
    
def littleHelpers(request):
    return render(request, "yayberhood/littleHelpers.html")