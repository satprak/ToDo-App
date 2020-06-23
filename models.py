from django.db import models

# Create your models here.
class ToDoItems(models.Model):
    content = models.TextField()
