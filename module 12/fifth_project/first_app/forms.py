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
class StudentData(forms.Form):
    name = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter your Name"}),
    )
    email = forms.EmailField(
        label="", widget=forms.EmailInput(attrs={"placeholder": "Enter your Email"})
    )
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
    
    

    