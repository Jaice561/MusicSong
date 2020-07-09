from django.db import models
from django.contrib.auth.models import User
from songs.models import Song

class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    songs = models.ManyToManyField(Song, related_name='songs')
    some_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}={self.active}"
