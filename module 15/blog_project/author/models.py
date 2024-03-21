from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)
    bio = models.TextField()
