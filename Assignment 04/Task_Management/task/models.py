from django.db import models

# Create your models here.
from category.models import AddCategory


class AddTask(models.Model):
    title = models.CharField(max_length=100)
    task_date = models.DateTimeField()
    description = models.TextField()
    category = models.ManyToManyField(AddCategory)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
