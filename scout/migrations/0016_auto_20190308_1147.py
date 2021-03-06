# Generated by Django 2.0.13 on 2019-03-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0015_robot_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachscout',
            name='unique_scout_key',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='unique_scout_key',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='pitscout',
            name='unique_scout_key',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='robots',
            field=models.ManyToManyField(blank=True, to='scout.Robot'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='team_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
