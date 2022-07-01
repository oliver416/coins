import traceback

from django.core.management.base import BaseCommand

from apps.currencies.services import GetCurrencyRateService
from apps.currencies.models import Currency


class Command(BaseCommand):
    help = 'Fill currency rates with Coingecko API response'

    def handle(self, *args, **options):
        try:
            rates = GetCurrencyRateService.get_currency_rates()
            rates = {currency.id: currency.rate for currency in rates}

            currencies = []

            for currency in Currency.objects.all():
                currency.rate = rates[currency.name.market_id]
                currencies.append(currency)

            Currency.objects.bulk_update(currencies, ['rate'])
            print('Currency rates have been successfully updated')
        except Exception as e:
            print(f'An error has been occurred: {e.__class__.__name__}: {e}'
                  f'{traceback.format_tb(e.__traceback__)}')
