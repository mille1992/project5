from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    return render(request, "yayberhood/landingPage.html")

def littleProjects(request):
    return render(request, "yayberhood/littleProjects.html")

def createLittleProject(request):
    if request.method == "POST":
        title = request.POST["littleProjects-createTitle"]
        description_short = request.POST["littleProjects-createDescriptionShort"]
        description_detailed = request.POST["littleProjects-createDescriptionDetailed"]
        donation_bool = request.POST["littleProjects-donationBool"]=="True"
        currUser = User.objects.get(id = request.user.id)
        
        newProject = Project.objects.create(
            projectOwner = currUser,
            projectName = title,
            projectDescriptionShort = description_short,
            projectDescriptionDetailed = description_detailed,
            projectDonation_bool = donation_bool
        )
        newProject.projectAdmins.add(currUser)
        newProject.projectMembers.add(currUser)
        newProject.save()
        return HttpResponseRedirect(reverse("littleProjects"))
    else:
        return render(request, "yayberhood/createLittleProject.html")

def hobbies(request):
    return render(request, "yayberhood/hobbies.html")

def borrowIt(request):
    return render(request, "yayberhood/borrowIt.html")
    
def littleHelpers(request):
    return render(request, "yayberhood/littleHelpers.html")

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "yayberhood/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "yayberhood/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        profilePhotoUrl = request.POST["profilePhotoUrl"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "yayberhood/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, profilePhotoUrl = profilePhotoUrl)
            user.save()
        except IntegrityError:
            return render(request, "yayberhood/register.html", {
                "message": "Username already taken."
            })
        login(request, user)

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "yayberhood/register.html")