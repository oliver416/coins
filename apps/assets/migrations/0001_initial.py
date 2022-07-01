import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network',
                 models.CharField(blank=True, choices=[('ERC-20', 'Ethereum network'), ('BEP-20', 'Binance network')],
                                  max_length=10, null=True, verbose_name='Network name')),
                ('wallet', models.CharField(blank=True, max_length=255, null=True, verbose_name='Coin wallet')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Crypto asset amount')),
                ('purchase_price', models.DecimalField(decimal_places=6, max_digits=15, verbose_name='Purchase price')),
                ('price_usd', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True,
                                                  verbose_name='Purchase price in USD')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                               to='currencies.currency', verbose_name='Purchase currency')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assets',
                                           to='currencies.currency', verbose_name='Asset currency name')),
            ],
            options={
                'verbose_name': 'asset',
                'verbose_name_plural': 'assets',
                'db_table': 'asset',
            },
        ),
    ]
