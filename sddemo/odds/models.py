from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import OddsSerializer


class Market(SelfPublishModel, models.Model):
    name = models.CharField(max_length=100)


class Odds(SelfPublishModel, models.Model):
    serializer_class = OddsSerializer
    market = models.CharField(max_length=100)
    odds = models.DecimalField(max_digits=7, decimal_places=2)
