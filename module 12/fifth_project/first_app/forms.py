from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    check = forms.BooleanField()
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES)
