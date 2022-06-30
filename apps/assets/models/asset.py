from datetime import datetime

from django.db import models

from apps.currencies.models import Currency as MarketCurrency


class Asset(models.Model):
    class Network(models.TextChoices):
        ETH = 'ERC-20', 'Ethereum network'
        BNB = 'BEP-20', 'Binance network'

    class Currency(models.TextChoices):
        USDT = 'USD', 'USD'
        BNB = 'BNB', 'Binance coin'

    name = models.ForeignKey(
        MarketCurrency,
        on_delete=models.DO_NOTHING,
        related_name='assets',
        verbose_name='Asset currency name',
    )
    ticker = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Ticker',
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
    contract = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Contract address',
    )
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Crypto asset amount',
    )
    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=6,
        verbose_name='Purchase price',
    )
    currency = models.CharField(
        max_length=4,
        choices=Currency.choices,
        verbose_name='Purchase currency',
    )
    price_usd = models.DecimalField(
        max_digits=15,
        decimal_places=5,
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
        return f'{self.ticker} {self.name}'
