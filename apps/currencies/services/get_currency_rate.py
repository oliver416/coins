import traceback
from typing import final, List
from decimal import Decimal

from apps.currencies.structures import Currency
import apps.currencies.models as currencies_models

from .coingecko import CoingeckoClient


@final
class CreateCurrencyRateService:

    @classmethod
    def create_currency_list(cls):
        try:
            currency_list = cls._get_currency_list()
            currencies = [
                currencies_models.CoinGeckoCurrency(
                    name=currency.name,
                    market_id=currency.id,
                ) for currency in currency_list
            ]
            currencies_models.CoinGeckoCurrency.objects.bulk_create(currencies)
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

            for currency in currencies_models.Currency.objects.all():
                currency.rate = rates[currency.name.market_id]
                currencies.append(currency)

            currencies_models.Currency.objects.bulk_update(currencies, ['rate'])
            print('Currency rates have been successfully updated')
        except Exception as e:
            print(f'An error has been occurred: {e.__class__.__name__}: {e}'
                  f'{traceback.format_tb(e.__traceback__)}')

    @classmethod
    def get_currency_rate(cls, market_id: str) -> Currency:
        try:
            currency = cls._get_particular_currency_rate(market_id)
            print('Currency rate has been successfully obtained')
            return currency
        except Exception as e:
            print(f'An error has been occurred: {e.__class__.__name__}: {e}'
                  f'{traceback.format_tb(e.__traceback__)}')

    @classmethod
    def _get_currency_list(cls) -> List[Currency]:
        currency_list = CoingeckoClient.request_currency_list()
        return [Currency(id=currency['id'], name=currency['name']) for currency in currency_list]

    @classmethod
    def _get_currency_rates(cls) -> List[Currency]:
        market_ids = currencies_models.Currency.objects.all().values_list(
            'name__market_id',
            flat=True,
        )
        currency_rates = CoingeckoClient.request_currency_rates(list(market_ids))
        return [
            Currency(
                id=market_id,
                rate=Decimal(str(rate)),
            )
            for market_id, rate in currency_rates.items()
        ]

    @classmethod
    def _get_particular_currency_rate(cls, market_id: str) -> Currency:
        rate = CoingeckoClient.request_currency_rates([market_id])
        rate = rate[market_id]
        return Currency(
            id=market_id,
            rate=Decimal(str(rate)),
        )
