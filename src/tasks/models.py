from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField(blank=True, default="")
	modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	due = models.DateField(blank=True,null=True)

	def __unicode__(self):
		return self.title

