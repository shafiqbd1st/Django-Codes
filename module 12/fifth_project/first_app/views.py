from django.shortcuts import render
from .forms import ContactForm, StudentData


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        select = request.POST.get("select")
        return render(
            request, "about.html", {"name": name, "email": email, "select": select}
        )
    else:
        return render(request, "about.html", {"name": "None", "email": "None"})


def form(request):
    return render(request, "form.html")


def djangoForm(request):
    if request.method == "POST":
        print("is post")
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            print("is valid")

            # read data upload file
            
            # File = form.cleaned_data["CV"]
            # with open("./first_app/upload_file/" + File.name, "wb+") as destination:
            #     for chunk in File.chunks():
            #         destination.write(chunk)

            print(form.cleaned_data)
            # return render(request, "django.html", {"form": form})
    else:
        form = ContactForm()
    return render(request, "django.html", {"form": form})

def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    
    return render(request, 'django.html', {'form': form})
        