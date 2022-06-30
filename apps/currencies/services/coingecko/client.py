from typing import final, Iterable, Union
from pycoingecko import CoinGeckoAPI

from apps.currencies.exceptions import CurrencyListError, GetCurrencyRateError


@final
class CoingeckoClient:

    def __init__(self):
        self.coingecko = CoinGeckoAPI()

    @classmethod
    def request_currency_rates(
        cls,
        market_ids: Union[Iterable, str],
        output_currency: str = 'usd',
    ) -> dict:
        """
        Returns a dict like the following one:
        {'bitcoin': {'usd': 18994.75}}
        """
        try:
            response = cls().coingecko.get_price(market_ids, vs_currencies=output_currency)
        except Exception as e:
            raise GetCurrencyRateError from e

        return {market_id: price[output_currency] for market_id, price in response.items()}

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
