from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="User Name")
    email = forms.EmailField(label="User Email")
