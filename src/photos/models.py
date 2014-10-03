from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField()

