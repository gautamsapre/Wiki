from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"), 
    path("wiki/entry", views.entry, name = "entry"),
    path("wiki/<s>", views.givenEntry, name = "givenEntry"),
    path("wiki/wiki/<s>", views.givenEntry, name = "givenEntry1"),
]
