from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/littleProjects", views.littleProjects, name="littleProjects"),
    path("/hobbies", views.hobbies, name="hobbies"),
    path("/borrowIt", views.borrowIt, name="borrowIt"),
    path("/littleHelpers", views.littleHelpers, name="littleHelpers"),
]