from django.db import models

# Create your models here.
from author.models import Author

class profile(models.Model):
    name = models.CharField(max_length=100) 
    about = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)