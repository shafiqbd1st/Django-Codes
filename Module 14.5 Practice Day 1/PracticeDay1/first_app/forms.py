from django import forms
from django.forms.widgets import NumberInput

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    FAVORITE_COLORS_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black"),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    agree = forms.BooleanField(required=False)
