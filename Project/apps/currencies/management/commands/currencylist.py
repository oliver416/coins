from django.core.management.base import BaseCommand

from apps.currencies.services import GetCurrencyRateService


class Command(BaseCommand):
    help = 'Fill currencies with Coingecko API response'

    def handle(self, *args, **options):
        print(
            GetCurrencyRateService.currency_list(),
        )
