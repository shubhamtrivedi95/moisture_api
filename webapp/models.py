from django.db import models

# Create your models here.
class Machines(models.Model):

    TokenNo = models.CharField(max_length=10, unique=True)
    StackNo = models.CharField(max_length=10)
    Enable = models.IntegerField(null=True, blank=True)
    GrainMoisture = models.FloatField(null=True, blank=True)
    ValueCut = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.StackNo
