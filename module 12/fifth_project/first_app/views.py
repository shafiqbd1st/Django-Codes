from django.shortcuts import render
from . forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, "about.html", {"name": "None", "email": "None"})
def form(request):
    return render(request, 'form.html')


def djangoForm(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'django.html', {'form': form})
