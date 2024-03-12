from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length = 20)
    completed = models.BooleanField(default = False)