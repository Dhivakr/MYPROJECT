from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class TaskCreated(models.Model):
    task_choices = (
      ('low', 'Low'),
      ('medium', 'Medium'), 
      ('high', 'High'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=task_choices)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
