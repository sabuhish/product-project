# Generated by Django 2.1.5 on 2019-02-01 12:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlar',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 12, 18, 37, 317545, tzinfo=utc), verbose_name='date_created'),
        ),
    ]
