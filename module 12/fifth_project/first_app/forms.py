from django import forms

class contactForm(forms.Form):
    Name = forms.CharField(
        max_length=200,
        label="User name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"}),
    )
    Email = forms.EmailField(max_length=200, label="User Email",widget=forms.TextInput(attrs={'placeholder': "Enter your Email"} ))
    Age = forms.IntegerField(required=False)
    Gender = forms.ChoiceField(choices=[('m','male'), ('f', 'female')])
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    value = [('s', 'small'), ('m', 'medium'), ('l', 'large')]
    Size = forms.ChoiceField(choices=value, widget=forms.RadioSelect)
    meal = [('p', 'pizza'), ('b', 'burger'), ('s','sandwich'), ('c', 'cheese')]
    Meal = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)

    Message = forms.CharField(max_length=200, widget=forms.Textarea)
    # file = forms.FileField()
