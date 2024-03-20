from django.db import models

# Create your models here.
from author.models import Author
from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    
