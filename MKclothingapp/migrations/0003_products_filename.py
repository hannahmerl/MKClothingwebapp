# Generated by Django 3.2.8 on 2021-12-03 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKclothingapp', '0002_remove_products_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='filename',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
