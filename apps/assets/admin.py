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
        'price_usd',
        'wallet',
    )

    def roi(self, asset: Asset) -> str:
        roi = GetRoiService.get_roi(asset)
        color, sign = ('green', '+') if roi >= 0 else ('red', '')
        html = f'''<b style="color:{color}">{sign}{{}}%</b>'''
        return format_html(html, roi)
