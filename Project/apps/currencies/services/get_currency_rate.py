from typing import final
from decimal import Decimal


@final
class GetCurrencyRateService:

    @classmethod
    def get_currency_rate(cls, currency: str) -> Decimal:
        return Decimal('0')
