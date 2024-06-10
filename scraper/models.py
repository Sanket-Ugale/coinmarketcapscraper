import uuid
from django.db import models

# Create your models here.
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    coin = models.CharField(max_length=255)
    data = models.JSONField(null=True, blank=True)
