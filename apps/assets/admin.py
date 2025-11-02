from decimal import Decimal
from typing import Optional

from django.contrib import admin, messages
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
        'buy_price',
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

        if roi == Decimal('inf'):
            return format_html(
                '''<b style="color:black">CURRENCY IS NOT FOUND</b>''',
            )

        html = f'''<b style="color:{color}">{sign}{{}}%</b>'''
        return format_html(html, roi)

    def price(self, asset: Asset) -> str:
        price = GetRoiService.get_asset_price(asset)
        return str(price.quantize(Decimal('1.00')))

    @staticmethod
    def _get_zero_count_after_separator(number: Decimal) -> Optional[int]:
        zero_count = 0
        number = str(number)

        if 'E' in number:
            return

        decimal_part = number.split('.')[-1]

        for digit in decimal_part:
            if digit == '0':
                zero_count += 1
            else:
                break

        return zero_count

    def buy_price(self, asset: Asset) -> str:
        price = asset.price_usd / asset.amount
        zero_numbers = self._get_zero_count_after_separator(price)
        buy_price = f'{price:.2E}'

        if zero_numbers is not None and zero_numbers <= 5:
            buy_price = str(price.quantize(Decimal('1.0000000')))

        return buy_price

    @admin.display(description='Price USD')
    def price_usd_(self, asset: Asset) -> str:
        price = asset.price_usd
        return str(price.quantize(Decimal('1.00')))

    def changelist_view(self, request, extra_context=None):
        try:
            CreateCurrencyRateService.fill_currency_rates()
            messages.success(request, 'Currency rates has been successfully updated')
        except Exception as e:
            error = f'An error has been occured: {e.__class__.__name__} {e}'
            messages.error(request, error)
        return super().changelist_view(request, extra_context)

