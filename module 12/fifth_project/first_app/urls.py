from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="about"),
    path("form/", views.form, name="formpage"),
    # path("djangoForm/", views.djangoForm, name="DjangoForm"),
    # path("djangoForm/", views.StudentForm, name="DjangoForm"),
    path("djangoForm/", views.password_valid, name="DjangoForm"),
]
