from django import forms
from first_app.models import studentModel

class studentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }