from django.contrib import admin

from apps.currencies.models import Currency


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

    def get_queryset(self, request):
        return super().get_queryset(request)
