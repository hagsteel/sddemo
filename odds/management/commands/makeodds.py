import decimal
from django.core.management.base import BaseCommand
import random
import time
from sddemo.odds.models import Odds


def produce_odds():
    odds = Odds.objects.all()
    for o in odds:
        o.odds = decimal.Decimal(random.randrange(10000))/100
        o.save()


class Command(BaseCommand):
    def handle(self, frequency=1, **options):
        frequency = decimal.Decimal(frequency)
        while(True):
            try:
                produce_odds()
                time.sleep(frequency)
            except:
                return
