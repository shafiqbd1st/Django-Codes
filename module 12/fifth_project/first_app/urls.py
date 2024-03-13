from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('form/', views.form, name = 'form'),
    path('djangoForm/', views.djangoForm, name = 'django_form'),
]
