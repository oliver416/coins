from django.contrib import admin

from apps.currencies.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ticker',
    )
    search_fields = (
        'name',
    )
