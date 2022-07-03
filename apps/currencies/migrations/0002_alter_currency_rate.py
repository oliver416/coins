from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=17, null=True,
                                      verbose_name='Currency rate'),
        ),
    ]
