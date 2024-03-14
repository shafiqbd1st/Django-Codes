from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'about.html', {'name': name, 'email': email})
    else return render(request, 'about.html', {'name': 'None', 'email': 'None'})
def form(request):
    return render(request, 'form.html')


def djangoForm(request):
    return render(request, 'django.html')
