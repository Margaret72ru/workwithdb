import csv
import datetime

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone(
                name=phone['name'],
                image=phone['image'],
                price=float(phone['price']),
                release_date=datetime.datetime.strptime(phone['release_date'], '%Y-%m-%d'),
                lte_exists=bool(phone['lte_exists']),
                slug=slugify(phone['name'])
            ).save()
