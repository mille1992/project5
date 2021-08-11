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
        clicked_project.projectDonation_value = clicked_project.projectDonation_value + int(little_project_donation_value)
        clicked_project.save()

        return JsonResponse({"newdonationValue":clicked_project.projectDonation_value})
    else:
        projects = Project.objects.all()
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
    if request.method == "POST":
        curr_user = request.user
        post_owner = request.POST["borrowIt-rentalPostOwner"]
        message_content = request.POST["borrowIt-message"]
        message_type = request.POST["borrowIt-messageType"]
        message_recipient = User.objects.get(username = post_owner)
        
        newMessage = Message.objects.create(messageOwner = curr_user, messageRecipient = message_recipient, messageContent = message_content, messageType = message_type)
        newMessage.save()        
        
        rentals = Rental.objects.all()
        rentals = rentals.order_by("-rentalCreationTimestamp").all()
        return render(request, "yayberhood/borrowIt.html",{
            "rentals":rentals,
        })
    else:
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
    if request.method == "POST":
        print("test")
        curr_user = request.user
        post_owner = request.POST["littleHelpers-helpPostOwner"]
        message_content = request.POST["littleHelpers-message"]
        message_type = request.POST["littleHelpers-messageType"]
        
        message_recipient = User.objects.get(username = post_owner)
        
        newMessage = Message.objects.create(messageOwner = curr_user, messageRecipient = message_recipient, messageContent = message_content, messageType = message_type)
        newMessage.save()        
        
        little_helpers = Help.objects.all()
        little_helpers = little_helpers.order_by("-helpCreationTimestamp").all()
        return render(request, "yayberhood/littleHelpers.html",{
            "little_helpers":little_helpers,
        })
    else:
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


def profilePage_view(request):
    curr_user = request.user
    outbox = curr_user.messageOwnerships.all()
    inbox = curr_user.recipientOfMessages.all()

    little_project_participations = check_user_participations_projects(request)
    hobby_participations = check_user_participations_hobbies(request)
    little_helper_participations = check_user_participations_helps(request)
    borrow_it_participations = check_user_participations_rentals(request)

    return render(request,"yayberhood/profilePage.html", {
        "curr_user": curr_user,
        "inbox": inbox,
        "outbox": outbox,
        "project_participations": little_project_participations,
        "hobby_participations": hobby_participations,
        "little_helper_participations": little_helper_participations,
        "borrow_it_participations": borrow_it_participations
        })


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


def check_user_participations_projects(request):
    curr_user = request.user

    project_ownerships = curr_user.projectOwnerships.all()
    project_memberships = curr_user.projectMemberships.all()
    project_adminships = curr_user.projectsWithAdminRightsForThisUser.all()

    
    project_participations = []
    for project_participation in project_ownerships:
        project_info = [project_participation.projectName, "Owner"]
        project_participations.append(project_info)

    for project_participation in project_memberships:
        project_info = [project_participation.projectName, "Member"]
        project_participations.append(project_info)

    for project_participation in project_adminships:
        project_info = [project_participation.projectName, "Admin"]
        project_participations.append(project_info)
    project_participations.sort()

    return project_participations
    
def check_user_participations_hobbies(request):
    curr_user = request.user

    hobbyGroup_ownerships = curr_user.hobbyGroupOwnerships.all()
    hobbyGroup_memberships = curr_user.hobbyGroupMemberships.all()
    hobbyGroup_adminships = curr_user.hobbyGroupsWithAdminRightsForThisUser.all()

    
    hobbyGroup_participations = []
    for hobbyGroup_participation in hobbyGroup_ownerships:
        hobbyGroup_info = [hobbyGroup_participation.hobbyGroupName, "Owner"]
        hobbyGroup_participations.append(hobbyGroup_info)

    for hobbyGroup_participation in hobbyGroup_memberships:
        hobbyGroup_info = [hobbyGroup_participation.hobbyGroupName, "Member"]
        hobbyGroup_participations.append(hobbyGroup_info)

    for hobbyGroup_participation in hobbyGroup_adminships:
        hobbyGroup_info = [hobbyGroup_participation.hobbyGroupName, "Admin"]
        hobbyGroup_participations.append(hobbyGroup_info)
    hobbyGroup_participations.sort()

    return hobbyGroup_participations

def check_user_participations_helps(request):
    curr_user = request.user

    help_ownerships = curr_user.helpOwnerships.all()
    
    help_participations = []
    for help_participation in help_ownerships:
        help_info = [help_participation.helpTitle, "Owner", help_participation.helpType]
        help_participations.append(help_info)
    help_participations.sort()

    return help_participations

def check_user_participations_rentals(request):
    curr_user = request.user

    rental_ownerships = curr_user.rentalsOwnerships.all()
    rental_borrowed = curr_user.rentalsBorrowedByUser.all()
    
    rental_participations = []
    for rental_participation in rental_ownerships:
        rental_info = [rental_participation.rentalTitle, "Owner"]
        rental_participations.append(rental_info)

    for rental_participation in rental_borrowed:
        rental_info = [rental_participation.rentalTitle, "Borrower"]
        rental_participations.append(rental_info)

    rental_participations.sort()

    return rental_participations