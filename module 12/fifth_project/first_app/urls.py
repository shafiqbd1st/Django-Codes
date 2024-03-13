from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="aboutpage"),
    path("form/", views.form, name="form"),
    path("djangoForm/", views.djangoForm, name="django_form"),
]
