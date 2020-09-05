from django.db import models
from PIL import Image
from django.utils import timezone
from .storage import ImageStorage

class Slide(models.Model):

    slide_pic = models.ImageField(upload_to="slide", blank=True, null=True, default=False)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        # name the table in db
        db_table = "slide"


class Gallery(models.Model):

    cover = models.ImageField(upload_to="gallery", blank=True, null=True, default=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    # the date will be shown on blog page
    timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        # name the table in db
        db_table = "gallery"
        verbose_name_plural = "galleries"
        ordering=["timestamp", "name"]
    
    
class Photo(models.Model):
    # file names of uploaded photos are hashed by ImageStorage()
    photo_pic = models.ImageField(upload_to="photo", storage=ImageStorage(), blank=True, null=True, default=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.DO_NOTHING)
    # the date will be shown on blog page
    timestamp = models.DateField(default=timezone.now)
    # DateTime only used to sort, not shown on blog page
    time = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description

    class Meta:
        # name the table in db
        db_table = "photo"
        ordering=["time"]
