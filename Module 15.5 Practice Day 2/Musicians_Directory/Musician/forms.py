from django import forms
from .models import AddMusician

class AddMusicianForm(forms.ModelForm):
    class Meta:
        model = AddMusician
        fields = '__all__'
        