from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    cover = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    year = models.CharField(max_length=4, blank=True)
    description = models.TextField(blank=True)

