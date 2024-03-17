from django.shortcuts import render
from first_app.forms import studentForm
# Create your views here.
def home(request):
    # stu = studentForm()
    # return render(request, 'home.html', {'form': stu})
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = studentForm()
    return render(request, 'home.html', {'form': form})