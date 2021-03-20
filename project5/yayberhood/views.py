from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "yayberhood/index.html")

def littleProjects(request):
    return render(request, "yayberhood/littleProjects.html")