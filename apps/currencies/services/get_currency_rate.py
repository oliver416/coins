from typing import final, List
from decimal import Decimal

from apps.currencies.structures import Currency
from apps.assets.models import Asset

from .coingecko import CoingeckoClient


@final
class GetCurrencyRateService:

    @classmethod
    def currency_list(cls) -> List[Currency]:
        currency_list = CoingeckoClient.request_currency_list()
        return [Currency(id=currency['id'], name=currency['name']) for currency in currency_list]

    @classmethod
    def get_currency_rate(cls, asset: Asset) -> Decimal:
        market_id = asset.name.market_id
        currency_rate = CoingeckoClient.request_currency_rates(market_id)
        return Decimal(str(currency_rate[market_id]))
