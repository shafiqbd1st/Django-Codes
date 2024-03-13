from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def form(request):
    return render(request, 'form.html')


def djangoForm(request):
    return render(request, 'django.html')
