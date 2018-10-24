# Generated by Django 2.0.9 on 2018-10-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_country_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='is_available',
            field=models.BooleanField(db_column='can_drive', default=False, verbose_name='Pico y Placa?'),
        ),
    ]
