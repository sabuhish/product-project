# Generated by Django 2.1.5 on 2019-02-15 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0010_productlar_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlar',
            name='image',
        ),
    ]