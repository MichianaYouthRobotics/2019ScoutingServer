# Generated by Django 2.0.13 on 2019-03-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0008_auto_20190223_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='robots',
            field=models.ManyToManyField(blank=True, null=True, to='scout.Robot'),
        ),
    ]