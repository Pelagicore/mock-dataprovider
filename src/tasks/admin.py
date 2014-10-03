from django.contrib import admin
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
	list_display = ('title','due','modified')
	list_display_links = ('title','due','modified')
	search_fields = ('title','due','modified')

admin.site.register(Task, TaskAdmin)