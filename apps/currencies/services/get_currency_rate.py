import traceback
from typing import final, List
from decimal import Decimal

from apps.currencies.structures import Currency
from apps.currencies.models import Currency as CurrencyModel
from apps.currencies.models import CoinGeckoCurrency

from .coingecko import CoingeckoClient


@final
class CreateCurrencyRateService:

    @classmethod
    def create_currency_list(cls):
        try:
            currency_list = cls._get_currency_list()
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
    def fill_currency_rates(cls):
        try:
            rates = cls._get_currency_rates()
            rates = {currency.id: currency.rate for currency in rates}

            currencies = []

            for currency in CurrencyModel.objects.all():
                currency.rate = rates[currency.name.market_id]
                currencies.append(currency)

            CurrencyModel.objects.bulk_update(currencies, ['rate'])
            print('Currency rates have been successfully updated')
        except Exception as e:
            print(f'An error has been occurred: {e.__class__.__name__}: {e}'
                  f'{traceback.format_tb(e.__traceback__)}')

    @classmethod
    def _get_currency_list(cls) -> List[Currency]:
        currency_list = CoingeckoClient.request_currency_list()
        return [Currency(id=currency['id'], name=currency['name']) for currency in currency_list]

    @classmethod
    def _get_currency_rates(cls) -> List[Currency]:
        market_ids = CurrencyModel.objects.all().values_list('name__market_id', flat=True)
        currency_rates = CoingeckoClient.request_currency_rates(list(market_ids))
        return [
            Currency(
                id=market_id,
                rate=Decimal(str(rate)),
            )
            for market_id, rate in currency_rates.items()
        ]
