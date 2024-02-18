from django.shortcuts import render
from django import forms

from . import util
import markdown2

from django.urls import reverse
from django.http import HttpResponseRedirect

class NewWikiArticle(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    content = util.get_entry(title)
    if (content is None):
        return HttpResponseRedirect(reverse("wiki:404"))
    return render(request, "encyclopedia/article.html", {
        "title": title,
        "content": markdown2.markdown(content)
    })

def not_found(request):
    return render(request, "encyclopedia/404.html")

def add(request):
    if request.method == "POST":
        form = NewWikiArticle(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            util.save_entry(data['title'],data['content'])
            return HttpResponseRedirect(reverse("index"))
    else:    
        return render(request, "encyclopedia/add.html", {
            "form": NewWikiArticle
        })