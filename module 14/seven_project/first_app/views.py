from django.shortcuts import render
from first_app.forms import studentForm
# Create your views here.
def home(request):
    stu = studentForm()
    return render(request, 'home.html', {'form': stu})