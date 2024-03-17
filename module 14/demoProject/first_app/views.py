from django.shortcuts import render
from first_app import studentForm
# Create your views here.
def home(request):
    return render(request, 'django_form.html')