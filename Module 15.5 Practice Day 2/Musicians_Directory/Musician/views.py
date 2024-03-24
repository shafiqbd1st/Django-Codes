from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        form = forms.AddMusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')

    else:
        form = forms.AddMusicianForm()
        return render(request, 'add_musician.html', {'form': form})


def edit_musician(request, id):
    musician = models.AddMusician.objects.get(pk=id)
    musician_form = forms.AddMusicianForm(instance=musician)

    if request.method == "POST":
        musician_form = forms.AddMusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("homepage")

    return render(request, "add_musician.html", {"form": musician_form})
