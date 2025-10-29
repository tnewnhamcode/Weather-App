from django.db import models


class Weather(models.Model):
    Temperature=models.IntegerField()
    Humidity=models.IntegerField()
    Precipitation=models.IntegerField()
    Wind=models.IntegerField()


        



# Create your models here.
