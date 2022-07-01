from typing import final
from decimal import Decimal
from apps.assets.models import Asset


@final
class GetRoiService:

    @classmethod
    def get_roi(cls, asset: Asset) -> Decimal:
        """
        Returns return of investment value
        """
        roi = Decimal('inf')
        asset_price = cls.get_asset_price(asset)
        price_usd = getattr(asset, 'price_usd', None)

        if price_usd is not None and price_usd != Decimal('0'):
            roi = (asset_price - asset.price_usd) / asset.price_usd * 100
            roi = Decimal(roi).quantize(Decimal('1.00'))

        return roi

    @classmethod
    def get_asset_price(cls, asset: Asset) -> Decimal:
        currency_rate = asset.name.rate
        return currency_rate * asset.amount
