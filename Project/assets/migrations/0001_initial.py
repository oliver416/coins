from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Currency name')),
                ('ticker', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ticker')),
                ('network',
                 models.CharField(blank=True, choices=[('ERC-20', 'Ethereum network'), ('BEP-20', 'Binance network')],
                                  max_length=10, null=True, verbose_name='Network name')),
                ('wallet', models.CharField(blank=True, max_length=255, null=True, verbose_name='Coin wallet')),
                ('contract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contract address')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Crypto asset amount')),
                ('purchase_price', models.DecimalField(decimal_places=6, max_digits=15, verbose_name='Purchase price')),
                ('currency', models.CharField(choices=[('USDT', 'USDT Tether'), ('BNB', 'Binance coin')], max_length=4,
                                              verbose_name='Purchase currency')),
                ('current_price', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True,
                                                      verbose_name='Current price USD')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
