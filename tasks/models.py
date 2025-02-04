from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    last_date = models.DateField()
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
