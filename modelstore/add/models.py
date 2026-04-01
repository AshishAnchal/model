from django.db import models

# Create your models here.
class Attend(models.Model):
    roll = models.IntegerField()
    attendance = models.CharField(max_length=200)
    tarikh=models.DateField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.attendance
    