from django.contrib import admin

from apps.currencies.models import Currency, CoinGeckoCurrency
from apps.currencies.services import CreateCurrencyRateService


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ticker',
        'rate',
    )
    search_fields = (
        'name',
    )

    def changelist_view(self, request, extra_context=None):
        if CoinGeckoCurrency.objects.count() == 0:
            CreateCurrencyRateService.create_currency_list()

        CreateCurrencyRateService.fill_currency_rates()
        return super().changelist_view(request, extra_context)
