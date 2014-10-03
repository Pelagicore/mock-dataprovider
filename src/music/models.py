from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=200, default="No Title")
    album = models.CharField(max_length=200, default="No Album")
    artist = models.CharField(max_length=200, default="No Artist")
    track = models.CharField(max_length=8, default="")
    source = models.CharField(max_length=200, default="")
    cover = models.CharField(max_length=200, default="")

    def __unicode__(self):
        return self.title

