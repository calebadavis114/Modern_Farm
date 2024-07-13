from django.db import models

class Crops(models.Model):
    name = models.CharField(max_length=255)
    average_yield = models.CharField(max_length=255)
    growth_time = models.CharField(max_length=255)
    soil = models.CharField(max_length=255)
    waterring = models.CharField(max_length=255)
    health_benefits= models.CharField(max_length=255)

