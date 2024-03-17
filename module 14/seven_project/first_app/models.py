from django.db import models

class studentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    address = models.TextField()
# Create your models here.
    def __str__(self) -> str:
        return f'Name: {self.name}'