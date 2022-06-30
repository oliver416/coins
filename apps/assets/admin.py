from decimal import Decimal

from django.contrib import admin
from django.utils.html import format_html

from .models import Asset
from .services import GetRoiService


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    readonly_fields = (
        'price_usd',
    )
    list_display = (
        'id',
        'ticker',
        'name',
        'amount',
        'roi',
        'current_price',
        'initial_price',
        'wallet',
    )

    def roi(self, asset: Asset) -> str:
        roi = GetRoiService.get_roi(asset)
        color, sign = ('green', '+') if roi >= 0 else ('red', '')
        html = f'''<b style="color:{color}">{sign}{{}}%</b>'''
        return format_html(html, roi)

    def current_price(self, asset: Asset) -> str:
        roi = GetRoiService.get_roi(asset)
        price = asset.amount * asset.price_usd + asset.price_usd / 100 * roi
        price = Decimal(price).quantize(Decimal('1'))
        return str(price)

    def initial_price(self, asset: Asset) -> str:
        return str(asset.price_usd.quantize(Decimal('1')))
