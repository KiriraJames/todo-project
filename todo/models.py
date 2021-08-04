from django.db import models

# Create your models here.

#Task model
class Task(models.Model):
    Title = models.CharField(max_length=500)
    Description = models.CharField(max_length=3000, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Last_modified = models.DateTimeField(auto_now=True)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
