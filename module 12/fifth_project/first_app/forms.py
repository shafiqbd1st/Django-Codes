from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="User Name")
    email = forms.EmailField(label="User Email")
