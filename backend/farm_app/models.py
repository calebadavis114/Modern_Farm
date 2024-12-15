from django.db import models
from animals_app.models import Animals
from crops_app.models import Crops

class Farm(models.Model):
    name = models.CharField()

