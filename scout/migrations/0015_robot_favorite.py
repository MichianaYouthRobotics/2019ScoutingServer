# Generated by Django 2.0.13 on 2019-03-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0014_auto_20190307_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]