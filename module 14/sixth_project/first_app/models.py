from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=20, default="Rana")

    def __str__(self):
        return f"Roll: {self.roll} Name: {self.name} Father Name: {self.father_name} Address: {self.address}"
