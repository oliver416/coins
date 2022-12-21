from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Crypto asset amount'),
        ),
    ]
