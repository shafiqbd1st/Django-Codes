from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("This first app page.")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
