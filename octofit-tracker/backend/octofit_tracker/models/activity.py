from djongo import models

class Activity(models.Model):
    _id = models.ObjectIdField()
    user_email = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'
