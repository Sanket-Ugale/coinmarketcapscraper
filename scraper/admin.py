from django.contrib import admin

# Register your models here.

from scraper.models import Job, Task
admin.site.register(Job)
admin.site.register(Task)
