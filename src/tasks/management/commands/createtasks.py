# scanmusic.py
from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task

class Command(BaseCommand):
	help = "re-scans the music db"

	def handle(self, *args, **options):
		Task.objects.all().delete()
		for i in range(100):
			task = Task()
			task.title = 'Task-%d'%i
			task.text = 'Text %d'%i
			task.save()

				