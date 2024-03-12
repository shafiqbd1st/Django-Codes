from django import forms
from django.core import validators

class contactForm(forms.Form):
    Name = forms.CharField(
        max_length=200,
        label="User name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"}),
    )
    Email = forms.EmailField(
        max_length=200,
        label="User Email",
        widget=forms.TextInput(attrs={"placeholder": "Enter your Email"}),
    )
    Age = forms.IntegerField(required=False)
    Gender = forms.ChoiceField(choices=[("m", "male"), ("f", "female")])
    birthday = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    value = [("s", "small"), ("m", "medium"), ("l", "large")]
    Size = forms.ChoiceField(choices=value, widget=forms.RadioSelect)
    meal = [("p", "pizza"), ("b", "burger"), ("s", "sandwich"), ("c", "cheese")]
    Meal = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)

    Message = forms.CharField(max_length=200, widget=forms.Textarea)
    file = forms.FileField()


# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     def clean(self):
#         clean_data = super().clean()
#         name = self.cleaned_data['name']
#         email = self.cleaned_data["email"]
#         if len(name) < 10:
#             raise forms.ValidationError(
#                 "please enter a name with at least 10 characters"
#             )
#         if ".com" not in email:
#             raise forms.ValidationError("Your email must contain .com")

class studentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Please enter at least 10 characters")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Please enter a valid email address")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35, message="Age must be maximum 35"), validators.MinValueValidator(30, message="Age must be minimum 30")])
    
    
class passwordValidationProject(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Please enter at least 10 characters")])
    
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    