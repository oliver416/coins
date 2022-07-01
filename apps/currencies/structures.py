from typing import NamedTuple
from decimal import Decimal


class Currency(NamedTuple):
    id: str
    name: str = None
    rate: Decimal = None
