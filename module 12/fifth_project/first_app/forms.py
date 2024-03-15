from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="User Name",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter your Name"}),
    )
    email = forms.EmailField(
        label="User Email",
        widget=forms.TextInput(attrs={"placeholder": "Enter your Email"}),
    )
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # CHOICES = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
    # size = forms.ChoiceField(choices=CHOICES)

    # CHOICES1 = [("P", "Pizza"), ("M", "Meet"), ("C", "Chicken"), ("I", "Ice-cream")]
    # Meals = forms.MultipleChoiceField(choices=CHOICES1)
    country = forms.CharField(initial="Bangladesh", disabled=True)
    # CV = forms.FileField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Enter your message"})
    )
    # check = forms.BooleanField()
