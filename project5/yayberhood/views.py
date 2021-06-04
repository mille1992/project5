from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *
import json

# Create your views here.
def index(request):
    return render(request, "yayberhood/landingPage.html")

def littleProjects(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        little_project_donation_value = request_data["littleProjectNewDonationValue"]
        little_project_post_id = request_data["littleProjectPostId"]

        clicked_project = Project.objects.get(id=little_project_post_id)
        clicked_project.projectDonation_value = little_project_donation_value
        clicked_project.save()

        return JsonResponse({"newdonationValue":little_project_donation_value})
    else:
        projects = Project.objects.all()
        for project in projects:
            print(project.projectDonation_value)
        projects = projects.order_by("-projectCreationTimestamp").all()
        return render(request, "yayberhood/littleProjects.html",{
            "projects":projects,
        })

def createLittleProject(request):
    if request.method == "POST":
        ### create project from create projects page ###
        title = request.POST["littleProjects-createTitle"]
        description_short = request.POST["littleProjects-createDescriptionShort"]
        description_detailed = request.POST["littleProjects-createDescriptionDetailed"]
        donation_bool = request.POST["littleProjects-donationBool"]=="True"
        curr_user = User.objects.get(id = request.user.id)
        
        new_project = Project.objects.create(
            projectOwner = curr_user,
            projectName = title,
            projectDescriptionShort = description_short,
            projectDescriptionDetailed = description_detailed,
            projectDonation_bool = donation_bool
        )
        new_project.projectAdmins.add(curr_user)
        new_project.projectMembers.add(curr_user)
        new_project.save()
        return HttpResponseRedirect(reverse("littleProjects"))
    else:
        return render(request, "yayberhood/createLittleProject.html")

def hobbies(request):
    if request.method == "POST":
        curr_user = request.user
        hobby_group_id = request.POST["hobbies-hobbyGroupId"]
        hobby_group = HobbyGroup.objects.get(id = hobby_group_id)
        hobby_group.hobbyGroupMembers.add(curr_user)
        hobby_group.save()

        hobby_groups = HobbyGroup.objects.all()
        hobby_groups = hobby_groups.order_by("-hobbyGroupCreationTimestamp").all()
        hobby_group_categories_used = HobbyGroup.objects.values_list('hobbyGroupCategories', flat=True).distinct()
        
        curr_user_memberships = curr_user.hobbyGroupMemberships.all()

        return render(request, "yayberhood/hobbies.html",{
            "hobby_groups":hobby_groups,
            "hobby_group_categories_used": hobby_group_categories_used,
            "curr_user_memberships": curr_user_memberships
        })
    else:
        hobby_groups = HobbyGroup.objects.all()
        hobby_groups = hobby_groups.order_by("-hobbyGroupCreationTimestamp").all()
        hobby_group_categories_used = HobbyGroup.objects.values_list('hobbyGroupCategories', flat=True).distinct()
        if request.user.is_authenticated:
            curr_user = request.user
            curr_user_memberships = curr_user.hobbyGroupMemberships.all()
        else:
            curr_user_memberships = []
        return render(request, "yayberhood/hobbies.html",{
            "hobby_groups":hobby_groups,
            "hobby_group_categories_used": hobby_group_categories_used,
            "curr_user_memberships": curr_user_memberships
        })

def createHobbyGroup(request):
    if request.method == "POST":
        ### create hobby group from create hobby group page ###
        title = request.POST["hobbies-createTitle"]
        description_short = request.POST["hobbies-createDescriptionShort"]
        description_detailed = request.POST["hobbies-createDescriptionDetailed"]
        hobbies_category = request.POST["hobbies-category"]
        curr_user = User.objects.get(id = request.user.id)
        
        new_hobby_group = HobbyGroup.objects.create(
            hobbyGroupOwner = curr_user,
            hobbyGroupName = title,
            hobbyGroupDescriptionShort = description_short,
            hobbyGroupDescriptionDetailed = description_detailed,
            hobbyGroupCategories = hobbies_category
        )
        new_hobby_group.hobbyGroupAdmins.add(curr_user)
        new_hobby_group.hobbyGroupMembers.add(curr_user)
        new_hobby_group.save()
        return HttpResponseRedirect(reverse("hobbies"))
    return render(request, "yayberhood/createHobbyGroup.html")

def borrowIt(request):
    rentals = Rental.objects.all()
    rentals = rentals.order_by("-rentalCreationTimestamp").all()
    return render(request, "yayberhood/borrowIt.html",{
        "rentals":rentals,
    })

def createBorrowIt(request):
    if request.method == "POST":
        ### create hobby group from create hobby group page ###
        title = request.POST["borrowIt-createTitle"]
        description_short = request.POST["borrowIt-createDescriptionShort"]
        description_detailed = request.POST["borrowIt-createDescriptionDetailed"]
        borrowIt_rentalType = request.POST["borrowIt-rentalType"]
        curr_user = User.objects.get(id = request.user.id)
        
        new_rental = Rental.objects.create(
            rentalOwner = curr_user,
            rentalTitle = title,
            rentalDescriptionShort = description_short,
            rentalDescriptionDetailed = description_detailed,
            rentalType = borrowIt_rentalType
        )
        new_rental.save()
        return HttpResponseRedirect(reverse("borrowIt"))
    return render(request, "yayberhood/createBorrowIt.html")
    
def littleHelpers(request):
    little_helpers = Help.objects.all()
    little_helpers = little_helpers.order_by("-helpCreationTimestamp").all()
    return render(request, "yayberhood/littleHelpers.html",{
        "little_helpers":little_helpers,
    })

def createLittleHelpers(request):
    if request.method == "POST":
        ### create hobby group from create hobby group page ###
        title = request.POST["littleHelpers-createTitle"]
        description_short = request.POST["littleHelpers-createDescriptionShort"]
        description_detailed = request.POST["littleHelpers-createDescriptionDetailed"]
        littleHelpers_helpType = request.POST["littleHelpers-helpType"]
        curr_user = User.objects.get(id = request.user.id)
        
        new_help = Help.objects.create(
            helpOwner = curr_user,
            helpTitle = title,
            helpDescriptionShort = description_short,
            helpDescriptionDetailed = description_detailed,
            helpType = littleHelpers_helpType
        )
        new_help.save()
        return HttpResponseRedirect(reverse("littleHelpers"))
    return render(request, "yayberhood/createLittleHelpers.html")

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