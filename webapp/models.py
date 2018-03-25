from django.db import models

# Create your models here.
class sensors(models.Model):
    roomNo=models.CharField(max_length=10)
    sensorId=models.IntegerField()
    sensorValue=models.IntegerField()

    def __str__(self):
        return self.roomNo
