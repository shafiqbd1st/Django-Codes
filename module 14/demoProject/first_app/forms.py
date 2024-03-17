from django import forms
from first_app.models import studentModle

class studentForm(forms.ModelForm):
    class Meta:
        model = studentModle
        fields = '__all__'
