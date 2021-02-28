from django.db import models
from django.contrib.auth.models import Permission, User

class Album(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=500)
    album_title = models.CharField(max_length=500)
    album_log = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=500)
    audio_file = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.song_title
    

