import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinGeckoCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Currency name')),
                ('market_id', models.CharField(max_length=255, verbose_name='Market ID')),
            ],
            options={
                'verbose_name': 'Coingecko currency',
                'verbose_name_plural': 'Coingecko currencies',
                'db_table': 'coingecko_currency',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ticker')),
                ('contract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contract address')),
                ('rate', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True,
                                             verbose_name='Currency rate')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='currencies',
                                           to='currencies.coingeckocurrency', verbose_name='Currency name')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'db_table': 'currency',
            },
        ),
    ]
