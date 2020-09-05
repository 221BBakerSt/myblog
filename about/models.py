from django.db import models
from PIL import Image


class Board(models.Model):
    # 4 blanks for the guest to fill
    nickname = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=512, blank=True)
    message = models.TextField(max_length=2000, blank=True)
    # record the time and the date of the message
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        # name the table in db
        db_table = "guest_board"


class Owner(models.Model):
    pic = models.ImageField(upload_to="owner", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description[:40]


class Bulletin(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to="music")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "song"
