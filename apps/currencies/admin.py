from django.contrib import admin

from apps.currencies.models import Currency, CoinGeckoCurrency
from apps.currencies.services import RunCommandService


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
            RunCommandService.currency_list()

        if not all(Currency.objects.all().values_list('rate', flat=True)):
            RunCommandService.currency_rates()

        return super().changelist_view(request, extra_context)
