from datetime import datetime

from django.db import models

from apps.currencies.models import Currency
from apps.currencies.services import CreateCurrencyRateService


class Asset(models.Model):
    class Network(models.TextChoices):
        ETH = 'ERC-20', 'Ethereum network'
        BNB = 'BEP-20', 'Binance network'

    name = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        related_name='assets',
        verbose_name='Asset currency name',
    )
    network = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        choices=Network.choices,
        verbose_name='Network name',
    )
    wallet = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Coin wallet',
    )
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=3,
        verbose_name='Crypto asset amount',
    )
    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=6,
        verbose_name='Purchase price',
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        verbose_name='Purchase currency',
    )
    price_usd = models.DecimalField(
        max_digits=15,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='Purchase price in USD',
    )

    created_at = models.DateField(
        auto_now_add=datetime.now(),
    )

    class Meta:
        db_table = 'asset'
        verbose_name = 'asset'
        verbose_name_plural = 'assets'

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, **kwargs):
        if self.price_usd is None:
            self.price_usd = self.purchase_price

            if self.currency is not None:
                CreateCurrencyRateService.fill_currency_rates()
                self.price_usd = self.purchase_price * self.currency.rate

        return super().save(**kwargs)
