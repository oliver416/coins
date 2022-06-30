from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Currency name')),
                ('market_id', models.CharField(max_length=255, verbose_name='Market ID')),
                ('market', models.CharField(default='Coingecko', max_length=10, verbose_name='Market name')),
                ('rate', models.DecimalField(decimal_places=6, max_digits=15, blank=True, null=True,
                                             verbose_name='Currency rate')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'db_table': 'currency',
            },
        ),
    ]
