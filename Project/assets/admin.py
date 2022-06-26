from django.contrib import admin
from django.utils.html import format_html

from .models import Asset


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
        return format_html('''<b style="color:green">+{}%</b>''', 100)
