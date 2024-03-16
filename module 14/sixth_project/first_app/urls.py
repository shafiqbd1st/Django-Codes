from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.home, 'homepage'),
    path('delete/<int:roll>', views.delete_student, name = 'delete_student'),
]