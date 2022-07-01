from django.db import models


class CoinGeckoCurrency(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Currency name',
    )
    market_id = models.CharField(
        max_length=255,
        verbose_name='Market ID',
    )

    class Meta:
        db_table = 'coingecko_currency'
        verbose_name = 'Coingecko currency'
        verbose_name_plural = 'Coingecko currencies'

    def __str__(self) -> str:
        return f'{self.name} - {self.market_id}'
