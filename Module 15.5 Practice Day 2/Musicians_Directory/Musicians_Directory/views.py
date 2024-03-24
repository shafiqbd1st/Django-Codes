from django.shortcuts import render
from Album.models import AddAlbum


def home(request):
    data = AddAlbum.objects.all()
    return render(request, "index.html", {"data": data})
