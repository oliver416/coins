from typing import final
from pycoingecko import CoinGeckoAPI

from apps.currencies.exceptions import CurrencyListError


@final
class CoingeckoClient:

    def __init__(self):
        self.coingecko = CoinGeckoAPI()

    @classmethod
    def get_currency_rate(cls, ticker: str) -> str:
        return '0'

    @classmethod
    def _request_currency_rates(cls) -> dict:
        return {}

    @classmethod
    def request_currency_list(cls) -> list:
        """
        Returns a list of dicts like the following:
        {'id': 'zyx', 'symbol': 'zyx', 'name': 'ZYX'}
        """
        try:
            return cls().coingecko.get_coins_list()
        except Exception as e:
            raise CurrencyListError from e
