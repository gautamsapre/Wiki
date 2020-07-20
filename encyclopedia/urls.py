from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.entry, name = "entry"),
    path("wiki/<s>", views.givenEntry, name = "givenEntry"),
    path("redir", views.redir, name="redir"),
    path("wiki/<s>/edit", views.edit, name="edit"),
    path("wiki/<title>/edit1", views.confirmEdit, name="confirmEdit"),
    path("add", views.add, name="add"),
    path("addNew", views.addNew, name="addNew")

]
