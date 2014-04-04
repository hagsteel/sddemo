import decimal
from django.core.management.base import BaseCommand
import random
import time
from sddemo.odds.models import Odds


def produce_odds(random_odd):
    odds = Odds.objects.all()
    if random_odd:
        odds = [odds.order_by('?').first()]
    for o in odds:
        o.odds = decimal.Decimal(random.randrange(10000))/100
        o.save()


class Command(BaseCommand):
    def handle(self, frequency=1, random_odd=False, **options):
        frequency = decimal.Decimal(frequency)
        while(True):
            try:
                produce_odds(random_odd)
                time.sleep(frequency)
            except:
                return
