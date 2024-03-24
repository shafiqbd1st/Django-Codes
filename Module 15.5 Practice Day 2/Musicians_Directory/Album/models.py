from django.db import models

# Create your models here.
from Musician.models import AddMusician

class AddAlbum(models.Model):
    album_name = models.CharField(max_length=100)
    Release_Date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AddMusician, on_delete=models.CASCADE)
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    Rating = {
        one: "1",
        two: "2",
        three: "3",
        four: "4",
        five: "5",
    }
    Album_Rating = models.CharField(
        max_length=2,
        choices=Rating,
        default="5",
    )

    def __str__(self):
        return self.album_name
