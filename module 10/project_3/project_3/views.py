from django.http import HttpResponse

def home1(request):
    return HttpResponse("Hello, world. You're at the home page.")