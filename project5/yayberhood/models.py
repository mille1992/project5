from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class User(AbstractUser):
    profilePhotoUrl = models.CharField(max_length=255)

class Project(models.Model):
    projectCreationTimestamp = models.DateTimeField(auto_now_add=True)
    projectOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projectOwnerships")
    projectName = models.CharField(max_length=255)
    projectDescription = models.TextField(blank=False)
    projectAdmins = models.ManyToManyField(User, related_name="projectsWithAdminRightsForThisUser")
    projectDonation_bool = models.BooleanField(default=False)
    projectDonation_value = models.IntegerField(default=0)
    projectMembers = models.ManyToManyField(User, related_name="projectMemberships")

class HobbyGroup(models.Model): 
    hobbyGroupCreationTimestamp = models.DateTimeField(auto_now_add=True)
    hobbyGroupOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hobbyGroupOwnerships")
    hobbyGroupName = models.CharField(max_length=255)
    hobbyGroupDescription = models.TextField(blank=False)
    hobbyGroupAdmins = models.ManyToManyField(User, related_name="hobbyGroupsWithAdminRightsForThisUser")
    hobbyGroupMembers = models.ManyToManyField(User, related_name="hobbyGroupMemberships")
    hobbyGroupCategories = models.CharField(max_length=15)

class Help(models.Model):
    helpCreationTimestamp = models.DateTimeField(auto_now_add=True)
    helpTitle = models.CharField(max_length=255)
    helpDescription = models.TextField(blank=False)
    helpOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="helpOwnerships")
    HelpTypes = models.TextChoices('helpTypes', 'Requests Offers')
    helpType = models.CharField(blank=False, choices = HelpTypes.choices, max_length=10)

class Rental(models.Model):
    rentalCreationTimestamp = models.DateTimeField(auto_now_add=True)
    rentalOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rentalsOwnerships")
    rentalTitle = models.CharField(max_length=255)
    rentalDescription = models.TextField(blank=False)
    RentalTypes = models.TextChoices('rentalTypes', 'Searches Offers')
    rentalType = models.CharField(blank=False, choices = RentalTypes.choices, max_length=10)
    rentalRentable = models.BooleanField(default=True)
    borrowingUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rentalsBorrowedByUser")