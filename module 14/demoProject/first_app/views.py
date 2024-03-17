from django.shortcuts import render
from first_app import studentForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = studentForm()
    return render(request, 'django_form.html', {'form': form})