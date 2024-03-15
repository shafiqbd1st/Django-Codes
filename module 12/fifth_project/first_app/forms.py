from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="User Name", help_text=)
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # CHOICES = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
    # size = forms.ChoiceField(choices=CHOICES)
    
    # CHOICES1 = [("P", "Pizza"), ("M", "Meet"), ("C", "Chicken"), ("I", "Ice-cream")]
    # Meals = forms.MultipleChoiceField(choices=CHOICES1)
    # CV = forms.FileField()
    # check = forms.BooleanField()
