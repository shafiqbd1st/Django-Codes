from django import forms
from .models import AddTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = "__all__"

        widgets = {"task_date": forms.DateInput(attrs={"type": "datetime-local"})}
