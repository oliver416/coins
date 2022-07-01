from django.core.management.base import BaseCommand

from apps.currencies.services import RunCommandService


class Command(BaseCommand):
    help = 'Fill currency rates with Coingecko API response'

    def handle(self, *args, **options):
        RunCommandService.currency_rates()
