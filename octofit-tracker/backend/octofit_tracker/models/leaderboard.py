from djongo import models

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
