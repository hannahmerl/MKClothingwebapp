# Generated by Django 3.2.8 on 2022-01-31 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKclothingapp', '0005_history_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.IntegerField(default=0)),
                ('cancels', models.IntegerField(default=0)),
            ],
        ),
    ]
