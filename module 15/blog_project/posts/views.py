from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.


def add_post(request):
    if request.method == "POST":
        post_form = forms.PostFrom(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("add_post")

    else:
        post_form = forms.PostFrom()
        return render(request, "add_post.html", {"form": post_form})
def add_post(request):
    if request.method == "POST":
        post_form = forms.PostFrom(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("add_post")

    else:
        post_form = forms.PostFrom()
        return render(request, "add_post.html", {"form": post_form})
