import traceback

from apps.currencies.services import GetCurrencyRateService
from apps.currencies.models import CoinGeckoCurrency, Currency


class RunCommandService:

    @classmethod
    def currency_list(cls):
        try:
            currency_list = GetCurrencyRateService.currency_list()
            currencies = [
                CoinGeckoCurrency(
                    name=currency.name,
                    market_id=currency.id,
                ) for currency in currency_list
            ]
            CoinGeckoCurrency.objects.bulk_create(currencies)
            print('Currency list has been successfully created')
        except Exception as e:
            print(f'An error has been occurred: {e.__class__.__name__}: {e} '
                  f'{traceback.format_tb(e.__traceback__)}')

    @classmethod
    def currency_rates(cls):
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
