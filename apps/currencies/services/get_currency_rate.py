from typing import final, List
from decimal import Decimal

from apps.currencies.structures import Currency
from apps.currencies.models import Currency as CurrencyModel

from .coingecko import CoingeckoClient


@final
class GetCurrencyRateService:

    @classmethod
    def currency_list(cls) -> List[Currency]:
        currency_list = CoingeckoClient.request_currency_list()
        return [Currency(id=currency['id'], name=currency['name']) for currency in currency_list]

    @classmethod
    def get_currency_rates(cls) -> List[Currency]:
        market_ids = CurrencyModel.objects.all().values_list('name__market_id', flat=True)
        currency_rates = CoingeckoClient.request_currency_rates(list(market_ids))
        return [
            Currency(
                id=market_id,
                rate=Decimal(str(rate)),
            )
            for market_id, rate in currency_rates.items()
        ]
