from decimal import Decimal

from django.contrib import admin
from django.utils.html import format_html

from apps.currencies.services import CreateCurrencyRateService
from .models import Asset
from .services import GetRoiService


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    readonly_fields = (
        'price_usd',
    )
    list_display = (
        'id',
        'name_',
        'amount_',
        'roi',
        'price',
        'price_usd_',
        'wallet',
    )

    @admin.display(description='Name')
    def name_(self, asset: Asset):
        ticker, name, symbol = str(asset.name).split(' - ')
        html = f'''
            <div><strong>{ticker}</strong></div>
            <div>{name}</div>
            <div>{symbol}</div>
        '''
        return format_html(html)

    @admin.display(description='Amount')
    def amount_(self, asset: Asset):
        return asset.amount

    def roi(self, asset: Asset) -> str:
        roi = GetRoiService.get_roi(asset)
        color, sign = ('green', '+') if roi >= 0 else ('red', '')
        html = f'''<b style="color:{color}">{sign}{{}}%</b>'''
        return format_html(html, roi)

    def price(self, asset: Asset) -> str:
        price = GetRoiService.get_asset_price(asset)
        return str(price.quantize(Decimal('1.00')))

    @admin.display(description='Price USD')
    def price_usd_(self, asset: Asset) -> str:
        price = asset.price_usd
        return str(price.quantize(Decimal('1.00')))

    def changelist_view(self, request, extra_context=None):
        CreateCurrencyRateService.fill_currency_rates()
        return super().changelist_view(request, extra_context)
