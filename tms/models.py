from django.db import models
from django.utils import timezone


class Contributor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        db_table = 'contributors'
    
    def __str__(self):
        return self.name


class Task(models.Model):
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'tasks'
    
    def __str__(self):
        return self.title
