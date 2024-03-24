from django.shortcuts import render
from . import forms

# Create your views here.


def home(request):
    if request.method == "POST":
        post_form = forms.ExampleForm(request.POST)
        if post_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            birth_date = request.POST.get("birth_date")
            favorite_color = request.POST.get("favorite_color")
            agree = request.POST.get("agree")
            if agree == "on":
                agree = "YES"
            else:
                agree = "NO"
            return render(
                request,
                "about.html",
                {
                    "name": name,
                    "email": email,
                    "birth_date": birth_date,
                    "favorite_color": favorite_color,
                    "agree": agree,
                },
            )
    else:
        post_form = forms.ExampleForm()
        return render(request, "django.html", {"form": post_form})


# if request.method == "POST":
#     print(request.POST)
#     name = request.POST.get("name")
#     email = request.POST.get("email")
#     select = request.POST.get("select")
#     return render(
#         request, "about.html", {"name": name, "email": email, "select": select}
#     )
