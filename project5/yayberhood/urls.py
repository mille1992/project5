from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("littleProjects", views.littleProjects, name="littleProjects"),
    path("createLittleProject", views.createLittleProject, name="createLittleProject"),
    path("hobbies", views.hobbies, name="hobbies"),
    path("createHobbyGroup", views.createHobbyGroup, name="createHobbyGroup"),
    path("borrowIt", views.borrowIt, name="borrowIt"),
    path("littleHelpers", views.littleHelpers, name="littleHelpers"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]