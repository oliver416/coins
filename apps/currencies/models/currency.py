from django.db import models


class Currency(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Currency name',
    )
    market_id = models.CharField(
        max_length=255,
        verbose_name='Market ID',
    )
    market = models.CharField(
        max_length=10,
        default='Coingecko',
        verbose_name='Market name',
    )

    class Meta:
        db_table = 'currency'
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'

    def __str__(self) -> str:
        return f'{self.name} - {self.market_id}'
