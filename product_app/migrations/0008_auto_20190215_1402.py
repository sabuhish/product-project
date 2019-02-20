# Generated by Django 2.1.5 on 2019-02-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0007_auto_20190215_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pcitures'),
        ),
        migrations.AlterField(
            model_name='productlar',
            name='gram',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productlar',
            name='qiymeti',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]