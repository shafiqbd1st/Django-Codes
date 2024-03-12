from django import forms

class contactForm(forms.Form):
    Name = forms.CharField(max_length=200, label="User name", widget=forms.TextInput(attrs={'placeholder': "Enter your name"} ))
    Email = forms.EmailField(max_length=200, label="User Email",widget=forms.TextInput(attrs={'placeholder': "Enter your Email"} ))
    Age = forms.IntegerField()
    Gender = forms.ChoiceField(choices=[('m','male'), ('f', 'female')])
    # meal = [('p', 'pizza'), ('b', 'burger'), ('s','sandwich'), ('c', 'cheese')]
    # Meal = forms.MultipleChoiceField(choices=meal)
    # Check = forms.BooleanField()
    # Message = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    value = [('s', 'small'), ('m', 'medium'), ('l', 'large')]
    Size = forms.ChoiceField(choices=value, widget=forms.RadioSelect)
    # file = forms.FileField()