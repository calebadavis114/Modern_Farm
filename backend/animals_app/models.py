from django.db import models

class Animals(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    size = models.IntegerField()
    average_age = models.IntegerField()
    feed = models.CharField(max_length=255)
    bathe = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    yields = models.CharField(max_length=255)


