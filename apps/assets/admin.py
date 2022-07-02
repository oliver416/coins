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
        'name',
        'amount',
        'roi',
        'current_price',
        'price_usd',
        'wallet',
    )

    def roi(self, asset: Asset) -> str:
        roi = GetRoiService.get_roi(asset)
        color, sign = ('green', '+') if roi >= 0 else ('red', '')
        html = f'''<b style="color:{color}">{sign}{{}}%</b>'''
        return format_html(html, roi)

    def current_price(self, asset: Asset) -> str:
        return str(GetRoiService.get_asset_price(asset))

    def changelist_view(self, request, extra_context=None):
        CreateCurrencyRateService.fill_currency_rates()
        return super().changelist_view(request, extra_context)
