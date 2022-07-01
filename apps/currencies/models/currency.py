from django.db import models

from .coingecko_currency import CoinGeckoCurrency


class Currency(models.Model):
    name = models.ForeignKey(
        CoinGeckoCurrency,
        on_delete=models.DO_NOTHING,
        related_name='currencies',
        verbose_name='Currency name',
    )
    ticker = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Ticker',
    )
    contract = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Contract address',
    )
    rate = models.DecimalField(
        max_digits=15,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='Currency rate',
    )

    class Meta:
        db_table = 'currency'
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'

    def __str__(self) -> str:
        return f'{self.ticker} - {self.name}'
