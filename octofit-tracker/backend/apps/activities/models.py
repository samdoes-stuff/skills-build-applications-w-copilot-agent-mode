from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()
    distance = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user.username} on {self.date}"