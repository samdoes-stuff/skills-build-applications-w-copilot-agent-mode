from djongo import models

class LeaderboardEntry(models.Model):
    user_id = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.score}"
