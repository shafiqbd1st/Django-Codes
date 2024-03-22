from django.db import models

# Create your models here.
from author.models import Author

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    Author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name