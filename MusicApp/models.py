from django.db import models


# Create your models here.

class Musics(models.Model):
    name = models.CharField(max_length=100)
    song_type = models.CharField(max_length=100)
    song_description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
