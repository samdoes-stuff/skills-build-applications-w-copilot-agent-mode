from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
