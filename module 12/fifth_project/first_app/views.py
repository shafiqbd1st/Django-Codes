from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')

def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'about.html', {'name': name, 'email': email})
    else:
        form = contactForm()
    return render(request, 'django_form.html', {'form': form})