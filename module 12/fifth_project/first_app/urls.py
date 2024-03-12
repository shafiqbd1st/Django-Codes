from django.urls import path, include

from .import views
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("form/", views.form, name="form"),
    # path('django_form/', views.djangoForm, name = 'django_form'),
    path("studentData/", views.password_check, name="django_form"),
]
