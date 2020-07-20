from django import forms
from django.shortcuts import render
from django.urls import reverse
import markdown2
import random 
from django.shortcuts import redirect
from django.http import (HttpResponse, HttpResponseNotFound, Http404, 
HttpResponseRedirect, HttpResponsePermanentRedirect)

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request):
    return redirect('givenEntry', request.POST['q'])

def givenEntry(request, s):
    if util.get_entry(s) != None:
        return  render(request, "encyclopedia/entry.html", {
        "entry": convert_md(util.get_entry(s)),
        "entry_name": s
        })
    else:
        return similar_results(request, s)

def similar_results(request, s):
    not_found=[]
    for entry in util.list_entries():
            ent = entry.lower()
            if ent.find(s.lower()) != -1:
                not_found.append(entry)
    if len(not_found) == 0:
        return  render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(s),
            "entry_name": s
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": not_found
        })

def convert_md(md_file):
    md = markdown2.markdown(md_file)
    return md

def redir(request):
    return redirect('givenEntry', util.list_entries()[random.randint(0,len(util.list_entries())-1)])


def edit(request,s):
    return render(request, "encyclopedia/edit.html", {
        "entryname": s,
        "entry": util.get_entry(s)
    })

def confirmEdit(request,title):
    util.save_entry(title, request.POST['content'])
    return redirect('givenEntry', title)

def add(request):
    return render(request, "encyclopedia/add.html", { 
        "err": False
    })

def addNew(request):
    title = request.POST['title'].replace(" ", "_")
    if (util.entry_exists( f"entries/{title}.md")):
        return render(request, "encyclopedia/add.html", {
        "fill": request.POST['content'],    
        "err": True
    })
    else:
        util.save_entry(title, request.POST['content'])
        return redirect('givenEntry', title)