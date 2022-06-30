from typing import final, List
from decimal import Decimal

from apps.currencies.structures import Currency
from .coingecko import CoingeckoClient


@final
class GetCurrencyRateService:

    @classmethod
    def currency_list(cls) -> List[Currency]:
        currency_list = CoingeckoClient.request_currency_list()
        return [Currency(id=currency['id'], name=currency['name']) for currency in currency_list]

    @classmethod
    def get_currency_rate(cls, currency: str) -> Decimal:
        currency_rate = CoingeckoClient.get_currency_rate(currency)
        return Decimal(currency_rate)
