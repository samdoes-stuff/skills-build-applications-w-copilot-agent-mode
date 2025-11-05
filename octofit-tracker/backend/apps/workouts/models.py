from djongo import models

class Workout(models.Model):
    user_id = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.activity}"
