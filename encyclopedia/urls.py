from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.entry, name = "entry"),
    path("wiki/<s>", views.givenEntry, name = "givenEntry"),
    path("redir", views.redir, name="redir")
]
