from django import forms

class contactForm(forms.Form):
    Name = forms.CharField(max_length=200, label="User name")
    Email = forms.EmailField(max_length=200, label="User Email")
    # Age = forms.IntegerField()
    # Gender = forms.ChoiceField(choices=[('m','male'), ('f', 'female')])
    # value = [('s', 'small'), ('m', 'medium'), ('l', 'large')]
    # Size = forms.ChoiceField(choices=value)
    # meal = [('p', 'pizza'), ('b', 'burger'), ('s','sandwich'), ('c', 'cheese')]
    # Meal = forms.MultipleChoiceField(choices=meal)
    # Check = forms.BooleanField()
    # Message = forms.CharField(widget=forms.Textarea)
    file = forms.FileField()