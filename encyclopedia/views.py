from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request):
    s = request.POST['q']
    return  render(request, "encyclopedia/entry.html", {
    "entry": util.get_entry(s)
    })

