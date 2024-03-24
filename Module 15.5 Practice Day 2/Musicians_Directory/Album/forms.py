from django import forms
from .models import AddAlbum


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = AddAlbum
        fields = "__all__"
