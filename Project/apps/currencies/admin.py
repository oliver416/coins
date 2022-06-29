from django.contrib import admin

from apps.currencies.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'market_id',
    )
    search_fields = (
        'name',
    )
