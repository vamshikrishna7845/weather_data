from django.db import models

# Create your models here.


class WeatherData(models.Model):
    date = models.IntegerField()
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    precipitation = models.IntegerField()
    weather_station = models.CharField(max_length=255)

    class meta:
        unique_together = ('date', 'weather_station')

    def __str__(self):
        return f'{self.date}'


class YieldData(models.Model):
    year = models.IntegerField(unique=True)
    qty_harvested = models.IntegerField()

    def __str__(self):
        return f'{self.year}'

    
class StatisticsData(models.Model):
    weather_station = models.CharField(max_length=255)
    year = models.IntegerField()
    max_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    min_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
