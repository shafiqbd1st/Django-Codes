from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES)
    meals =[('P', 'Pizza'), ('M', 'meet'), ('C' 'Chicken')]
    foodItems = forms.MultipleChoiceField(choices=meals) 
    check = forms.BooleanField()
