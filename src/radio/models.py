from django.db import models

class Station(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(blank=True)
	cover = models.ImageField(upload_to='stations', blank=True)

	def __unicode__(self):
		return self.title

