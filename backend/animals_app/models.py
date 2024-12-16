from django.db import models
from .validator import validate_name
from ..farm_app.models import Farm

class Animals(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, validators=[validate_name])
    image = models.CharField(max_length=255)
    size = models.IntegerField(default=1)
    average_age = models.IntegerField(default=1)
    feed = models.CharField(max_length=255)
    bathe = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    yields = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name} is an animal"

