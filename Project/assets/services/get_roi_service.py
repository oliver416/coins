from typing import final
from decimal import Decimal
import random


@final
class GetRoiService:

    @classmethod
    def get_roi(cls, asset) -> Decimal:
        """
        Returns return of investment value
        """
        return Decimal(random.choice([-1, 1]))
