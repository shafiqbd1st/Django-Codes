from django import forms


# class ContactForm(forms.Form):
#     name = forms.CharField(
#         label="",
#         required=False,
#         widget=forms.TextInput(attrs={"placeholder": "Enter your Name"}),
#     )
#     email = forms.EmailField(
#         label="", widget=forms.TextInput(attrs={"placeholder": "Enter your Email"})
#     )
#     birthday = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
#     # age = forms.IntegerField()
#     # weight = forms.FloatField()
#     CHOICES = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
#     size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

#     CHOICES1 = [("P", "Pizza"), ("M", "Meet"), ("C", "Chicken"), ("I", "Ice-cream")]
#     Meals = forms.MultipleChoiceField(
#         choices=CHOICES1, widget=forms.CheckboxSelectMultiple
#     )
#     country = forms.CharField(initial="Bangladesh", disabled=True)
#     # CV = forms.FileField()
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={"placeholder": "Enter your message"})
#     )
#     # check = forms.BooleanField()


# check validation
# class StudentData(forms.Form):
#     name = forms.CharField(
#         label="",
#         required=False,
#         widget=forms.TextInput(attrs={"placeholder": "Enter your Name"}),
#     )
#     email = forms.EmailField(
#         label="", widget=forms.EmailInput(attrs={"placeholder": "Enter your Email"})
#     )
# def clean_name(self):
#     name = self.cleaned_data['name']
#     if len(name) < 10:
#         raise forms.ValidationError("Enter a name with at least 10 character")
#     return name
# def clean_email(self):
#     email = self.cleaned_data['email']
#     if '.com' not in email:
#         raise forms.ValidationError("Enter a valid email address")
#     return email

# def clean(self):
#     cleaned_data = super().clean()
#     valname = self.cleaned_data['name']
#     valemail = self.cleaned_data['email']

#     if len(valname) < 10:
#         raise forms.ValidationError("Enter a name with at least 10 character")
#     if '.com' not in valemail:
#         raise forms.ValidationError("Please enter a valid email address")
from django.core import validators
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a message at least 10 character")
    
class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Please enter at least 10 characters")])
    email = forms.EmailField()
    age = forms.IntegerField(validators=[validators.MinValueValidator(21, message="age must be greater than 20")])
    # File = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=["jpg"], message="file extension must be ended with .jpg")])
    message = forms.CharField(validators=[len_check], widget=forms.Textarea(attrs={"placeholder": "Enter your message"}))

class passwordValidator(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    comfirm_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        valpassword = self.cleaned_data['password']
        valcomfirm_password = self.cleaned_data['comfirm_password']
        
        if valcomfirm_password != valpassword:
            raise forms.ValidationError("Passwords doesn't match")
            