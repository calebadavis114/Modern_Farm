from rest_framework import serilaizers
from .models import Farm

class FarmSerializer(serilaizers.ModelSerializer):
    class Meta:
        model = Farm
        