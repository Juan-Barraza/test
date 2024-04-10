from django.db import models

class Feature(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=255)
    magnitude = models.FloatField()
    place = models.CharField(max_length=255)
    time = models.DateTimeField()
    tsunami = models.BooleanField()
    mag_type = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    external_url = models.URLField()