from django.core.management.base import BaseCommand

from apps.currencies.services import GetCurrencyRateService
from apps.currencies.models import Currency


class Command(BaseCommand):
    help = 'Fill currencies with Coingecko API response'

    def handle(self, *args, **options):
        try:
            currency_list = GetCurrencyRateService.currency_list()
            currencies = [
                Currency(
                    name=currency.name,
                    market_id=currency.id,
                ) for currency in currency_list
            ]
            Currency.objects.bulk_create(currencies)
            print('Currency list has been successfully created')
        except Exception as e:
            print(f'An error has been occurred: {e.__class__.__name__}: {e}')
