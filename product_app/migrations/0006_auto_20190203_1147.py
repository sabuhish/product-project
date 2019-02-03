# Generated by Django 2.1.5 on 2019-02-03 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_auto_20190201_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlar',
            name='miqdari',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productlar',
            name='qiymeti',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
