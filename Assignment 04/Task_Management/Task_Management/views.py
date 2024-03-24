from django.shortcuts import render
from task.models import AddTask

def home(request):
    data = AddTask.objects.all()
    return render(request, 'index.html', {'data': data})
