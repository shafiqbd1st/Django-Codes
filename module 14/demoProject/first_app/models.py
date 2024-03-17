from django.db import models


# Create your models here.
class studentModle(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()    
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)

    def __str__(self):
        return f'Name: {self.name}'