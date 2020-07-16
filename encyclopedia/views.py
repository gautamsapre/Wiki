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
    not_found=[]
    s = request.POST['q']
    if util.get_entry(s) != None:
        return  render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(s)
        })
    else:
        for entry in util.list_entries():
            ent = entry.lower()
            if ent.find(s.lower()) != -1:
                not_found.append(entry)
        if len(not_found) == 0 :
            return  render(request, "encyclopedia/entry.html", {
                "entry": util.get_entry(s)
            })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": not_found
            })

 

