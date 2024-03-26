from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            print(form)
    else:
        form = forms.UserRegisterForm()
    return render(request, 'home.html', {'form': form})
