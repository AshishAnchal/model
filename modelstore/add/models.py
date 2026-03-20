from django.db import models

# Create your models here.
class Attend(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    attendance = models.CharField(max_length=200)
    tarikh=models.DateField()

    def __str__(self):
        return self.attendance