from django.shortcuts import render, redirect
from . import forms
from . import models


# Create your views here.
def add_album(request):
    if request.method == "POST":
        form = forms.AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_album")

    else:
        form = forms.AddAlbumForm()
        return render(request, "add_album.html", {"form": form})


def edit_album(request, id):
    album = models.AddAlbum.objects.get(pk=id)
    album_form = forms.AddAlbumForm(instance=album)

    if request.method == "POST":
        album_form = forms.AddAlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")

    return render(request, "add_album.html", {"form": album_form})


def delete_album(request, id):
    musician = models.AddMusician.objects.get(pk=id).delete()
    return redirect("homepage")
