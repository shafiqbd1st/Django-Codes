from django.db import models

# Create your models here.
from categories.models import Category
from author.models import Author

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    