from django.db import models
from ..animals_app.models import Animals
from ..crops_app.models import Crops
from ..farmer_app.models import Farmer


class Farm(models.Model):
    name = models.CharField()
    farner = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    animals = models.ManyToManyField(Animals, relate_name="farms")
    crops = models.ManyToManyField(Crops, relate_name="crops")

